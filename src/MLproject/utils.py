
from src.MLproject.logger import logging
from src.MLproject.exception   import CustomException
import pickle
import pymysql
import numpy as np
import sys
import pandas as pd

# host='localhost'
# user='root'
# password='iloveyou@123@'
# db='mydb'
def read_sql_data():
    logging.info("reading SQL database started")
    try:
        mydb=pymysql.connect(
                    host='localhost',
                    user='root',
                    password='**',
                    db='mydb'

        )
        logging.info("Connection established",mydb)
        df=pd.read_sql_query('SELECT * FROM data',mydb)
        
        return df
    except Exception as ex:
        raise CustomException(ex,sys)
#     def save_object(file_path,obj):
#         try:
#             dir_path - os.path.dirname(file_path)
#             os.makedirs(dir_path,exist_ok=True)
#             with open(file_path,"wb")as file_obj:
#                 pickle.dump(obj,file_obj)

        



# # app=Flask(__name__)



# # mysql=MySQL(app)
# # app.config["MYSQL_HOST"]="localhost"

# # app.config["MYSQL_USER"]="root"

# # app.config["MYSQL_PASSWORD"]="write your password"

# # app.config["MYSQL_DB"]="mydb"

# # @app.route("/",methods=['GET',"POST"])
# # def index():
# #      if request.method=="POST":
#          username=request.form['username']
#          email=request.form['email']
#          cur =mysql.connection.cursor()
#          cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(username,email))
#          mysql.connection.commit()
#          cur.close()
#          return " <h1>succesfully updated in database</h1>"
    
#      return render_template("index.html")
# @app.route("/users")
# def getusers():
#     cur =mysql.connection.cursor()
#     user= cur.execute("SELECT * FROM users")
#     if user >0:
#         userDetails=cur.fetchall()
#     return render_template("users.html",users=userDetails)

# if __name__=="__main__":
#     app.run(debug=True)
         
# # @app.route("/")
# # def home():
# #     return render_template("home.html")


# # @app.route("/about")
# # def about():
# #     return render_template("about.html")

# # @app.route("/contact")
# # def contact():
# #     return render_template("contact.html")
# # @app.route("/form",methods=['get','post'])
# # def form():
# #     if request.method=='GET':
# #              return render_template("home.html")
# #     else:
# #         math=float(request.form['maths'])
# #         eng=float(request.form['eng']) 
# #         science=float(request.form['science']) 
# #         avg=(math+science+eng)/3    
# #         return render_template("home.html",score=avg) 
     
