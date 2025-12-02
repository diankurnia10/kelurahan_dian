# warga/serializers.py
from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon', 'tanggal_registrasi']
        # 'id' wajib ada agar bisa diakses di API

class PengaduanSerializer(serializers.ModelSerializer):
    # Field read-only untuk menampilkan nama pelapor secara langsung
    # Berguna saat GET list/detail
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)

    class Meta:
        model = Pengaduan
        # 'pelapor' tetap disertakan agar klien API bisa mengirim ID Warga saat POST/PUT
        fields = ['id', 'judul', 'deskripsi', 'status', 'tanggal_lapor', 'pelapor', 'pelapor_nama']
        read_only_fields = ['pelapor_nama']