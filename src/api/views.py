from rest_framework import mixins, permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from web.models import Application, SolvedApplication

from .permissions import CustomAuthPermission
from .serializers import ApplicationSerializer, ApplicationViewSerializer, SolvedApplicationViewSerializer


class ApplicationsView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Application.objects.all()
    permission_classes = [CustomAuthPermission]
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.action in ('create',):
            return ApplicationSerializer
        if self.action in ('retrieve', 'list'):
            return ApplicationViewSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        print(request.headers)
        if Application.objects.filter(phone_number=request.data['phone_number']).count() > 2:
            return Response(data={'detail': 'Слишком много записей для этого номера телефона'},
                            status=status.HTTP_429_TOO_MANY_REQUESTS)

        return super().create(request, *args, **kwargs)


class SolvedApplicationsView(mixins.ListModelMixin, GenericViewSet):
    queryset = SolvedApplication.objects.all()
    serializer_class = SolvedApplicationViewSerializer
    permission_classes = [permissions.AllowAny]
