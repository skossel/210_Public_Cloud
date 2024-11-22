import requests

url = "quotes-244212-skossel.apps.exoscale-ch-gva-2-0.appuio.cloud"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

while True:
    response = requests.get(url, headers=headers)  # GET-Request
