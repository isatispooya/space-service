from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import response
from . import models
from . import serializer
import datetime


class AuthViewSet(viewsets.ModelViewSet):
    queryset = models.Auth.objects.all()
    serializer_class = serializer.Auth
    def list(self, request):
        Domain = request.query_params.get('Domain')
        if Domain is None:
            raise serializers.ValidationError('Parameter "Domain" is required.')
        filtered_object = self.get_queryset().filter(Domain=Domain).last()
        serializer = self.get_serializer(filtered_object)
        return response.Response(serializer.data)
