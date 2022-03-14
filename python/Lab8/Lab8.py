import requests, re
from bs4 import BeautifulSoup

url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
webpage = requests.get(url, headers=agent)

soup = BeautifulSoup(webpage.content, "lxml")



try: 
	title = soup.find("h1", attrs={"class": 'heading-5 v-fw-regular'})
	titleValue = title.string
	print("Product Title: ", titleValue)
	
	costDiv = soup.find("div" , attrs={"class": 'priceView-hero-price priceView-customer-price'})
	for cost in costDiv.find_all('span', attrs={"aria-hidden": 'true'}):
		print("Product Cost: ", cost.string)
	
	statusDiv = soup.find("div", attrs={"class": 'v-m-top-m v-p-top-m v-border-next v-border-top'})
	for status in statusDiv.find_all('strong'):
		if status.string != "Sold Out":
			print("Status: In Stock")
		else:
			statusValue = status.string
			print("Status: ", statusValue)
	
	
	
		
except AttributeError: 	
	print("Error.")
