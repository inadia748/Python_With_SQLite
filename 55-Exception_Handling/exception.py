''''
Exception Handing in Python:

1) Zero Division Error
    example:  a = 10
              print(a/0)


2) Name Error
            In this example, b is not defined, but you are printing 'b'
        example: print(b)


3) TypeError
         concatenation always works with string
        example:
            print('10' + 10)

4) Value Error
        example:
            a = int(input('Enter the value'))
            but you entered a string. You are supposed to enter an integer.


5) Index Error
        example:
            l = [1, 2, 3, 4]
            print(l[4])


6) Key Error
        example:
            d = {'name': 'Testing', 'fees': 8000}
            print(d['fee'])


7) Module Not Found Error
        example:-
                you are creating a file 'cal.py'
                but in another file, you are importing
                'import cals.py'


8) Import Error:
        example:- You create a file 'cal.py', and you created a function in it like:
                    def sum():
                        print(10 + 20)
        in another file, you write,
                from cal import sum1

        # you will get an error because sum1 does not exist on cal.py, only def sum is used.



'''

