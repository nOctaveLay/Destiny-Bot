import configparser as cfp

config_parser = cfp.ConfigParser()

config_parser['info'] = {
    'name': '사기라',
    'nation': 'kor',
    'owner': 'NULL'
}

config_parser['default'] ={
    'hello': ''
}
with open('./config_default.ini', 'w') as f:
    config_parser.write(f)
