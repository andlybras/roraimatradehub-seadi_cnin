from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts_management.urls')),
    path('profile/', include('profiles_management.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('inteligencia-de-mercado/', include('market_intelligence_management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)