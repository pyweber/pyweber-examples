import pyweber as pw
from manage_sql import SQLITE

# using function to create pyweber templates
def Registar():
    def registar(e: pw.EventHandler):
        username = e.template.querySelector(selector='#nome')
        email = e.template.querySelector(selector='#email')
        password = e.template.querySelector(selector="#senha")
        db = SQLITE(database='usuarios')

        if username.value and email.value and password.value:
            db.insert_data(
                tablename='usuarios',
                insert_query=[
                    db.ColumnData(
                        column='username',
                        value=username.value
                    ),
                    db.ColumnData(
                        column='password',
                        value=db.encrypt_value(password.value)
                    ),
                    db.ColumnData(
                        column='email',
                        value=email.value
                    )
                ]
            )
        
            username.value = ''
            password.value = ''
            email.value = ''
    
    template = pw.Template(template='registar.html')
    template.querySelector(selector='button').events = pw.Events(onclick=registar)

    return template

# pyweber Element using class (Form)
class Form(pw.Element):
    def __init__(self, app: pw.Router):
        super().__init__(tag='form')
        self.classes = ['formulario']
        self.db = SQLITE(database='usuarios')
        self.attrs = {'method': 'dialog'}
        self.app = app
        child_1 = pw.Element(
            tag='i',
            classes=["bi", "bi-key"]
        )
        self.childs = [
            pw.Element(
                tag='input',
                id='username',
                attrs={'name': 'username', 'placeholder': 'username', 'type': 'text'}
            ),
            pw.Element(
                tag='input',
                id='password',
                attrs={'name': 'password', 'placeholder': 'password', 'type': 'password'}
            ),
            pw.Element(
                tag='button',
                content=f'{{{child_1.uuid}}} Login',
                classes=['btn-login'],
                events=pw.Events(onclick=self.logar),
                childs=[child_1]
            )
        ]
    
    def logar(self, e: pw.EventHandler):
        username = e.template.querySelector(selector='#username')
        password = e.template.querySelector(selector='#password')

        usuarios = self.db.select_data(
            tablename='usuarios',
            condition=self.db.filter_by(
                column='username'
            ).EQUAL(value=username.value).AND.filterby(
                column='password'
            ).EQUAL(
                value=self.db.encrypt_value(
                    value=password.value
                )
            )
        )

        if usuarios:
            self.app.launch_url('http://localhost:8800/')


class Container(pw.Element):
    def __init__(self, app):
        super().__init__(tag='div')
        self.classes = ['container']
        self.childs = [
            Form(app=app)
        ]

# using POO to create a pyweber template
class Login(pw.Template):
    def __init__(self, app: pw.Router):
        super().__init__(template='login.html')
        self.body = self.querySelector(selector='body')
        self.body.childs = [Container(app=app)]

def main(app: pw.Router):
    app.add_route(route='/', template=pw.Template(template='index.html'))
    app.add_route('/login', template=Login(app=app))
    app.add_route('/registar', template=Registar())

if __name__ == '__main__':
    pw.run(target=main)