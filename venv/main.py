import requests

api_key = "a098ebc08c7c42f8a1a4873b34233167"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-23&sortBy=publishedAt&apiKey=a098ebc08c7c42f8a1a4873b34233167"

#make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

