"""
Generated Controller
flaskmvcmini v4.0
"""

from flask import render_template
from model import m_read_data


# ============================================================
# STEP 001 : INDEX CONTROLLER
# ============================================================

def c_index():

    data = m_read_data()

    return render_template(
        "index.html",
        data=data
    )
