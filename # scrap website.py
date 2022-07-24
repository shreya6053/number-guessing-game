# scrap website 
#  use API 
# HTML web scraping using some tool like bs4

# pip install 
# pip install bs4
# pip install html5lib

import requests
import shutil
from bs4 import BeautifulSoup

urls =  ["https://books.toscrape.com/", "https://books.toscrape.com/catalogue/page-2.html", "https://books.toscrape.com/catalogue/page-3.html", "https://books.toscrape.com/catalogue/page-4.html","https://books.toscrape.com/catalogue/page-5.html"] 

i = 1 

for url in urls :

    page = requests.get(url)
    soup = BeautifulSoup(page.content , "html.parser")

    books = soup.findAll("li" , {"class" :"col-xs-6 col-sm-4 col-md-3 col-lg-3" })
   

    for book in books :
        bookTitle = book.article.h3.a["title"]
        print("Title of the books is " + bookTitle)

        bookPrice = book.find("p" , {"class" :"price_color"})
        print("Price of book is " + bookPrice.text)
        
        bookRating = book.article.p["class"]
        print("This book has " + bookRating[1] + " stars ")

        bookUrl = book.article.div.a["href"]
        print("URL of this book is https://books.toscrape.com/" + bookUrl)

        imageUrl = book.article.div.a.img["src"]

        fullUrl = urls[0] + imageUrl


        imageRequest = requests.get(fullUrl,stream = True ).content
        
        with open ("C:\\Users\\HP Pavilion\\OneDrive\\Documents\\images\\file" + str(i) + ".jpg",'wb' ) as file:
            
            file.write(imageRequest)
            
            i = i+1
    
