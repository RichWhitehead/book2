from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class BookTest(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(username='testuser1', password='password')
    
    testuser1.save()
    
    testpost = Post.objects.create(
      author=testuser1,
      title='To Kill A Mocking Bird',
      body= 'You never really understand a person until you consider things from his point of view.'
    )
    
    testpost.save()
    
    
def test_book_content(self):
  post = Post.objects.get(id=1)
  actual_author = str(post.author)
  actual_title = str(post.title)
  actual_body = str(post.body)
  
  self.assertEqual(actual_author, 'testuser1')
  self.assertEqual(actual_title, 'To Kill A Mocking Bird')
  self.assertEqual(actual_body, 'You never really understand a person until you consider things from his point of view.')
