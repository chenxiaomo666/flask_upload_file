# @Time    : 2020/3/6 11:42
# @Author  : 帅气的陈小陌
# @Email   : 13784197113@163.com
# File     : config.py
# Software : PyCharm
import os


class Config(object):

    # mysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ch1315203091@112.124.4.178:3306/cxm_develop"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc'])   # 允许上传的文件类型

    UPLOAD_FOLDER = os.path.join(os.getcwd(), "file")
