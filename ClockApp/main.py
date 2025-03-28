import pyweber as pw
from datetime import datetime
import asyncio

class Text(pw.Element):
    def __init__(self, title: str, value: str):
        super().__init__(tag=pw.HTMLTag.div)
        self.classes = ['time-element']
        self.childs = [
            pw.Element(tag=pw.HTMLTag.p, content=str(value), classes=['time-value']),
            pw.Element(tag=pw.HTMLTag.span, content=title)
        ]

class Button(pw.Element):
    def __init__(self, id: str, content: str, events: pw.Events = None, classes: list[str] = None):
        super().__init__(tag=pw.HTMLTag.button, id=id, events=events)
        self.childs = [pw.Element(tag=pw.HTMLTag.i, classes=classes)]
        self.content = f'{{{self.childs[0].uuid}}} {content}'

class Title(pw.Element):
    def __init__(self, title: str):
        super().__init__(tag=pw.HTMLTag.h2, classes=['time-title'], content=title)
        self.childs = [
            pw.Element(
                tag='i',
                classes=['bi', 'bi-alarm']
            )
        ]

class Time(pw.Element):
    def __init__(self):
        super().__init__(tag=pw.HTMLTag.div, classes=['time-values'])
        self.childs = [Text(title='hours', value=0), Text(title='minutes', value=0), Text(title='seconds', value=0)]

class Buttons(pw.Element):
    def __init__(self):
        super().__init__(tag=pw.HTMLTag.div, classes=['time-buttons'])
        self.childs = [
            Button(id='startbtn', content='start', classes=['bi', 'bi-play-fill'], events=pw.Events(onclick=self.set_time))
        ]
    
    async def set_time(self, e: pw.EventHandler):
        while True:
            hour, minutes, seconds = datetime.now().strftime('%H:%M:%S').split(':')
            el_hr, el_min, el_sec = e.template.getElementByClass(class_name='time-value')
            el_hr.content, el_min.content, el_sec.content = hour, minutes, seconds
            e.update
            await asyncio.sleep(1)

class Clock(pw.Template):
    def __init__(self, app: pw.Router):
        super().__init__(template='index.html')
        self.app = app
        self.container = self.querySelector(selector='.container')
        self.container.childs = [
            Title(title='Clock'),
            Time(),
            Buttons()
        ]

def main(app: pw.Router):
    app.add_route(route='/', template=Clock(app=app))

if __name__ == '__main__':
    pw.run(target=main)