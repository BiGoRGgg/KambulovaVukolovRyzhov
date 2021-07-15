function = eval("lambda x:" + input("Введите функцию:\n"))
limit = [float(s) for s in input("Введите отрезок:\n").split(" ")]
e = float(input("Введите точность:\n"))

def goldenRatio(function, limit, e):

    '''
        Метод Золотого Сечения
                                '''

    goldenNumber = 0.61803
    
    fX1 = function(limit[0])
    fX2 = function(limit[1])
    xTilde = (limit[1]-limit[0])*goldenNumber + limit[0]
    
    if abs(limit[0] - limit[1]) < e:
        return xTilde
    
    else:
        xDoubleTilde = (limit[1] - xTilde)*goldenNumber + xTilde    
        fXtilde = function(xTilde)
        fXdoubleTilde = function(xDoubleTilde)    
    
        if fX1 <= fXtilde < fX2:
            return goldenRatio(function, [limit[0], xTilde], e)
    
        elif fXtilde <= fXdoubleTilde:
            return goldenRatio(function, [limit[0], xDoubleTilde], e)
        
        else:
            return goldenRatio(function, [xTilde, limit[1]], e)

    '''
        goldenNumber - число, обратное Золотому Числу        
        xTilde - x~
        xDoubleTilde - x~~
        fX1 - f(x1)
        fX2 - f(x2)
        fXtilde - f(x~)
        fXdoubleTilde - f(x~~)
                                ''' 


answer = goldenRatio(function, limit, e)

print("x* = "+ str(answer))
print("f(x*) = "+ str(function(answer)))
