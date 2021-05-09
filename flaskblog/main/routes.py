from flask import render_template, request, Blueprint, send_from_directory
from flaskblog.models import Post
import markdown

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    for p in posts.items:
        p.content = markdown.markdown(p.content)
    return render_template('blog.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/ridership")
def ridership():
    return send_from_directory('templates', 'ridership_eda.html')

@main.route("/plotly.js")
def plotly_script():
    return send_from_directory('static', 'plotly.js')
