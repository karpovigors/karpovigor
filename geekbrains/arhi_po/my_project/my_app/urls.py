from django.urls import path
from . import views


app_name = 'my_app'

urlpatterns = [
    path('', views.upload_transcription, name='upload_transcription'),
    path('word_timing/<int:pk>/', views.word_timing, name='word_timing'),
    path('download_audio/<int:transcription_id>/', views.download_audio, name='download_audio'),
    path('update_word_timing/<int:pk>/', views.update_word_timing, name='update_word_timing'),
    path('delete_word_timing/<int:pk>/', views.delete_word_timing, name='delete_word_timing'),
    path('export_txt/<int:transcription_id>/', views.export_txt, name='export_txt'),
    path('export_eaf/<int:transcription_id>/', views.export_eaf, name='export_eaf'),
]
