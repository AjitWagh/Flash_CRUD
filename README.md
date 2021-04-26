# Flash_CRUD
Flask Dashboard



https://teams.microsoft.com/l/meetup-join/19%3ameeting_NjJhNWFlYWMtYmJlZS00YjkyLThkOTMtYTFjZTcwYmUzZGYx%40thread.v2/0?context=%7b%22Tid%22%3a%22ac0208f1-f65d-4e1e-be1d-e62cf55ca6ff%22%2c%22Oid%22%3a%22769b4a6b-bcc9-429e-82b2-d3938046b216%22%7d





<!-- Script -->


<script>
$(document).ready(function(){
    $.datepicker.setDefaults({
        dateFormat: 'yy-mm-dd'
    });
    $(function(){
        $("#From").datepicker();
        $("#to").datepicker();
    });
    $('#range').click(function(){
        var From = $('#From').val();
        var to = $('#to').val();
        if(From != '' && to != '')
        {
            $.ajax({
                url:"/range",
                method:"POST",
                data:{From:From, to:to},
                success:function(data)
                {
                    $('#purchase_order').html(data);
                    $('#purchase_order').append(data.htmlresponse);
                }
            });
        }
        else
        {
            alert("Please Select the Date");
        }
    });
});
</script>







---- app.py-------

@app.route("/range",methods=["POST","GET"])
def range(): 
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
    if request.method == 'POST':
        From = request.form['From']
        to = request.form['to']
        print(From)
        print(to)
        query = "SELECT * from orders WHERE purchased_date BETWEEN '{}' AND '{}'".format(From,to)
        cur.execute(query)
        ordersrange = cur.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', ordersrange=ordersrange)})
 




-----All Code-----
app.py
 
#app.py
from flask import Flask, render_template, request, jsonify, flash, redirect
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb

app = Flask(__name__)
        
app.secret_key = "caircocoders-ednalan"
        
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'testingdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM orders ORDER BY id desc")
    orders = cur.fetchall() 
    return render_template('index.html', orders=orders)
 
@app.route("/range",methods=["POST","GET"])
def range(): 
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
    if request.method == 'POST':
        From = request.form['From']
        to = request.form['to']
        print(From)
        print(to)
        query = "SELECT * from orders WHERE purchased_date BETWEEN '{}' AND '{}'".format(From,to)
        cur.execute(query)
        ordersrange = cur.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', ordersrange=ordersrange)})

if __name__ == "__main__":
    app.run(debug=True)
templates/index.html
//templates/index.html
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Python Flask Date Range Search with jQuery Ajax DatePicker MySQL Database</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"/>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.css"/>
</head>
<body>
<br/>
<div class="container">
<h2 align="center">Python Flask Date Range Search with jQuery Ajax DatePicker MySQL Database</h2>
<br/>
<br/>
<div class="col-md-2">
<input type="text" name="From" id="From" class="form-control" placeholder="From Date"/>
</div>
<div class="col-md-2">
<input type="text" name="to" id="to" class="form-control" placeholder="To Date"/>
</div>
<div class="col-md-8">
<input type="button" name="range" id="range" value="Range" class="btn btn-success"/>
</div>
<div class="clearfix"></div>
<br/>
<div id="purchase_order">
<table class="table table-bordered">
<tr>
<th width="5%">ID</th>
<th width="35%">Customer Name</th>
<th width="40%">Purchased Item</th>
<th width="10%">Purchased Date</th>
<th width="5%">Price</th>
</tr>
{% for row in orders %}
    <tr>
    <td>{{row.id}}</td>
    <td>{{row.customer_name}}</td>
    <td>{{row.purchased_items}}</td>
    <td>{{row.purchased_date}}</td>
    <td>{{row.price}}</td>
    </tr>
    {% endfor %}
</table>
</div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.js"></script>
<!-- Script -->
<script>
$(document).ready(function(){
    $.datepicker.setDefaults({
        dateFormat: 'yy-mm-dd'
    });
    $(function(){
        $("#From").datepicker();
        $("#to").datepicker();
    });
    $('#range').click(function(){
        var From = $('#From').val();
        var to = $('#to').val();
        if(From != '' && to != '')
        {
            $.ajax({
                url:"/range",
                method:"POST",
                data:{From:From, to:to},
                success:function(data)
                {
                    $('#purchase_order').html(data);
                    $('#purchase_order').append(data.htmlresponse);
                }
            });
        }
        else
        {
            alert("Please Select the Date");
        }
    });
});
</script>
</body>
</html>
templates/response.html
//templates/response.html
<table class="table table-bordered">
      <tr>
      <th width="5%">ID</th>
      <th width="35%">Customer Name</th>
      <th width="40%">Purchased Item</th>
      <th width="10%">Purchased Date</th>
      <th width="5%">Price</th>
      </tr>
      {% for row in ordersrange %}
          <tr>
          <td>{{row.id}}</td>
          <td>{{row.customer_name}}</td>
          <td>{{row.purchased_items}}</td>
          <td>{{row.purchased_date}}</td>
          <td>{{row.price}}</td>
          </tr>
      {% endfor %}
</table>



https://teams.microsoft.com/meetingOptions/?organizerId=4ccfad99-9a3e-4491-b130-56001515ba31&tenantId=5047bca2-da88-442e-a09a-d9b8af692adc&threadId=19_meeting_MzkwMGRhM2QtZmNlOC00NmZjLTlkYjMtYzQ4OGZlZGM3NmNh@thread.v2&messageId=0&language=en-US
