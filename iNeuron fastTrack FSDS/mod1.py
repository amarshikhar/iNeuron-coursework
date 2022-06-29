#to print all even numbers
import logging as lg
lg.basicConfig(filename="even.log",level=lg.ERROR)

def even_number(start,end):
    try:
#         start=int(input("start"))
#         end=int(input("end"))
        for i in range(start,end+1):
            if i%2==0:
                print(i)
    except Exception as e:
        lg.error(e)