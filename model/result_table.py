from flask_table import Table, Col, DatetimeCol, ButtonCol

class ResultTable(Table):
    

    id = Col('ID') #, show=False
    name = Col('Name')
    created_at = DatetimeCol('Created At', datetime_format="dd/MM-YYYY hh:mm:ss")
    updated_at = DatetimeCol('Updated At', datetime_format="dd/MM-YYYY hh:mm:ss")
    language = Col('Language')
    button_col = ButtonCol('Clone', 'repository_page', url_kwargs=dict(id='id'))
    # 1. argument is the name ie. label on the button
    # 2. argument is the endpoint ie. the method form git_flask_app to call ie. the route
    # 3. argument is the what we pass along ie. the id of the repository that gets cloned 