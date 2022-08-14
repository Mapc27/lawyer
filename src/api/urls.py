from rest_framework.routers import SimpleRouter

from .views import ApplicationsView

router = SimpleRouter()
router.register("applications", ApplicationsView, "applications")


urlpatterns = [*router.urls]
