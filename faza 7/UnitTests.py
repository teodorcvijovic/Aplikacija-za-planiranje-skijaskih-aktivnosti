import datetime

from django.test import TestCase
from .models import *
from django.contrib.auth.models import Group

# Create your tests here.

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

