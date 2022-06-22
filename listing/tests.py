from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Comment, Business,Profile,Post
# Create your tests here.


class BusinessTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        
        self.business = Business(name='jirani',image='jirani.png',pub_date='21,Jun,2022',user='1',NeighborHood='1')
    '''
    test instance of business
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
        '''
        test for save instance of business
        '''
    def test_save_business(self):
        self.business.save_business()
        name = Business.objects.all()
        self.assertTrue(len(name)>0)



class profileTestCLass(TestCase):
    '''
    setup self instance of profile
    '''
    def setUp(self):
        self.prof = Profile(Bio='We are in this together')
    
    ''' 
    test instance of profile
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_profile(self):
        self.prof.save_profile()
        bio = Profile.objects.all()
        self.assertTrue(len(bio)>0)



