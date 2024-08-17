########################################################
# Company blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db


company = Blueprint('company', __name__)

# Get all companies from the DB
@company.route('/company', methods=['GET'])
def get_all_companies():
    current_app.logger.info('company_routes.py: GET /company')
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM company
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Update company info in DB
@company.route('/company', methods=['PUT'])
def update_company():
    current_app.logger.info('PUT /company route')
    corp_info = request.json
    name = corp_info['name']
    numemp = corp_info['numEmployees']
    founding_date = corp_info['foundingDate']
    empbens = corp_info['empBenefits']
    value = corp_info['value']
    ind_id = corp_info['indID']
    corp_id = corp_info['companyID']
    query = 'UPDATE company SET name = %s, numEmployees = %s, foundingDate = %s, empBenefits = %s, value = %s, indID = %s WHERE companyID = %s'
    values = (name, numemp, founding_date, empbens, value, ind_id, corp_id)
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, values)
    db.get_db().commit()
    return 'company updated!'

# Get company details for company with particular companyID
@company.route('/company/<companyID>', methods=['GET'])
def get_company(companyID):
    current_app.logger.info('GET /company/<companyID> route')
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM company
        WHERE companyID = {0}'''.format(companyID)
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add new company to database
@company.route('/company', methods=['POST'])
def add_new_company():
    
    # collecting data from the request object 
    corp_info = request.json
    current_app.logger.info(corp_info)

    #extracting the variable
    name = corp_info['name']
    numemp = corp_info['numEmployees']
    founding_date = corp_info['foundingDate']
    empbens = corp_info['empBenefits']
    value = corp_info['value']
    ind_id = corp_info['indID']

    # Constructing the query
    query = 'insert into company (name, numEmployees, foundingDate, empBenefits, value, indID) values (%s, %s, %s, %s, %s, %s)'
    values = (
        name,
        numemp,
        founding_date,
        empbens,
        value,
        ind_id
    )
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    
    return 'Success!'

# Remove a company from the database
@company.route('/company/<companyID>', methods=['DELETE'])
def remove_company(companyID):
    current_app.logger.info('DELETE /company/<companyID> route')
    cursor = db.get_db().cursor()
    query = '''
        DELETE FROM company
        WHERE companyID = {0}'''.format(companyID)
    cursor.execute(query)
    db.get_db().commit()
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response