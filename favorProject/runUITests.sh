#!/bin/bash

if [ $# -gt 0 ]; then
    if [ "$1" == "--help" ]; then
        echo -e "To run all UI tests: ./runUITests.sh\nTo run a specific UI test: ./runUITests.sh ui_tests/<file name in ui_tests>"
    else
        filename="$1"
        dir_in=${PWD##*/}
        if [ "$dir_in" == "ui_tests" ]; then
            if [ -f $filename ]; then
                python3 ../manage.py test $1
            else
                echo "File $1 does not exist in ui_tests directory!"
            fi
        else
            if [[ "$1" != "ui_tests/"* ]]; then
                echo -e "WARNING: running UI test OUTSIDE UI directory!!... Consider putting test in ui_tests directory"
                if [ -f $1 ]; then
                    python3 manage.py test $1
                else
                    echo "Path $1 not acceptable for UI tests or doesn't exist!"
                fi
            else
                if [ -f $1 ]; then
                    python3 manage.py test $1
                else
                    echo "ui_tests/$1 is not a valid path"
                fi
            fi
        fi
    fi
else
    python3 manage.py test ui_tests/*.py
fi
