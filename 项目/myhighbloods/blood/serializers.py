from rest_framework import serializers
from .models import MyBlood
class MyBloodSerializer(serializers.ModelSerializer):
    class Meta():
        model=MyBlood
        fields="__all__"