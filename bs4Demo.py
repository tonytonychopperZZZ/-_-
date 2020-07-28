#-*- codeing = utf-8 -*-
#@Time : 2020/7/13 15:38
#@Author:CHOPPER
#@File : bs4Demo.py
#@Software: PyCharm
'''
BeautifulSoup 将复杂的html文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为四种：(BeautifulSoup可以解析js，xml等)
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''

from bs4 import BeautifulSoup

file = open("./baidu,html","rb")
html = file.read()
#html.parser 是一个解析器
bs = BeautifulSoup(html,"html.parser")

# 1.Tag_标签及其内容：拿到找到的第一个内容(标签有：head,div,a...)
print(bs.title)
print(bs.a)
print(bs.head)
print(type(bs.title))

# 2.NavigableString_标签里的内容（字符串）
print(bs.title.string)

# 拿到标签里的所有属性，且是键值对的形式
print(bs.a.attrs)

# 3.BeautifulSoup  表示整个文档
print(type(bs))

# 4.comment 是一个特殊的NavigableString，输出不包含注释的string
print(bs.a.string)


# 文档的遍历   很少用
print(bs.head.contents)
print(bs.head.content[1])

# 文档搜索  重要***

# 1.find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")

# 正则表达式搜索：使用search（）方法来匹配,以标签为单位匹配
t_list = bs.find_all(re.compile("a") # 查找有a的内容

# 方法：传入一个函数（方法），根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")  #标签里有name的内容

t_list = bs.find_all(name_is_exists)

# 2.kwargs   参数
t_list = bs.find_all(id="head")
t_list = bs.find_all(class=True)

# 3.text参数
t_list = bs.find_all(text = "hao123")
t_list = bs.find_all(text=["hao123","地图","贴吧"])

t_list = bs.find_all(text = re.compile("\d"))  #应用正则表达式查找包含特定文本的内容（标签里的字符串）

# 4.limit 参数
t_list = bs.find_all("a",limit=3)  #得到结果为三条

# css选择器

# t_list = bs.selct('title')  #通过标签来查找
# t_list = bs.selct(".mnav")  #通过类名来查找
# t_list = bs.selct("#u1")  #通过id来查找
# t_list = bs.selct("a[class='bri']")  #通过属性来查找
# 未完 视频21,25分



# 输出
print(t_list)
for item in t_list:
    print(item)



