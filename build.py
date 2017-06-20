def solution(list_of_nums):
    d = {"ODD": 0, "EVEN": 0}

    for i in list_of_nums:
        if i % 2 == 0:
            d['EVEN'] +=1
        else:
            d['ODD'] +=1

    return d
