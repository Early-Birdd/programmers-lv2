def solution(phone_book):
    hashmap = {}
    for phone_number in phone_book:
        hashmap[phone_number] = 1

    for p_number in phone_book:
        jd = ""
        for n in p_number:
            jd += n
            if jd in hashmap and jd != p_number:
                return False

    return True

#회고
#hash의 사용법 숙지하기 - hash 저장법과 조회법을 숙지하자