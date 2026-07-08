# flaskmvcmini v4.0 User Guide


## INSTALL

Go to package folder:

    cd flaskmvcmini


Install:

    pip install .


Verify:

    flaskmvcmini


## CREATE NEW PROJECT


Command:

    flaskmvcmini new ProjectName


Example:

    flaskmvcmini new StockApp


Created structure:

    StockApp/
    |
    ├── app.py
    ├── controller.py
    ├── model.py
    ├── requirements.txt
    ├── run.sh
    |
    ├── data/
    |
    ├── templates/
    |
    └── static/


## RUN PROJECT


Enter project:

    cd StockApp


Install requirements:

    pip install -r requirements.txt


Run:

    ./run.sh


or:

    python app.py


## MVC FLOW


Browser

    |
    v

app.py

    |
    v

controller.py

    |
    v

model.py

    |
    v

CSV file


## NAMING RULE


app.py

    a_ functions


controller.py

    c_ functions


model.py

    m_ functions


## DATA STORAGE


Default:

    data/data.csv


Storage:

    CSV module only


## PROJECT PURPOSE


Minimal Flask MVC generator.

Features:

- Flask application
- MVC structure
- CSV model
- HTML templates
- Static files
- Simple generation


