from rest_framework import serializers
from .models import *


class snippestserailizers(serializers.ModelSerializer):
    class Meta:
        model=snippest
        fields='__all__'
        