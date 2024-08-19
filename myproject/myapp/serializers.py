from rest_framework import serializers
from myapp.models import NamespaceStatus

class NamespaceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamespaceStatus
        fields = '__all__'  # Include all fields from the model
