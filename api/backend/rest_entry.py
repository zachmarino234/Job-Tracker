import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask

from backend.db_connection import db


#Adding all Blueprint objects needed
from backend.jobRecords.job_records_routes import job_records
from backend.appNotes.appNotes_routes import appNotes
from backend.recruiterNotes.recruiterNotes_routes import recruiterNotes
from backend.applicants.applicants_routes import applicants
from backend.industry.industry_routes import industry
from backend.company.company_routes import company
from backend.aggData.aggregate_data_routes import aggregate

import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Load environment variables
    load_dotenv()

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    # app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # # these are for the DB object to be able to connect to MySQL. 
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_ROOT_PASSWORD')
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT'))
    app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME')  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)

    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the TalentTrace API</h1>"
    
    
    
    app.logger.info('current_app(): registering blueprints with Flask app object.')

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    
    app.register_blueprint(applicants, url_prefix='/a')
    app.register_blueprint(industry,url_prefix='/i')
    app.register_blueprint(company,url_prefix='/co')
    app.register_blueprint(aggregate, url_prefix = '/agg' )
    app.register_blueprint(job_records, url_prefix='/jbr')
    app.register_blueprint(appNotes, url_prefix = '/an')
    app.register_blueprint(recruiterNotes, url_prefix = '/rn')

    

    # Don't forget to return the app object
    return app

