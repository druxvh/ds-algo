from array import *
'''
Python doesn't have inbuilt array datatype though we can import it to use it into our program.

- Collection of same type elements 
- fixed size
- indexed

Python have better & efficient ways to handle data than array like its pre-defined class based datatype called 'List'.
'''

#TypeCodes for arrays: (C type)
#  Type code      C Type             Minimum size in bytes  
#-------------------------------------------------------------
#     'b'         signed integer     1  
#     'B'         unsigned integer   1  
#     'u'         Unicode character  2  
#     'h'         signed integer     2  
#     'H'         unsigned integer   2  
#     'i'         signed integer     2  
#     'I'         unsigned integer   2  
#     'l'         signed integer     4  
#     'L'         unsigned integer   4  
#     'q'         signed integer     8 
#     'Q'         unsigned integer   8   
#     'f'         floating point     4  
#     'd'         floating point     8

arr = array('i', [1,2,3,4,4,4,4,6,87,8])

#Append
arr.append(4)

#count
arr.count(4)

#extend
arr.extend()

#fromList
arr.fromlist()

#index
arr.index()

#insert
arr.insert()

#pop
print(arr.pop())

#remove
arr.remove()

#reverse
arr.reverse()

#toList
arr.tolist()