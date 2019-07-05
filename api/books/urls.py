from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books import views

router = DefaultRouter()
router.register('books', views.BooksList)


urlpatterns = [
    path('', include(router.urls))
]
