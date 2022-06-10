import datetime

from django.test import TestCase
from .models import *
from django.contrib.auth.models import Group

class AddActivityTest(TestCase):

    def test_add_activity(self):
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

        response = self.client.get('/addActivity/')
        self.assertContains(response, 'Izaberite kojoj kategoriji pripada aktivnost koju želite da dodate', html=True)

    def test_define_activity_post(self):
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

        response = self.client.get('/addActivity/')

        cat = Category(
            name='kafica',
            root=0,
        )
        cat.save()
        response = self.client.post('/defineActivity/', data={
            'cat': cat.name,
        })
        self.assertContains(response, 'definisanje aktivnosti', html=True)

class PlanMyDayTest(TestCase):

    def test_plan_my_day_first(self):
        cat = Category(
            name='kafica',
            root=0,
        )
        cat.save()

        response = self.client.get('/planMyDayFirst/')
        self.assertContains(response, 'kafica', html=True)

    def test_plan_my_day_second_post(self):
        testCategory = Category(
            name='TestCat',
            root='0',
            message='Test message'
        )
        testCategory.save()

        testSkiTrack = SkiTrack(
            name='TestStaza',
            color=0,
            length=123,
        )
        testSkiTrack.save()

        testActivity = Activity(
            type=testCategory,
            skitrack=testSkiTrack,
            obj_name='TestName',
            obj_contact='+381 123456'
        )
        testActivity.save()

        response = self.client.get('/planMyDayFirst/')

        response = self.client.post('/planMyDaySecond/', data={
            'range': 0,
            'checks[]': '["TestName"]',
        })

        self.assertNotContains(response, testActivity.obj_name, html=True)

    def test_plan_my_day_final(self):
        testCategory = Category(
            name='TestCat',
            root=0,
            message='Test message'
        )
        testCategory.save()

        testSkiTrack = SkiTrack(
            name='TestStaza',
            color=0,
            length=123,
        )
        testSkiTrack.save()

        testActivity = Activity(
            type=testCategory,
            skitrack=testSkiTrack,
            obj_name='TestName',
            obj_contact='+381 123456'
        )
        testActivity.save()

        response = self.client.post('/planMyDayFinal/', data={
            'skiing': 0,
            'activity_id_list': ','+str(testActivity.id)+',',
        })

        self.assertNotContains(response, testActivity.obj_name, html=True)





