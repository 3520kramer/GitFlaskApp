from flask_table import Table, Col, LinkCol, BoolCol
from flask import url_for

class DirectoryTable(Table):
    classes = ['table', 'table-light', 'table-bordered', 'thead-light', 'tbody-light', 'my-table']
    is_dir = BoolCol('', yes_display='<img class="my-image" src="static/folder_icon.png">', no_display='<img class="my-image" src="static/file_icon.png">', show=True)
    name = LinkCol(name='name', endpoint='github_command_route', attr='name', url_kwargs=dict(command='name'))

class DirectoryTableForClone(Table):
    classes = ['table', 'table-light', 'table-bordered', 'thead-light', 'tbody-light', 'my-table']

    is_dir = BoolCol('isFolder', yes_display='yes', no_display='no')
    name = LinkCol(name='name', endpoint='repository_command_route', attr='name', url_kwargs=dict(command='name'))

    
    