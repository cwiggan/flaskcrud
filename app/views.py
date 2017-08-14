from flask import render_template, request, url_for, redirect

from app import app
from models import Comment
from app import db

@app.route('/')
def index():
    guest = Comment.query.order_by(Comment.id)
    return render_template("index.html", guest=guest)

@app.route('/add')
def about():
    return render_template("about.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    sign = Comment(name=name, comment=comment)
    db.session.add(sign)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/edit')
def edit():
    guests = Comment.query.all() 
    return render_template("admin.html", guests=guests)

@app.route('/edit<id>')
def update(id):
    guest = Comment.query.(id)
    return render_template("edit.html",guest=guest)