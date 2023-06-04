from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from werkzeug.datastructures import FileStorage
import pandas as pd
import os

app = Flask(__name__)
api = Api(app)

UPLOAD_DIRECTORY = "./uploads"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


def handle_upload(file):
    filename = file.filename
    file.save(os.path.join(UPLOAD_DIRECTORY, filename))


class FileUploadResource(Resource):
    def post(self):
        file = request.files['file']
        if file:
            handle_upload(file)
            return {"message": "File successfully uploaded"}, 200
        else:
            return {"message": "Request does not contain a file"}, 400


class FileListResource(Resource):
    def get(self):
        files = os.listdir(UPLOAD_DIRECTORY)
        return {"files": files}, 200


class FileContentsResource(Resource):
    def get(self, filename):
        filepath = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.exists(filepath):
            df = pd.read_csv(filepath)
            return df.to_dict(), 200
        else:
            return {"message": f"No file named {filename}"}, 404


api.add_resource(FileUploadResource, "/upload")
api.add_resource(FileListResource, "/files")
api.add_resource(FileContentsResource, "/files/<string:filename>")

if __name__ == '__main__':
    app.run(debug=True)
