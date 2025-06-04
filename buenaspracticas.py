def math(*nums):
    suma= sum(nums)

    avg=suma/len(nums)

    greater= nums[1]
    for i in nums:
        if i>greater:
            greater=i
    return suma,avg,greater       


sum, prom, mayor = math(1,2,3,4)


print(f"La suma de los números es: {sum}, el promedio es: {prom} y el número mayor es: {mayor}")
