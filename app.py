from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", my_name=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")


@app.route('/password-generator')
def password_generator():
    from pliki_python.password_generator import generate_password
    password = generate_password()
    return render_template("password-generator.html", new_password=password)

@app.route('/iframe')
def iframe():
    return render_template("iframe.html")



if __name__=="__main__":
    app.run()
