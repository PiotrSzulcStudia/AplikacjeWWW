import urllib
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from vote2.models import Commission, District
from _scrapper import *

class Command(BaseCommand):
	help = ''
	base_url = "http://prezydent2010.pkw.gov.pl/PZT/PL/WYN/W/index.htm"

	def handle(self, *args, **options):
		self.delete_data()
		scrap_page(base_url)
		#scrap_page(base_url, BaseDistrict)

	def delete_data(self):
		District.objects.all().delete()
		Commission.objects.all().delete()
