from api.services import send_email
from rest_framework import mixins, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from web.models import Application

from .permissions import CustomAuthPermission
from .serializers import ApplicationSerializer


class ApplicationsView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Application.objects.all()
    permission_classes = [CustomAuthPermission]
    parser_classes = [MultiPartParser]
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        if Application.objects.filter(phone_number=request.data['phone_number']).count() > 2:
            return Response(data={'detail': 'Слишком много записей для этого номера телефона'},
                            status=status.HTTP_429_TOO_MANY_REQUESTS)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()

        send_email(obj, request)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
