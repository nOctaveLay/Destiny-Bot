from configparser import ConfigParser as cf

config = cf()
config['Default'] = dict()
config['Default']['name'] = '사기라'
config['Default']['token'] = 'token_value'

config['Test']= dict()
config['Test']['name'] = '베타'
config['Test']['token'] = 'token_value'

with open('./env/config.ini', 'w',encoding='utf8') as configfile:
    config.write(configfile)