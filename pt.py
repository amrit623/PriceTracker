import requests
from bs4 import BeautifulSoup

URL = 'https://www.aliexpress.com/item/32999977516.html?spm=a2g01.12617084.fdpcl001.1.7bbb8lFQ8lFQkJ&gps-id=5547572&scm=1007.19201.130907.0&scm_id=1007.19201.130907.0&scm-url=1007.19201.130907.0&pvid=8297308c-e867-4374-b5f6-f6b34df7edac'

headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()

print(title.strip())