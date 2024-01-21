import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('https://httpbin.org/get', params=payload)

print(r.url) 

# import requests
# url = "http://date.jsontest.com/"


# response = requests.get(url)
# response = requests.post(url)
# response = requests.delete(url, data={'key':'value'})
# response = requests.head(url)
# response = requests.options(url)


# def get_json(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         json_data = response.json()
#         return json_data
#     else:
#         print("Error accessing the URL:", response.status_code)
#         return None

# # Example usage
# data = get_json(url)
# if data:
#     print(data)
