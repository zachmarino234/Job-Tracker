########################################################
# Sample jobRecords blueprint of endpoints
########################################################


from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

job_records = Blueprint('job_records', __name__)

# Get all job records from the existing database
@job_records.route('/jobRecords', methods=['GET'])
def get_all_job_records():

    # produces a cursor object from the database
    cursor = db.get_db().cursor()
    the_query = '''
    SELECT * FROM jobRecords;
    '''

    # use the cursor to query the database for a list of existing job records
    cursor.execute(the_query)
    
    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # create theResponse object
    theResponse = make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse


# Return all the jobs that a certain applicant has applied to
@job_records.route('/jobRecords/appID/<appID>', methods=['GET'])
def get_applicant_jobRecord(appID):
    current_app.logger.info('GET /jobRecords/<appID> route')
    cursor=db.get_db().cursor()
    cursor.execute('select * from jobRecords where appID = {0}'.format(appID))

    
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

    



# Return all the jobs within a company
@job_records.route('/jobRecords/companyID/<companyID>', methods=['GET'])
def get_company_jobRecord(companyID):
    current_app.logger.info('GET /jobRecords/<companyID> route')
    cursor=db.get_db().cursor()
    cursor.execute('select * from jobRecords where companyID = {0}'.format(companyID))
   
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
    

# Return all jobs based on a jobID
@job_records.route('/jobRecords/jobID/<jobID>', methods=['GET'])
def get_jobID_jobRecord(jobID):
    current_app.logger.info('GET /jobRecords/<jobID> route')
    cursor=db.get_db().cursor()
    cursor.execute('select * from jobRecords where jobID = {0}'.format(jobID))

    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
    

# Return all jobs within a certain industry
@job_records.route('/jobRecords/<indID>', methods=['GET'])
def get_indID_jobRecord(indID):
    current_app.logger.info('GET /jobRecords/<indID> route')
    cursor=db.get_db().cursor()
    cursor.execute('select * from jobRecords where indID = {0}'.format(indID))

    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Adding a new job records for specified applicant
@job_records.route('/job_records', methods=['PUT'])
def add_specified_job_records():
    current_app.logger.info('PUT /job_records_route')
    jobRecords_info = request.json

    #current_app.logger.info(jobRecords_info)
    job_ID = jobRecords_info['jobID']
    app_ID = jobRecords_info['appID']
    ind_ID = jobRecords_info['indID']
    company_ID = jobRecords_info['companyID']
    job_title = jobRecords_info['jobTitle']
    salary = jobRecords_info['salary']
    date_applied = jobRecords_info['dateApplied']
    description = jobRecords_info['description']
    pos_level = jobRecords_info['posLevel']
    job_type = jobRecords_info['jobType']
    job_address = jobRecords_info['jobAddress']
    job_city = jobRecords_info['jobCity']
    job_country = jobRecords_info['jobCountry']


    # Query to update this info
    query = 'insert into jobRecords (jobID, appID, indID, companyID, jobTitle, salary, dateApplied, description, posLevel, jobType, jobAddress, jobCity, jobCountry) values ("'
    query += job_ID + '", "'
    query += app_ID + '", "'
    query += ind_ID + '", '
    query += company_ID + '", '
    query += job_title + '", '
    query += salary + '", '
    query += date_applied + '", '
    query += description + '", '
    query += pos_level + '", '
    query += job_type + '", '
    query += job_address + '", '
    query += job_city + '", '
    query += job_country + ')'
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    r = cursor.execute(query)
    db.get_db().commit()
    return 'Job record updated'


# Remove a record for a certain applicant
@job_records.route('/job_records', methods=['DELETE'])
def remove_job_records(appID):
    current_app.logger.info('DELETE /job_records_route/appID/<appID>')
    jobRecords_info = request.json

    cursor = db.get_db().cursor()
    query = '''
        DELETE FROM jobRecords
        WHERE appID = {0}'''.format(appID)
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response








