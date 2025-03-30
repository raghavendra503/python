import requests
with open("companies.txt") as fobj:
    for line in fobj:
        url = line.strip()
        resp = requests.get(url)
        if(resp.status_code ==200):
            print("success")
