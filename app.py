#! /usr/bin/env python
from cvapp import app

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')

#    extra_files=['./cvapp/static/css/style.css']) 
# DOES NOT HELP, the problem with CSS update comes from browser cache (ctrl+f5 to force css load)
