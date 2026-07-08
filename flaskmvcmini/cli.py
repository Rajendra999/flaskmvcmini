"""
CLI Module
flaskmvcmini v4.0
"""

import sys
from .generator import m_generate


# ============================================================
# STEP 001 : HELP
# ============================================================
def c_help():

    print()
    print("flaskmvcmini v4.0")
    print()
    print("Usage")
    print("-----")
    print("python -m flaskmvcmini")
    print("python -m flaskmvcmini new ProjectName")
    print()


# ============================================================
# STEP 002 : NEW COMMAND
# ============================================================
def c_new(project_name):

    print()
    print("Creating Project")
    print("----------------")
    print(project_name)

    m_generate(project_name)

    print("Generator : OK")
    print()


# ============================================================
# STEP 003 : MAIN
# ============================================================
def c_main():

    args = sys.argv[1:]

    if len(args) == 0:
        c_help()
        return

    command = args[0]

    if command == "new":

        if len(args) < 2:
            print("ERROR : Missing Project Name")
            return

        c_new(args[1])
        return

    print("Unknown Command :", command)
