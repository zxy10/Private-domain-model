# FastAPI

## 预备知识

### 爬虫

- 爬虫是模拟浏览器发送请求，获取响应

**爬虫的分类**

- 通用爬虫：通常指搜索引擎的爬虫
- 聚焦爬虫：针对特定网站的爬虫

![image-20240131093359439](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131093359439.png)



### `http`协议

![image-20240131095035986](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131095035986.png)

![image-20240129090851114](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240129090851114.png)

**http协议特性**

1. 基于TCP/IP协议

   http协议是基于TCP/IP协议之上的应用层协议

2. 基于请求-响应模式

   http协议规定：请求从客户端发出，最后服务器端相应该请求并返回。换句话说，肯定是先从客户端开始建立通信的，服务器端在没有金额收到请求之前，不会发送响应

3. 无状态请求

   http协议是一种不保存状态，即无状态协议。http协议自生不对请求和通信状态及逆行保存。也就是说http这个级别协议对于发送过的请求或者响应都不做持久化处理

   使用http协议，每当在新的请求发送时就会有对应的新的响应产生，协议本身并不保留之前一切请求或者响应报文的信息。这是为了更快地处理大量事物，确保协议的可伸缩性，而特意把HTTP协议设计成如此简单的

4. 短连接

   

**http请求协议与响应协议**

![image-20240129093209026](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240129093209026.png)

传输的整个过程

![image-20240130144740789](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240130144740789.png)

![image-20240129093723252](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240129093723252.png)

请求协议的请求首行：请求方式，请求路径，参数，协议

请求头：键值对有浏览器来决定是未知的

空行

请求体：post请求的时候会存放数据，get请求不会存放

![image-20240130151210647](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240130151210647.png)

### requests模块

![image-20240131100030451](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131100030451.png)

![image-20240131100321764](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131100321764.png)

**`requests`中解决编解码的方法**

- `response.content.decode()`
- `response.content.decode("gbk")`
- `response.text`

![image-20240131101302910](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131101302910.png)

例子：

![image-20240131101637172](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131101637172.png)

response的一些用法

![image-20240131102251806](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131102251806.png)

![image-20240131102818005](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131102818005.png)

![image-20240131105523494](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131105523494.png)

![image-20240131105608509](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131105608509.png)

例子：

![image-20240131110136536](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131110136536.png)

**`requests`深入**

- 发送`post`请求
- 使用代理
- 使用cookies session

![image-20240131143638984](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131143638984.png)

![image-20240131143704751](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131143704751.png)

![image-20240131145915005](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131145915005.png)

![image-20240131145957826](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131145957826.png)

![image-20240131150150079](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131150150079.png)

**使用代理的原因**

- 让服务器以为不是同一客户端在发送请求
- 防止我们真实地址被泄露，以防被追究

**使用代理IP**

- 准备一堆的IP地址，组成IP池，随机选这一个ip来用
- 如何随机选择代理ip，让使用次数更少的ip地址有更大的可能性被用到
  - ![image-20240131152126000](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131152126000.png)
- 检查ip的可用性
  - 可以使用`requests`添加超时参数，判断ip地址的质量
  - 在线代理ip地址质量检测的网站

![image-20240131152230686](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131152230686.png)

**爬虫处理cookie和session**

带上`cookie`和`session`的好处

- 能够请求到登陆之后的页面

带上`cookie`和`session`的弊端

- 一套`cookie`和`session`往往和一个用户对应
- 请求太快，请求次数太多，容易被服务器识别为爬虫

*不需要`cookies`的时候尽量不要去使用*

*但是为了获取登陆之后的页面，我们必须使用`cookie`*

![image-20240131153719329](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131153719329.png)

![image-20240131154000473](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131154000473.png)

![image-20240131154713599](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131154713599.png)

**获取登陆后页面的三种方式**

1. 实例化`session`，使用`session`发送`post`请求，再使用他获取登陆后的页面
2. `headers`中添加`cookie`键，值为`cookie`字符串
3. 在请求方法中添加`cookies`参数，接受字典形式的`cookie`,字典形式中的`cookie`键是`cookie`的`name`,值是`cookie`的`value`

