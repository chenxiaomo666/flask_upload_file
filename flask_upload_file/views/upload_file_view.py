# @Time    : 2020/3/6 12:01
# @Author  : 帅气的陈小陌
# @Email   : 13784197113@163.com
# File     : upload_file_view.py
# Software : PyCharm
import os
import datetime
from .. import db
from ..models import UploadFile, User
from ..config import Config
from flask import Blueprint, request, render_template, session
from ..services.upload_file_service import allowed_file

upload_file = Blueprint("upload_file", __name__)


@upload_file.route("/upload", methods=["GET", "POST"])
def upload():
    user_id = session.get("user_id", None)
    if user_id is None:
        return render_template("login.html")
    user = User.query.get(user_id)
    if request.method == 'POST':  # 如果是 POST 请求方式
        file = request.files['file']  # 获取上传的文件
        if file and allowed_file(file):  # 如果文件存在并且符合要求则为 true
            file_name = file.filename  # 获取上传文件的文件名
            file_path = os.path.join(Config.UPLOAD_FOLDER, file_name)
            file.save(file_path)  # 保存文件

            file_url = "../../file/" + file_name
            up_file = UploadFile.query.filter_by(file_name=file_name).first()
            if up_file is not None:
                pass
            else:
                up_file = UploadFile()
                up_file.file_name = file_name
                up_file.file_url = file_url
                up_file.upload_time = datetime.datetime.now()
                up_file.upload_people = user.id
                db.session.add(up_file)
                db.session.commit()

            return render_template("download.html", file_name=file_name, file_url=file_url)  # 返回保存成功的信息
        # 使用 GET 方式请求页面时或是上传文件失败时返回上传文件的表单页面
    return render_template("upload.html", name=user.name)


@upload_file.route("/files", methods=["GET"])
def get_all_files():
    user_id = session.get("user_id", None)
    if user_id is None:
        return render_template("login.html")
    user = User.query.get(user_id)

    file_list = []
    files = UploadFile.query.filter_by(is_delete=0, upload_people=user.id).all()
    for file in files:
        cur = {}
        cur["file_name"] = file.file_name
        cur["file_url"] = file.file_url
        file_list.append(cur)

    return render_template("files.html", file_list=file_list)

