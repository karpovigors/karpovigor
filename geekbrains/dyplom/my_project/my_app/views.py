# Импорт необходимых модулей Django и Python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings

from .models import Transcription, WordTiming
from .forms import TranscriptionForm, WordTimingForm

import codecs
from pydub import AudioSegment
import json

# Функция для загрузки транскрипций
@login_required
def upload_transcription(request):
    if request.method == 'POST':
        form = TranscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            transcription = form.save(commit=False)
            transcription.user = request.user
            transcription.save()

            # Обработка файла с таймингами слов, если он был загружен
            if request.FILES.get('word_timing_file'):
                word_timing_file = request.FILES['word_timing_file']
                word_timing_file.open(mode='rt')
                content = word_timing_file.read().decode('utf-8')
                for line in content.splitlines():
                    start_time, end_time, word = line.strip().split('\t')
                    WordTiming.objects.create(
                        transcription=transcription,
                        start_time=float(start_time),
                        end_time=float(end_time),
                        word=word
                    )
            else:
                # Если файл с таймингами слов не был загружен, генерируем их автоматически
                word_timings = generate_word_timings(transcription, transcription.audio_file)
                for start_time, end_time, word in word_timings:
                    WordTiming.objects.create(
                        transcription=transcription,
                        start_time=start_time,
                        end_time=end_time,
                        word=word
                    )

            return redirect('my_app:word_timing', pk=transcription.pk)
    else:
        form = TranscriptionForm()

    return render(request, 'my_app/upload_transcription.html', {'form': form})


# Функция для работы с таймингами слов
@login_required
def word_timing(request, pk):
    transcription = Transcription.objects.get(id=pk)
    if request.method == 'POST':
        form = WordTimingForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES.get('word_timing_file'):
                word_timing_file = request.FILES['word_timing_file']
                word_timing_file.open(mode='rt')
                content = word_timing_file.read().decode('utf-8')
                for line in content.splitlines():
                    start_time, end_time, word = line.strip().split('\t')
                    WordTiming.objects.create(
                        transcription=transcription,
                        start_time=float(start_time),
                        end_time=float(end_time),
                        word=word
                    )
            else:
                word_timing = form.save(commit=False)
                word_timing.transcription = transcription
                word_timing.save()

            return redirect('my_app:word_timing', pk=transcription.id)
    else:
        form = WordTimingForm()
    word_timings = WordTiming.objects.filter(transcription=transcription)
    context = {
        'form': form,
        'word_timings': word_timings,
        'transcription_id': transcription.id,
        'audio_file_url': transcription.audio_file.url,  # Add this line
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'my_app/word_timing.html', context)

def generate_word_timings(transcription, audio_file):
    audio = AudioSegment.from_file(audio_file.path)
    duration = audio.duration_seconds

    words = transcription.text.split()
    word_count = len(words)
    if word_count == 0:  # Если нет слов в тексте
        return []  # Вернуть пустой список

    time_per_word = duration / word_count

    word_timings = []
    padding_ratio = 0.1  # Определите отношение отступа к длительности аудио
    max_padding = 0.5  # Определите максимальный отступ между словами

    # Вычислите фактическую величину отступа на основе отношения отступа и ограничьте его максимальным значением
    padding = min(padding_ratio * time_per_word, max_padding)

    for i, word in enumerate(words):
        start_time = i * time_per_word + padding * i
        end_time = start_time + time_per_word
        word_timings.append((start_time, end_time, word))

    return word_timings


@login_required
def download_audio(request, transcription_id):
    transcription = Transcription.objects.get(id=transcription_id)
    return FileResponse(transcription.audio_file, as_attachment=True, filename=transcription.audio_file.name)

@login_required
def update_word_timing(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_time = float(data.get('start_time'))
        end_time = float(data.get('end_time'))
        word = data.get('word')

        word_timing = get_object_or_404(WordTiming, pk=pk)
        word_timing.start_time = start_time
        word_timing.end_time = end_time
        word_timing.word = word
        word_timing.save()

        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})





@csrf_exempt
@login_required
def delete_word_timing(request, pk):
    if request.method == 'POST':
        word_timing = get_object_or_404(WordTiming, pk=pk)
        word_timing.delete()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})

@login_required
def export_txt(request, transcription_id):
    transcription = get_object_or_404(Transcription, id=transcription_id)
    word_timings = WordTiming.objects.filter(transcription=transcription)

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="word_timings_{transcription_id}.txt"'

    for word_timing in word_timings:
        line = f"{word_timing.start_time}\t{word_timing.end_time}\t{word_timing.word}\n"
        response.write(line)

    return response

@csrf_exempt
@require_POST
def add_word_timing(request):
    if request.method == "POST":
        data = json.loads(request.body)
        transcription_id = data.get('transcription_id')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        word = data.get('word')
        transcription = get_object_or_404(Transcription, id=transcription_id)

        word_timing = WordTiming.objects.create(
            transcription=transcription,
            start_time=start_time,
            end_time=end_time,
            word=word
        )
        word_timing.save()
        return JsonResponse({'word_timing': {'id': word_timing.id, 'start_time': start_time, 'end_time': end_time}})
    else:
        return JsonResponse({'result': 'error', 'message': 'Неправильный метод запроса'})

def create_eaf_content(transcription):
    # Здесь должен быть код для создания содержимого EAF-файла
    # на основе данных транскрипции.
    # Возвращает строку с содержимым EAF-файла.

    # Для примера создадим пустой EAF-файл:
    eaf_content = '<?xml version="1.0" encoding="UTF-8"?>\n<ANNOTATION_DOCUMENT />'

    return eaf_content

def export_eaf(request, transcription_id):
    try:
        transcription = Transcription.objects.get(pk=transcription_id)
    except Transcription.DoesNotExist:
        # Обработка ошибки, если транскрипция не найдена
        return HttpResponse(status=404)

    # Создание содержимого EAF-файла на основе данных транскрипции
    eaf_content = create_eaf_content(transcription)

    # Установите имя файла в соответствии с вашими требованиями:
    file_name = f"transcription_{transcription_id}.eaf"

    response = HttpResponse(eaf_content, content_type='application/xml')
    response['Content-Disposition'] = f'attachment; filename={file_name}'
    return response
