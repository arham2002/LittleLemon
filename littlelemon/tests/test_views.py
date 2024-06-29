from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status



class MenuViewTest(TestCase):
  def setup(self):
    self.item1 = Menu.objects.create(title="LaysChips", price=40, inventory=100)
    self.item2 = Menu.objects.create(title="Pizza", price=50, inventory=100)
    self.item3 = Menu.objects.create(title="GarlicBread", price=30, inventory=100)
    self.item4 = Menu.objects.create(title="Cake", price=80, inventory=100)
    print(f'Created: {self.item1}, {self.item2}, {self.item3}')
    