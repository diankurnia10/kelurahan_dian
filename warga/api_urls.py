# warga/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

# Inisialisasi Router
router = DefaultRouter()

# Daftarkan ViewSet Warga (membuat URL: /api/warga/, /api/warga/1/, dll.)
router.register(r'warga', WargaViewSet, basename='warga')

# Daftarkan ViewSet Pengaduan (membuat URL: /api/pengaduan/, /api/pengaduan/1/, dll.)
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

urlpatterns = [
    # Include semua URL yang dibuat oleh router
    path('', include(router.urls)),
]