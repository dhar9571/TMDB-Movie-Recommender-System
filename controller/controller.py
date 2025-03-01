from flask import render_template, Blueprint, request, jsonify
import pandas as pd 
import numpy as np 
from utility.log_handler import Logger
from utility.params_utils import ParamsUtils
<<<<<<< HEAD
=======
from src.data_preparation import PrepareData

# creating preparedata class object
prep_data_obj = PrepareData()
>>>>>>> master

# creating a variable controller using flask Blueprint
controller = Blueprint('controller', __name__)

# Setup Logger
logger = Logger.setup_logger()

# Get application settings:
settings = ParamsUtils.get_configuration('config.yaml')
<<<<<<< HEAD
=======
#

>>>>>>> master

@controller.route('/')
def onload():
    logger.debug("Onload successfull...")
<<<<<<< HEAD
    return render_template('layout.html')
=======
    return render_template('layout.html')


@controller.route('/get_movies')
def get_movies():
    credits = pd.read_csv(settings['paths']['credits'])
    
    movies_titles = sorted(list(credits['title'].values))
    
    return jsonify(movies_titles)  # Return movie list as JSON


@controller.route('/recommend')
def recommend():
    
    prep_data_obj
>>>>>>> master
