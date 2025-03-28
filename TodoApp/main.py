# TodoApp Example using PyWeber
# This example demonstrates how to build a complete Todo application
# with PyWeber, showcasing components, event handling, and DOM manipulation.

import pyweber as pw

class Input(pw.Element):
    """
    Reusable input component for task entry.
    Creates a styled text input with appropriate attributes.
    """
    def __init__(self):
        super().__init__(tag='input')
        self.attrs = {'type': 'text', 'name': 'task', 'placeholder': 'add your task'}
        self.id = 'task-input'

class Button(pw.Element):
    """
    Reusable button component with event handling.

    Args:
        value: The text to display on the button
        event: The event handler to attach to the button
    """
    def __init__(self, value: str, event: pw.Events = None):
        super().__init__(tag='button')
        self.classes = ['btn-task']
        self.content = value
        self.events = event

class Task(pw.Element):
    """
    Component representing a single task in the todo list.
    Each task has its own text and action buttons (edit and remove).

    Args:
        task: The text content of the task
    """
    def __init__(self, task: str):
        super().__init__(tag='div')
        self.classes = ['task']
        self.childs = [
            pw.Element(
                tag='p',
                classes=['task-text'],
                content=task
            ),
            pw.Element(
                tag='span',
                classes=['task-buttons'],
                childs=[
                    Button(value='Edit', event=pw.Events(onclick=self.edit_task)),
                    Button(value='Remove', event=pw.Events(onclick=self.remove_task))
                ]
            )
        ]

    def remove_task(self, e: pw.EventHandler):
        """
        Event handler to remove a task from the list.

        Args:
            e: The event handler object containing references to the current state
        """
        # Navigate up the DOM tree to find the task element
        task = e.element.parent.parent
        # Remove the task from its parent
        task.parent.remove_child(task)

    def edit_task(self, e: pw.EventHandler):
        """
        Event handler to edit a task.
        Moves the task text to the input field and removes the task.

        Args:
            e: The event handler object containing references to the current state
        """
        # Navigate up the DOM tree to find the task element
        task = e.element.parent.parent
        # Get the input field from the template
        input_text = e.template.querySelector(selector='#task-input')

        # Set the input value to the task text for editing
        input_text.value = task.childs[0].content
        # Remove the task from the list
        task.parent.remove_child(task)

class TodoForm(pw.Element):
    """
    Main container for the Todo application.
    Contains the title, input form, and task list.
    """
    def __init__(self):
        super().__init__(tag='div')
        self.classes = ['container']
        self.childs = [
            pw.Element(
                tag='h2',
                classes=['title'],
                content='Todo App'
            ),
            pw.Element(
                tag='form',
                attrs={'method': 'dialog'},
                childs=[
                    Input(),
                    Button(
                        value='Add',
                        event=pw.Events(
                            onclick=self.add_task
                        )
                    )
                ]
            ),
            pw.Element(
                tag='div',
                classes=['tasks'],
                childs=[]
            )
        ]

    def add_task(self, e: pw.EventHandler):
        """
        Event handler to add a new task to the list.

        Args:
            e: The event handler object containing references to the current state
        """
        # Get the input field and tasks container from the template
        task_input = e.template.querySelector(selector='#task-input')
        tasks = e.template.querySelector(selector='.tasks')

        # Only add a task if the input has a value
        if task_input.value:
            # Create and append a new Task component
            tasks.childs.append(
                Task(task=task_input.value)
            )

            # Clear the input field and set focus for better UX
            task_input.value = ''
            task_input.attrs['autofocus'] = ''

class TodoApp(pw.Template):
    """
    Main application template.
    Sets up the page structure and adds the TodoForm to the body.

    Args:
        app: The PyWeber router instance
    """
    def __init__(self, app: pw.Router):
        super().__init__(template='index.html')
        self.app = app
        # Add the TodoForm to the body of the HTML template
        self.querySelector(selector='body').childs.append(
            TodoForm()
        )

def main(app: pw.Router):
    """
    Application entry point.
    Registers routes with the PyWeber router.

    Args:
        app: The PyWeber router instance
    """
    app.add_route(route='/', template=TodoApp(app=app))

if __name__ == '__main__':
    # Start the PyWeber application
    pw.run(target=main)