from flask import Flask, render_template, url_for, redirect, flash, request
import time, subprocess

# modules and classes created that needs to be imported
from modules import file_manager

from model.username_form import UsernameForm
from model.result_table import ResultTable
from model.directory_table import DirectoryTable

from model.github_account import GithubAccount
from model.github_handler import GithubHandler
from model.repository import Repository
from model.directory import Directory


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c390c9de932d68e83f5d7a81d85cb5ed' # prevents cross site forgery

github_account = GithubAccount()
github_handler = GithubHandler()

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

    # sets the account name to the name of the user
    github_account.username = request.args.get('username')
    
    github_account.fetch_repositories()
    table = ResultTable(github_account.repositories)

    if len(github_account)>0:
        flash(f'Found {len(github_account)} of {github_account.username}\'s repositories', 'success')
    
    
    return render_template('result.html', form=form, table=table)


@app.route('/repository/<int:id>', methods=['GET', 'POST'])
def repository_page(id):
    form = UsernameForm()

    if directory.has_error_changing_dir:
        flash(f'You are only allowed to change into folders', 'danger')

    if github_handler.has_executed_command:
        flash(f'Succesfully cloned {repository.name} of {github_handler.folder_size} in {github_handler.time_spend} seconds', 'success')
        github_handler.has_executed_command = False
    
    # sets the repository to be the one we want to clone
    repository.id, repository.name, repository.created_at, repository.updated_at, repository.language, repository.clone_url = github_account.find_repo_with_gen(id)
    
    table = DirectoryTable(directory.content)
    
    return render_template('repository.html', form=form, repo=repository, table=table)


# NEW ROUTE FOR BACK BUTTON AND DIR LINK IN DIRECTORY TABLE'
@app.route('/repository/<string:command>')
def repository_command_route(command):

    if command == 'one_up':
        directory.change_dir('..')

    elif command == 'clone_here':
        github_handler.time_spend = github_handler.clone_repo(repository.clone_url)
        github_handler.folder_size = github_handler.find_size_of_folder(repository.name)
        github_handler.has_executed_command = True

    elif not command == '...': # Flask apparently tests the route by using '...',
        # so to avoid errors we check if the command is other than that
        directory.change_dir(command)
        #directory += command
    
    return redirect(url_for('repository_page', id=repository.id))



@app.route('/change_logo')
def change_logo_page():
    form = UsernameForm()


    file_manager.download_github_logos()


    return render_template('change_logo.html', form=form)

@app.route('/change_logo/<filename>')
def change_logo_command_page(filename):
    # TEMPORARY LOCATION
    # FIGURE OUT WHERE TO PUT CONTEXTMANAGER AND LOGODOWNLOADER
    import os
    #os.remove(f'{os.getcwd()}/static/selected_logo.png')
    os.rename(f'{os.getcwd()}/static/{filename}',f'{os.getcwd()}/static/selected_logo.png')

    return redirect(url_for('change_logo_page'))

@app.route('/test', methods=['GET', 'POST'])
def testroute():
    return render_template('test.html')


# makes it runnable from python by typing 'python git_flask_app.py' in terminal
if __name__ == '__main__':
    app.run(debug=True)