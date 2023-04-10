# API -> Application Programming Interface
# 애초에 프로그래밍용이어서 파싱을 할 필요도 없고 용량도 적다!
# UI -> User Interface 와 반대되는 말! 

import requests
# 그래도 요청은 해야함.

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1058'

res = requests.get(url).json()

print(res)