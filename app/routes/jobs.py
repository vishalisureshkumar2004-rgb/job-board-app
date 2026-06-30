from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Job

jobs = Blueprint('jobs', __name__)


@jobs.route('/')
def index():
    search = request.args.get('search', '').strip()
    location = request.args.get('location', '').strip()
    job_type = request.args.get('job_type', '')

    query = Job.query

    if search:
        search_terms = search.split()
        for term in search_terms:
            query = query.filter(
                db.or_(
                    Job.title.ilike(f'%{term}%'),
                    Job.company.ilike(f'%{term}%'),
                    Job.description.ilike(f'%{term}%')
                )
            )
    if location:
        query = query.filter(Job.location.ilike(f'%{location}%'))
    if job_type:
        query = query.filter(Job.job_type == job_type)

    all_jobs = query.order_by(Job.created_at.desc()).all()
    return render_template('jobs/index.html', jobs=all_jobs, search=search, location=location, job_type=job_type)


@jobs.route('/job/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('jobs/detail.html', job=job)


@jobs.route('/new', methods=['GET', 'POST'])
@login_required
def new_job():
    if current_user.role != 'employer':
        flash('Only employers can post jobs.', 'danger')
        return redirect(url_for('jobs.index'))

    if request.method == 'POST':
        job = Job(
            title=request.form.get('title'),
            description=request.form.get('description'),
            company=request.form.get('company'),
            location=request.form.get('location'),
            salary=request.form.get('salary'),
            job_type=request.form.get('job_type'),
            posted_by=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!', 'success')
        return redirect(url_for('jobs.employer_dashboard'))

    return render_template('jobs/new_job.html')


@jobs.route('/job/<int:job_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)

    if job.posted_by != current_user.id:
        flash('You can only edit your own job postings.', 'danger')
        return redirect(url_for('jobs.employer_dashboard'))

    if request.method == 'POST':
        job.title = request.form.get('title')
        job.description = request.form.get('description')
        job.company = request.form.get('company')
        job.location = request.form.get('location')
        job.salary = request.form.get('salary')
        job.job_type = request.form.get('job_type')
        db.session.commit()
        flash('Job updated successfully!', 'success')
        return redirect(url_for('jobs.employer_dashboard'))

    return render_template('jobs/edit_job.html', job=job)


@jobs.route('/job/<int:job_id>/delete', methods=['POST'])
@login_required
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)

    if job.posted_by != current_user.id:
        flash('You can only delete your own job postings.', 'danger')
        return redirect(url_for('jobs.employer_dashboard'))

    db.session.delete(job)
    db.session.commit()
    flash('Job deleted successfully.', 'info')
    return redirect(url_for('jobs.employer_dashboard'))


@jobs.route('/dashboard')
@login_required
def employer_dashboard():
    if current_user.role != 'employer':
        flash('Access denied. Employer account required.', 'danger')
        return redirect(url_for('jobs.index'))

    my_jobs = Job.query.filter_by(posted_by=current_user.id).order_by(Job.created_at.desc()).all()
    return render_template('jobs/dashboard.html', jobs=my_jobs)