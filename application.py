from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('message.html', string="test_api")

@app.route('/test_api', methods=['GET'])
def test_api():
    
    return render_template('hello.html', name = "World!")

if __name__ == '__main__':

    app.run(debug=True)

    
