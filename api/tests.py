from django.test import TestCase, Client
from django.contrib.auth.models import User
from api.constants import PASSWORD_ONE, PASSWORD_TWO, TEST_URL, USER_ONE, USER_TWO

from api.models import Message


class SystemApiTest(TestCase):  # django is creating new DB
    def setUp(self):
        '''
        This function defines class variables.
        '''
        # initialize time and location
        self.first_user = User.objects.create_user(
            username=USER_ONE, email='test1@gmail.com', password=PASSWORD_ONE
        )
        self.second_user = User.objects.create_user(
            username=USER_TWO, email='tes21@gmail.com', password=PASSWORD_TWO
        )
        self.client = Client()
        self.url = TEST_URL

        # logging in a user
        self.client.login(username=USER_ONE, password=PASSWORD_ONE)

        self.create_message(self.second_user, self.first_user, USER_ONE, USER_ONE)
        self.create_message(self.second_user, self.first_user, USER_TWO, USER_TWO)
        self.create_message(self.first_user, self.second_user, USER_TWO, 'test3')

        super(SystemApiTest, self).setUp()

    def test_get_and_delete_messages(self):

        single_message_response = self.client.get(
            self.url + '/api/message/1', content_type='application/json', follow=True
        )

        all_message_response = self.client.get(
            self.url + '/api/message/', content_type='application/json', follow=True
        )

        # should return message object dict with six fields
        self.assertEqual(len(single_message_response.data), 6)

        # there are three messages in the DB but the user should see only two
        self.assertEqual(all_message_response.data['count'], 2)

        # deleting message as a receiver
        message = self.create_message(self.second_user, self.first_user, USER_ONE, 'test15')

        response = self.client.delete(
            self.url + f'/api/message/{message.id}',
            content_type='application/json',
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_write_message(self):

        self.client.post(
            self.url + '/api/message/',
            data={
                "message": "testing",
                "subject": "test10",
                "sender": 3,
                "receiver": 4,
            },
            content_type='application/json',
        )

        messages = Message.objects.filter(sender=self.first_user)
        self.assertEqual(len(messages), 1)

    def test_get_unread_messages(self):

        # getting the user's unread messages with django filters
        response = self.client.get(
            self.url + f'/api/message-to-user/?receiver=3&was_seen=false',
            content_type='application/json',
        )

        self.assertEqual(response.data['count'], 2)

    def create_message(self, sender, receiver, message: str, subject: str) -> Message:
        message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            message=message,
            subject=subject,
        )

        return message
