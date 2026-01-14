import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.head(url)
if response.status_code==200:
  #data=response.json()
  #print(f"Setup:{data['setup']}")
  #print(f"punchline:{data['punchline']}")
  print(response)
else:
  print("Something went wrong")