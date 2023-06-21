def percentage_of(num, of_num):
    try:
        answer = (num/of_num) * 100
    except ZeroDivisionError:
        answer = 0 # return 0 in case answer is equal to zero
    return round(answer, 1) # return answer rounded to 1 decimal place