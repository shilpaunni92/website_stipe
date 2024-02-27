from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('main.html')

# Admin page route
@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
