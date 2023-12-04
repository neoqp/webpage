from flask import *
import pymysql
import matplotlib.pyplot as plt

app = Flask(__name__)
db = pymysql.connect(host='127.0.0.1', user='root', password='eodus6450', db='test', charset='utf8')
'''
cursor = db.cursor()
sql = "insert into trash (type, amount) values (\"steel\", 1)"
cursor.execute(sql)
db.commit()
'''

@app.route('/', methods = ['GET'])
def main():
    return render_template("home.html")

@app.route('/control', methods = ['GET'])
def control():
    return render_template("control.html")


@app.route('/control/opcontrol', methods = ['GET'])
def opcontrol():
    return render_template("op-control.html")

@app.route('/control/opcontrol/<tp>', methods = ['GET'])
def opcontrol2(tp):
    return render_template(tp + ".html")


@app.route('/control/checkdata', methods = ['GET'])
def checkdata():
    return render_template("check-data.html")

@app.route('/control/checkdata/<tp>', methods = ['GET'])
def checkdata2(tp): # tp : stack or graph

    cursor = db.cursor()
    sql = "select * from trash"
    cursor.execute(sql)
    rows = cursor.fetchall()
    data = []
    idx = 0
    for row in rows:
        data.append([idx//5, row[1], row[2], row[3], row[4]]) # id type amount(g) amount(%) date
        idx+=1
    db.commit()

    if tp=='stack':
        return render_template(tp + ".html", data=data)

    elif tp=='graph':
        g_dict = {}
        percent_dict = {}

        for row in data:
            if row[1] in g_dict.keys():
                g_dict[row[1]].append(int(row[2]))
            else:
                g_dict[row[1]] = [int(row[2])]

        x = [int(i) for i in range(len(g_dict['plastic']))]
        plt.figure(figsize=(14, 5))
        plt.subplot(1,2,1)
        for name in g_dict.keys():
            plt.plot(x, g_dict[name], label = name)
    
        plt.title('amount(g)')
        plt.legend()
        plt.show()

        for row in data:
            if row[1] in percent_dict.keys():
                percent_dict[row[1]].append(int(row[3]))
            else:
                percent_dict[row[1]] = [int(row[3])]

        x = [int(i) for i in range(len(percent_dict['plastic']))]
        plt.subplot(1,2,2)
        for name in percent_dict.keys():
            plt.plot(x, percent_dict[name], label = name)
    
        plt.title('amount(%)')
        plt.legend()
        plt.savefig('static/result1.png')
        plt.show()

        return render_template(tp + ".html")
        
if __name__=='__main__':
    app.run()