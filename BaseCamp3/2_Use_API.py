# Import requests module to make http requests
# import requests
import json

# # The URL and the query params, as indicated by the API spec / doc.
# # Refer https://rapidapi.com/hub
# url = "https://real-time-news-data.p.rapidapi.com/search"
# querystring = {"query":"AI Research","limit":"10","time_published":"anytime","country":"US","lang":"en"}

# # Add Headers to the request
# headers = {
# 	"x-rapidapi-key": "aaf2f390b7msheaa8d215f651e4p14658jsnfd40ab2b478",					   
# 	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
# }

# # Place a request and receive the response
# response = requests.get(url, headers=headers, params=querystring)
# response_data = response.json ()

# # Align better the JSON content
# print(json.dumps(response_data, indent=4))

import requests

url = "https://movies-ratings2.p.rapidapi.com/ratings"

querystring = {"id":"tt0111161"}

headers = {
	"x-rapidapi-key": "041adcc2d9msh3ff39b341362615p147409jsn6a231a6ddb42",
	"x-rapidapi-host": "movies-ratings2.p.rapidapi.com"
}
# Place a request and receive the response
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
