from flask import Flask, render_template, url_for, redirect, flash, request
import time

import sys
sys.path.append('/Users/kramer/Documents/DAT18b/4_semester/python/exam/GitFlask/model')

from username_form import UsernameForm
from user import User
from github import Github
from repository import Repository
from result_table import ResultTable
from directory_table import DirectoryTable
from directory import Directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c390c9de932d68e83f5d7a81d85cb5ed' # prevents cross site forgery

user = User()
github = Github()
repository = Repository()
directory = Directory()


# decorator which takes in the route from the url
@app.route('/')
def home_page():
    form = UsernameForm()

    return render_template('home.html', form=form) 


@app.route('/user')
def result_page():
    form = UsernameForm()
    
    # sets the username of the user
    user.name = request.args.get('username')
    
    # sets the account name to the name of the user
    github.account_username = user.name
    
    github.fetch_repo_info()
    table = ResultTable(github.repo_info)
    
    return render_template('result.html', form=form, repo_info=github.repo_info, table=table)


@app.route('/repository/<int:id>', methods=['GET', 'POST'])
def repository_page(id):
    form = UsernameForm()
    print(user.name)
    
    # sets the repository to be the one we want to clone
    global repository
    repository = github.find_repo_with_gen(id)
    
    table = DirectoryTable(directory.content)
    
    return render_template('something.html', form=form, repo=repository, table=table)


# NEW ROUTE FOR BACK BUTTON AND DIR LINK IN DIRECTORY TABLE'
@app.route('/repository/<string:command>')
def repository_command_route(command):
    global directory

    if command == 'one_up':
        directory = directory.go_one_dir_up()
    elif command == 'clone_here':
        pass
    else:
        directory += command
    
    return redirect(url_for('repository_page', id=repository.id))



@app.route('/repository/clone')
def repository_clone_page():
    form = UsernameForm()

    # the form which contains the up button
    back_form = BackForm()
    
    # the form which contains the clone button
    clone_form = CloneForm()
    
    # 
    if clone_form.validate_on_submit():
        flash(f'Cloned repository to here', 'success')
    else:
        # TODO implement
        #flash(f'Some failure', 'danger')
        pass

    table = DirectoryTable(directory.content)


    return render_template('something.html', form=form, repo=repository, table=table, clone_form=clone_form, back_form=back_form)


@app.route('/back', methods=['POST'])
def back():
    back_form = BackForm()
    if back_form.validate_on_submit():
        #brug data fra form
        pass
    print('test')
    print(directory.current_dir)
    directory.go_one_dir_up()

    return redirect(url_for('repository_clone_page'))

@app.route('/repository/clone/<name>')
def dir_selected(name):
    global directory
    directory += name
    print('test')
    print(directory.current_dir)
    return redirect(url_for('repository_clone_page'))

def clone_here():
    pass


@app.route('/test', methods=['GET', 'POST'])
def testroute():
    return render_template('test.html')


# makes it runnable from python by typing 'python git_flask_app.py' in terminal
if __name__ == '__main__':
    app.run(debug=True)