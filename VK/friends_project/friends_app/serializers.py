from rest_framework import serializers
from .models import FriendRequest, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class FriendRequestSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = FriendRequest
        fields = ('sender', 'receiver')

    def create(self, validated_data):
        sender = validated_data.get('sender')
        receiver = validated_data.get('receiver')
        return FriendRequest.objects.create(sender=sender, receiver=receiver)
