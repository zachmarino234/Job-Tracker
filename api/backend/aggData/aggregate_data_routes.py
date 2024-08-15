from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
from backend.ml_models.model01 import predict

aggregate = Blueprint('aggregate', __name__)

# Get all applicants from the DB
@aggregate.route('/mostpopularinds', methods=['GET'])
def get_most_popular_industries():
    cursor = db.get_db().cursor()
    query = '''
        SELECT i.name, COUNT(*) AS count
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