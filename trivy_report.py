import requests
import json

url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def get_products():
    headers = {
        'accept' : 'application/json',
        'Authorization' : api_key 
    }
    
    r = requests.get(url_api.format(method='products'), headers = headers, verify = False)
    
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=4))
        
    
def create_product():
    headers = {
        'accept' : 'application/json',
        'Content-Type': 'application/json',
        'Authorization' : api_key 
    }
    
    body = {
         "tags": [
             ""
        ],    
        "name": "cecy",
        "description": "bunny",
        "prod_numeric_grade": 2147483647,
        "business_criticality": "very high",
        "platform": "web service",
        "lifecycle": "construction",
        "origin": "third party library",
        "user_records": 2147483647,
        "revenue": "04652832.",
        "external_audience": True,
        "internet_accessible": True
    }
    
    q = requests.post(url_api.format(method='products'), headers = headers, json = body, verify = False)
    
    print(q.status_code)
    
    if q.status_code == 201:
        print(json.dumps(q.json(), indent=4))
        
def trivycecy():
    headers = {
        'accept' : 'application/json',
        'Authorization' : api_key 
    }
    
    reports = {
        'file': open('prueba.json', 'rb')
    }
    
    body = {
        'active': True,
        'verified': True,
        'scan_type': 'Trivy Scan',
        'test_title': 'ccy',
        'product_name': 'WebGoat',
        'engagement_name': 'prueba'
    } 
     
    t = requests.post(url_api.format(method='import-scan/'), data = body, files = reports, headers = headers, verify = False)

    print(t.status_code)
    if t.status_code == 201:
        print(json.dumps(t.json(), indent=4))
        
 
if __name__ == '__main__':
    #get_products()
    #create_product()
    trivycecy()