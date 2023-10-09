from rest_framework import serializers
from .models import Label, Document

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields= ('id', 'name', 'color')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields= ('id', 'name', 'content')