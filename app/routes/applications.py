from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Application, Job

applications = Blueprint('applications', __name__)


@applications.route('/apply/<int:job_id>', methods=['POST'])
@login_required
def apply(job_id):
    if current_user.role != 'candidate':
        flash('Only candidates can apply for jobs.', 'danger')
        return redirect(url_for('jobs.job_detail', job_id=job_id))

    job = Job.query.get_or_404(job_id)

    existing = Application.query.filter_by(user_id=current_user.id, job_id=job_id).first()
    if existing:
        flash('You have already applied for this job.', 'warning')
        return redirect(url_for('jobs.job_detail', job_id=job_id))

    application = Application(
        user_id=current_user.id,
        job_id=job_id,
        status='pending'
    )
    db.session.add(application)
    db.session.commit()

    flash('Application submitted successfully!', 'success')
    return redirect(url_for('applications.my_applications'))


@applications.route('/my-applications')
@login_required
def my_applications():
    if current_user.role != 'candidate':
        flash('Access denied.', 'danger')
        return redirect(url_for('jobs.index'))

    my_apps = Application.query.filter_by(user_id=current_user.id).order_by(Application.applied_at.desc()).all()
    return render_template('applications/my_applications.html', applications=my_apps)


@applications.route('/job/<int:job_id>/applicants')
@login_required
def job_applicants(job_id):
    job = Job.query.get_or_404(job_id)

    if job.posted_by != current_user.id:
        flash('Access denied.', 'danger')
        return redirect(url_for('jobs.employer_dashboard'))

    applicants = Application.query.filter_by(job_id=job_id).order_by(Application.applied_at.desc()).all()
    return render_template('applications/job_applicants.html', job=job, applicants=applicants)


@applications.route('/application/<int:app_id>/status/<string:new_status>', methods=['POST'])
@login_required
def update_status(app_id, new_status):
    application = Application.query.get_or_404(app_id)
    job = Job.query.get_or_404(application.job_id)

    if job.posted_by != current_user.id:
        flash('Access denied.', 'danger')
        return redirect(url_for('jobs.employer_dashboard'))

    if new_status not in ['accepted', 'rejected', 'pending']:
        flash('Invalid status.', 'danger')
        return redirect(url_for('applications.job_applicants', job_id=job.id))

    application.status = new_status
    db.session.commit()
    flash(f'Application marked as {new_status}.', 'success')
    return redirect(url_for('applications.job_applicants', job_id=job.id))