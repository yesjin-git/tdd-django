from django.template.loader import render_to_string
from django.test import TestCase, Client
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item

class ItemModelTest(TestCase):

  def test_saving_and_retrieving_items(self):
    first_item = Item()
    first_item.text = '첫 번째 아이템'
    first_item.save()

    second_item = Item()
    second_item.test = '두 번째 아이템'
    second_item.save()

    saved_items = Item.objects.all()
    self.assertEqual(saved_items.count(), 2)

    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]

    self.assertEqual(first_saved_item.text, '첫 번째 아이템')
    self.assertEqual(second_saved_item.text, '두 번째 아이템')


class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  # CSRF 에 따라 다르게 나오는 부분을 처리해줘야 하는데 어떻게 해야되는지 모르겠음. 

  # def test_home_page_returns_correct_html(self):
  #   request = HttpRequest()
  #   response = home_page(request)
  #   # expected_html = render_to_string('home.html')
  #   csrf_client = Client(enforce_csrf_checks=True)
  #   expected_html = csrf_client.get('/').content
  #   self.assertEqual(response.content.decode(), expected_html.decode())

  # def test_home_page_can_save_a_POST_request(self):
  #   request = HttpRequest()
  #   request.method = 'POST'
  #   request.POST['item_text'] = '신규 작업 아이템'

  #   response = home_page(request)

  #   csrf_client = Client(enforce_csrf_checks=True)
  #   expected_html = csrf_client.post('/', {'item_text': '신규 작업 아이템'}).content
  #   self.assertIn('신규 작업 아이템', response.content.decode())
  #   # expected_html = render_to_string(
  #   #   'home.html',
  #   #   {'new_item_text': '신규 작업 아이템'}
  #   # )
  #   self.assertEqual(response.content.decode(), expected_html.decode())



# Create your tests here.
