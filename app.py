import feedparser
from flask import Flask, render_template, request


app = Flask(__name__)

FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
         'sky': 'http://feeds.skynews.com/feeds/rss/world.xml',
         'cnn': 'http://rss.cnn.com/rss/edition.rss'}


@app.route("/")
@app.route("/<publication>")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(FEEDS[publication])
    return render_template("index.html",
                           articles=feed['entries'])


if __name__ == '__main__':
    app.run(debug=True, port=8000)
