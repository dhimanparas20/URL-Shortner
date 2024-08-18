from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import URLViewSet, index

router = DefaultRouter()
router.register(r'urls', URLViewSet)

urlpatterns = [
    path('', index, name='index'),  # This will render the index.html template
    path('api/', include(router.urls)),
    path('<str:pk>/', URLViewSet.as_view({'get': 'redirect_to_long_url'}), name='redirect-short-url'),
]
