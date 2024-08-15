########################################################
# Sample recruiterNotes blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

recruiterNotes = Blueprint('recruiterNotes', __name__)

# Access all notes made by a certain recruiter
@recruiterNotes.route('/recruiterNotes/<recruiterID>', methods=['GET'])
def get_recruiterNotes(recruiterID):
    current_app.logger.info('recruiterNotes.routes.py: GET /recruiterNotes')
    cursor = db.get_db().cursor()
    cursor.execute('select * from recruiterIntNotes where recruiterID = {0}'.format(recruiterID))
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
    
# Updating notes from a certain recruiter
@recruiterNotes.route('/recruiterNotes/<recruiterID>', methods=['PUT'])
def update_recruiterNotes(recruiterID):
    current_app.logger.info('PUT /recruiterNotes route')
    recruiterNotes_info = request.json
    recruiter_ID = recruiterNotes_info['recruiterID']
    interview_ID = recruiterNotes_info['interviewID']
    certificates = recruiterNotes_info['PopularCertificates']
    skill = recruiterNotes_info['PopularSkill']
    role = recruiterNotes_info['Role']
    compensation = recruiterNotes_info['compensation_range']

    query = 'update recruiterIntNotes set interviewID = %s, PopularCertificates = %s, PopularSkill = %s, Role = %s, compensation_range = %s where recruiterID = %s'.format(recruiterID)
    data = (interview_ID, certificates, skill, role, compensation, recruiter_ID)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'note updated!'

# Removing irrelevant recruiterNote
@recruiterNotes.route('/recruiterNotes/<recruiterID>', methods=['DELETE'])
def remove_recruiterNotes(recruiterID):
    current_app.logger.info('DELETE /recruiterNotes/<recruiterID> route')
    cursor = db.get_db().cursor()
    query = '''
        DELETE FROM recruiterIntNotes
        WHERE appID = {0}'''.format(recruiterID)
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
    