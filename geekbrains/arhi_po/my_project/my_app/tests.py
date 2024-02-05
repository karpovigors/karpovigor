from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Transcription, WordTiming
import json

class TranscriptionViewTest(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')


    def test_upload_transcription(self):
        
        url = reverse('my_app:upload_transcription')
        with open('/Users/igorkarpov/Desktop/my_project/media/audio_files/111.wav', 'rb') as audio_file:
            data = {
                'text': 'Test transcription text',
                'audio_file': audio_file,
            }
            response = self.client.post(url, data, follow=True)

            
            self.assertRedirects(response, expected_url=reverse('my_app:word_timing', kwargs={'pk': 1}), status_code=302, target_status_code=200)

            
            self.assertTrue(Transcription.objects.exists())
            print(response.content)


    def test_delete_word_timing(self):
        
        transcription = Transcription.objects.create(user=self.user, text='Test', audio_file='path/to/file')
        word_timing = WordTiming.objects.create(transcription=transcription, start_time=0.0, end_time=1.0, word='test')

        url = reverse('my_app:delete_word_timing', args=[word_timing.id])

        response = self.client.post(url, {}, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "success"})

        self.assertFalse(WordTiming.objects.filter(id=word_timing.id).exists())
        print(response.content)


    def test_update_word_timing(self):
        transcription = Transcription.objects.create(user=self.user, text='Test', audio_file='path/to/file')
        word_timing = WordTiming.objects.create(transcription=transcription, start_time=0.0, end_time=1.0, word='test')

        url = reverse('my_app:update_word_timing', args=[word_timing.id])

        updated_data = json.dumps({
            'start_time': 1.0,
            'end_time': 2.0,
            'word': 'updated'
        })

        response = self.client.post(url, updated_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "success"})

        word_timing.refresh_from_db()
        self.assertEqual(word_timing.start_time, 1.0)
        self.assertEqual(word_timing.end_time, 2.0)
        self.assertEqual(word_timing.word, 'updated')
        print(response.content)