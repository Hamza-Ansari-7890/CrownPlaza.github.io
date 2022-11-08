from datetime import datetime
from model import *

@app.route("/",methods=['GET','POST'])
def display():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    try:
        if "uname" in session:
            flash("You have already logged in!","error")
            return redirect('/home')
        else:
            if request.method == 'POST':
                email = request.form['uname']
                password = request.form['pass']
                log = Users.query.filter_by(Email=email).first()
                if email == 'admin1234@gmail.com' and password == 'admin':
                    session["uname"] = "Hamza"
                    flash("Welcome Admin","success")
                    return redirect('/admin')
                elif email == log.Email and password == log.Password:
                    session["uname"] = log.UserName
                    flash("Welcome","success")
                    return redirect('/home')
                else:
                    flash('Email or Password dosent match', 'wrong')
                    return redirect("/login")
            return render_template("login.html")
    except:
        flash('Email or Password dosent match','wrong')
        return redirect("/login")

@app.route("/register",methods=['GET','POST'])
def register():
    try:
        if request.method=='POST':
            username = request.form.get('username')
            email=request.form.get('email')
            Npassword=request.form.get('Npass')
            Cpassword = request.form.get('Cpass')
            if Npassword != Cpassword:
                flash("password dosen't matched",'error')
                return render_template("register.html")
            else:
                flash("Account has been Created!",'success')
                entry3 = Users(UserName =username,Email=email, Password=Cpassword)
                db.session.add(entry3)
                db.session.commit()
                return redirect("/login")
        return render_template("register.html")
    except:
        flash('The Username already exist','error')
        return redirect('/register')

@app.route("/home")
def Home():
    try:
        if "uname" not in session:
            return redirect("/login")
        adminData = Admin.query.all()
        return render_template('home.html',adminData=adminData)
    except:
        flash("sorry something went worg")
        return redirect('/login')


@app.route("/detail/<int:RoomNo>", methods=['GET', 'POST'])
def roomBooking(RoomNo):
    try:
        if "uname" not in session:
            return redirect("/login")
        room = Admin.query.filter_by(RoomNo=RoomNo).first()
        if request.method == 'POST':
           RoomNo = request.form.get('RoomNo')
           room_type = request.form.get('type')
           check_in_date = request.form.get('check_in_date')
           check_out_date = request.form.get('check_out_date')
           no_of_days = request.form.get('days')
           price = request.form.get('price')
           name= request.form.get('name')
           mobile_no= request.form.get('number')
           Id = request.form.get('Id')
           IdNo = request.form.get('IdNo')
           Male = request.form.get('Male')
           Female = request.form.get('Female')
           Child = request.form.get('Child')
           entry1 = Room_booking(Room_NO=RoomNo,Room_type=room_type,Check_in_Date=check_in_date,Check_out_Date=check_out_date,
                                 No_of_days=no_of_days,Price=price,Name=name,Mobile_no=mobile_no,Id_Proof=Id,Id_No=IdNo,
                                 Male=Male,Female=Female,Child=Child)
           db.session.add(entry1)
           db.session.commit()
           flash("Room has been booked","success")
           room.status = 'BOOKED'
           db.session.commit()
           return redirect('/home')
        return render_template('detail.html',date=datetime.now(),room=room)
    except:
        flash("The Room is already booked!","error")
        return render_template("detail.html")


@app.route("/admin",methods=['GET','POST'])
def admin():
    try:
        if request.method == 'POST':
            RoomNo = request.form.get('RoomNo')
            RoomType = request.form.get('RoomType')
            status = request.form.get('status')
            entry2 = Admin(RoomNo = RoomNo,RoomType=RoomType,status=status)
            db.session.add(entry2)
            db.session.commit()
            flash("Room has been added","success")
            return  render_template('admin.html')
        return render_template('admin.html')
    except:
        flash("Sorry! This Room number is already exists","error")
        return redirect("/admin")

  # if "Hamza" in session:
        #     flash("welcome admin","success")
        #     return render_template("admin.html")
@app.route("/booked")
def booked():
    try:
        if "uname" not in session:
            return redirect("/login")
        roomBooking = Room_booking.query.all()
        return render_template('booked.html', roomBooking=roomBooking)
    except:
        flash("something went wrong!","error")
        redirect("/home")

@app.route("/delete/<string:Room_NO>")
def remove(Room_NO):
    try:
        if "uname" not in session:
            return redirect("/login")

        if session["uname"] == "Hamza":
            repair = Admin.query.filter_by(RoomNo=Room_NO).first()
            db.session.delete(repair)
            db.session.commit()
            remove = Room_booking.query.filter_by(Room_NO=Room_NO).first()
            if repair == remove:
                flash("This room Is already occupied by someone","error")
            flash("removed","success")
            # remove = Room_booking.query.filter_by(Room_NO=Room_NO).first()
            db.session.delete(remove)
            db.session.commit()

            return redirect("/home")
        else:
            remove = Room_booking.query.filter_by(Room_NO=Room_NO).first()
            room = Admin.query.filter_by(RoomNo=Room_NO).first()
            room.status = 'AVAILABLE'
            db.session.delete(remove)
            db.session.commit()
            flash("succesfully removed","success")
            return redirect('/booked')
    except:
        flash("Unable to delete the data","error")
        return redirect('/booked')


@app.route("/edit/<int:Room_NO>", methods = ['GET','POST'])
def edit(Room_NO):
    try:
        if "uname" not in session:
            return redirect("/login")
        edit = Room_booking.query.filter_by(Room_NO=Room_NO).first()
        if request.method == 'POST':
            edit.Name = request.form.get('name')
            edit.Mobile_no = request.form.get('number')
            edit.Id_Proof = request.form.get('Id')
            edit.Id_No = request.form.get('IdNo')
            edit.Check_in_Date = request.form.get('check_in_date')
            edit.Check_out_Date = request.form.get('check_out_date')
            edit.Male = request.form.get('Male')
            edit.Female = request.form.get('Female')
            edit.Child = request.form.get('Child')
            db.session.commit()
            flash("successfully updated!","success")
            return redirect('/booked')
        return render_template('Edit.html',edit=edit)
    except:
        flash("unable to edit the data","error")
        return redirect('/booked')



@app.route("/logout",methods=['GET','POST'])
def logout():
    try:
        session.pop('uname',None)
        flash("successfully Logout!","logout")
        return redirect("/login")
    except:
        flash("Something went wrong","error")




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)







