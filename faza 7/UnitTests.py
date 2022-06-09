import datetime

from django.test import TestCase
from .models import *
from django.contrib.auth.models import Group

# Create your tests here.

# teodor
class LogoutTest(TestCase):

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, expected_url='/')
        # self.assertContains(response, 'Prijavite se', html=True)

# teodor
class IndexTest(TestCase):

    def test_index(self):
        response = self.client.get('')
        self.assertContains(response, 'Poljice', html=True)

# teodor
class RegisterTest(TestCase):

    def test_register_get(self):
        response = self.client.get('/register/')
        self.assertContains(response, 'Registracija', html=True)

    def test_register_post(self):
        Group.objects.create(name='default')

        response = self.client.post('/register/', data={
            'username': 'marko',
            'password1': '123',
            'password2': '123',
            'first_name': 'Marko',
            'last_name': 'Stankovic',
            'email': 'mare@gmail.com',
            'phone': '+381 313 331',
            'experience': 3,
            'birthdate': datetime.date.today()
        })
        # self.assertTemplateUsed(response, 'index.html')
        self.assertRedirects(response, expected_url='/')
        # response = self.client.get('/instructors/')
        # self.assertContains(response, 'Odjavite se', html=True)

class InstructorsTest(TestCase):

    def test_instructors_get(self):
        Group.objects.create(name='default')
        testUser = SkiInstructor(
            username='test',
            first_name='Test',
            last_name='Testic',
            phone='+231 3131 31',
            email='test@mail.com',
            experience=5,
            birthdate=datetime.datetime.now()
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        response = self.client.get('/instructors/')
        self.assertContains(response, 'Test', html=True)

    def test_instructors_post(self):
        Group.objects.create(name='default')

        testUser = SkiInstructor(
            username='test1',
            first_name='Test1',
            last_name='Testic',
            phone='+231 3131 31',
            email='test@mail.com',
            experience=2,
            birthdate=datetime.datetime.now()
        )
        testUser.set_password("T@sh@1234")
        testUser.save()
        testUser.groups.add(Group.objects.get(name='default'))

        testUser = SkiInstructor(
            username='test2',
            first_name='Test2',
            last_name='Testic',
            phone='+231 3131 31',
            email='test@mail.com',
            experience=4,
            birthdate=datetime.datetime.now()
        )
        testUser.set_password("T@sh@1234")
        testUser.save()
        testUser.groups.add(Group.objects.get(name='default'))

        testUser = SkiInstructor(
            username='test3',
            first_name='Mare',
            last_name='Markovic',
            phone='+231 3131 31',
            email='test@mail.com',
            experience=6,
            birthdate=datetime.datetime.now()
        )
        testUser.set_password("T@sh@1234")
        testUser.save()
        testUser.groups.add(Group.objects.get(name='default'))

        response = self.client.post('/instructors/', data={
            'name': 'Test',
            'experience': 'low'
        })
        self.assertContains(response, 'Test1', html=True)
        self.assertNotContains(response, 'Test2', html=True)
        self.assertNotContains(response, 'Mare', html=True)

        response = self.client.post('/instructors/', data={
            'name': 'Mare',
            'experience': '/'
        })
        self.assertContains(response, 'Mare', html=True)
        self.assertNotContains(response, 'Test1', html=True)
        self.assertNotContains(response, 'Test2', html=True)

class DeleteSkiInstructorTest(TestCase):

    def test_delete_ski_instructor_post(self):
        Group.objects.create(name='default')

        testUser = SkiInstructor(
            username='test1',
            first_name='Test1',
            last_name='Testic',
            phone='+231 3131 31',
            email='test@mail.com',
            experience=2,
            birthdate=datetime.datetime.now()
        )
        testUser.set_password("T@sh@1234")
        testUser.save()
        testUser.groups.add(Group.objects.get(name='default'))

        admin = MyUser(
            username='admin',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_superuser=1,
        )
        admin.set_password("T@sh@1234")
        admin.save()

        self.client.post('/login/', data={
            'username': admin.username,
            'password': 'T@sh@1234'
        })

        response = self.client.post('/deleteSkiInstructor/', data={
            'i_id': testUser.id
        })
        response = self.client.get('/instructors/')
        self.assertNotContains(response, 'Test1', html=True)

