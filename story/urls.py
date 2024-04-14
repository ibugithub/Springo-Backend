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
  path('create_story/', views.CreateStoryAPI.as_view()),
  path('show_story/', views.ShowStoryAPI.as_view()),
  path('check_isWriter/', views.IsWriterAPI.as_view()),
]