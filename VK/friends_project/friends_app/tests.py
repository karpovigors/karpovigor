from django.test import TestCase
from django.contrib.auth.models import User
from .models import FriendRequest

class UserCreateTest(TestCase):
    def test_user_create(self):
        response = self.client.post('/api/users/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

class FriendRequestSendTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_send_friend_request(self):
        self.client.login(username='user1', password='password')
        response = self.client.post('/api/friend-request/', {'to_user': self.user2.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(FriendRequest.objects.count(), 1)

class FriendRequestAcceptRejectTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.friend_request = FriendRequest.objects.create(from_user=self.user1, to_user=self.user2)

    def test_accept_friend_request(self):
        self.client.login(username='user2', password='password')
        response = self.client.put(f'/api/friend-request/{self.friend_request.id}/', {'action': 'accept'})
        self.assertEqual(response.status_code, 200)
        self.friend_request.refresh_from_db()
        self.assertEqual(self.friend_request.status, 'accepted')

    def test_reject_friend_request(self):
        self.client.login(username='user2', password='password')
        response = self.client.put(f'/api/friend-request/{self.friend_request.id}/', {'action': 'reject'})
        self.assertEqual(response.status_code, 200)
        self.friend_request.refresh_from_db()
        self.assertEqual(self.friend_request.status, 'rejected')

class FriendRequestListTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.user3 = User.objects.create_user(username='user3', password='password')
        self.friend_request1 = FriendRequest.objects.create(from_user=self.user1, to_user=self.user2)
        self.friend_request2 = FriendRequest.objects.create(from_user=self.user3, to_user=self.user2)

    def test_friend_request_list(self):
        self.client.login(username='user2', password='password')
        response = self.client.get('/api/friend-requests/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

class FriendsListTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.user3 = User.objects.create_user(username='user3', password='password')
        self.friend_request1 = FriendRequest.objects.create(from_user=self.user1, to_user=self.user2, status='accepted')
        self.friend_request2 = FriendRequest.objects.create(from_user=self.user2, to_user=self.user3, status='accepted')

    def test_friends_list(self):
        self.client.login(username='user2', password='password')
        response = self.client.get('/api/friends/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

class FriendshipStatusTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.friend_request = FriendRequest.objects.create(from_user=self.user1, to_user=self.user2, status='accepted')

    def test_friendship_status(self):
        self.client.login(username='user1', password='password')
        response = self.client.get(f'/api/friendship-status/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'accepted')

class FriendRemoveTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.friend_request = FriendRequest.objects.create(from_user=self.user1, to_user=self.user2, status='accepted')

    def test_friend_remove(self):
        self.client.login(username='user1', password='password')
        response = self.client.delete(f'/api/friend-remove/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.friend_request.refresh_from_db()
        self.assertEqual(FriendRequest.objects.count(), 0)
