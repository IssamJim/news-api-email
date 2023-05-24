import requests
from send_email import send_email

topic= "tesla"

api_key = "a098ebc08c7c42f8a1a4873b34233167"
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
    "from=2023-04-23&"\
    "sortBy=publishedAt&"\
    "apiKey=a098ebc08c7c42f8a1a4873b34233167&"\
    "language=en"

#make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" \
            + body + article["title"] + "\n" \
            + article["description"] + "\n"\
            + article["url"] + 2*"\n"
    
body = body.encode("utf-8")    
send_email(message=body)