'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
c1 = complex(2,3)
print("Complex no C1 = "+str(c1))
print("Real Part = "+str(c1.real))
print("Imaginary Part= "+str(c1.imag))
print("Conjugate = "+str(c1.conjugate()))
c2=c1*c1.conjugate()
print("Multiplication is :" + str(c2))
print("Multiplication is :" + str(c1*c1.conjugate()))