from django.db import models

# Create your models here.
class Logs(models.Model):

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
        ordering = ['-data']

    temperatura = models.FloatField()
    status = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.temperatura} - {self.status} - {self.data}'