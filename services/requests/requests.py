import requests
import random
import time

for i in range(55):
    params = {'cus_id': 157}
    data = {
        "age":          random.randint(1,65),
        "job":          "housemaid",
        "marital":	    "married",
        "education":	"secondary",
        "default":	    "no",
        "balance":	    random.randint(5000,120000),
        "housing":	    "yes",
        "loan":	        "no",
        "contact":	    "cellular",
        "day":	        random.randint(3,15),
        "month":	    "jun",
        "duration":     579,
        "campaign":     3
    } 
    
    response = requests.post('http://score-model:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())