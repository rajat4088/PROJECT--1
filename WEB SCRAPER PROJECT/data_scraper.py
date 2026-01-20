import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://webscraper.io/test-sites/e-commerce/allinone"
req = requests.get(url)
#print(req)x

soup = BeautifulSoup(req.text, features="html.parser")
#print(soup)
#productCards = soup.find_all(name="div",class_= "col-md-4 col-xl-4 col-lg-4")
#print(len(productCards))

titles = [item.text.strip() for item in soup.find_all("a", class_="title")]
prices = [item.text.strip() for item in soup.find_all("h4", class_="price float-end card-title pull-right")]
descriptions = [item.text.strip() for item in soup.find_all("p", class_="description card-text")]
noOfReviews = [item.text.strip() for item in soup.find_all("p", class_="review-count float-end")]
#creating a dataframe
df = pd.DataFrame({
    "Title" : titles,
    "Description" : descriptions,
    "Price" : prices,
    "Reviews" : noOfReviews
})
print(df)

df.to_excel("laptops_data.xlsx", index=False)
print("Data has been save successfully.!")