### **将数据存储到表格中**

1. 下载所需要的包 

   ```python
   pip install pandas
   ```

   报错的话就查询，先要下载好包

2. 在使用前，一定要导入

   ```python
   import pandas as pd
   ```

3. ![image-20240205103323016](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240205103323016.png)

下边是一个爬虫的实例，将其保存到一个表格中

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

#创建一个类
class MovieDouban:
    def __init__(self):
        self.url = "https://movie.douban.com/top250?start={}&filter="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
        }
        self.movie_data = []

    # 2.发送请求，获取响应
    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 3.获取数据
    def extraction_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all('div', class_='item')
        for item in items:
            movie_info = {}
            movie_info['title'] = item.find('span', class_='title').get_text()
            movie_info['quote'] = item.find('span', class_='inq').get_text() if item.find('span', class_='inq') else ''
            movie_info['director'] = item.find('div', class_='bd').find('p').get_text().split('\n')[1].strip().split('导演: ')[1]
            movie_info['rating'] = item.find('span', class_='rating_num').get_text()

            self.movie_data.append(movie_info)

    def run(self):
        num = 0
        while True:
            #1.初始的url地址
            start_url = self.url.format(num)

            #2.发送请求，获取响应
            html = self.parse_url(start_url)

            #3.处理数据
            self.extraction_data(html)

            #作为打破循环的条件
            if num > 225:
                break

            #4.进入下一轮循环
            num += 25

        # 将数据保存到Excel表格
        df = pd.DataFrame(self.movie_data)
        df.to_excel('douban_top250.xlsx', index=False)


# 实例化对象
movie = MovieDouban()
movie.run()

```

### **`BeautifulSoup`**

是python解析html的一个很好用的数据库

**安装**

```
pip install beautifulsoup4  
```

在终端上执行，打开终端的方式是`win + R`

**导入**

```python
from bs4 import BeautifulSoup
```

**解析库**

| 序号 | 解析库          | 使用方法                             | 优势                            | 劣势                  |
| ---- | --------------- | ------------------------------------ | ------------------------------- | --------------------- |
| 1    | Python标准库    | `BeautifulSoup(html,’html.parser’)`  | Python内置标准库；执行速度快    | 容错能力较差          |
| 2    | lxml HTML解析库 | `BeautifulSoup(html,’lxml’)`         | 速度快；容错能力强              | 需要安装，需要C语言库 |
| 3    | lxml XML解析库  | `BeautifulSoup(html,[‘lxml’,’xml’])` | 速度快；容错能力强；支持XML格式 | 需要C语言库           |
| 4    | htm5lib解析库   | `BeautifulSoup(html,’htm5llib’)`     | 以浏览器方式解析，最好的容错性  | 速度慢                |

**使用技巧**

```python
from bs4 import BeautifulSoup

bs = BeautifulSoup(html,"html.parser")

# 缩进格式
print(bs.prettify()) 

# 获取title标签的所有内容
print(bs.title) 

# 获取title标签的名称
print(bs.title.name) 

# 获取title标签的文本内容
print(bs.title.string) 

# 获取head标签的所有内容
print(bs.head) 

# 获取第一个div标签中的所有内容
print(bs.div) 

# 获取第一个div标签的id的值
print(bs.div["id"])

# 获取第一个a标签中的所有内容
print(bs.a) 

# 获取所有的a标签中的所有内容
print(bs.find_all("a"))

# 获取id="u1"
print(bs.find(id="u1")) 

# 获取所有的a标签，并遍历打印a标签中的href的值
for item in bs.find_all("a"): 
	print(item.get("href")) 
	
# 获取所有的a标签，并遍历打印a标签的文本值
for item in bs.find_all("a"): 
	print(item.get_text())

```

**`BeautifulSoup4`四大对象种类**

`BeautifulSoup4`将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

- `Tag`
- `NavigableString`
- `BeautifulSoup`
- `Comment`

**（1）Tag ：** Tag通俗点讲就是HTML中的一个个标签，例如：

```python
from bs4 import BeautifulSoup
bs = BeautifulSoup(html,"html.parser")

# 获取title标签的所有内容
print(bs.title)

