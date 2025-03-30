import pyweber as pw

class Label(pw.Element):
    def __init__(self, id: str, content: str):
        super().__init__(tag='label', content=content, attrs={'for': id})

class Input(pw.Element):
    def __init__(self, id: str, name: str, type: str = 'text', placeholder: str = None):
        super().__init__(tag='input', id=id)
        self.attrs={'type': type, 'placeholder': placeholder, 'name': name}

class Button(pw.Element):
    def __init__(self, content: str, id: str = None, classes: list[str] = None, events: pw.TemplateEvents = None):
        super().__init__(tag='button', id=id, content=content, classes=classes, events=events)

class H2(pw.Element):
    def __init__(self, content: str, classes=['form-title']):
        super().__init__(tag=pw.HTMLTag.h2, classes=classes, content=content)

class Form(pw.Element):
    def __init__(self, method: str = 'dialog'):
        super().__init__(tag='form', classes=['form'])
        self.attrs = {'method': method}
        self.childs = [
            H2(content='Create your Account Here'),
            Label(id='fullname', content='Nome Completo'),
            Input(id='fullname', name='fullname', type='text', placeholder='Nome Completo'),
            Label(id='contact', content='Contacto'),
            Input(id='contact', name='contact', type='tel', placeholder='Contacto'),
            Label(id='email', content='Email'),
            Input(id='email', name='email', type='email', placeholder='Email'),
            Label(id='password', content='Palavra-Passe'),
            Input(id='password', name='password', type='password', placeholder='Palavra-Passe'),
            Label(id='confirm-password', content='Confirmar Palavra-Passe'),
            Input(id='confirm-password', name='confirm-password', type='password', placeholder='Confirmar Palavra-Passe'),
            Button(content='Registar', classes=['btn-register'], events=pw.TemplateEvents(onclick=self.register))
        ]
    
    def register(self, e: pw.EventHandler):
        inputs = [child for child in e.template.querySelectorAll('input')]
        for input in inputs:
            pw.print_line(text=f'tag={input.tag}\tvalue={input.value}')

class Home(pw.Template):
    def __init__(self):
        super().__init__(template='index.html')
        self.container = self.querySelector('.container')
        self.container.childs.append(Form())

def main(app: pw.Pyweber):
    app.add_route(route='/', template=Home())

if __name__ == '__main__':
    pw.run(target=main)