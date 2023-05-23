import requests
from send_email import send_email

api_key = "a098ebc08c7c42f8a1a4873b34233167"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-23&sortBy=publishedAt&apiKey=a098ebc08c7c42f8a1a4873b34233167"

#make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
    
body = body.encode("utf-8")    
send_email(message=body)