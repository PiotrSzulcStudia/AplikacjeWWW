import urllib
from bs4 import BeautifulSoup
from vote2.models import Commission, District

base_url = "http://prezydent2010.pkw.gov.pl/PZT/PL/WYN/W/index.htm"

def get_soup_wrapper(func):
	def func_wrapper(target_url):
		return BeautifulSoup(func(target_url), "html.parser")
	return func_wrapper

@get_soup_wrapper
def get_page(target_url):
	response = urllib.urlopen(target_url)
	pageText = response.read()
	response.close()
	return pageText

def log_create_model(func):
	# log_called = [0]

	def func_wrapper(name, parent):
		# log_called[0] = log_called[0] + 1
		# print(str(log_called) + ". " + name)
		print(name)
		return func(name, parent)

	return func_wrapper


@log_create_model
def create_district_model(name, parent):
	district = District(name=name, parentId=parent)
	district.save()
	return district

@log_create_model
def create_commision_model(name, parent):
	commission = Commission(name=name, parentId=parent)
	commission.save()


soup = get_page(base_url)

def scrap_page(page_url, parent=None, selector='td.col5 .link1'):
	try:
		soup = get_page(page_url)
	except URLError as e:
		print e.reason
		return

	for l in soup.select(selector):
		if (l['href'].startswith("..")):
			create_commision_model(l.contents[0], parent)
		else:
			scrap_page(base_url[:-9]+l['href'], create_district_model(l.contents[0], parent))
