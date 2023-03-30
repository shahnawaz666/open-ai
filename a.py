import openai
query= " a cartoon playing chess  "

# insert  your api key here
openai.api_key="..."

response= openai.Image.create(
    prompt=query, 
    n=2,
    size="1024x1024",
)
print(response["data"][0]["url"])