from django.db import models

class SDM(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    jabatan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
