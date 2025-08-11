import requests
# GoldAPI endpoint
gold_url = "https://www.goldapi.io/api/XAU/USD"
headers = {
	"x-access-token": "APİ"
}
gold_response = requests.get(gold_url, headers=headers)
gold_data = gold_response.json()
# You can now use gold_data as needed

# Frankfurter API endpoint
url = "https://api.frankfurter.dev/v1/latest?from=USD&to=TRY"

# API'den veriyi çek
response = requests.get(url)

# JSON formatına dönüştür
datapara = response.json()

# Kur bilgisi
usd_try = datapara["rates"]["TRY"]

print(f"1 USD = {usd_try}")

responsealtın = requests.get('https://www.goldapi.io/api/XAU/USD', headers=headers)
data = responsealtın.json()

# Altın fiyatı (ons cinsinden TRY)
#print("Ons Altın (USD):", data["price"])

# Gram altın hesaplama (1 ons = 31.1035 gram)
altin = data["price"]
#print("Gram Altın (USD):", round(gram_altin, 2))


hamaltın = altin * usd_try
gramaltın = (altin * usd_try) / 31.1035
print(f"Altının ham değeri: {hamaltın}, altının gram değeri: {gramaltın}dir")