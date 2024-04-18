from django.urls import path 
from . import views

urlpatterns = [
  path('create_story/', views.CreateStoryAPI.as_view()),
  path('show_story/', views.ShowStoryAPI.as_view()),
  path('show_inde_story/', views.ShowIndeStoryAPI.as_view()),
  path('check_isWriter/', views.IsWriterAPI.as_view()),
  path('make_writer/', views.MakeWriterAPI.as_view()),
  path('update/<int:pk>/', views.StoryUpdateAPIView.as_view()),
  path('delete/<int:pk>/', views.StoryDeleteAPIView.as_view()),
  path('show_story/<int:id>/', views.ShowSingleStoryAPI.as_view()),
]