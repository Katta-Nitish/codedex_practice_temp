import requests
API_KEY="Your api key"
url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
headers={
  "Content-Type":"application/json"
}
payload={
  "contents":[{
    "parts":[{"text":"Explain about PATCH in requests library in python"}]
  }]
}
response=requests.post(url,headers=headers,json=payload)
if response.status_code == 200:
    data = response.json()
    
    # We have to dig deep to find the text!
    # Structure: candidates[0] -> content -> parts[0] -> text
    try:
        answer = data['candidates'][0]['content']['parts'][0]['text']
        print("\nGemini says:")
        print(answer)
    except KeyError:
        print("Got a response, but couldn't find the text. Here is the raw data:")
        print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
