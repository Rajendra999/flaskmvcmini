"""
Generated Flask App
flaskmvcmini v4.0
"""

from flask import Flask, render_template
from controller import c_index


# ============================================================
# STEP 001 : CREATE APP
# ============================================================

app = Flask(__name__)


# ============================================================
# STEP 002 : ROUTE
# ============================================================

@app.route("/")
def a_index():

    return c_index()


# ============================================================
# STEP 003 : RUN APP
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)
