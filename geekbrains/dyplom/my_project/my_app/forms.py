from django import forms
from django.core.exceptions import ValidationError
from .models import Transcription, WordTiming

def validate_wav_file(value):
    if not value.name.endswith('.wav'):
        raise ValidationError("Файл должен быть в формате .wav")

def validate_txt_file(value):
    if not value.name.endswith('.txt'):
        raise ValidationError("Файл должен быть в формате .txt")

class TranscriptionForm(forms.ModelForm):
    class Meta:
        model = Transcription
        fields = ['text', 'audio_file', 'word_timing_file']
        labels = {
            'text': 'Текст',
            'audio_file': 'Аудиофайл',
            'word_timing_file': 'Файл тайминга слов (.txt)',
        }
    
    audio_file = forms.FileField(validators=[validate_wav_file])
    word_timing_file = forms.FileField(required=False, validators=[validate_txt_file])
    text = forms.CharField(widget=forms.Textarea, required=False)



class WordTimingForm(forms.ModelForm):
    class Meta:
        model = WordTiming
        fields = ('word', 'start_time', 'end_time', 'word_timing_file')
        labels = {
            'word': 'Слово',
            'start_time': 'Начало диапазона',
            'end_time': 'Конец диапазона',
            'word_timing_file': 'Файл тайминга слов (.txt)'
        }

    word_timing_file = forms.FileField(required=False, validators=[validate_txt_file])
