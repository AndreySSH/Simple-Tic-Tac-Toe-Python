sum_ = 0
sqr_ = 0

while True:
    num = int(input(''))
    sum_ += num
    sqr_ += num*num
    if sum_ == 0:
        print(sqr_)
        break
