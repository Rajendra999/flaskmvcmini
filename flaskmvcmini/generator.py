"""
Generator Module
flaskmvcmini v4.0
"""

import os
import shutil


# ============================================================
# STEP 001 : CREATE FOLDER
# ============================================================

def m_create_folder(path):

    os.makedirs(path, exist_ok=True)


# ============================================================
# STEP 002 : COPY TEMPLATE AND REMOVE .tpl
# ============================================================

def m_copy_template(source, target):

    shutil.copy(source, target)


# ============================================================
# STEP 003 : CREATE PROJECT STRUCTURE
# ============================================================

def m_create_structure(project):

    folders = [
        project,
        f"{project}/templates",
        f"{project}/static",
        f"{project}/data"
    ]

    for folder in folders:
        m_create_folder(folder)


# ============================================================
# STEP 004 : GENERATE PROJECT
# ============================================================

def m_generate(project):

    m_create_structure(project)

    base = os.path.dirname(__file__)
    template = os.path.join(base, "templates")


    files = [
        ("app.py.tpl", f"{project}/app.py"),
        ("controller.py.tpl", f"{project}/controller.py"),
        ("model.py.tpl", f"{project}/model.py"),
        ("index.html.tpl", f"{project}/templates/index.html"),
        ("data.csv.tpl", f"{project}/data/data.csv"),
        ("requirements.txt.tpl", f"{project}/requirements.txt"),
        ("run.sh.tpl", f"{project}/run.sh")
    ]


    for source, target in files:

        print("SOURCE:", os.path.join(template, source))
        print("TARGET:", target)

        m_copy_template(
            os.path.join(template, source),
            target
        )


    os.chmod(
        f"{project}/run.sh",
        0o755
    )


    print()
    print("Project Generated")
    print("-----------------")
    print(project)
