function = eval("lambda x:" + input("Введите функцию:\n"))
limit = [float(s) for s in input("Введите отрезок:\n").split(" ")]
e = float(input("Введите точность:\n"))

def dichotomy(function, limit, e):

    '''
        Метод Дихотомии
                        '''

    x = (limit[0] + limit[1])/2    

    if abs(limit[0] - limit[1]) < e:
        return x

    else:        
        f1 = function(x-e/2)
        f2 = function(x+e/2)
        
        if f1 == f2:
            return x

        elif f1 > f2:
            return dichotomy(function, [x, limit[1]], e)

        elif f2 > f1:
            return dichotomy(function, [limit[0], x], e)
        
answer = dichotomy(function, limit, e)

print("x* = "+ str(answer))
print("f(x*) = "+ str(function(answer)))
