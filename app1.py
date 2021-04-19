from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'rgctisvccapu01'
app.config['MYSQL_PASSWORD'] = 'global.ip.user.analytics.008'
app.config['MYSQL_DB'] = 'cd20analytics'

mysql = MySQL(app)




@app.route('/')
def Index():
    #all_data = db.all()
    #all_data = Data.query.all()

    return render_template("tracker.html")


@app.route('/tasks')
def tasks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM cd20analytics")
    data = cur.fetchall()
    cur.close()




    return render_template('tasks.html', tasks=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        Date = request.form['Date']
        Month = request.form['Month']
        JIRA_URL = request.form['JIRA_URL']
        Task = request.form['Task']
        Deliverable = request.form['Deliverable']
        Dashboard_URL = request.form['Dashboard_URL']
        BusinessValue = request.form['BusinessValue']
        Stakeholders = request.form['Stakeholders']
        Designation = request.form['Designation']
        
        
        
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cd20analytics (id, Date, Month, JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)", (id, Date, Month, JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation))
        mysql.connection.commit()
        return redirect(url_for('tasks'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('tasks'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id = request.form['id']
        Date = request.form['Date']
        Month = request.form['Month']
        JIRA_URL = request.form['JIRA_URL']
        Task = request.form['Task']
        Deliverable = request.form['Deliverable']
        Dashboard_URL = request.form['Dashboard_URL']
        BusinessValue = request.form['BusinessValue']
        Stakeholders = request.form['Stakeholders']
        Designation = request.form['Designation']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE cd20analytics
               SET Date=%s, Month=%s, JIRA_URL=%s, Task=%s, Deliverable=%s, Dashboard_URL=%s, BusinessValue=%s, Stakeholders=%s, Designation=%s,
               WHERE id=%s
            """, (Date, Month, JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation, id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('tasks'))









if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='localhost', port='5002', debug=True)
