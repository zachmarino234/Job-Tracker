########################################################
# Sample jobRecords blueprint of endpoints
########################################################


from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db


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
@job_records.route('/job_records', methods=['POST'])
def add_specified_job_records():
    current_app.logger.info('POST /job_records_route')
    jobRecords_info = request.json

    #current_app.logger.info(jobRecords_info)

    #since auto-increment not needed??
    #job_ID = jobRecords_info['jobID']


    app_ID = jobRecords_info['appID']
    ind_ID = jobRecords_info['indID']
    company_ID = jobRecords_info['companyID']
    job_title = jobRecords_info['jobTitle']
    salary = jobRecords_info['salary']

    #also defaulted to today
    #date_applied = jobRecords_info['dateApplied']

    description = jobRecords_info['description']
    pos_level = jobRecords_info['posLevel']
    job_type = jobRecords_info['jobType']
    job_address = jobRecords_info['jobAddress']
    job_city = jobRecords_info['jobCity']
    job_country = jobRecords_info['jobCountry']


    # Query to update this info
    query = 'insert into jobRecords (appID, indID, companyID, jobTitle, salary, description, posLevel, jobType, jobAddress, jobCity, jobCountry) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    values = (
    app_ID,
    ind_ID,
    company_ID,
    job_title,
    salary,
    description,
    pos_level,
    job_type,
    job_address,
    job_city,
    job_country
    )

    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, values)
    db.get_db().commit()
    return 'Job record added'


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
    db.get_db().commit()
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



# Get all job entries for a user
@job_records.route('/job_records/user_job_entries/<appID>', methods=['GET'])
def get_user_job_entries(appID):
    current_app.logger.info('GET user_job_entries route')
    cursor=db.get_db().cursor()
    the_query = '''
        SELECT jobTitle AS Position, c.name AS Company, i.name AS Industry, salary AS Salary, dateApplied As Applied, description AS Description, posLevel AS Level, jobAddress AS Address, jobCity As City, jobCountry AS Country FROM jobRecords jr
    LEFT JOIN company c on c.companyID = jr.companyID
    LEFT JOIN industry i ON i.indID = jr.indID = i.indID
    WHERE appID = {0}'''.format(appID)
    cursor.execute(the_query)
    theData = cursor.fetchall()
    theResponse=make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse





