import requests
response = requests.get(url="https://api.kanye.rest")
#print(response)

#response is a requests's method
#[200] - response codes, like 404 not found error
#1## : hold on
#2## : here you go
#3## : Go away
#4## : you screwed up
#5## : i screwed up

print(response.status_code)
response.raise_for_status()

data = response.json()
print(data)
