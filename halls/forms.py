from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'url', 'youtube_id']
        labels = {'url': 'URL', 'youtube_id': 'YouTube ID'}