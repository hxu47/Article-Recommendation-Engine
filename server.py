# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    return render_template('articles.html', articles = articles_loaded)
    
@app.route("/article/<topic>/<filename>")
def article(topic, filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    filenames = [article[0] for article in articles_loaded]    # a list of filenames 'topic/filename'
    article_index = filenames.index(topic + '/' + filename)    # get the index of the article
    article = articles_loaded[article_index]                   # get the tuple associated with the article
    title = article[1]                # get the title of the article
    text = article[2].split('\n')     # get the text of the article
    similar_articles = recommended(article, articles_loaded, 5)   # get 5 similar articles 
    return render_template('article.html', title = title, text = text, similar_articles = similar_articles)
    
# initialization
i = sys.argv.index('server:app')
glove_filename = sys.argv[i+1]
articles_dirname = sys.argv[i+2]

gloves = load_glove(glove_filename)
articles_loaded = load_articles(articles_dirname, gloves)   

