from django.urls import path 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Device Tracker API",
        default_version='v1',
        description="API documentation for deviceTracker project",
        contact=openapi.Contact(email="outsideworkibrahim@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
  path('create_company/', views.CreateCompanyAPI.as_view(), name='create-company'),
  path('show_company/', views.ShowCompanyAPI.as_view(), name='show-company'),
  path('create_employee/', views.CreateEmployeeAPI.as_view(), name='create-employee'),
  path('show_employee/', views.ShowEmployeeAPI.as_view(), name='show-employee'),
  path('create_device/', views.CreateDeviceAPI.as_view(), name='create-device'),
  path('show_device/', views.ShowDeviceAPI.as_view(), name='show-device'),
  path('create_transaction/', views.CreateTransactionAPI .as_view(), name='create-transaction'),
  path('show_transaction/', views.ShowTransactionAPI.as_view(), name='show-transaction'),
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]