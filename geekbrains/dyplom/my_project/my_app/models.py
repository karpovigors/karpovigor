from django.db import models
from django.contrib.auth.models import User

class Transcription(models.Model):
    text = models.TextField()
    audio_file = models.FileField(upload_to='audio_files/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class WordTiming(models.Model):
    transcription = models.ForeignKey(Transcription, on_delete=models.CASCADE)
    start_time = models.FloatField()
    end_time = models.FloatField()
    word = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.word} ({self.start_time}-{self.end_time})"
