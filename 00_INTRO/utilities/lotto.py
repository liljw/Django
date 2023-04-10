from . import crawling  # ./crawling.py 를 가져온다.
# import로 모듈 가져올 수 있는 건 같은 파일 경로 내에 위치하고 있어야 가능!
import random

def lotto():
    real_numbers, bonus_number = crawling.get_real_lotto()
    this_week_numbers = real_numbers, bonus_number
    real_numbers = set(real_numbers)

    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers = set(lucky_numbers)

    intersection_number = list(lucky_numbers & real_numbers)

    if len(intersection_number) == 6:
        return "1등"
    if len(intersection_number) == 5:
        if bonus_number in real_numbers:
            return "2등"
        else:
            return "3등"
    if len(intersection_number) == 4:
        return "4등"
    if len(intersection_number) == 4:
        return "5등"
    else:
        return "꽝"



# 1등 : lucky_numbers 랑 real_numbers가 똑같아야 함. 
# 2등 : 5개 같음 + 나머지 1개가 bonus 넘어여야함.
# 3등 : ln, rn 5개 같음 
# 4등 : 4개 같음
# 5등 : 3개 같음
