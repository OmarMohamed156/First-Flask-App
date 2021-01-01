from flask import Flask,render_template,request #render_template is used to make the python functions display an html file
import mysql.connector #connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="mypython_db"
)
mycursor = mydb.cursor()

app = Flask(__name__)#created an instant for the app with main function called (__name__)

@app.route('/') # what will be written to execute this function, functions are attached to the url
def index():
   return render_template("index.html")

@app.route('/addDoctor', methods=['GET','POST']) #SO THat it knows that iam sending data to my server
def addDoctor():
   if request.method == "POST":
      name = request.form["name"]
      dep = request.form["department"]
      id = request.form["ID"]
      
      sql="INSERT INTO doctors (name,department,id) VALUES (%s,%s,%s)"
      val = (name,dep,id)
      mycursor.execute(sql,val)
      mydb.commit()

      return render_template("index.html")
   else:
      return render_template("addDoctor.html")

@app.route('/viewDoctor')
def viewDoctor():
   mycursor.execute("SELECT * FROM doctors")
   myresult = mycursor.fetchall()
   return render_template("viewDoctor.html",doctors=myresult)

if __name__ == '__main__':
   app.run() #runs server on local host 

