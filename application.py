from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('message.html', string="HOME")

@app.route('/test_api', methods=['GET'])
def test_api():
    
    return render_template('message.html', string="GET")

if __name__ == '__main__':

    app.run(debug=True)

    
