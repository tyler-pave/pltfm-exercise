from flask import Flask, request, render_template_string
from nanoid import generate # might be handy

app = Flask(__name__)
port = 3000

# We want to build a simple URL shortener server.

# Two main endpoints:

# POST /create:
# - takes a longUrl as a body parameter
# - returns a shortCode

# GET /go/:shortCode
# - takes a shortCode URL parameter
# - returns (or redirects to) the saved longUrl

# Stage 1: Store in memory. Will implement.
# Stage 2: Store in SQLite. Will discuss, may or may not implement.
# Stage 3: Cache in Redis. Will discuss, may or may not implement.
# Stage 4: Further optimizations and enhancements. Will discuss, but will not implement.

# Potential additional functionality:
# - On creation, if we already have a shortCode for a given longUrl, just return the existing shortCode
# - Allow a user to specify a desired shortCode on creation
# - Track how many times a shortCode has been visited
# - Performance optimizations
# - Deployment scenarios



short_codes = {}

@app.route('/', methods=['GET'])
def home():
    form_html = '''<form action="/create" method="post">
                       <input type="text" name="longUrl">
                       <input type="submit">
                   </form>'''
    return render_template_string(form_html)

@app.route('/create', methods=['POST'])
def create():
    long_url = request.form['longUrl']
    # Get a longUrl body param, store it, return a shortCode

@app.route('/go/<short_code>', methods=['GET'])
def go(short_code):
    # Look up the shortCode, return the longUrl
    pass

if __name__ == '__main__':
    app.run(debug=True, port=port)
