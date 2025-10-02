import requests

HF_API_KEY = "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"
api_url = "https://api-inference.huggingface.co/models/Tejas3/distillbert_base_uncased_amazon_food_review_300"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

text = input("Just write down anything: ")
response = requests.post(api_url, headers=headers, json={"inputs": text})

if response.status_code == 200:
    classification = response.json()
    if isinstance(classification, list):
        label = classification[0][0]["label"]
        print(f"Predicted label: {label}")
    else:
        print("Unexpected response:", classification)
else:
    print(f"Error: {response.status_code}")

