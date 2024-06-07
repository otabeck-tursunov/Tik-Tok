from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Tik Tok clone API",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(url="otabeck.uz"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),

    path('users/', include('users.urls')),
    path('videos/', include('videos.urls')),
]