# 获取head标签的所有内容
print(bs.head)

# 获取第一个a标签的所有内容
print(bs.a)

# 类型
print(type(bs.a))
```

我们可以利用 soup 加标签名轻松地获取这些标签的内容，这些对象的类型是 **bs4.element.Tag。**
但是注意，它查找的是在所有内容中的第一个符合要求的标签。

对于 Tag，它有两个重要的属性，是 `name `和 `attrs`：

```python
# [document] 
#bs 对象本身比较特殊，它的 name 即为 [document]
print(bs.name)

# head 
#对于其他内部标签，输出的值便为标签本身的名称
print(bs.head.name) 

# 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
print(bs.a.attrs)

#还可以利用get方法，传入属性的名称，二者是等价的
print(bs.a['class']) # bs.a.get('class')

# 可以对这些属性和内容等等进行修改
bs.a['class'] = "newClass"
print(bs.a) 

# 还可以对这个属性进行删除
del bs.a['class'] 
print(bs.a)
```

**（2）`NavigableString `**：获取标签内部的文字用 .string 即可，例如：

```python
print(bs.title.string)

print(type(bs.title.string))
```

**（3）`BeautifulSoup`**：表示的是一个文档的内容。

大部分时候，可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性，例如：

```python
print(type(bs.name))

print(bs.name)

print(bs.attrs)
```

**（4）Comment**：是一个特殊类型的 `NavigableString` 对象，其输出的内容不包括注释符号。

```python
print(bs.a)  # 此时不能出现空格和换行符，a标签如下：
# <a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!--新闻--></a>

print(bs.a.string) # 新闻

print(type(bs.a.string)) # <class 'bs4.element.Comment'>
```

**遍历文档树**

（1）.contents：获取Tag的所有子节点，返回一个list

```python
# tag的.content 属性可以将tag的子节点以列表的方式输出
print(bs.head.contents)

# 用列表索引来获取它的某一个元素
print(bs.head.contents[1])
```

（2）.children：获取Tag的所有子节点，返回一个生成器

```python
for child in  bs.body.children:
    print(child)
```

**搜索文档树**

**1.** `find_all(name, attrs, recursive, text, **kwargs)`

**（1）name参数：**

**字符串过滤**：会查找与字符串完全匹配的内容

```python
a_list = bs.find_all("a")
print(a_list)
```

**正则表达式过滤**：如果传入的是正则表达式，那么`BeautifulSoup4`会通过search()来匹配内容

```python
t_list = bs.find_all(re.compile("a"))
for item in t_list:
    print(item)
```

**列表：** 如果传入一个列表，`BeautifulSoup4`将会与列表中的任一元素匹配到的节点返回

```python
t_list = bs.find_all(["meta","link"])
for item in t_list:
    print(item)
```

**方法：** 传入一个方法，根据方法来匹配

```python
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)
for item in t_list:
    print(item)
```

**（2）kwargs参数：**

```python
# 查询id=head的Tag
t_list = bs.find_all(id="head")
print(t_list)

# 查询href属性包含ss1.bdstatic.com的Tag
t_list = bs.find_all(href=re.compile("http://news.baidu.com"))
print(t_list)

# 查询所有包含class的Tag(注意：class在Python中属于关键字，所以加_以示区别)
t_list = bs.find_all(class_=True)
for item in t_list:
    print(item)
```

**（3）`attrs`参数：**

并不是所有的属性都可以使用上面这种方式进行搜索，比如HTML的data-*属性，我们可以使用attrs参数，定义一个字典来搜索包含特殊属性的tag：

```python
t_list = bs.find_all(attrs={"data-foo":"value"})
for item in t_list:
    print(item)
```

**（4）text参数：**
通过text参数可以搜索文档中的字符串内容，与name参数的可选值一样。
text参数接受 *字符串，正则表达式，列表*

```python
t_list = bs.find_all(attrs={"data-foo": "value"})
for item in t_list:
    print(item)

t_list = bs.find_all(text="hao123")
for item in t_list:
    print(item)

t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
for item in t_list:
    print(item)

t_list = bs.find_all(text=re.compile("\d"))
for item in t_list:
    print(item)
