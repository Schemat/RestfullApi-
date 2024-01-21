from rest_framework import serializers
from .models import Model1

class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = '__all__'