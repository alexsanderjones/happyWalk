from bs4 import BeautifulSoup
import requests
import pandas as pd

happy_site = "https://wallethub.com/edu/happiest-places-to-live/32619"
happy_page = requests.get(happy_site)
soup = BeautifulSoup(happy_page.text, 'html.parser')

happy_table = soup.find('table')
headers = []
for i in happy_table.find_all("th"):
 title = i.text
 headers.append(title)

happy_data = pd.DataFrame(columns = headers)
for j in happy_table.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(happy_data)
 happy_data.loc[length] = row

happy_data.to_csv("happy_data.csv", index = False)


