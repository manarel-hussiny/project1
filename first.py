list=[1,2,3,4]
try:
    c=input('enter name :- ')
    print(c.upper())
    print(list[6])
except IndexError as err:
    print('error')
except Exception as other:
    print('error1')