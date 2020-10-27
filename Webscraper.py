import requests
from bs4 import BeautifulSoup
from lxml import html
import selenium

source = requests.get('https://www.ovulation-calculators.com/coronavirus/gb/leicester/#reports')
html_text = source.text
soup = BeautifulSoup(html_text, "html.parser")

table = soup.find("table")
# print(table.prettify())
for x in table.find_all("tr"):
    for z in x.find_all("td"):
        print(z.text)



# print(soup.prettify ())

#print(soup.title)

# with open("PSP.html") as html_file:
#     soup = BeautifulSoup(html_file, "lxml")  # "lxml"
#
# # match = soup.find("div", class_="writing_container")
# # a=1
# # for text in match.find_all("p"):
# #     print(f"{a} {text}")
# #     a+=1
#
# for para in soup.find_all("div", class_="writing_container"):
#     for text in para.find_all("p"):
#         print(text.text)
#




