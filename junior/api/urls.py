from django.urls import path

from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'books/v4', views.BookViewSet)

urlpatterns = [
    path(r'books/', views.get_books),
    path(r'books/v2/', views.BookAPIView.as_view()),
    path(r'books/v3/', views.BookGenericAPIView.as_view()),
    path(r'books/v3/<int:pk>/', views.BookGenericDetailAPIView.as_view()),
]
urlpatterns += router.urls
