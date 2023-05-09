# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import ShirtViewSet

router = SimpleRouter()

router.register(r'shirts', ShirtViewSet, basename="shirts")

urlpatterns = router.urls
