from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    return 'hi 안녕'

@app.route('/pptaa')
def pptaa():
    return 'pptaa'

@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세용</h1>'

@app.route('/html_file')
def html_file():
    return render_template('index.html')

@app.route('/variable')
def variable():
    name = "이정철"
    return render_template('variable.html', html_name = name)
    
@app.route('/greeting/<string:name>/') ##동적라우팅하는 부분
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/cube/<int:num>/')
def cube(num):
    cube_num=num**3
    return render_template('cube.html', num = num, cube_num=cube_num)

if __name__=='__main__':
    app.run(debug=True)