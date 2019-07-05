# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/4 18:16
    file   : index.py
    
"""
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>image</title>
</head>
<body>
<img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562245045590&di=5e4257334c0174d7a66b74c514fd27d6&imgtype=0&src=http%3A%2F%2Fimg.ph.126.net%2FwpR2sizFIqC7f_zg5LoCJA%3D%3D%2F3400217718665946440.jpg"
     alt="">
</body>
</html>
"""  # 要返回的数据 response 的body

# 返回响应的头部，具体描述的要返回的内容类型，在cgi中用print进行返回
print("content-type:text/html")
# 返回头部结束
print("\n")
# 返回响应的body
print(html)
