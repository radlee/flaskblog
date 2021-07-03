from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required 
from flaskblog import db
from flaskblog.models import Service
from flaskblog.services.forms import ServiceForm

services = Blueprint('services', __name__)

@services.route('/service/new', methods=['GET', 'POST'])
@login_required
def new_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(title=form.title.data, description=form.description.data)
        db.session.add(service)
        db.session.commit()
        flash('Your service has been created!', 'success')
        return redirect(url_for('main.service'))
    return render_template('create_service.html', title='New Service', form=form, legend='New Service')


