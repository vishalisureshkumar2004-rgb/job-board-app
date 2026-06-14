from flask import Blueprint

applications = Blueprint('applications', __name__)

@applications.route('/my-applications')
def my_applications():
    return "My Applications - Coming in Phase 4"