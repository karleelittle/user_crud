from flask import Flask, render_template, request, redirect

from users import User  #this wont connect even if my life depended on it

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("read.html", users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }

    return render_template("edit_user.html", user=User.getOne(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        "id": id
    }
    User.destroy(data)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }

    return render_template("show_user.html", user=User.getOne(data))


# if __name__ == "__main__":
#     app.run(debug=True)