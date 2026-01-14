import requests

API_KEY = "AIzaSyAXAlnURwCMALRALpSS0F7KAyshBlQwDL8" # Your key

# We use the 'list models' endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

print("Checking available models...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Here are the models you can use:")
    for model in data.get('models', []):
        # We only want models that support 'generateContent'
        if "generateContent" in model['supportedGenerationMethods']:
            # The name usually comes like "models/gemini-pro", we just want the last part
            print(f" - {model['name']}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)