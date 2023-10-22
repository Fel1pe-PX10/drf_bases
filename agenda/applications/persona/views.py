from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )

# Models
from .models import Person

# Serializers
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    )


class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all();



class PersonCreateApiView(CreateAPIView):

    serializer_class = PersonSerializer



class PersonDetailApiView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDeleteApiView(DestroyAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateApiView(RetrieveUpdateAPIView):
    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()






