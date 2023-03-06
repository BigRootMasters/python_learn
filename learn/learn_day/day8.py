"""
json使用
"""
import json

# 测试

data = [{"age": 13, "name": "li"}, {"age": 14, "name": "zhang"}]
json_Str = json.dumps(data, ensure_ascii=False)
print(json_Str)
print(type(json_Str))
list_json = json.loads(json_Str)
print(list_json)
print(type(list_json))
