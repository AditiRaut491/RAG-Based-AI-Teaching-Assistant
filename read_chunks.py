import requests
import os
import json
# ollama local instance port
def  create_embeddings(text):
    r = requests.post("http://localhost:11434/api/embeddings", json = { # here model and prompt comes for payload
    "model": "bge-m3",
    "prompt": text # sentence which we want to convert into embeddings
    }) 
    # print(r.json())
    embedding = r.json()["embedding"]
    return embedding

jsons = os.listdir("jsons")
print(jsons)

for json_file in jsons:
    with open (f"jsons/{json_file}") as f:
        content = json.load(f)
    for chunk in content["chunks"] :
        print(chunk)
    break
# print(embedding[0:5])
# a = create_embeddings("Aditi is a good gurlll !!!!!!")
# print(a)





# Basically what's happening here is that running ollama instance give prompt by using bge-m3 model