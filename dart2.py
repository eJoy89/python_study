import requests

api_key = '1b71ebc44b5343892c2b050c94121db21de94eb2'
url = 'https://opendart.fss.or.kr/api/list.json'

# 파라미터에 API 키 추가
params = {
    'crtfc_key': api_key,
    'bgn_de': '20221117',
    'end_de': '20230117',
    'corp_cls': 'Y',
    'page_no': '1',
    'page_count': '100',
    'pblntf_ty': 'B' 
}
pblntf_ty_mapping = {
    'A': '정기공시',
    'B': '주요사항보고',
    'C': '발행공시',
    'D': '지분공시',
    'E': '기타공시',
    'F': '외부감사관련',
    'G': '펀드공시',
    'H': '자산유동화',
    'I': '거래소공시',
    'J': '공정위공시',
}

response = requests.get(url, params=params)

# 응답 확인
if response.status_code == 200:
    data = response.json()
    print(data)

    # Print only 'pblntf_ty_meaning'
    pblntf_ty_param = params.get('pblntf_ty', '')
    pblntf_ty_meaning = pblntf_ty_mapping.get(pblntf_ty_param, 'Unknown')

    print(f'pblntf_ty meaning: {pblntf_ty_meaning}')

    # Print each item in the 'list'
    result_list = data.get('list', [])
    for item in result_list:
        print(f"Corp Name: {item['corp_name']}")
        print(f"Stock Code: {item['stock_code']}")
        print(f"Report Name: {item['report_nm']}")
        print(f"Receipt Number: {item['rcept_no']}")
        print(f"Filer Name: {item['flr_nm']}")
        print(f"Receipt Date: {item['rcept_dt']}")
        print(f"Remarks: {item['rm']}")
        print('\n' + '-'*50 + '\n')

else:
    print(f"Error {response.status_code}: {response.text}")
data = response.json()

# 'list' 키에 해당하는 값 가져오기
result_list = data.get('list', [])

# 'corp_name' 출력
# for item in result_list:
#     corp_name = item.get('corp_name', '')
#     print(f'Corp Name: {corp_name}')