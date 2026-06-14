from flask import Blueprint, render_template
from app.models import Job

jobs = Blueprint('jobs', __name__)

@jobs.route('/')
def index():
    all_jobs = Job.query.order_by(Job.created_at.desc()).all()
    return render_template('jobs/index.html', jobs=all_jobs)


@jobs.route('/new')
def new_job():
    return "New Job Page - Coming in Phase 3"


@jobs.route('/dashboard')
def employer_dashboard():
    return "Employer Dashboard - Coming in Phase 3"