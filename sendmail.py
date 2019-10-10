import requests
from bs4 import BeautifulSoup
import smtplib
import time
url='https://www.amazon.in/Puma-Azalea-Peacoat-Running-Shoes-3-37079403_3/dp/B07SZ8QH3P/ref=sr_1_5?dchild=1&field-pct-off-with-tax=50-&fst=as%3Aoff&pf_rd_i=1983578031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=cacb5e09-7d82-4873-89b6-51629eb9c51d&pf_rd_r=Q2T338TM790QZQ3H9GXD&pf_rd_s=merchandised-search-12&qid=1569991225&refinements=p_n_feature_nineteen_browse-bin%3A11301363031%2Cp_89%3APuma&rnid=3837712031&s=shoes&sr=1-5'
user={'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
page=requests.get(url,headers=user) 
soup=BeautifulSoup(page.content,'html.parser') 

search_name=soup.find(id='productTitle')
search_price=soup.find(id='priceblock_ourprice')
print(search_name.getText().strip()) 

price=search_price.getText() 

p1=price.split(',')

p2=''.join(p1)

s=p2[2:6]

print("Price of the shoe is:",(s)) 

email=input("Enter yout email id: ")
password=input("Please enter your password: ")

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    subject="Price fell down"
    body="Check the amazon link:"+url 
    message="Subject:"+subject+"\n\n"+body
    server.sendmail(email,'500060041@stu.upes.ac.in',message)
    print("Email has been sent!")

if int(s)>=1599:
    send_mail()
      
            
    
