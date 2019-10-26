from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
posts = {
    0: {
        'post_id': 0,
        'title': 'Hello, world',
        'content': 'This is my first post on Flask!'
    }
}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')  # /post/0
def post_view(post_id):
    post = posts.get(post_id)
    if not post:  # if post not found
        return render_template('404.html', message=f'A post with id {post_id} was not found.')

    # post=post argument and value
    return render_template('post.html', post=post)


# recieve entered data from /post/form
@app.route('/post/create', methods=['GET', 'POST'])
def create_post():
    # use POST method to get data not showing in url window
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}
        # redirect from form to view entered post
        return redirect(url_for('post_view', post_id=post_id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
