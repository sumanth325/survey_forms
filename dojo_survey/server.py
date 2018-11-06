from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['username']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template('result.html', name=name, location=location, language=language, comments=comments)

@app.route('/danger')
def danger():
    print('a user tried to visit /danger.  we have redirected the user to /')
    return redirect('/')

if __name__=="__main__":
    
    app.run(debug=True) 