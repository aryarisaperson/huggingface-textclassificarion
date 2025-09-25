import requests
from config import HF_API_KEY

def classify_text(text): 
    api_url="https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    headers={"Authorization": f"Bearer {HF_API_KEY}"}
    payload={"inputs" :text}
    response=requests.post(api_url, headers=headers, json=payload)
    return response.json()

if __name__=="__main__":
    sample_text=input("just write down anything")
    result=classify_text(sample_text)
    you_got_label=result[0][0]['label']
    score=int(result[0][0]['score']*100)
    print(f"We've detected that your text is {you_got_label.lower()}, with a score of {score}%!")


