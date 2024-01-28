# import requests

# payload = {'key1': 'value1', 'key2': 'value2'}

# r = requests.get('https://httpbin.org/get', params=payload)

# print(r.url) 

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
import requests
import ssl

url = 'https://apis.data.go.kr/6300000/openapi2022/kinderschInfo/getkinderschInfo?serviceKey=jDDorJlGEy5KVTpmpQ+YZwmN5QwdCO+3sLo1RvCg9I8bwv1YIO3Oo+jXLG+eFaGq3IrOiUh5bNVgSsbLq3y+zQ==&gu=N&pageNo=2&numOfRows=5'

# Specify the desired TLS version (TLSv1.2 in this case)
tls_version = ssl.PROTOCOL_TLSv1_2

# Create an SSLContext with the specified TLS version
ssl_context = ssl.SSLContext(tls_version)

# Disable SSL verification (you may want to remove this in production)
ssl_context.verify_mode = ssl.CERT_NONE

# Create a custom adapter with the SSLContext
class TLSSSLAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = kwargs.pop('ssl_context', None)
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

# Specify the custom adapter in the adapters parameter
response = requests.get(url, verify=True, headers={'Connection': 'close'}, timeout=5, cert=None, proxies=None, adapters={'https://': TLSSSLAdapter(ssl_context=ssl_context)})

print(response.text)
