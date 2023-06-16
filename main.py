from bs4 import BeautifulSoup
import requests
import pandas as pd

# excel column to list
df = pd.read_excel("E:/ASI/KEYWORDS.xlsx")
ali_links = df["name"].tolist()
print(ali_links)

# scrape keywords from the link

for link in ali_links:

    response = requests.get(link)
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")
    result = soup.find("meta", attrs={"name": "keywords"})["content"]
    print(result)
