from utils.utils import db
posts = db['posts']
    
def addPostToDB(post):
        post = {
            'title': post.get('title'),
            'content': post.get('content'),
            'author': post.get('author'),
            'date': post.get('date'),
            'likes': 0,
            'dislikes': 0,
        }
        posts.insert_one(post)
