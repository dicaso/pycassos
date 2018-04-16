pycassos development
====================

Contributing to the project
---------------------------

    pip install pycassos[development]

Style guide
-----------
TODO

Original project setup
----------------------

    # doc tree
    mkdir docs && cd docs
    sphinx-quickstart #initiating the documentation
    git add Makefile conf.py index.rst
    make html
    cd ..

    # angular frontend tree
    # => dir for development, dir for build end that will be flask served
    mkdir -p pycassos/static/song && ng new pycassong && cd pycassong
    git add README.md e2e karma.conf.js package-lock.json package.json \
      protractor.conf.js src tsconfig.json tslint.json .gitignore \
      .angular-cli.json .editorconfig
