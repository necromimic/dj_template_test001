from django.urls import path
from web.views import contact, index, about

urlpatterns = [
    path('', index, name='หน้าหลัก'),
    path('about/', about, name='เกี่ยวกับ'),
    path('contact/', contact, name='เพจติดต่อ'),
]