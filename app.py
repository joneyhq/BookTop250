from flask import Flask,render_template
import sqlite3

app = Flask(__name__)    #初始化


@app.route('/')
def index():
    infos = []
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    sql = "select * from booktop limit 0,10"
    data = cur.execute(sql)
    for item in data:
        infos.append(item)


    score = []
    num = []
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    sql = "select 得分,count(得分) from booktop group by 得分"
    data1 = cur.execute(sql)
    for item in data1:
        score.append(item[0])
        num.append(item[1])


    datalist = []
    con = sqlite3.connect("book.db")
    cur = con.cursor()
    sql = "select 得分,评价人数 from booktop group by 得分"
    data2 = cur.execute(sql)
    for item in data2:
        datalist.append([item[0],item[1]])

    cur.close()
    con.close()
    return render_template('index.html', infos=infos,score=score,num=num,datalist=datalist)


if __name__ == '__main__':    #全局名称
    app.run()                 #开始运行
