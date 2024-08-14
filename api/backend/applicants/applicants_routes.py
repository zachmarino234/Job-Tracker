########################################################
# Applicants blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

applicants = Blueprint('applicants', __name__)

# Get all applicants from the DB
@applicants.route('/applicants', methods=['GET'])
def get_all_applicants():
    current_app.logger.info('applicants_routes.py: GET /applicants')
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM applicants
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Update an applicants info in DB
@applicants.route('/applicants', methods=['PUT'])
def update_customer():
    current_app.logger.info('PUT /applicants route')
    app_info = request.json
    app_id = app_info['appID']
    first = app_info['fName']
    last = app_info['lName']
    email = app_info['email']
    prospect_pos = app_info['prospectPos']
    query = 'UPDATE applicants SET fName = %s, lName = %s, email = %s, prospectPos = %s where appID = %s'
    data = (first, last, email, prospect_pos, app_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'account updated!'

# Get applicant detail for applicant with particular appID
@applicants.route('/applicants/<appID>', methods=['GET'])
def get_applicant(appID):
    current_app.logger.info('GET /applicants/<appID> route')
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM applicants
        WHERE appID = {0}'''.format(appID)
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add new applicant to database
@applicants.route('/applicants', methods=['POST'])
def add_new_applicant():
    
    # collecting data from the request object 
    app_info = request.json
    current_app.logger.info(app_info)

    #extracting the variable
    first = app_info['fName']
    last = app_info['lName']
    email = app_info['email']
    prospect_pos = app_info['prospectPos']

    # Constructing the query
    query = 'insert into applicants (fName, lName, email, prospect_pos) values ("'
    query += first + '", "'
    query += last + '", "'
    query += email + '", '
    query += prospect_pos + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Remove an applicant from the database
@applicants.route('/applicants/<appID>', methods=['DELETE'])
def get_applicant(appID):
    current_app.logger.info('DELETE /applicants/<appID> route')
    cursor = db.get_db().cursor()
    query = '''
        DELETE FROM applicants
        WHERE appID = {0}'''.format(appID)
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response