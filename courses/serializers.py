from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer): # Hyperlinked adds url to self
    class Meta:
        model = Course
        fields = ('id', 'url','name', 'language', 'price')
