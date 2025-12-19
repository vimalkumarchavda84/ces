import requests
import pytest

url='https://api.restful-api.dev/'
response=requests.get(url=url+'/objects')
print(response.status_code)
print (response.text)
##get all ids in to response
jsn=response.json()
#### second Tcs
for i in jsn:
    print(i)
    print(i['id'])
    id=i['id']
    response=requests.get(url=url+'/objects/'+str(id))
    print(response.status_code)
    print (response.text)

