from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from staff_list.viewsets import StaffViewSet, SubstationViewSet, OrganizationViewSet

router = DefaultRouter()
router.register('substations', SubstationViewSet)
router.register('staff', StaffViewSet)
router.register('organizations', OrganizationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', include('staff_list.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
