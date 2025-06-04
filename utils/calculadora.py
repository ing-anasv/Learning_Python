#Modulo calculadora

def suma(*nums):
    return sum(nums)

def resta(*nums):
    res= nums[0]
    for i in nums[1:]:
        res= res - i
    return res

def mult(*nums):
    m= 1
    for i in nums:
        m= i*m
    return m

def div(*nums):
    numerador= sum(nums[:-1])
    denominador= nums[-1]

    if denominador==0:
        print("No se puede dividir por cero")
    else: 
        return numerador/denominador