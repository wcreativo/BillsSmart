from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    document = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    def validate_email(self, value):
        client = Client.objects.filter(email=value).first()
        if client:
            raise serializers.ValidationError("A client already exists with that email")
        return value

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.document = validated_data.get("document", instance.document)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
