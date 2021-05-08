
def fun1():
    print('Inside Module 1 fun 1')
    
def fun2():
    print('Inside Module 1 fun 2')
       
def fun3():
    print('Inside Module 1 fun 3')
    
import logging as lg

def evenNumbers(data):
    lg.basicConfig(filename='log_1.txt',level= lg.INFO, format  = '%(asctime)s %(message)s')
    lst = []
    try:
        if(type(data) != int):
            msg = "Plz Enter Integer"
            raise ValueError(msg)
        else:
           
            try:
                for i in range(data):  
                    if(i%2 ==0):
                        lst.append(i)                  
                 
            except Exception as e:
                try:
                    lg.error(e)
                except:
                    msg = "logging failed"
                    print(msg)
    except ValueError as ve:
        lg.error(ve)
    else:
        msg = "Execuation successfull"
        lg.info(msg)        
    finally:
        lg.shutdown()
        return lst,msg    
    