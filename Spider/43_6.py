# 本案例用request.Request类实现
# 对比43_5案例

"""
利用parse模块模拟post请求
分析百度词典，参考图片43_5
分析步骤：
1. 打开网页检查（F12），输入单次girl,
2. 一个字母一个字母的输入，每输入一个字母，都会发生一次请求
3. headers采用name排序，会看见有四个sug,发生了四次请求
4. 查看headers里面的FormData的值是kw:girl
5. 检查返回的内容content-type是json格式，需要用到json包
"""
"""
大致流程：
1. 利用Request请求内容（可以进行大量的请求），然后urlopen打开
2. 返回一个json格式的内容
3. 结果就应该是girl的释义
"""

from urllib import request, parse
import json

baseurl = 'https://fanyi.baidu.com/sug'

# 存储用来模拟formdata的数据一定是字典格式
wd = input('Input your keyword: ')
data = {'kw': wd}

# 需要对data进行编码
data = parse.urlencode(data).encode('utf-8')

# 我们需要构造一个请求头，请求头至少包含数据的长度
# request要求传入的请求头是一个dict格式
headers = {'Content-Length': len(data)}

# 构造一个Request类的实例，可以ctrl然后右键查看Request类的源代码
req = request.Request(url=baseurl, data=data, headers=headers)

# 已经构造了一个Request类的实例，然后用urlopen打开
rsp = request.urlopen(req)
json_data = rsp.read().decode('utf-8')

# 把json的原始字符串数据形式转换成python可编写的字典格式
json_data = json.loads(json_data)

# 查看结果是一个字典，取出字典中键data对应的值是一个列表，
# 列表中又是有多个字典,每个字典中有两个键值对，将两个值取出，一一对应
for item in json_data['data']:
    # print(item)
    print(item['k'], "-----", item['v'])
