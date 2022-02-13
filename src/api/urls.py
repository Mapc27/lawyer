from rest_framework.routers import SimpleRouter

from .views import ApplicationsView, SolvedApplicationsView

router = SimpleRouter()
router.register("applications", ApplicationsView, "applications")
router.register("solved_applications", SolvedApplicationsView, "solved_applications")


urlpatterns = [*router.urls]
