# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import TelevisionViewSet

router = SimpleRouter()

router.register(r'television', TelevisionViewSet, basename="television")

urlpatterns = router.urls