```

**(5）limit参数：**
传入一个limit参数来限制返回的数量
例如下列放回数量为2

```python
t_list = bs.find_all("a",limit=2)
for item in t_list:
    print(item)
```

**2.`find（）`**
返回符合条件的第一个Tag
即当我们要取一个值的时候就可以用这个方法

```python
t = bs.div.div

# 等价于
t = bs.find("div").find("div")
```

## `api`接口

在开发web中，有两种应用模式：

1. 前后端不分离【客户端看到的内容和所有界面效果都由服务端提供出来的】

   ![image-20240130171655924](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240130171655924.png)

2. 前后端分离【把前端的界面效果（html，css，js分离到一个服务器，python服务器只需要返回数据即可）】

   ![image-20240130171749864](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240130171749864.png)

### resful接口

![image-20240130175040084](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240130175040084.png)

![image-20240130175401277](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240130175401277.png)

### quick  start

1. 导入fastapi
2. 创建一个app实例
3. 编写一个路径操作装饰器（`@app.get("/")`)
4. 编写一个路径操作函数（如`def root(): ...`)
5. 定义返回值
6. 运行开发服务器（如`uvicorn main:app --reload`）

![image-20240131172752949](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131172752949.png)

代码

```python
from fastapi import FastAPI  #FastAPI是一个为所有的api提供功能的类
app = FastAPI()  #这个实例是创建你所有API的交互对象。这个app同样在如下命令中被uvicorn利用

@app.get("/")#装饰器
async def root():
	return {"message":"hello yuan"}
```

![image-20240131173904748](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131173904748.png)

**直接运行的代码**

```python
from fastapi import FastAPI  #FastAPI是一个为所有的api提供功能的类
import uvicorn
app = FastAPI()  #这个实例是创建你所有API的交互对象。这个app同样在如下命令中被uvicorn利用

@app.get("/")#装饰器
async def root():
	return {"message":"hello yuan"}

if __name__ == '__main__':
    uvicorn.run("需要运行的文件的名称，例如：需要运行本代码，那么就写本代码的名称:app(app是一个实例化的对象)",port=8080(端口信息),debug=True,reload=True)
```



## 路径操作

### **路径操作装饰器**

**`fastapi`支持的请求方式**

![image-20240131175032846](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240131175032846.png)

```python
from fastapi import FastAPI 
import uvicorn

app = FastAPI() 

@app.get("/get")#装饰器
def get_test():
	return {"method":"get方法"}

@app.post("\post")
def post_test():
	return {"method":"post方法"}

@app.put("\put")
def put_test():
	return {"method":"put方法"}

@app.delete("\delete")
def delete_test():
	return {"method":"delete方法"}

if __name__ == '__main__':
    uvicorn.run("需要运行的文件的名称，例如：需要运行本代码，那么就写本代码的名称:app(app是一个实例化的对象)",port=8080(端口信息),debug=True,reload=True)
```

**路径操作装饰器的参数**

```python
from fastapi import FastAPI 
import uvicorn

app = FastAPI() 

@app.post("\post",tags=["这是测试items测试接口"],summary="this is items测试 summary",description="this is items测试 description")#tages表示的是标签，当别人在浏览器打开的时候就可以很清楚的明白下边的代码的作用
def post_test():
	return {"method":"post方法"}

if __name__ == '__main__':
    uvicorn.run("需要运行的文件的名称，例如：需要运行本代码，那么就写本代码的名称:app(app是一个实例化的对象)",port=8080(端口信息),debug=True,reload=True)
```

![image-20240219113110859](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219113110859.png)

### `include_router`

`main.py`

```python
from typing import Union
from fastapi import FastAPI
import uvicorn
from apps import app01,app02	#在app这个文件夹下有app01，app02这两个文件夹，还有这个main文件
app = FastAPI()
app.include_router(app01.prefix="/app01",tags=["第一章节：商城接口"])
app.include_router(app02.prefix="/app01",tags=["第二章节：用户中心接口"])

