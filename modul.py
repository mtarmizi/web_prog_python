import mysql.connector
from functools import wraps
from flask import session,flash,redirect,url_for

sql=mysql.connector.connect(host="localhost",
                            user="root",
                            password="",
                            database="project1")

query = sql.cursor()


def countartist():
    query.execute("SELECT CEILING((COUNT(*)/5)) FROM artist")
    result=query.fetchone()
    return(results)

def result():
    rows=list_artist()
    list_gallery() 
    for row in rows:
        print(row)

def list_artwork1():
    query.execute("select * from v_art")
    result=query.fetchall()
    return(result)
    
def list_artist():
    query.execute("select * from artist")
    result=query.fetchall()
    return(result)
    
def list_gallery():
    query.execute("select * from gallery")
    result=query.fetchall()
    return(result)

def list_artwork():
    query.execute("select * from artwork")
    result=query.fetchall()
    return(result)

def find_artist(artist_id):
    qry="select * from artist where artist_id=%s"
    query.execute(qry,(artist_id,))
    result=query.fetchone()
    return(result)


def find_gallery(gallery_id):
    qry="select * from gallery where gallery_id=%s"
    query.execute(qry,(gallery_id,))
    result=query.fetchone()
    return(result)

def find_artwork(artwork_id):
    qry="select * from artwork where artwork_id=%s"
    query.execute(qry,(artwork_id,))
    result=query.fetchone()
    return(result)

def find_artwork1(artist_id):
    qry="select * from artwork where artist_id=%s"
    query.execute(qry,(artist_id,))
    result=query.fetchall()
    return(result)
    
def find_staff(username):
    qry="select * from admin where username=%s"
    query.execute(qry,(username,))
    result=query.fetchone()
    return(result)

def insert_artist(artist_id,artist_name,artist_style,birthplace,dob,age):
    qry="insert into artist (artist_id,artist_name,artist_style,birthplace,dob,age) values (%s,%s,%s,%s,%s,%s)" 
    query.execute(qry,(artist_id,artist_name,artist_style,birthplace,dob,age))
    sql.commit()
    
def insert_gallery(gallery_id,gallery_name,address,contact):
    qry="insert into gallery (gallery_id,gallery_name,address,contact) values (%s,%s,%s,%s)"
    query.execute(qry,(gallery_id,gallery_name,address,contact))
    sql.commit()
    
def insert_artwork(artwork_id,title,artwork_type,year,artist_id,gallery_id,picture_name):
    qry="insert into artwork (artwork_id,title,artwork_type,year,artist_id,gallery_id,picture_name) values (%s,%s,%s,%s,%s,%s,%s)"
    query.execute(qry,(artwork_id,title,artwork_type,year,artist_id,gallery_id,picture_name))
    sql.commit()
    
def insert_staff(username,password):
    qry="insert into admin (username,password) values (%s,%s)"
    query.execute(qry,(username,password))
    sql.commit()
    
def update_artist(artist_name,artist_style,birthplace,dob,age,artist_id):
    qry="update artist set artist_name=%s,artist_style=%s,birthplace=%s,dob=%s,age=%s where artist_id=%s"
    query.execute(qry,(artist_name,artist_style,birthplace,dob,age,artist_id))
    sql.commit()
    
def update_gallery(gallery_name,address,contact,gallery_id):
    qry="update gallery set gallery_name=%s,address=%s,contact=%s where gallery_id=%s"
    query.execute(qry,(gallery_name,address,contact,gallery_id))
    sql.commit()
    
def update_artwork(title,artwork_type,year,artist_id,gallery_id,picture,artwork_id):
    qry="update artwork set title=%s,artwork_type=%s,year=%s,artist_id=%s,gallery_id=%s,picture_name=%s where artwork_id=%s" 
    query.execute(qry,(title,artwork_type,year,artist_id,gallery_id,picture,artwork_id))
    sql.commit()
    
def update_staff(password,username):
    qry="update admin set password=%s where username=%s"
    query.execute(qry,(password,username))
    sql.commit()

def delete_artist(artist_id):
    qry="delete from artist where artist_id=%s" 
    query.execute(qry,(artist_id,))
    sql.commit()
    
def delete_gallery(gallery_id):
    qry="delete from gallery where gallery_id=%s"
    query.execute(qry,(gallery_id,))
    sql.commit()
    
def delete_artwork(artwork_id):
    qry="delete from artwork where artwork_id=%s" 
    query.execute(qry,(artwork_id,))
    sql.commit()

    
def check_artist_id(artist_id):
    qry = "select artist_id from artist where artist_id=%s"
    query.execute(qry,(artist_id,))
    result=query.fetchone()
    return(result)

def check_gallery_id(gallery_id):
    qry = "select gallery_id from gallery where gallery_id=%s"
    query.execute(qry,(gallery_id,))
    result=query.fetchone()
    return(result)
    
def check_artwork_id(artwork_id):
    qry = "select artwork_id from artwork where artwork_id=%s"
    query.execute(qry,(artwork_id,))
    result=query.fetchone()
    return(result)

def check_admin(username):
    qry = "select username from admin where username=%s"
    query.execute(qry,(username,))
    result=query.fetchone()
    return(result)

def checklogin(username,password):
    qry = "select username,password from admin where username=%s and password=%s"
    query.execute(qry,(username,password))
    result=query.fetchone()
    return(result)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('admin'))
        return wrap