import requests
from bs4 import BeautifulSoup
import pandas as pd


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}


#looping through page 1 to 5

pages=[1,2,3,4,5]
container=[]

for page in pages:

    Base_url=f"https://nigeriapropertycentre.com/for-sale/houses/showtype?page={page}"


    r=requests.get(Base_url, headers=headers)
    print(r.status_code)
    soup=BeautifulSoup(r.text, 'html.parser')

        # grabbing relevant contents from soup

    contents=soup.find_all('div', class_='wp-block-content clearfix text-xs-left text-sm-left')
        #extracting apartment, price, location and link to item
    
    store={}
    for item in contents:
        Apartment_type=item.find('h4').text
        Price=item.find('span',class_='pull-sm-left').get_text().strip().replace('\n', " ,")
        Location=item.find('address', class_='voffset-bottom-10').get_text().strip().replace('\n\n\n', " ,")
        link_to_property=('https://nigeriapropertycentre.com'+item.find('a' , href=True).get('href'))
        contacts=item.find('span',class_='marketed-by pull-right hidden-xs hidden-sm text-right').get_text().strip().replace('\n', "").split('\xa0')[-1]
            
        store={

            'apartment_type':Apartment_type,
            'price':Price,
            'location':Location,
            'link_to_property':link_to_property,
            'contacts':contacts
                
        }

        container.append(store)

#     print(container)
# print(len(container))

df=pd.DataFrame(columns=['apartment_type','price','location','link_to_property','contacts'])
df=pd.DataFrame(container)
#print(df.head())
df.to_csv('extract.csv')
