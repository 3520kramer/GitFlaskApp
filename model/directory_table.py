from flask_table import Table, Col, LinkCol, BoolCol

class DirectoryTable(Table):


    is_dir = BoolCol('isFolder', yes_display='yes', no_display='no')
    name = LinkCol(name='name', endpoint='repository_command_route', attr='name', url_kwargs=dict(command='name'))
    
    