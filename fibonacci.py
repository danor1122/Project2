# 1 + 2 = 3         # 
# 2 + 3 = 5         # 5/3 = 1.66666667
# 3 + 5 = 8         # 8/5 = 1.6

class Fibonacci():
    counter = 0 # Nie ma dostepu, why?

    def Fibo():
        counter = 0
        a = 1
        b = 2
        while counter < 1111:
            counter += 1
            # print(counter)
            c = float(a + b)
            Fi = c / b
            print(counter, ' = ', Fi)
            # Fi = c % b
            # print(Fi)
            a = b
            b = c
            
            


    Fibo()