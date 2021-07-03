from flask import render_template, request, Blueprint
from flaskblog.models import Post, Service

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page = 4)
    
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/services')
def services():
    page = request.args.get('page', 1, type=int)
    services = Service.query.order_by(Service.date_posted.desc()).paginate(page=page, per_page = 4)
    print("services ------ ", services)
    return render_template('services.html', title='Services', services=services)