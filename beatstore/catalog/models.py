from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class AudioTrack(models.Model):
    CATEGORY_CHOICES = [
        ('GENGETONE', 'gengetone'),
        ('Hip Hop', 'rap'),
        ('AFRO', 'afro'),
        ('OTHER', 'other'),
    ]

    title = models.CharField(max_length=200)
    audio_file = models.FileField(
        upload_to='audio/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])]
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='OTHER'
    )

    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    tempo = models.CharField(max_length=20)
    key = models.CharField(max_length=20)
    duration = models.CharField(max_length=20, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title}"

