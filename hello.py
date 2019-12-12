from flask import Flask, escape, request, render_template
import random

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

@app.route('/lunch')
def lunch():
    name = "이정철"
    menu = ['함박스테이크', '부대찌개', '편의점', '짜장면']
    image = ['http://recipe1.ezmember.co.kr/cache/recipe/2018/05/09/10948a1953ce6ab70aa545eb38780ac81.jpg',
           'http://static.hubzum.zumst.com/hubzum/2017/11/27/10/093162fe81a040c0874fcb2a4dccc299.jpg',
           'https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/guest/image/eUCAh1FhS9DLB6yA-c1yuCuXz4o',
           'https://previews.123rf.com/images/nontoxicguy/nontoxicguy1611/nontoxicguy161100439/66442742-%EC%9E%90%EC%9E%A5%EB%A9%B4-%EC%A7%9C%EC%9E%A5%EB%A9%B4-%EA%B2%80%EC%9D%80-%EC%BD%A9-%EC%86%8C%EC%8A%A4-%EA%B5%AD%EC%88%98.jpg']
    i = random.randint(0,3)
    return render_template('lunch.html', choice_menu=menu[i], choice_image=image[i], name=name,)

@app.route('/lunch1')
def lunch1():
    menus = {
        "짜장면":'http://recipe1.ezmember.co.kr/cache/recipe/2018/05/09/10948a1953ce6ab70aa545eb38780ac81.jpg',
        "짬뽕":'http://recipe1.ezmember.co.kr/cache/recipe/2017/06/19/2756808e5603db7a18c4f5ee9a699ee41.jpg',
        '김밥':'http://recipe1.ezmember.co.kr/cache/recipe/2016/04/08/1d26c0444e724bca8ed271b24da0057a1.jpg'
    }
    menu_list = list(menus.keys())
    pick = random.choice(menu_list)
    img = menus[pick]
    return render_template('lunch1.html', pick=pick, img=img)

@app.route('/movies')
def movies():
    movies = ['겨울왕국2','쥬만지', '포드v페라리']
    return render_template('movies.html', movies=movies)


if __name__=='__main__':
    app.run(debug=True)