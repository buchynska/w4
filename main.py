from flask import Flask, request, render_template

from dao.helper import UserHelper
from forms.student import userForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def user():
    form = userForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            print(form.user_age.errors)
            print(form.user_name.errors)
            return render_template('student.html', form=form)
        else
            user_id , status = helper.newUser(

                                            form.user_name.data,
                                            form.user_age.data

                                       )

            return "Status {} ID {}".format(status,user_id)


    return render_template('student.html', form=form, action='')


if __name__ == '__main__':
    app.run(debug=True)
