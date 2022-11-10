# API & Database Template for a Workplace Session Recorder

## Quick Start

- Clone the repository

    ```bash
    git clone https://github.com/blackprince001/Workplace-Session-Manager
    ```

- Move into the directory

    ```bash
    cd Workplace-Session-Manager
    ```

- Set up a virtual environment with Venv on Vscode or any python environment manager you have installed, and it will automatically install the dependencies. This project uses pipenv to handle dependency installs and virtual environments.

- To simply install project dependencies, run the command below.

  ```bash
  pipenv sync
  ```

- Set up a dev environment by running the command to install dependencies to work on the project. Do note that the make command is already dependent on the one above. So if you use this command, there will be no need for you to run the prev one.
  
  ```bash
  pipenv sync --dev
  ```

  while you're in `/Workplace-Session-Manager`

## Testing

To run the tests in the project:

- You need to install the dev packages:

  ```bash
  pipenv install --dev
  ```
  
- Run pytest make commands highlighted above

## Architecture Design

![Desing](design.png)

## File Structure for Project

```bash
.
├── design.png
├── manager
│   ├── core.py
│   ├── crud
│   │   ├── checker.py
│   │   ├── __init__.py
│   │   └── worker.py
│   ├── __init__.py
│   ├── models.py
│   ├── schema
│   │   ├── checkbook.py
│   │   ├── __init__.py
│   │   └── worker.py
│   └── utils
│       ├── __init__.py
│       └── utils.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── tests
    ├── api
    │   ├── __init__.py
    │   ├── test_checkbook_table_api.py
    │   └── test_worker_table_api.py
    ├── conftest.py
    └── __init__.py

6 directories, 20 files
```
