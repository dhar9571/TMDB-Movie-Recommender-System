from flask import render_template, Blueprint, request, jsonify
import pandas as pd 
import numpy as np 
from utility.log_handler import Logger
from utility.params_utils import ParamsUtils

# creating a variable controller using flask Blueprint
controller = Blueprint('controller', __name__)

# Setup Logger
logger = Logger.setup_logger()

# Get application settings:
settings = ParamsUtils.get_configuration('config.yaml')

@controller.route('/')
def onload():
    logger.debug("Onload successfull...")
    return render_template('layout.html')