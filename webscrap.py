from bs4 import BeautifulSoup

with open("webscrap.html", "r") as website:
    content_html = website.read()

    web = BeautifulSoup(content_html, "lxml")
    
    list_items = web.find_all("div", class_="card")
    for list in list_items:
        list_li = list.li.text
        div = list.div.text

        print(div)
        print(list_li)

    lists = web.find_all("li")
    for list in lists:
        print(list.text)


        
