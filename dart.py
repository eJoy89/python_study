import dart_fss as dart

api_key = '1b71ebc44b5343892c2b050c94121db21de94eb2'
dart.set_api_key(api_key=api_key)

corp_list = dart.get_corp_list()
samsung = corp_list.find_by_corp_name('LG전자',exactly=True)[0]

fs = samsung.extract_fs(bgn_de='20120101')

fs.save()

print(samsung)