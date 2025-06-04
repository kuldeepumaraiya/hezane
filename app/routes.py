from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__)

# In-memory storage for blog posts
posts = []


@bp.route('/')
def index():
    return render_template('index.html', posts=posts)


@bp.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post_id=post_id)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        posts.append({'title': title, 'content': content})
        return redirect(url_for('main.index'))
    return render_template('create.html')
