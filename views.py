from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

# template param
# http://127.0.0.1:8000/views
@views.route('/')
def home():
    return render_template("index.html", name = "Python")

# url param
# http://127.0.0.1:8000/views/profile/Mariana
#@views.route('/profile/<username>')
#def profile(username):
#    return render_template("index.html", name = username)

# query param
# http://127.0.0.1:8000/views/profile?name=Mariana
# @views.route('/profile')
# def profile():
#     args = request.args
#     name = args.get('name')
#     return render_template("index.html", name = name)

# template inheritance
# http://127.0.0.1:8000/views/profile
@views.route('/profile')
def profile():
    return render_template("profile.html")

# returning JSON
# http://127.0.0.1:8000/views/json
@views.route('/json')
def get_json():
    return jsonify({'name': 'Name', 'lastname': 'Lastname'})

# getting JSON data 
@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

# redirect
@views.route('go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))