if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8080,debug=True,reload=True)
```

## 请求与响应

### 路径参数

![image-20240219151703244](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219151703244.png)

![image-20240219150615614](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219150615614.png)

像上边的代码一样`{id}`就是一个路径参数，这样可以向代码中传入想要的数字，进而去返回相应的值

![image-20240219151240576](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219151240576.png)

进行类型声明，这样，可以保证输入的id就是一个整型数字

### 查询参数

路径函数中声明不属于路径参数的其他函数参数时，他们将被自动解释为“查询字符串”参数，就是url？之后用&分割的key-value键值对

```python
from fastapi import APIRouter

app02 = APIRouter()

@app02.get("/jobs")
async def get_jobs(kd, xl, gj):
    #基于kd,xl,gj数据库查询岗位信息
    return{
        "kd": kd,
        "xl": xl,
        "gj": gj,
    }
```

`Union`是当有多种可能的数据类型时使用，比如函数有可能根据不同情况有时返回str或返回list，那么就可以写成`Union[list, str]`

`Optional`是`Union`的一个简化，当数据类型中有可能是None时，比如有可能是str或这是None，那么`Optional[str]`相当于`Union[str, None]`

### 请求体数据

当你需要将数据从客户端（例如浏览器）发送给API时，你将其作为 **请求体** 发送，**请求体**是客户端发送给API的数据，**响应体**是API发送给客户端的数据。

安装上手`pip install pydantic`

![image-20240219160002208](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219160002208.png)

```python
from typing import Union,List,Optional
from fastapi import FastAPI
from pydantic import BaseModle,Field,ValidationError,validator
import uvicorn
from datetime import date

class Addr(BaseModle):
    name = 'root'
    age: int = Field(default=0, lt=100, gt=0)
    birth: Optional(data) = None
    friends: Union[str, None] = None
    #addr: Union[Addr, None] = None  类型嵌套
    @validator('name')
    def name_must_alpha(cla, v):
        assert v.isapha(), 'name must be alpha'
        return v
    
class Data(BaseModel):  #类型嵌套
    users: List(User)
    
app = FastAPI()

```

### `from`表单数据

在OAthu2规范的一种使用方式（密码流）中，需要将用户名、密码作为表单字段发送，而不是JSON。

FastAPI可以使用 **From** 组件来接受表单数据，需要先使用`pip install python-multipart`命令进行安装

![image-20240219170246048](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219170246048.png)

### 文件上传

![image-20240219171415620](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219171415620.png)

注意参数那块，传入的是字节流

适合小文件上传

![image-20240219171623091](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240219171623091.png)

上传多个文件的例子

返回的是上传文件的个数，`for`循环遍历的是每一个文件中的字节数

### `Request`对象

有些情况下我们希望能直接访问`Request`对象。例如，我们在路径操作函数中想获取客户端的ip地址，需要在函数中声明`Request`类型的参数，FastAPI就会自动传递`Request`类型的参数，我们就可以获取到`Request`对象及其属性信息，例如`header`、`url`、`cookie`、`session`等。

```python
from fastapi import Request
@app.get("/items")
async def items(request: Request):
    {"请求url": requests.url,
    "请求IP": requests.client.host,
    "请求宿主": requests.headers.get("user-agent"),
    "cookies":request.cookies,
    }
```

### 请求静态文件

静态文件：不是由服务器生成的文件

动态文件：由服务器生成的文件

在web开发中，需要请求很多的静态源文件（不是有服务器生成的文件），如css/js和图片文件等。

```python
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static",StaticFiles(directory="static(和项目目录下存放静态文件的文件名称一致)"))
```

### 响应模型相关参数

**(1) `response_model`参数**

前面写的那么多路径函数最终 `return` 的都是自定义结构的字典，FastAPI提供了`response_model`参数，声明`return`响应体的模型

```javascript
#路径操作
@app.post("/items/",response_model=Item)
#路径函数
async def create_item(item: Item):
	...
```

**`response_model`是路径操作的参数，并不是路径函数的参数**

FastAPI将使用`response_model`进行以下操作：

- 将输出数据转换为`response_model`中声明的数据类型
- 验证数据结构和类型
- 将输出数据类型限制为该model定义的
- 添加到OpenAPI中
- 在自动文档系统中使用

你可以在任意的路径操作中使用`response_model`参数来声明用于响应的模型

案例：

- 注册功能
- 输入账号、密码、昵称、邮箱，注册成功后返回个人信息

```python
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()

