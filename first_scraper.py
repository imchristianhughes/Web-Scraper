import requests
import bs4

#setting a main URL
main_url = 'https://webscraper.io/test-sites/e-commerce/allinone/product/{}'

#assigning list for each category and a starting page number
titles = []
prices = []
page = 1

for page in range(486, 1000):
       
    scraping_url = main_url.format(page)

    res = requests.get(scraping_url)
    
    if 'Not Found' not in res.text:
        
        soup = bs4.BeautifulSoup(res.text, 'lxml')
            
        price = soup.select('h4')[0]

        item_title = soup.select('h4')[1]

		prices.append(price.text)

		titles.append(item_title.text)

        print(f'\n{item_title.text} costs {price.text}')
     
        page += 1

    else:
    	break
        
    
#item_dict = dict(zip(titles, prices))





    

    


    

		







		

