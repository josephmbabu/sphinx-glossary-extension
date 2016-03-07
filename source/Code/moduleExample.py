#!/usr/bin/env python3

'''
An example module 
'''

class A():

    '''
    class A ...
    '''

    def __init__(self):
        '''
        __init__ of class A
        '''
        self.example= 'A'

    def myA(self):
        '''
        method myA of class A
        '''
        x = self.example
        return x

class B():

    '''
    class B ...
    '''

    def __init__(self):
        '''
        __init__ of class B
        '''
        self.example= 'B'

    def myB(self):
        '''
        method myB of class B
        '''
        y = self.example
        return y


if __name__ == '__main__':
    ''' protection from be accidently run '''
    print('Testing Class A and B')
    a = A()
    b = B()
    print(a.myA())
    print(b.myB())
