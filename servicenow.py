
import requests

# Set the request parameters
url = 'https://dev69736.service-now.com//api/now/table/incident?sysparm_limit=10'
url1='https://dev69736.service-now.com//api/now/attachment/file?table_name=incident&table_sys_id=d71f7935c0a8016700802b64c67c11c6&file_name=test.txt'
user = 'admin'
pwd = 'xxxx'

# Set proper headers
headers = {"Accept": "application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

 # Decode the JSON response into a dictionary and use the data
print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())
print('Cookies', response.cookies)

headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, data="{'short_description':'Unable to connect to office wifi','assignment_group':'287ebd7da9fe198100f92cc8d1d2154e','urgency':'2','impact':'2','caller':'Abel Tuter'}")
# Check for HTTP codes other than 200
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data

print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())


data = open('test.txt', 'rb').read()
headers = {"Content-Type":"txt","Accept":"application/json"}
response = requests.post(url1, auth=(user, pwd), headers=headers, data=data)
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data

print('Status:', response.status_code, 'Headers:', response.headers, 'Response:', response.json())
