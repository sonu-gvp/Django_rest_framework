from django.urls import path
from class_based_views import views
from class_based_views import mixin_views
from class_based_views import generic_class_view

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('mixin_snippets/', mixin_views.SnippetList.as_view()),
    path('mixin_snippets/<int:pk>/', mixin_views.SnippetDetail.as_view()),
    path('generic_snippets/', generic_class_view.SnippetList.as_view()),
    path('generic_snippets/<int:pk>/', generic_class_view.SnippetDetail.as_view()),
]
