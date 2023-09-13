from django.urls import path, include
from .views import CustomerDetailView, CustomerListView
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="NIU-Customer",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("Customer/", CustomerListView.as_view(),
         name="customer_list_view"),
    path("Customer/<int:id>/", CustomerDetailView.as_view(), 
         name="customer_detail_view"),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)