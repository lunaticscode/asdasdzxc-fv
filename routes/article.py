import codecs
from flask import Blueprint, request, redirect, jsonify
from werkzeug.utils import secure_filename
from util.constant import avail_file_ext
from os import path
from db_init import db
from gridfs import GridFS
import uuid

uploads_path = 'uploads'
grid_fs = GridFS(db, uploads_path)
print(grid_fs)
bp = Blueprint("product_route", __name__, url_prefix="/article")

@bp.get("/all")
def get_prod_all():
    try:
        article_list = list(db['article'].find())
        # result_list = []
        # for article_item in article_list:
        #     img_id = article_item["imgId"]
        #     img_binary = grid_fs.get(img_id)
        #     base64_data = codecs.encode(img_binary.read(), "base64")
        #     article_item["img"] = base64_data.decode("utf-8")
        #     result_list.append(article_item)

        return jsonify({"data": article_list, "isError": False})

    except ValueError as err:
        print(f'(!)Error {err}')
        return []

def _get_img_src(imgId):
    img_binary_data = grid_fs.get(imgId)
    img_base64_data = codecs.encode(img_binary_data.read(), "base64")
    return img_base64_data.decode("utf-8")

@bp.get("/detail")
def get_prod_detail():
    try:
        article_id = request.args.get("id")
        article_data = db['article'].find_one({"_id": article_id})
        img_id = article_data["imgId"]
        img_src = _get_img_src(img_id)
        article_data['imgSrc'] = img_src
        return jsonify({"data": article_data, "isError": False})
    except ValueError as err:
        print(err)
        return jsonify({"data": None, "isError": True})

@bp.post("/upload")
def upload_prod():
    try:
        form_data = request.form
        title = form_data.get("title")
        description = form_data.get("description")

        file_data = request.files['article_img']
        file_ext = path.splitext(file_data.filename)[1]

        if file_ext not in avail_file_ext:
            print('(!) Can not upload this file_ext format.')
            return redirect('/')

        save_file_name = secure_filename(file_data.filename) + "-" + str(uuid.uuid1())
        img_id = str(uuid.uuid1())
        grid_fs.put(file_data, _id=img_id, filename=save_file_name)
        print('file_id =>', img_id)
        save_data = {
            "_id": str(uuid.uuid1()),
            "title": title,
            "description": description,
            "imgId": img_id
        }
        db['article'].insert_one(save_data)
        return redirect('/')
    except ValueError as err:
        print(f'(!)Error {err}')
        return redirect('/')