"""
Generated Model
flaskmvcmini v4.0
"""

import csv
import os


# ============================================================
# STEP 001 : CSV FILE
# ============================================================

FILE = "data/data.csv"


# ============================================================
# STEP 002 : CREATE CSV IF NOT EXISTS
# ============================================================

def m_create_file():

    if not os.path.exists(FILE):

        with open(FILE, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(
                [
                    "ID",
                    "Name",
                    "Value"
                ]
            )


# ============================================================
# STEP 003 : READ CSV
# ============================================================

def m_read_data():

    m_create_file()

    data = []

    with open(FILE, "r", newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            data.append(row)

    return data
