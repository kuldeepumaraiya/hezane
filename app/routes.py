from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post_id=post_id)


@bp.route('/create')
def create():
    return render_template('create.html')
