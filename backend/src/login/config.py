import yaml
import os

class Config:
    _config = None

    @classmethod
    def load(cls,file_path):
        if cls._config is None:
            with open(file_path, 'r',encoding='utf-8') as file:
                cls._config = yaml.safe_load(file)
        return cls._config

    @classmethod
    def get(cls, key):
        return cls._config.get(key)

# 加载配置文件
import os
config_path = os.path.join('src','saves', 'login','loginConfig.yaml')
os.makedirs(os.path.dirname(config_path), exist_ok=True)
config = Config.load(config_path)

# print(config.get("token"))

# 现在可以在程序的任何地方使用config对象来访问配置
# 例如：
# database_host = config.get('database')['host']
# logging_level = config.get('logging')['level']