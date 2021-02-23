import json

__all__ = ['read_json','write_json']

def read_json(file_name:str):
    with open(file_name,'r',encoding='utf-8') as f:
        json_content = json.load(f)
    return json_content

def write_json(content,file_name:str):
    with open(file_name,'w',encoding='utf-8') as f:
        json.dump(content,f)