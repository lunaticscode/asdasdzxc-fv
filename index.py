from flask import Flask, send_file, request
from util.constant import pages
from routes.article import bp as article_bp

app = Flask(__name__, static_url_path="/static", template_folder="/static")
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 # 업로드 용량 제한 10MB

@app.get(pages["index"]["route_path"])
def show_index_page():
    return send_file(pages["index"]["file_path"])

@app.get(pages["regist"]["route_path"])
def show_article_page():
    return send_file(pages["regist"]["file_path"])

@app.get(pages["article"]["route_path"])
def show_article_detail_page():
    print(request.args.get("id"))
    return send_file(pages["article"]["file_path"])

app.register_blueprint(article_bp)

if __name__ == '__main__':
    app.run()
