Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> assess=[10,20,40,50,100,["python","animal","king"],"tara",12,16,17]
>>> len(assess)
10
>>> #clear()
>>> assess.clear()
>>> assess
[]
>>> assess=[10,20,40,50,100,["python","animal","king"],"tara",12,16,17]
>>> assess.clear("hello")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    assess.clear("hello")
TypeError: list.clear() takes no arguments (1 given)
>>> assess.clear(0)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    assess.clear(0)
TypeError: list.clear() takes no arguments (1 given)
>>> 
>>> 
>>> #insert
>>> assess=[10,20,40,50,100,["python","animal","king"],"tara",12,16,17]
>>> assess.insert()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    assess.insert()
TypeError: insert expected 2 arguments, got 0
>>> assess.insert("hii")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    assess.insert("hii")
TypeError: insert expected 2 arguments, got 1
>>> assess.insert("hii",4)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    assess.insert("hii",4)
TypeError: 'str' object cannot be interpreted as an integer
>>> assess.insert(4,"hii")
>>> assess
[10, 20, 40, 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17]
>>> assess.insert(88,"govinda")
>>> assess
[10, 20, 40, 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'govinda']
>>> assess.insert(88,"govinda",10)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    assess.insert(88,"govinda",10)
TypeError: insert expected 2 arguments, got 3
assess.insert(88,"got it")
assess
[10, 20, 40, 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'govinda', 'got it']
assess.insert(-1,"got it")
assess
[10, 20, 40, 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'govinda', 'got it', 'got it']
assess.insert(-1,"no")
assess
[10, 20, 40, 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'govinda', 'got it', 'no', 'got it']
assess.insert(-4,"no")
assess.insert(-4,"yes")
assess
[10, 20, 40, 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'no', 'yes', 'govinda', 'got it', 'no', 'got it']
assess.insert(3,[10,20,20,30])
assess
[10, 20, 40, [10, 20, 20, 30], 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'no', 'yes', 'govinda', 'got it', 'no', 'got it']
assess.insert(3,(10,20,20,30))
assess
[10, 20, 40, (10, 20, 20, 30), [10, 20, 20, 30], 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'no', 'yes', 'govinda', 'got it', 'no', 'got it']
assess.insert(3,{10:20,20:30})
assess
[10, 20, 40, {10: 20, 20: 30}, (10, 20, 20, 30), [10, 20, 20, 30], 50, 'hii', 100, ['python', 'animal', 'king'], 'tara', 12, 16, 17, 'no', 'yes', 'govinda', 'got it', 'no', 'got it']
assess.insert(3:5,12)
SyntaxError: invalid syntax


#indexing

assess=[10,20,40,50,100,["python","animal",{'name': 'Dinga'},"king"],"tara", (30, 60, 90),12,16,17]
assess
[10, 20, 40, 50, 100, ['python', 'animal', {'name': 'Dinga'}, 'king'], 'tara', (30, 60, 90), 12, 16, 17]
assess.index(10)
0
assess.index(20)
1
assess[5].index("animal")
1
assess[5].index("king")
3
assess[5][2].index("name")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    assess[5][2].index("name")
AttributeError: 'dict' object has no attribute 'index'
assess[5][2].index("name":"Dinga")
SyntaxError: invalid syntax
assess[5][2].index('name')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    assess[5][2].index('name')
AttributeError: 'dict' object has no attribute 'index'
assess=[10,20,40,50,100,["python","animal","king"],"tara",12,,10,20,40,60,16,17]
SyntaxError: invalid syntax
assess=[10,20,40,50,100,["python","animal","king"],"tara",12,10,20,40,60,16,17]
assess.index(10)
0
assess.index(10,9)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    assess.index(10,9)
ValueError: 10 is not in list
assess.index(10,8)
8
assess.index(20,9)
9


#count

assess=[10,203,30,40,50,10,30,40,50]
assess.count(10)
2
assess.count(20)
0
assess.count(20,10)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    assess.count(20,10)
TypeError: list.count() takes exactly one argument (2 given)
assess=["python","animal","king","thara"]
aassess.count("python")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    aassess.count("python")
NameError: name 'aassess' is not defined. Did you mean: 'assess'?
assess.count("python")
1
assess=["python","animal","king","python","thara"]
assess.count("python")
2
assess=[10,20,40,50,100,["python","animal","king"],"tara",12,10,20,40,60,16,17]
assess.count("python")
0
assess[5].count("python")
1


#sort

assess=["python","animal","king","python","thara"]
assess.sort()
assess
['animal', 'king', 'python', 'python', 'thara']
assess.sort(3)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    assess.sort(3)
TypeError: sort() takes no positional arguments
assess.sort("king")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    assess.sort("king")
TypeError: sort() takes no positional arguments
assess=[10,20,40,50,100,["python","animal","king"],"tara",12,10,20,40,60,16,17]
assess.sort()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    assess.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
assess=[10,203,30,40,50,10,30,40,50]
assess.sort()
assess
[10, 10, 30, 30, 40, 40, 50, 50, 203]
assess=[10,203,30,40,50,10,30,40,50]
assess.sort(reverse=True)
assess
[203, 50, 50, 40, 40, 30, 30, 10, 10]
assess=["java","python","mern","HTML","C","c","c++","JS","playwrite"]
assess.sort()
assess
['C', 'HTML', 'JS', 'c', 'c++', 'java', 'mern', 'playwrite', 'python']
assess=["java","python",["mern","HTML","C","c"],"c++","JS","playwrite"]
assess
['java', 'python', ['mern', 'HTML', 'C', 'c'], 'c++', 'JS', 'playwrite']
assess=["!@#$%^&*()*&%$$%^"]
assess.sort()
assess
['!@#$%^&*()*&%$$%^']
assess=["java","python",["mern","HTML","C","c"],"c++","JS","playwrite"]
assess.sort()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    assess.sort()
TypeError: '<' not supported between instances of 'list' and 'str'
assess=[10,203,30,40,[50,10],30,40,50]
assess.sort()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    assess.sort()
TypeError: '<' not supported between instances of 'list' and 'int'


#reverse()


assess=[10,3,20,9,30,10,40,0,20,30,5,50,60,50,8]
assess.reverse()
assess
[8, 50, 60, 50, 5, 30, 20, 0, 40, 10, 30, 9, 20, 3, 10]
assess=["java","python",["mern","HTML","C","c"],"c++","JS","playwrite"]assess.reverse()
SyntaxError: invalid syntax
assess=["java","python",["mern","HTML","C","c"],"c++","JS","playwrite"]
assess.reverse()
assess
['playwrite', 'JS', 'c++', ['mern', 'HTML', 'C', 'c'], 'python', 'java']
assess[2].reverse()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    assess[2].reverse()
AttributeError: 'str' object has no attribute 'reverse'
assess=[10,3,20,9,30,10,40,0,20,30,5,50,60,50,8]
assess=[10,3,[20,9,30,10],40,0,20,30,5,50,60,50,8]
assess[2].reverse()
assess
[10, 3, [10, 30, 9, 20], 40, 0, 20, 30, 5, 50, 60, 50, 8]
