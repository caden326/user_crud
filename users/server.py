from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
from user import User




@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

# ------------------------------create user------------------------------------


@app.route("/newuser")
def page():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["em"]
    }
    User.save(data)
    return redirect('/')


# --------------------------show user----------------------------------

@app.route('/showuser/<int:id>')
def showuser(id):
    data = {
        "id": id
    }
    users = User.get_one(data)
    return render_template('show_one.html', users_one = users)



# ----------------------------edit user---------------------------------

@app.route('/edit/<int:id>')
def edituser(id):
    data = {
        "id": id
    }
    users = User.get_one(data)
    return render_template('edit_user.html', users_one = users)

@app.route('/update_user/<int:id>', methods=["POST"])
def updateuser(id):
    data = {
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["em"],
        "id" : id
    }
    User.updateuser(data)

    return redirect ('/')



# ----------------------------------delete user---------------------------------------------

@app.route("/delete/<int:id>")
def deleteuser(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect ("/")




if __name__=="__main__":   
        app.run(debug=True)    
