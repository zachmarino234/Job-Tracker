from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

aggregate = Blueprint('aggregate', __name__)

# Get top 5 most popular industries (our mock data has each industry associated with 100 records
# so the results will be the same aka not a bug)
@aggregate.route('/mostpopularinds', methods=['GET'])
def get_most_popular_industries():
    cursor = db.get_db().cursor()
    query = '''
        SELECT i.name AS Industry, COUNT(*) AS Count
        FROM jobRecords jr 
        JOIN industry i ON jr.indID = i.indID
        GROUP BY i.name
        ORDER BY count DESC
        LIMIT 5

    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get top positions from other firms
@aggregate.route('/lucrativeposition', methods=['GET'])
def get_most_lucrative_positions():
    cursor = db.get_db().cursor()
    query = '''
        select c.name as Firm_Name, j.salary as Salary, sum(jobID) as Number_of_Applications, j.jobTitle as Title
        from jobRecords j
        join company c on j.companyID = c.companyID
        where salary is not null
        group by c.name, j.companyID, j.salary, j.jobTitle
        order by salary desc
        limit 50;

    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    the_response = make_response(theData)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Return industry and average salary
@aggregate.route('/industry_salary', methods=['GET'])
def get_industry_salary():
    current_app.logger.info('GET industry_salary route')
    cursor=db.get_db().cursor()
    the_query = '''
        SELECT name, ROUND(AVG(salary),0) AS Average_Salary 
        FROM jobRecords
        NATURAL JOIN industry
        GROUP BY name
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    theResponse=make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse

# Return top 10 countries by amount of job records
@aggregate.route('/country_count', methods=['GET'])
def get_country_count():
    current_app.logger.info('GET country_count route')
    cursor=db.get_db().cursor()
    the_query = '''
        SELECT jobCountry AS Country, COUNT(jobID) AS Count FROM jobRecords
        WHERE jobCountry IS NOT NULL
        GROUP BY jobCountry
        ORDER BY COUNT(jobID) DESC
        LIMIT 10
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    theResponse=make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse

# Return top 10 most popular employers
@aggregate.route('/popular_employers', methods=['GET'])
def get_popular_employers():
    current_app.logger.info('GET popular_employers route')
    cursor=db.get_db().cursor()
    the_query = '''
        SELECT name AS Company, COUNT(jobRecords.companyID) AS Count FROM jobRecords
        JOIN company ON jobRecords.companyID = company.companyID
        GROUP BY name
        ORDER BY COUNT(jobRecords.companyID) DESC 
        LIMIT 10
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    theResponse=make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse

# Get the amount of users (default is 1000 because of mock data)
@aggregate.route('/user_count', methods=['GET'])
def get_user_count():
    current_app.logger.info('GET user_count route')
    cursor=db.get_db().cursor()
    the_query = '''
        SELECT COUNT(appID) FROM applicants
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    theResponse=make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse

# Get the amount of job entries (default is 1000 because of mock data)
@aggregate.route('/job_entries', methods=['GET'])
def get_job_entries():
    current_app.logger.info('GET job_entries route')
    cursor=db.get_db().cursor()
    the_query = '''
        SELECT COUNT(jobID) FROM jobRecords
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    theResponse=make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse

# Get the amount of companies (default is 1000 because of mock data)
@aggregate.route('/companies', methods=['GET'])
def get_companies():
    current_app.logger.info('GET companies route')
    cursor=db.get_db().cursor()
    the_query = '''
        SELECT COUNT(companyID) FROM jobRecords
    '''
    cursor.execute(the_query)
    theData = cursor.fetchall()
    theResponse=make_response(theData)
    theResponse.status_code = 200
    theResponse.mimetype = 'application/json'
    return theResponse