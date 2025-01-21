from django.contrib import admin
from django.urls import path
from api.views import GetEmailLayout, UploadImage, UploadEmailConfig, RenderAndDownloadTemplate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getEmailLayout', GetEmailLayout.as_view()),
    path('api/uploadImage', UploadImage.as_view()),
    path('api/uploadEmailConfig', UploadEmailConfig.as_view()),
    path('api/renderAndDownloadTemplate', RenderAndDownloadTemplate.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
