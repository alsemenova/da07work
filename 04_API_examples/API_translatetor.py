import requests
textin = input("Enter the text you want to translate: ")
response = requests.get(
    "https://api.mymemory.translated.net/get",
        params={
            "q": textin,
            "langpair": "en|it"
    }
)

data = response.json()

print(data["responseData"]["translatedText"])