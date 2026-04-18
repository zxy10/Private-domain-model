# from src.login.config import config
from logging import ERROR

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from src.utils.password import get_password_hash

Base = declarative_base()

# 加载用户数据库
# mysql_host = config["mysql"]["host"]
# mysql_user = config["mysql"]["user"]
# mysql_password = config["mysql"]["password"]
# mysql_db = config["mysql"]["database"]

mysql_user = 'root'
mysql_password = 'zxy110'
#mysql_host = '47.103.8.209:19050'
mysql_host = 'localhost'
mysql_db = 'private_domain_model'

engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}?charset=utf8",
                       echo=True,
                       pool_size=8,
                       pool_recycle=60 * 30
                       )


class User(Base):
    __tablename__ = 'users'

    userid = Column(String(255), primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255))
    full_name = Column(String(255))
    password = Column(String(255), nullable=False)  # 添加 password 字段
    roleid = Column(Integer, default=0)

    def __init__(self, userid, username='', password='', email='', full_name='', roleid=0):
        self.userid = userid
        self.username = username
        self.email = email
        self.full_name = full_name
        self.password = get_password_hash(password)
        self.roleid = roleid

DbSession = sessionmaker(bind=engine)
session = DbSession()


def InsertUser(username,userid,password):
    try:
        userInsert = User(userid, username, password)
        session.add(userInsert)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False

def UpdateUser(userid, password):
    try:
        users = session.query(User).filter_by(userid=userid).first()
        users.password = get_password_hash(password)
        session.add(users)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False


def SelectUserByUserID(userid):
    try:
        users = session.query(User).filter_by(userid=userid).all()
        if not users:
            return None
        else:
            return users[0]
    except Exception as e:
        session.rollback()
        raise e

def SelectUserByUserName(username):
    try:
        users = session.query(User).filter_by(username=username).all()
        if not users:
            return None
        else:
            return users[0]
    except Exception as e:
        session.rollback()
        raise e

if __name__ == '__main__':
    InsertUser('admin','123456','123456')

    # user = SelectUserByUserName('nanxun')
    # user_select = User(user.userid, user.username, user.password)
    # print(user_select)
    # UpdateUser(25484,'123464565rg')