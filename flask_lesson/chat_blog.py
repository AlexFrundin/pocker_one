from flask import Flask, render_template, request, redirect, g, session
import pymongo

app=Flask(__name__)
@app.before_request
def before():
    g.m=pymongo.MongoClient()

@app.after_request
def after(r):
    g.m.close()
    return r


@app.route('/')
def index():
    return render_template(
    'index.html',
    messages=g.m.blog.message.find(),
    #message=request.args.get('message', '')
    message=session.pop('message','')
    )
    #m=pymongo.MongoClient()
    #m.close()
    #return render_template('index.html',name='Anonymus', messages=g.m.blog.message.find())

@app.route('/add', methods=('GET', 'POST'))
def add():
    author=''
    message=''
    if request.method== 'POST':
        author=request.form.get('author','')
        message=request.form.get('message', '')
        if author and message:
            #m=pymongo.MongoClient()
            g.m.blog.message.insert({'author':author, 'message':message})
            session['message']='ok'
            #m.close()
            return redirect ('/')
    return render_template('add.html', message=message, author=author)

app.secret_key='safhaklrioudghjsnvda'

if __name__=='__main__':
    app.run(debug=True)
