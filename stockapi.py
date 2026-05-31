import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("FINNHUB_API_KEY")
def fetch(company):
    url ="https://finnhub.io/api/v1/quote"
    url2='https://finnhub.io/api/v1/stock/profile2'
    url3 = "https://finnhub.io/api/v1/search"

    params = {
    "q": company,
    "token": API_KEY
     }
    data0 = requests.get(url3, params=params).json()
    if not data0.get("result"):

        raise Exception("Company not found")

    symbol =(data0["result"][0]["symbol"])
    para = {
        "symbol": symbol,
        "token" :API_KEY
        }
    
    para2= {
        "symbol": symbol,
        "token" :API_KEY
        }
    data = requests.get(url,params= para).json()
    respo2 =requests.get(url2,params=para2)
    data2 =respo2.json ()
    
    
    if "error" in data:
        raise Exception(data["error"])

    if data.get("c") is None:
        raise Exception("Invalid response")
    
    current = data["c"]
    high = data["h"]
    low = data["l"]
    open_price = round(data["o"],3)
    prev_close = round(data["pc"],3)
  
    if current > prev_close:
          status ="Bullish 📈"
    else:
          status="Bearish 📉"
    if prev_close != 0:
        percentage_change = ((current - prev_close) / prev_close) * 100
    else:
        percentage_change = 0

    if "error" in data2:
        raise Exception(data2["error"])

    if data2.get('name') is None:
        raise Exception("Invalid response")
    name = data2['name']
    industry= data2['finnhubIndustry']
    weburl=data2["weburl"]
    return name,symbol,industry,weburl,current,high,low,open_price,prev_close,status,percentage_change
   
    
   

def main() :
    try:
      company = input("Enter company name:")

      name,symbol,industry,weburl,current ,high,low,open_price,prev_close ,status,percentage_change= fetch(company=company)
      print("Company:",name)
      print("Ticker:", symbol)
      print("Industry:",industry)
      print("Website url:",weburl)
      print("Current Price:", current)
      print("High:", high)
      print("Low:", low)
      print("Open Price:", round(open_price,2))
      print("Previous Close:", round(prev_close,2))
      print("Status:",status)
      print("Precentage Change:",round(percentage_change,3),"%")
    except Exception as e:
        print(str(e))

if __name__== "__main__":
     main()  
 