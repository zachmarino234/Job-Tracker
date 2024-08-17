########################################################
# Sample recruiterNotes blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db


recruiterNotes = Blueprint('recruiterNotes', __name__)

# Access all notes made by recruiters
@recruiterNotes.route('/recruiterNotes', methods=['GET'])
def get_recruiterNotes():
    current_app.logger.info('recruiterNotes.routes.py: GET /recruiterNotes')
    cursor = db.get_db().cursor()
    cursor.execute('select * from recruiterIntNotes')
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
    db.get_db().commit()
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Creating a new note for a recruiter
@recruiterNotes.route('recruiterNotes', methods=['POST'])
def add_new_recruiter_note():

    #collecting data from request object
    app_info = request.json
    current_app.logger.info('POST /recruiterNotes_route')

    #get variable
    job_ID = app_info['jobID']
    app_ID = app_info['appID']
    recruiter_ID = app_info['recruiterID']
    date = app_info['date']

    # Constructing the query
    query = '''
        insert into interviewRecords 
        (jobID, appID, recruiterID) 
        values (%s, %s, %s)
    '''
    values = (job_ID, app_ID, recruiter_ID)
    
    current_app.logger.info(query)
    
    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    
    return 'Note added!'
    