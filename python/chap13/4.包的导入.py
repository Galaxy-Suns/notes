#导入方式
#import 完整包名.模块名
#from 完整包名 import 模块名
#from 完整包名.模块名 import 变量函数类等

import admin.my_admin as a
a.info()
from admin import my_admin as b
b.info()
from admin.my_admin import *
info()
print(name)

