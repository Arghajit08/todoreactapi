from django.db.models import fields
from rest_framework import serializers
from .models import *

class EntrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'