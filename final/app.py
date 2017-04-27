from flask import Flask, request,render_template
import quoteScraper as qs
import textGenerator as tg

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/create')
def create():
    # if request.form['submit'] == 'Answer Me':
    #     name=request.args.get('name','')
    #     question,answer=tg.getQA(name)
    # elif request.form['submit'] == 'One More Time':
    #         pass # do something else
    nameQ=request.args.get('nameQ','')
    nameA=request.args.get('nameA','')
    questions,a=tg.getQA(nameQ)
    q,answers=tg.getQA(nameA)
    QandA=''
    for i in range(10):
        question=questions[i]+"<br/>"
        answer=answers[i]+"<br/>"

        QandA=QandA+question+answer

    return render_template('home.html',QandA=QandA)

if __name__ =='__main__':
    app.run(debug=True)
