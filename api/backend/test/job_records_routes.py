########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################


from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

job_records = Blueprint('job records', __name__)

@job_records.route('/job_records', methods=['GET'])
def get_all_job_records():
    cursor = db.get_db().cursor()
    the_query = '''
    SELECT * FROM jobRecords;
    '''

    cursor.execute(the_query)
    
    theData = cursor.fetchall()
    theResponse = make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype
    return theResponse

