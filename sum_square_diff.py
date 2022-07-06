def sum_squares_of_numbers(a):
    sum=0
    for i in range(1,a+1):
        sum=i**2+sum
    return sum
def square_of_sum_numbers(a):
    sum=0
    for i in range(1,a+1):
        sum += i
    sum=sum**2
    return sum
def sum_square_diff(a):
    return square_of_sum_numbers(a)-sum_squares_of_numbers(a)
print(sum_square_diff(100))