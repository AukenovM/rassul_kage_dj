from rest_framework import serializers


class IinSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    iin = serializers.CharField(max_length=12, default="020130500456")


class AgeSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    age = serializers.IntegerField(default=0)


class SexSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    sex = serializers.BooleanField(default=None)
