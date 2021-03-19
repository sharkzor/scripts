import requests
import ../secrets/pass.py

url = 'https://10.0.0.9/api/?type=keygen&user=' + username + '&password=' + password
print(url)


#x = requests.post(url, data = myobj)
x = requests.get(url, verify=False)

print(x.text)