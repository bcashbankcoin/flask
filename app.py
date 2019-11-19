
from blog import app 



post = [
    {
        'blog_id': '1',
        'title': 'Blog Post 1',
        'body': 'First post content',
        'author': 'Ansarul'
    },
    {
        'blog_id': '5',
        'title': 'Blog Post 5',
        'body': 'First post content',
        'author': 'Ansarul Mulla2'
    }
]




if __name__ == '__main__':
    app.run(debug=True)