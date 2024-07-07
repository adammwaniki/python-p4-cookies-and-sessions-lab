#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles')
def index_articles():
    articles = Article.query.all()
    return jsonify([{'id': article.id, 'title': article.title, 'content': article.content} for article in articles])

@app.route('/articles/<int:id>', methods=['GET'])
def show_article(id):
    """
    article = Article.query.filter_by(id=id).first()
    if not article:
        return "Article not found", 404
    
    if "page_views" in session:
        session['page_views'] += 1  # Incrementing session data
    else:
        session['page_views'] = 1  # Initializing session data

    return f"Total visits: {session['page_views']}"

"""

if __name__ == '__main__':
    app.run(port=5555)


# Notes on getting website visitors counted through cookies
"""
# from flask import Flask, request, make_response 
  
app = Flask(__name__) 
app.config['DEBUG'] = True
  
  
@app.route('/') 
def vistors_count(): 
    # Converting str to int 
    count = int(request.cookies.get('visitors count', 0)) 
    # Getting the key-visitors count value as 0 
    count = count+1
    output = 'You visited this page for '+str(count) + ' times'
    resp = make_response(output) 
    resp.set_cookie('visitors count', str(count)) 
    return resp 
  
  
@app.route('/get') 
def get_vistors_count(): 
    count = request.cookies.get('visitors count') 
    return count 
  
  
app.run() 
"""
