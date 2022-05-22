from rest_framework.viewsets import ModelViewSet

from .serializers import StaffSerializer, SubstationSerializer, OrganizationSerializer
from .models import Staff, Substation, Organization


class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class SubstationViewSet(ModelViewSet):
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer