import myclass

def isInt(e):   #Проверка на целое
    try:
        int(e)
        return True
    except ValueError:
        return False

def isOp(e):    #Проверка на оператор
    return "+-*/".find(e) != -1

def pr(e):  #Приоритет операции
    priority = {'+' : 2,
            '-' : 2,
            '/' : 3,
            '*' : 3}
    return priority[e]

def operation(op, rnum, lnum):  #Арифметические операции между числами
    res = {
        '+': float(lnum) + float(rnum),
        '-': float(lnum) - float(rnum),
        '/': float(lnum) / float(rnum),
        '*': float(lnum) * float(rnum)
    }
    return res[op]


def brackets(s):    #Проверка на равное количество откр. и закр. скобочек
    l = 0
    r = 0
    for i in s:
        if(i == '('):
            l+=1
        elif(i == ')'):
            r+=1
    return l == r

class Calculator:

    def postfix(self,inpStr):

        inpStr = inpStr.replace(' ', '')
        i = -1
        outStr = ""
        stackOp = myclass.Stack()
        
        while(i < len(inpStr)):
            if(i < len(inpStr)-1):
                i+=1
            else:
                i += 1
                continue
            if((isOp(inpStr[i]) or isInt(inpStr[i]) or inpStr[i] == '(' or inpStr[i] == ')') and brackets(inpStr)):
                if(inpStr[i] == '-' and ((i > 0 and not isInt(inpStr[i-1]) and inpStr[i-1] != ')') or i == 0)): #Проверка на отрицательное число
                    outStr += '-'
                    continue
                if(isInt(inpStr[i])):   #Проверка на число
                    outStr += inpStr[i]
                    continue
                if(len(outStr) > 0 and outStr[len(outStr)-1] != ' '):  #Добавление пробела
                    outStr += ' '
                if(isOp(inpStr[i])):    #Проверка на знак 
                    if(stackOp.isEmpty() or stackOp.peek() == '('):
                        stackOp.push(inpStr[i])
                        continue
                    if(pr(inpStr[i]) > pr(stackOp.peek())):
                        stackOp.push(inpStr[i])
                        continue
                    if(pr(inpStr[i]) <= pr(stackOp.peek())):
                        while(not stackOp.isEmpty() and stackOp.peek() != '(' and pr(inpStr[i]) <= pr(stackOp.peek()) ):
                            outStr += stackOp.pop() + ' '
                        stackOp.push(inpStr[i])
                        continue
                if(inpStr[i] == '('):   #Проверка на левую скобку
                    stackOp.push('(')
                    continue
                if(inpStr[i] == ')'):   #Проверка на правую скобку
                    while(stackOp.peek() != '('):
                        outStr += stackOp.pop() + ' '
                    stackOp.pop()
            else:
                outStr = ''
                break
        if(len(outStr) > 0):
                if(outStr[len(outStr)-1] != ' '):   #Добавление пробела
                    outStr += ' '
                while(not stackOp.isEmpty()):   #Вывод знаков из стека в строку
                    outStr += stackOp.pop() + ' '
        return outStr

    def calc(self,counts):
        stackNum = myclass.Stack()
        try:
            outStr = Calculator.postfix(self,counts)
            for i in outStr.split():
                if(isInt(i)):
                    stackNum.push(i)
                elif(isOp(i)):
                    stackNum.push(operation(i, stackNum.pop(), stackNum.pop()))
            return stackNum.peek()
        except Exception as e:
            return e
   



