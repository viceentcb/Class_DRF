# Django and DRF imports
from rest_framework.routers import SimpleRouter

# proof class import
from .views import ShirtViewSet, MeShirtView

router = SimpleRouter()

router.register(r'shirts', ShirtViewSet, basename="shirts")
router.register(r'me/shirts', MeShirtView, basename="me_shirts")

urlpatterns = router.urls
