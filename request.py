#import requests
import requests

#define url and required parameters
url = "https://randomuser.me/api/?results=100&gender=male"

#create var response to store response from http
response = requests.get(url)

#access data
if response.status_code == 200:
    data = response.json()["results"]
    male_users = [user["name"]["first"] + " " + user["name"]["last"] for user in data]
    print("Top 100 male users:")
    print("\n".join(male_users))
else:
    print("Error accessing API:", response.status_code)