import math
import random
import time
from flask import Flask, render_template, request, make_response
import sqlite3

connection = sqlite3.connect('records.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS records
                (id integer primary key autoincrement, name TEXT, steps integer, time float)''')


def start():
    global mas, pysto, time1
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
    n1 = random.choice(a)
    a.pop(a.index(n1))
    n2 = random.choice(a)
    a.pop(a.index(n2))
    n3 = random.choice(a)
    a.pop(a.index(n3))
    n4 = random.choice(a)
    a.pop(a.index(n4))
    n5 = random.choice(a)
    a.pop(a.index(n5))
    n6 = random.choice(a)
    a.pop(a.index(n6))
    n7 = random.choice(a)
    a.pop(a.index(n7))
    n8 = random.choice(a)
    a.pop(a.index(n8))
    n9 = random.choice(a)
    a.pop(a.index(n9))
    n10 = random.choice(a)
    a.pop(a.index(n10))
    n11 = random.choice(a)
    a.pop(a.index(n11))
    n12 = random.choice(a)
    a.pop(a.index(n12))
    n13 = random.choice(a)
    a.pop(a.index(n13))
    n14 = random.choice(a)
    a.pop(a.index(n14))
    n15 = random.choice(a)
    a.pop(a.index(n15))
    n16 = random.choice(a)
    a.pop(a.index(n16))
    mas = [[n1, n2, n3, n4], [n5, n6, n7, n8], [n9, n10, n11, n12], [n13, n14, n15, n16]]
    pysto = []
    crow = 0
    for i in mas:
        ccolumn = 0
        crow += 1
        for j in i:
            ccolumn += 1
            if j == '':
                pysto = [crow, ccolumn]
                pystorow = pysto[0]
                pystocolumn = pysto[1]
    time1 = time.time()
    return [mas, pysto, time1]


username = ''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '']
n1 = random.choice(a)
a.pop(a.index(n1))
n2 = random.choice(a)
a.pop(a.index(n2))
n3 = random.choice(a)
a.pop(a.index(n3))
n4 = random.choice(a)
a.pop(a.index(n4))
n5 = random.choice(a)
a.pop(a.index(n5))
n6 = random.choice(a)
a.pop(a.index(n6))
n7 = random.choice(a)
a.pop(a.index(n7))
n8 = random.choice(a)
a.pop(a.index(n8))
n9 = random.choice(a)
a.pop(a.index(n9))
n10 = random.choice(a)
a.pop(a.index(n10))
n11 = random.choice(a)
a.pop(a.index(n11))
n12 = random.choice(a)
a.pop(a.index(n12))
n13 = random.choice(a)
a.pop(a.index(n13))
n14 = random.choice(a)
a.pop(a.index(n14))
n15 = random.choice(a)
a.pop(a.index(n15))
n16 = random.choice(a)
a.pop(a.index(n16))
mas = [[n1, n2, n3, n4], [n5, n6, n7, n8], [n9, n10, n11, n12], [n13, n14, n15, n16]]
mas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], ['', 13, 14, 15]]
pysto = 0
crow = 0
ccolumn = 0
for i in mas:
    ccolumn = 0
    crow += 1
    for j in i:
        ccolumn += 1
        if j == '':
            pysto = [crow, ccolumn]
            pystorow = pysto[0]
            pystocolumn = pysto[1]
time1 = time.time()

start_motion = -1
win_or_not = False
guest = 5


def step(mas, pystorow, pystocolumn, row, column):
    global win_or_not
    if row > 0 and column > 0:
        if row == pystorow and math.fabs(pystocolumn - column) == 1:
            mas[pystorow - 1][pystocolumn - 1] = mas[row - 1][column - 1]
            mas[row - 1][column - 1] = ''
            pystorow = row
            pystocolumn = column
        elif column == pystocolumn and math.fabs(pystorow - row) == 1:
            mas[pystorow - 1][pystocolumn - 1] = mas[row - 1][column - 1]
            mas[row - 1][column - 1] = ''
            pystorow = row
            pystocolumn = column
    win_mas = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, '']]
    if mas == win_mas:
        win_or_not = True
    return [mas, pystorow, pystocolumn]


timedelta = 0

app = Flask(__name__)


@app.route('/tag_game', methods=['GET', 'POST'])
def main():
    global mas, start_motion, pysto, time1, pystocolumn, pystorow, win_or_not, guest, timedelta, username
    press_start = request.args.get('start', type=int)
    press_exit = request.args.get('delete', type=int)
    username = request.cookies.get('nickname')
    if username is None:
        username = ''
    # if request.method == 'POST':
    #     nickname = request.form['nicknamee']
    # print(nickname)
    if press_start == 1:
        win_or_not = False
        start_motion = -1
        a = start()
        mas = a[0]
        pysto = a[1]
        time1 = a[2]
        pystorow = pysto[0]
        pystocolumn = pysto[1]
    # print(mas)
    # print(pysto)
    row = request.args.get('row', type=int)
    column = request.args.get('column', type=int)
    motion = request.args.get('motion', type=int)
    if row is None and column is None:
        row = -1
        column = -1
    # print(row, column)
    start_motion += 1
    time2 = time.time()
    timedelta = time2 - time1
    timedelta = round(timedelta, 3)
    stepp = step(mas, pystorow, pystocolumn, row, column)
    mas = stepp[0]
    pystorow = stepp[1]
    pystocolumn = stepp[2]
    # print(pystorow, pystocolumn)
    # print(mas)
    # print(row, column)
    # print(result)
    res = ['', ['', '', '', '']]
    if win_or_not:
        guest += 1
        count = 0
        connection.commit()
        result_guest = cursor.execute("SELECT * FROM records ORDER BY time").fetchall()
        connection.commit()
        for i in result_guest:
            count += 1
            if i[1] == f'Noname{guest}':
                res = []
                res.append(count)
                res.append(i)
        result = cursor.execute("SELECT * FROM records ORDER BY time").fetchall()
        connection.commit()
        return render_template('my_template_win.html', mas=mas, motion=start_motion, timedelta=timedelta,
                               result=result, res=res, nickname=username)
    else:
        result = cursor.execute("SELECT * FROM records ORDER BY time").fetchall()
        connection.commit()
        if press_exit == 1:
            username = ''
        resp = make_response(
            render_template('my_template.html', mas=mas, motion=start_motion, timedelta=timedelta, result=result,
                            res=res, nickname=username))
        if press_exit == 1:
            resp.set_cookie('nickname', 'nickname', max_age=0)

        return resp
        # return render_template('my_template.html', mas=mas, motion=start_motion, timedelta=timedelta,
        #                        result=result, res=res, nickname=username)


@app.route('/records', methods=['GET', 'POST'])
def records():
    global timedelta, start_motion, username
    username = request.cookies.get('nickname')
    if username is None:
        username = ''
    stroki = ''
    counter = 0
    result = cursor.execute("SELECT * FROM records ORDER BY time").fetchall()
    for i in range(len(result)):
        counter += 1
        stroki += f"<tr><td>{counter}</td><td>{result[i][1]}</td> <td>{result[i][2]}</td> <td>{result[i][3]}</td></tr> <br>"
    if request.method == 'POST':
        nickname = request.form['nicknamee']
        print(nickname)
        cursor.execute("INSERT INTO records (name, steps, time) VALUES (?, ?, ?)",
                       (nickname, start_motion, timedelta))
        connection.commit()
        resp = make_response(render_template('records.html', nickname=username, stroki=stroki))
        resp.set_cookie('nickname', nickname)
        return resp
    else:
        return render_template('records.html', nickname=username, stroki=stroki)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
