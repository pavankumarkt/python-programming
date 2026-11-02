Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> assess=(1,2,3,4,5,"hi","hello","done","yepp")
>>> len(assess)
9
>>> 
>>> 
>>> #index
>>> assess=(1,2,3,4,5,"hi","hello","done","yepp")
>>> assess.insex(1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    assess.insex(1)
AttributeError: 'tuple' object has no attribute 'insex'. Did you mean: 'index'?
>>> assess.index(1)
0
>>> assess.index(5)
4
>>> assess.index("hi")
5
>>> assess[0]
1
>>> assess[9]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    assess[9]
IndexError: tuple index out of range
>>> assess[5]
'hi'
>>> assess=("hello","hi",10,20,30,0.123,1.123,True,False,[10,20,30],(98,87,67),{"empname":"ram","empid":987})
>>> assess[7]
True
>>> assess[9]
[10, 20, 30]
>>> assess[11]
{'empname': 'ram', 'empid': 987}
>>> assess.index("ram")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    assess.index("ram")
ValueError: tuple.index(x): x not in tuple
>>> assess[11].index("ram")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    assess[11].index("ram")
AttributeError: 'dict' object has no attribute 'index'
>>> assess[11].index('empid': 987)
SyntaxError: invalid syntax
assess[11].index("'empid': 987")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    assess[11].index("'empid': 987")
AttributeError: 'dict' object has no attribute 'index'



#count

assess=(10,20,30,40,10,40,50,70,80,9,90,50,20,10,1000,244,322,332,244,244)
assess.count(10)
3
assess.count(244)
3
assess.count(20)
2
assess=(10,20,30,(40,10,40,50,70),80,9,90,50,20,10,1000,244,322,332,244,244)
assess=(10,20,30,(40,10,40,50,70),80,9,90,50,20,10,1000,244,322,332,244,244)
assess.count(10)
2
assess[3].count(10)
1
assess=(10,20,30,(40,10,40,50,,40,40,70,50,70),80,9,90,50,20,10,1000,244,322,332,244,244)
SyntaxError: invalid syntax
assess=(10,20,30,(40,10,40,50,40,40,70,50,70),80,9,90,50,20,10,1000,244,322,332,244,244)
assess[3].count(10)
1
assess[3].count(40)
4
assess.count(20)
2
assess[3].count(70)
2
assess[3].count(4070)
0
assess[3].count(40,70)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    assess[3].count(40,70)
TypeError: tuple.count() takes exactly one argument (2 given)
