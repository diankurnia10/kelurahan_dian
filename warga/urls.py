# warga/urls.py
from django.urls import path
from .views import (
    WargaListView, WargaDetailView, WargaCreateView, WargaUpdateView, WargaDeleteView,
    PengaduanListView, PengaduanCreateView # Tambahkan view pengaduan lain jika sudah dibuat
)

urlpatterns = [
    # Warga URLs (CRUD HTML)
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),
    
    # Pengaduan URLs (HTML)
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    # ... (Tambahkan path detail, edit, hapus pengaduan)
]