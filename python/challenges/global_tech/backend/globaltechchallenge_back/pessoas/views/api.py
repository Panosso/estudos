from rest_framework.viewsets import ModelViewSet

from ..models import Person
from ..serializer import PersonSerializer


class PersonAPIList(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_queryset(self):

        qs = super().get_queryset()

        return qs