# from bs4 import BeautifulSoup

# html = '''
# <html>
# <h1>여기 가지고오기</h1>
#     <table border=1> 
#         <tr>
#             <td> 항목 </td> 
#             <td> 2013 </td> 
#             <td> 2014 </td> 
#             <td> 2015 </td>
#         </tr> 
#         <tr>
#             <td> 매출액 </td> 
#             <td> 100 </td> 
#             <td> 200 </td>
#             <td> 300 </td>
#         </tr> 
#     </table>
# </html> 
# '''
# soup = BeautifulSoup(html, 'html5lib') 
# result = soup.select('h1') 
# print(result)
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.kcar.com/'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

elements_with_class = soup.find_all(class_='title')

for element in elements_with_class:
    print(element.text)

# text_content_list = [element.text.strip() for element in elements_with_class]

# df = pd.DataFrame({'Text Content': text_content_list})

# df.to_excel('output.xlsx', index=False)


# if response.status_code == 200:
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')

#     elements_with_class = soup.find_all(class_='txtContentText')

#     for element in elements_with_class:
#         print(element.text)
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
