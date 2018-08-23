from rest_framework import serializers
from .models import Flexer


class FlexerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flexer
        exclude = ['id', 'token']




