
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as Ureq

from tkinter import *



window = Tk()
window.geometry("1000x400")
window.title("Simple_WebScraper -AdamCM")
frame1 = Frame(window, width = 300, height = 340, bg = "grey")
frame1.place(x= 10, y  = 50)
frame2 = Frame(window, width = 660, height = 1000, bg = "grey")
frame2.place(x = 330, y = 50)

#-----------------------------------------SETUP FOR LABEL
brands = Label(window, text = "BRAND", width = 20 ,bg = "white")
brands.place(x = 340, y = 20)
price = Label(window, text = "PRICE", width = 20 ,bg = "white")
price.place(x = 500, y = 20)
ship = Label(window, text = "TYPE-SHIP", width = 20 ,bg = "white")
ship.place(x = 660, y = 20)
titles = Label(window, text = "TITLES", width = 20 ,bg = "white")
titles.place(x = 820, y = 20)



def display():
    my_url = "https://www.newegg.com/global/ph-en/p/pl?d=graphics+card"  
    
    
    #opening up connection, grabbing the page
    uClient = Ureq(my_url)
    
    page_html = uClient.read()
    uClient.close()
    #html_parsing
    page_soup = Soup(page_html, "html.parser")
    #grabe each         
    containers = page_soup.findAll("div", {"class": "item-container"})
    
     
     
    #print(len(containers))
    #print(containers[4])
    #container = containers[4]
    fileName = "Online_Sales.csv"
    f = open(fileName, "w")
    
    headers = "Brand    , Title                                                      \n"
    
    f.write(headers)
    for container in containers[4:]:
        brand_container = container.findAll("a", {"class": "item-brand"})
        
        brand = brand_container[0].img["title"] #brand name
        title = container.a.img["title"] #Name of selling
        
        print("Brand_Name    :" + brand)
        print("Title         :" + title)
        
        
        
        brands = Listbox(frame2, text = "Brand_Name : " + brand  , width = 20)
        brands.grid(pady = 2, padx = 2, column = 0 )
        
        #titles = Label(frame2, text = "Titles : " + title, width = 50)
        #titles.grid()
            
            
        f.write(brand  + "              " +  ", " + title + "                                          " + "\n")
    f.close()
    

def click():
    
    Display = Label(window, text = display)
    Display.pack()


url = Entry(frame1, text = "seacrh", width = 30 , bg= "LightBlue1")#concatinate to url
url.place(x = 50, y = 20)

search = Button(frame1, command = display, text ="Search", width = 20)
search.place(x = 65, y = 50)
#scrollbar.config(command = click)

window.mainloop()