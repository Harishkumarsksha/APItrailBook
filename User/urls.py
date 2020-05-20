from django.urls import path,include
from User.views import UserViewSet,BookViewSet,AuthorViewSet,PublicationsVieSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'book', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'publication', PublicationsVieSet, basename='publication')
urlpatterns = [
    path('',include(router.urls))
] 