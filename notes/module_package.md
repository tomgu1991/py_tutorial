# Python Module and Package

Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。

一个简单的模块
support.py:
```python
def print_func( par ):
   print ("Hello : ", par)
   return
```

###Module

##### 直接用：import module1

```
import module1

module1.functionName
```

例如：

test.py 文件代码：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

> Hello : Runoob
```

##### from…import 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：from modname import name1[, name2[, ... nameN]]

##### from…import* 语句

把一个模块的所有内容全都导入到当前的命名空间也是可行的

### Package

包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。**__init__.py** 用于标识当前文件夹是一个包。

在package_test中，有a b 两个module，用的时候，
```python
from package_test.a import runA
from package_test.b import runB
 
runA()
runB()
```

### __.init.__
这个文件会在import包的时候被调用，其中的变量可以认为是全局变量。
当我们在这个文件中引用这个包里面的其他文件后，
```python
print("import package_test")

intArray = [100, 200, 300]

import package_test.a, package_test.b
```
当import package_test后，自动就引入了a和b，可以调用相应的内容
```python
import package_test
from package_test.mod import bar

package_test.a.runA()
package_test.b.runB()
bar()
```


#####总结
1. import ModuleName as M, 那么用M中的东西就用M.XXX
2. 如果ModuleName在一个package中，比如
```python
pck：
    - mA
    - mB
```
import pck.mA 来引用模块