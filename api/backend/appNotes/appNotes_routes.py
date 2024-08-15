########################################################
# Notes blueprint of applicantNotes endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

appNotes = Blueprint('appNotes', __name__)

# Get notes from a particular applicant
@appNotes.route('/appNotes/<appID>', methods=['GET'])
def get_app_notes(appID):
    current_app.logger.info('GET /appNotes/<appID> route')
    cursor = db.get.db().cursor()
    query = 'select * from applicantIntNotes where appID={0}'.format(appID)
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Update content of a particular note for an applicant
@appNotes.route('/appNotes/<appID>', methods=['PUT'])
def update_app_notes(appID):
    current_app.logger.info('PUT /appNotes route')
    app_info = request.json
    content = app_info['content']
    app_id = app_info['appID']
    interview_ID = app_info['interviewID']
    query = 'update applicantIntNotes set content = %s where appID = {0}'.format(appID)
    data = (content, app_id, interview_ID)
    cursor = db.get_db().cursor()
    r=cursor.execute(query, data)
    db.get_db().commit()
    return 'note updated!'


# Remove a note record from the from an applicant
@appNotes.route('/appNotes/<appID>', methods=['DELETE'])
def remove_app_notes(appID):
    current_app.logger.info('DELETE /appNotes route')
    appNotes_info = request.json
    content = appNotes_info['content']
    app_id = appNotes_info['appID']
    interview_ID = appNotes_info['interviewID']
    query = 'delete from applicantIntNotes where appID = {0}'.format(appID)
    data = (content, app_id, interview_ID)
    cursor = db.get_db().cursor()
    r=cursor.execute(query, data)
    db.get_db().commit()
    return 'note updated!'
