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
    second_item.text = '두 번째 아이템'
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

  def test_uses_home_template(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')

  def test_home_page_can_save_a_POST_request(self):
    response = self.client.post('/', data={'item_text': '신규 작업 아이템'})
    self.assertEqual(Item.objects.count(),1)

    new_item = Item.objects.first()
    self.assertEqual(new_item.text, '신규 작업 아이템')

    self.assertIn(response.content.decode(), '신규 작업 아이템')

  def test_home_page_only_save_items_when_necessary(self):
    request = HttpRequest()
    home_page(request)
    self.assertEqual(Item.objects.count(),0)

  def test_home_page_redirects_after_POST(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['item_text'] = '신규 작업 아이템'

    response = home_page(request)

    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], '/')


# Create your tests here.
