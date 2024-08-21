# HMP Power supply series python wrapper

## Installation

Installation from the Pypi repository:

```bash
pip install ragnarok_pyrs
```

To install the latest development version

```bash
pip install git+https://github.com/durufle/pyrs.git
```

## development

clone the repository in your workspace:

```bash
cd ./workspace
~/workspace $ git clone https://github.com/durufle/pyrs.git
```

select package folder, create a virtual environment and select it:

```bash
~/workspace $ cd pyrs
~/workspace/pyrs $ python -m venv venv
~/workspace/pyrs $ source ./venv/bin/activate
# install dependency package
(venv) ~/workspace/pyrs $ pip install -r requirements.txt
(venv) ~/workspace/pyrs $ pip install -r development.txt
```
Use you preferred IDE to develop (PyCharm,...)

To build a wheel package:

```bash
(venv) ~/workspace/pyrs $ python -m build
```

To execute pylint locally you can do the following:

```bash
(venv) ~/workspace/pyrs $ p pylint $(git ls-files '*.py')
```
This will execute pylint for all python files in the repository.

