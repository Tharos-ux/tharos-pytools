make:
    @git pull && pip install --upgrade pip && python -m pip install -r requirements.txt --upgrade && python -m pip install .

install:
    @pip install tharos-pytools --upgrade

build:
    @rm -f dist/* && python -m build && twine upload dist/*

local:
    @python -m pip install .