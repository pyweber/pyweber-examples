# PyWeber Examples

This repository contains example applications built with PyWeber, a Python web framework for building interactive web applications using pure Python.

### Examples
Bellow, get all examples projects made with pyweber.
* [TodoApp](https://github.com/pyweber/pyweber-examples/tree/master/TodoApp)
* [ClockApp](https://github.com/pyweber/pyweber-examples/tree/master/ClockApp)
* [LoginApp](https://github.com/pyweber/pyweber-examples/tree/master/LoginApp)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. Install PyWeber:

   ```bash
   pip install pyweber
   ```

2. Clone this examples repository:

   ```bash
   git clone https://github.com/pyweber/pyweber-examples.git
   cd pyweber-examples
   ```

3. Choose an example and navigate to its directory:

   ```bash
   cd pyweber-example
   ```

4. Install any example-specific dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running Examples

PyWeber provides a command-line interface (CLI) for running applications:

#### Development Mode (with auto-reload)

```bash
pyweber run --reload
```

This mode automatically reloads the application when you make changes to your code, which is ideal for development.

#### Production Mode

```bash
pyweber run
```

This mode runs the application without auto-reload, which is more suitable for production environments.

## Project Structure

Each example follows a similar structure:

```
example-name/
├── main.py           # Main application file
├── templates/        # HTML templates
│   └── index.html    # Base HTML template
├── static/           # Static assets
│   ├── css/          # CSS stylesheets
│   │   └── style.css
│   └── js/           # JavaScript files (if needed)
├── requirements.txt  # Example-specific dependencies
└── README.md         # Example-specific documentation
```

## Configuration

PyWeber applications can be configured using a `config.json` file in the project root:

```json
{
  "app": {
    "name": "My PyWeber App",
    "debug": true,
    "icon": "/static/favicon.ico"
  },
  "server": {
    "host": "localhost",
    "port": 8000
  },
  "websocket": {
    "host": "localhost",
    "port": 8765
  }
}
```

## Resources

- [PyWeber Documentation](https://github.com/pyweber/pyweber)
- [PyWeber GitHub Repository](https://github.com/pyweber/pyweber)
- [Report Issues](https://github.com/pyweber/pyweber/issues)
- [YouTube Channel](https://youtube.com/@devpythonMZ)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.