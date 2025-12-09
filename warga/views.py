# warga/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm # Diperlukan untuk CreateView/UpdateView

# Impor untuk Django REST Framework (DRF)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

# --- 1. DJANGO CLASS-BASED VIEWS (CBV) untuk HTML (Pertemuan 1-4) ---

# Warga CRUD (HTML)
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

# Pengaduan CRUD (HTML)
class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list') # Ubah ke 'pengaduan-list' jika sudah dibuat

# ... (Tambahkan PengaduanDetailView, UpdateView, DeleteView serupa)

# --- 2. DRF VIEWSETS untuk API (JSON) (Pertemuan 7 & 9) ---

# Warga API (CRUD Penuh)
class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    # Publik bisa baca, tapi harus login untuk ubah/buat 
    permission_classes = [IsAuthenticatedOrReadOnly] 

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

# Pengaduan API (CRUD Penuh)
class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    # Hanya Admin/Staff yang bisa mengakses 
    permission_classes = [IsAdminUser]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi', 'status']
    ordering_fields = ['tanggal_lapor', 'status']