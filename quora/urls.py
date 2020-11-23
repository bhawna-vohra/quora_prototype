from django.conf.urls import url
from quora import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'quora'
urlpatterns = [
   url(r'^register/$',views.register_view,name = 'register'),
   url(r'^login/$',views.login_view,name = 'login_view'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)