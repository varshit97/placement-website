## Readme

It is a website having features of a placement portal made as an assignment using the web2py framework.

web2py is a free open source full-stack framework for rapid development of fast, scalable, secure and portable database-driven web-based applications. 

It is written and programmable in Python. LGPLv3 License

Learn more at http://web2py.com

## Google App Engine deployment

    cp examples/app.yaml ./
    cp handlers/gaehandler.py ./
    
Then edit ./app.yaml and replace "yourappname" with yourappname.

## Installation Instructions

To start web2py there is NO NEED to install it. Just unzip and do:

    python web2py.py

That's it!!!

## web2py directory structure

    project/
        README
        LICENSE
        VERSION                    > this web2py version
        web2py.py                  > the startup script
        anyserver.py               > to run with third party servers
        ...                        > other handlers and example files
        gluon/                     > the core libraries
            contrib/               > third party libraries
            tests/                 > unittests  
        applications/              > are the apps
            admin/                 > web based IDE
                ...
            examples/              > examples, docs, links
                ...
            welcome/               > the scaffolding app (they all copy it)
                ABOUT
                LICENSE
                models/
                views/
                controllers/
                sessions/
                errors/
                cache/
                static/
                uploads/
                modules/
                cron/
                tests/
            ...                    > your own apps
        examples/                  > example config files, mv .. and customize
        extras/                    > other files which are required for building web2py
        scripts/                   > utility and installation scripts
        handlers/
            wsgihandler.py         > handler to connect to WSGI
            ...                    > handlers for Fast-CGI, SCGI, Gevent, etc
        site-packages/             > additional optional modules
        logs/                      > log files will go in there
        deposit/                   > a place where web2py stores apps temporarily
