from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def info():
    return render_template('webhome.html')


@app.route('/contactus')
def contact():
    return render_template('webcontact.html')

@app.route('/products')
def products():
    return render_template('webproducts.html')

@app.route('/clients')
def clients():
    return render_template('webclients.html')

if __name__=='__main__':
    app.run()