class UserIn(BaseModel):
	username:str
	password:str
	email:EmailStr
	full_name:Union[str, None] = None

class UserOut(BaseModel):
	username:str
	email:EmailStr
	full_name:Union[str, None] = None

@app.post("/user/",response_model=UserOut)
async def create_user(user:UserIn):
	return user
```

**(2) `response_model_exclude_unset`**

通过上面的例子，我们学会了如何使用`response_model`控制响应体结构，但是如果他们实际上没有存储，则可能从结果中忽略他们。例如，如果model在NoSQL数据库中具有很多可选属性，但是不想发送很长的JSON响应，其中那个包含默认值。

案例：

```python
from typing import List,Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:Union[str, None] = None
    price:float
    tax:float = 10.5
    tags:List[str] = []
    
items = {
    "foo":{"name":"Foo", "price":50.2},
    "bar":{"name":"Bar", "descripition": "The bartendera","price":62,"tax":20.2},
    "baz":{"name":"Baz", "descripition": None,"price":50.2,"tax":10.5,"tags":[]},
}

@app.get("/item/{item_id}", response_model = Item,response_model_exclude_unset=True)
```

![image-20240220091818092](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240220091818092.png)

`response_model_exclude_unset`是起到一个过滤的效果，过滤掉没有设置的值，只保留设置之后的值

**INCLUDE和EXCLUDE**

```python
#response_model_exclude
@app.get("/items/{item_id}", response_model=Item,response_model_exclude={"description"})
async def read_item(item_id: str):
	return items{item_id}
	
#response_model_include
@app.get("/items/{item_id}", response_model=Item,response_model_includee={"name","price"})
async def read_item(item_id: str):
	return items{item_id}
```

## jinja2模板

要了解jinja2，那么需要先理解模板的概念。模板在python的web开发中广泛使用，它能够有效的将业务逻辑和页面逻辑分开，是代码可读性增强、并且更容易理解和维护。

模板简单来说就是一个其中包涵占位变量表示动态的部分文件，模板文件在经过动态赋值后，返回给用户。

jinja2就是Flask作者开发的一个模板系统，起初是仿django模板的一个模板引擎，为Flask提供模板支持，由于其灵活，快速和安全等优点被广泛使用。

![image-20240220165420395](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240220165420395.png)

在jinja2中，存在三种语法：

1. 变量取值{{}}
2. 控制结构{%%}

### jinja2的变量

main.py

```python
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def hello(requests:Requests):
	return templates.TemplateResponse(
    'index.html',{
        'request':request,	#注意，返回模板响应时，必须有request键值对，且值为request请求对象,'index.html'是一个模板文件
        'user':'yuan'，
        'books':["金瓶梅","聊斋","剪灯新话","国色天香"],
        "booksDict":{
            "金瓶梅":{"price":100,"publish":"苹果出版社"}，
            "聊斋":{"price":200,"publish":"橘子出版社"}，
        }
    }
)
if __name__ == '__main__':
    uvicorn.run("main:app",port=8080,debug=True)

