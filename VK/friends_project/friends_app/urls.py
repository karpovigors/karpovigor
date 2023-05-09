from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserCreate.as_view(), name='user-create'),
    path('friend-request/', views.FriendRequestSend.as_view(), name='friend-request-send'),
    path('friend-request/<int:friend_request_id>/', views.FriendRequestAcceptReject.as_view(), name='friend-request-accept-reject'),
    path('friend-requests/', views.FriendRequestList.as_view(), name='friend-requests-list'),
    path('friends/', views.FriendsList.as_view(), name='friends-list'),
    path('friendship-status/<int:user_id>/', views.FriendshipStatus.as_view(), name='friendship-status'),
    path('friend-remove/<int:user_id>/', views.FriendRemove.as_view(), name='friend-remove'),
]
