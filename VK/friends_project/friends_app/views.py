from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer
from django.db import models
from django.db.models import Q

class UserCreate(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FriendRequestSend(APIView):
    def post(self, request):
        serializer = FriendRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Устанавливаем отправителя заявки на основе текущего пользователя
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FriendRequestAcceptReject(APIView):
    def put(self, request, friend_request_id):
        try:
            friend_request = FriendRequest.objects.get(id=friend_request_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Friend request not found'}, status=status.HTTP_404_NOT_FOUND)
        action = request.data.get('action')
        if action == 'accept':
            friend_request.status = 'accepted'
        elif action == 'reject':
            friend_request.status = 'rejected'
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        friend_request.save()
        return Response(FriendRequestSerializer(friend_request).data)

class FriendRequestList(APIView):
    def get(self, request):
        friend_requests = FriendRequest.objects.filter(Q(sender=request.user) | Q(receiver=request.user), status='pending')
        serializer = FriendRequestSerializer(friend_requests, many=True)
        return Response(serializer.data)

class FriendsList(APIView):
    def get(self, request):
        friend_requests = FriendRequest.objects.filter(status='accepted').filter(
            models.Q(sender=request.user) | models.Q(receiver=request.user)
        )
        friends = {request.user}
        for fr in friend_requests:
            friends.add(fr.sender)
            friends.add(fr.receiver)
        friends.remove(request.user)
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)

class FriendshipStatus(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        friend_request = FriendRequest.objects.filter(
            Q(sender=request.user, receiver=user) | Q(sender=user, receiver=request.user)
        ).first()
        status = 'none'
        if friend_request:
            status = friend_request.status
            if friend_request.sender == request.user:
                status = 'sent' if status == 'pending' else status
            else:
                status = 'received' if status == 'pending' else status
        return Response({'status': status})


class FriendRemove(APIView):
    def delete(self, request, user_id):
        user = User.objects.get(id=user_id)
        friend_request = FriendRequest.objects.filter(
            status='accepted',
            sender__in=[request.user, user],
            receiver__in=[request.user, user],
        ).first()
        if friend_request:
            friend_request.delete()
            return Response(status=status.HTTP_200_OK)
        return Response({'error': 'No friendship found'}, status=status.HTTP_404_NOT_FOUND)
