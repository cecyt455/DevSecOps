import requests
import json
import argparse
import os

url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = os.environ ["api_key_ccy"]

def upload (file_report, type_scan):
    headers = {
        'accept': 'application/json',
        'Authorization':api_key
    }
    
    report = {
        'file': open(file_report, 'rb')
    }
    
    body = {
        'active': True,
        'verified': True,
        'scan_type': type_scan,
        'test_title': 'ccy',
        'product_name': 'WebGoat',
        'product_type_name': 'Research and Development',
        'engagement_name': 'cecy'
    } 
    
    t = requests.post(url_api.format(method='import-scan/'), data = body, files = report, headers = headers, verify = False)

    print(t.status_code)
    if t.status_code == 201:
        print(json.dumps(t.json(), indent=4))
       
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser() #es una interfaz de un argumento dentro del script.
    
    parser.add_argument('--file', '-f', dest='file',help='Nombre del Reporte', required=True)
    parser.add_argument('--type-scan', '-t', dest='type_scan',help='Nombre del escaner', required=True)
    
    args = parser.parse_args()
    # get_products()  # Puedes llamar a esta función aquí si es necesario
    # create_product()
    upload(args.file, args.type_scan)