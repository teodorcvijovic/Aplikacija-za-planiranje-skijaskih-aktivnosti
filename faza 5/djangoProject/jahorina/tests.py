from django.test import TestCase
from .models import *
from django.contrib.auth.models import Group


class LoginTest(TestCase):
    def test_login_post(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_moderator=0,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        response = self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })
        self.assertRedirects(response, expected_url='/')

    def test_login_get(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'authentication/login.html')


class CategoryTest(TestCase):
    def test_add_category(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_moderator=0,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })

        response1 = self.client.post('/addCategory/', follow=True, data={
            'message': 'Test poruke',
            'name': 'TestIme',
            'root': 0
        })

        self.assertContains(response1, 'TestIme', html=True)

    def test_delete_category(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_superuser=1,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })

        testCategory = Category(
            name= 'Test',
            root= 0,
            message= 'Test poruka'
        )

        testCategory.save()

        self.client.post('/deleteCategory/', data={
            'category_id': testCategory.id
        })

        response = self.client.get('/addActivity/')

        self.assertNotContains(response, testCategory.name, html=True)


class TracksTest(TestCase):
    def test_show_track_information(self):
        response = self.client.get('/trackInformation/')
        self.assertTemplateUsed(response, 'trackInformation.html')

    def test_add_track(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_moderator=0,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })

        response = self.client.post('/addTrack/', follow=True, data={
            'name': 'TestStaza1',
            'length': 123,
            'trackColor': 0
        })

        self.assertContains(response, 'TestStaza1', html=True)

    def test_delete_ski_track(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_superuser=1,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })

        testTrack = SkiTrack(
            name='TestStaza1',
            color=0,
            length=123,
        )
        testTrack.save()
        # self.client.post('/updateTrackInformation/', data={
        #     'updateTrack': testTrack.id
        # })

        self.client.post('/deleteSkiTrack/', data={
            'skitrack_id': testTrack.id
        })

        response = self.client.get('/trackInformation/')
        # self.assertTemplateUsed(response, 'trackInformation.html')
        self.assertNotContains(response, 'TestStaza1', html=True)

    def test_update_track_info_get(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_moderator=0,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })
        testTrack = SkiTrack(
            name='TestStaza1',
            color=0,
            length=123,
        )
        testTrack.save()
        response = self.client.post('/updateTrackInformation/', data={
            'updateTrack': testTrack.id
        })

        self.assertTemplateUsed(response, 'updateTrackInformation.html')

    def test_update_track_info_post(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_moderator=0,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })
        testTrack = SkiTrack(
            name='TestStaza1',
            color=0,
            length=123,
        )
        testTrack.save()
        response = self.client.post('/updateTrackInformation/', follow=True, data={
            'updateTrack': testTrack.id,
            'is_foggy': True,
            'opened': 1
        })

        self.assertContains(response, 'maglovito', html=True)


class ActivityTest(TestCase):
    def test_show_all_activities_get(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_superuser=1,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })

        response = self.client.get('/showAllActivities/')
        self.assertTemplateUsed(response, 'allActivities.html')

    def test_show_all_activities_post(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_superuser=1,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })

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

        response = self.client.post('/showAllActivities/', data={
            'name': testActivity.obj_name
        })

        self.assertContains(response, testActivity.obj_name, html=True)

    def test_delete_activity(self):
        Group.objects.create(name='default')
        testUser = MyUser(
            username='test',
            first_name='test',
            last_name='testic',
            email='test@mail.com',
            is_superuser=1,
        )

        testUser.set_password("T@sh@1234")
        testUser.save()

        testUser.groups.add(Group.objects.get(name='default'))
        self.client.post('/login/', data={
            'username': testUser.username,
            'password': 'T@sh@1234'
        })

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

        self.client.post('/deleteActivity', data={
            'activity_id': testActivity.id
        })

        response = self.client.get('/showAllActivities/')
        self.assertNotContains(response, testActivity.obj_name, html=True)