```

### jinja2的过滤器

变量可以通过“过滤器”进行修改，过滤器可以理解为是jinja2里面的内置函数和字符串处理函数。常用的过滤器有：

![image-20240220173818608](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240220173818608.png)

那么如何使用这些过滤器呢？只需要在变量后面使用管道（|）分割，多个过滤器可以链式调用，前一个过滤器的输出会作为后一个过滤器的输入。

```python
{{'abc'|captialize}}	#Abc
{{'abc'|upper}}		#ABC
{{'hello world'|title}}	#Hello World
{{'hello world'|replace('world','yuan')|upper}}		#HELLO YUAN
{{10.10|round|int}}	#18
```

让业务逻辑层的数据在模板语法上得到更好地展示

### jinjia2的控制结构

#### 分支控制

jinja2中的if语句类型与python中的if语句类型类似，它也是具有单分支、多分支等多种结构，不同的是，条件语句不需要使用冒号结尾，而结束控制语句则需要使用`endif`关键字

```jinja2
{% if %}
	<p>{{ book }}</p>
{{% endif %}}
```



#### 循环控制

jinja2中`for`循环用于迭代python的数据类型，包括列表、元组和字典。在jinja2中不存在`while`循环

```jinja2
{% for book in books %}
	<p>{{ book }}</p>
{{% endfor %}}
```









## `mysql`

数据库：存储数据的仓库，数据是有组织地进行存储

数据库管理系统：模拟和管理数据库的大型软件

`SQL`：操作关系型数据库的编程语言，定义了一套关系型数据库统一标准

![image-20240205151516470](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240205151516470.png)

![image-20240205151940173](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240205151940173.png)

- **[mysql命令行查看表字段](https://blog.csdn.net/IT_Boy_/article/details/107096018)**

![image-20240205174755515](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240205174755515.png)

![image-20240205180014145](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240205180014145.png)

![image-20240206090734218](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206090734218.png)

![image-20240206091001643](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206091001643.png)

```sql
create table 表名(
	列名 类型,
	列名 类型,
	列名 类型		--最后不用加标点
)default charset = utf8;
```

注意点：最后一个列名和类型最后是不用加标点符号的

![image-20240206092404049](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206092404049.png)

- 删除表 `drop table 表名`;
- 清空表 `delete from 表名` 或 `truncate table 表名`(不会删除表，只会删除表的内容，但是不会恢复)

![image-20240206093029217](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206093029217.png)

![image-20240206094635658](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206094635658.png)

![image-20240206095508022](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206095508022.png)

![image-20240206095647137](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206095647137.png)

![image-20240206095830676](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206095830676.png)

![image-20240206100132958](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206100132958.png)

![image-20240206102536481](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206102536481.png)

![image-20240206102645213](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206102645213.png)

![image-20240206102906735](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206102906735.png)

![image-20240206105608801](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206105608801.png)

![image-20240206105655814](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206105655814.png)

### **内置客户端操作**

数据行操作的相关`SQL`语句（指令）如下：

- 新增数据

  ```sql
  insert into 表名（列名，列名，列名）values(对应列的值，对应列的值，对应列的值);
  ```

- 删除数据

  ```sql
  delete from 表名;
  delete from 表名 where 条件;
  ```

  

- 修改数据

  ```sql
  update 表名 set 列名 = 值;
  update 表名 set 列名 = 值 where 条件;
  ```

  

- 查询数据

  ```sql
  select * from 表名;--查询这张表中的所有数据
  select 列民，列名，列名 from 表名;
  select 列名,列名 as 别名,列名 from 表名;
  select * from 表名 where 条件;
  ```

  ### **python代码操作**

  ```python
  import pymysql
  #连接MySQL
  conn = pymysql.connect(
      "host": "localhost",
      "user":"root",
      "password":"zxy110",
      "database": "mysql",
      "db" : "userdb"
  )
  cursor = conn.cursor()
  
  #1.新增（需commit）
  cursor.execute("insert into tb1(name,password) value("zxy","123123")")
  conn.commit()
  
  #2.删除（需commit）
  cursor.execute("delete from tb1 where id=1")
  conn.commit()
  
  #3.修改（需commit）
  cursor.execute("update tb1 set name='xx' where id=1")
  conn.commit()
  
  #4.查询
  cursor.execute("select * from tb where id>10")
  data = cursor.fetchone()
  print(data)
  
  #关闭链接
  cursor.close()
  conn.close()
  ```
















### 关于`SQL`注入

![image-20240206154505298](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206154505298.png)

![image-20240206154616931](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206154616931.png)

![image-20240206154639846](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206154639846.png)

因此会发生SQL注入的问题

![image-20240206154828825](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240206154828825.png)

## NATAPP

打开natapp隧道`natapp -authtoken=YOUR_TOKEN -authtype=tunnel -log=stdout`

再进入自己的服务器，根据终端提示的信息进行输入

![image-20240229180316798](https://typora-zxy10.oss-cn-beijing.aliyuncs.com/image-20240229180316798.png)
