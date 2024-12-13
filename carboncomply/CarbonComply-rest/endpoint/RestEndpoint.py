from pathlib import Path

from flask import request, jsonify, Blueprint
from flask_cors import cross_origin

from werkzeug.utils import secure_filename

# import jsonpickle
import json

from endpoint import Config
from service.FileService import FileService
from service.PipelineService import PipelineService
from CommunicationReport import FileNames

ALLOWED_EXTENSIONS = set(['xls', 'csv', 'xlsx'])

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/api/test/', methods=['GET'])
@cross_origin(supports_credentials=True)
def test():
    return jsonify({"test":True})


@main_blueprint.route('/api/uploadFile/', methods=['POST'])
@cross_origin(supports_credentials=True)
def upload_file():
    file_service = FileService()
    file = request.files.getlist('files')
    print(request.files, "....")
    data_folder = file_service.create_workdir(Config.DATA_FOLDER)
    for f in file:
        print(f.filename)
        filename = secure_filename(f.filename)
        if _allowed_file(filename):
            file_service = FileService()
            file_service.save(data_folder, f, filename)
            return jsonify({"name": filename, "status": "success"})
        else:
            return jsonify({'message': 'File type not allowed'}), 400
    return jsonify({"message": "No file detected."})


@main_blueprint.route('/api/convert/', methods=['POST'])
@cross_origin(supports_credentials=True)
def convert_cbam_excel_file():
    pipeline_service = PipelineService()
    file_service = FileService()
    workdir = file_service.create_workdir(Config.DATA_FOLDER)
    files = request.files.getlist('cbam_xls')
    return pipeline_service.execute_pipeline(workdir, files)



def _allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
