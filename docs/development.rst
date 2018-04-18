pycassos development
====================

Contributing to the project
---------------------------

Requirements:
- python3 >= 3.6
- virtualenvwrapper
- npm >= 3
- node >= 5
- angular cli
  
Prepare virtualenv:

    PYCASSOSDIR=~/repos/pycassos #set to dir where pycassos was cloned
    mkvirtualenv -a $PYCASSOSDIR -i twine -i Sphinx \
                 -r $PYCASSOSDIR/requirements.txt dicaso

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
    ng new pycassong --style=scss --routing --skip-git
    mkdir -p pycassos/static && cd pycassong
    git add README.md e2e karma.conf.js package-lock.json package.json \
      protractor.conf.js src tsconfig.json tslint.json .gitignore \
      .angular-cli.json .editorconfig
    sed -i '' 's+dist+../pycassos/static+' .angular-cli.json
    ## style
    npm install --save normalize.css bootstrap@4.0.0-alpha.6 font-awesome tether
    npm install --save @ng-bootstrap/ng-bootstrap
    ## components
    for comp in nav home dosage; do
      ng g c $comp
      git add src/app/$comp
    done
    ## build
    ng build --prod --build-optimizer --base-href=/


References
----------
- https://github.com/hawzie197/Flask_Angular4_Skeleton
