from flask import Flask, request,render_template
import quoteScraper as qs


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/create')
def create():
    name=request.args.get('name','')
    poem=qs.scrape(name)
    return render_template('home.html',poem=poem)

if __name__ =='__main__':
    app.run(debug=True)
