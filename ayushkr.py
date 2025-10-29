def swap_first_last(num):
    temp=num
    count=0
    ldigit=num%10
    while temp>0:
        count+=1
        temp//=10
    power=10**(count-1)
    fdigit=num//(power)
    mdigits=(num%(power))//10
    final=ldigit*power+mdigits*10+fdigit
    return final
