from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('Id', show=False)
    user_name = Col('Name')
    user_email = Col('Email')
    user_password = Col('Password', show=False)
    edit = LinkCol('Editar', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Eliminar', 'delete_user', url_kwargs=dict(id='user_id'))