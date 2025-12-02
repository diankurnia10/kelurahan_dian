# warga/models.py
from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True, verbose_name="Nomor Induk Kependudukan")
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    alamat = models.TextField(verbose_name="Alamat Tinggal")
    no_telepon = models.CharField(max_length=15, blank=True, verbose_name="Nomor Telepon")
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Tambahan: mengurutkan berdasarkan nama secara default
        ordering = ['nama_lengkap']
        verbose_name_plural = "Warga"

    def __str__(self):
        return self.nama_lengkap

class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]
    
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU')
    tanggal_lapor = models.DateTimeField(auto_now_add=True)
    
    # ForeignKey: Menghubungkan ke Warga (Relasi One-to-Many)
    pelapor = models.ForeignKey(
        Warga, 
        on_delete=models.CASCADE, 
        related_name='pengaduan', # Memungkinkan akses: warga.pengaduan.all()
        verbose_name="Pelapor"
    )

    class Meta:
        ordering = ['-tanggal_lapor']
        verbose_name_plural = "Pengaduan"

    def __str__(self):
        return self.judul