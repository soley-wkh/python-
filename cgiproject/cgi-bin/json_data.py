# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/4 18:56
    file   : json_data.py
    
"""
import time
import random
import json

now = time.strftime("%H:%M:%S", time.localtime())
num = random.randint(1, 11)

result = {"now": now, "num": num}

# 将字典转换为json
json_result = json.dumps(result)

print("content-type:application/json")
print("\n")  # 返回头部结束

print(json_result)
