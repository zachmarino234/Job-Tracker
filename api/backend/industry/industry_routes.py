#######################################################
# Industry blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

industry = Blueprint('industry', __name__)

# Get all industries from the DB
@industry.route('/industry', methods=['GET'])
def get_all_industries():
    cursor = db.get_db().cursor()
    query = '''
        SELECT name
        FROM industry
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Update an industry's info in the DB
@industry.route('/industry', methods=['PUT'])
def update_industry():
    ind_info = request.json
    ind_id = ind_info['indID']
    name = ind_info['name']
    size = ind_info['size']
    query = 'UPDATE industry SET name = %s, size = %s where indID = %s'
    data = (ind_id, name, size)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'industry updated!'

# Get industry detail for applicant with particular indID
@industry.route('/industry/<indID>', methods=['GET'])
def get_industry(indID):
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM industry
        WHERE indID = {0}'''.format(indID)
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add new industry to database
@industry.route('/industry', methods=['POST'])
def add_new_industry():
    
    # collecting data from the request object 
    ind_info = request.json
    current_app.logger.info(ind_info)

    #extracting the variable
    #ind_id = ind_info['indID']
    name = ind_info['name']
    size = ind_info['size']

    # Constructing the query
    query = 'insert into industry (name, size) values ("'
    #query += ind_id + '", "'
    query += name + '", "'
    query += size + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Remove an industry from the database
@industry.route('/industry/<indID>', methods=['DELETE'])
def remove_industry(indID):
    current_app.logger.info('DELETE /industry/<indID> route')
    cursor = db.get_db().cursor()
    query = '''
        DELETE FROM industry
        WHERE industryID = {0}'''.format(indID)
    cursor.execute(query)
    db.get_db().commit()
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

