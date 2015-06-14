#!/bin/bash
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "Fibonacci\n"

case $1 in

    setup)

        echo -e "Installing dependencies...\n"

        pip install -r $BASE_DIR/requirements.txt

        ;;

    run)

        $BASE_DIR/run.py

        ;;

    test)

        echo "Running the test suit..."

        nosetests test

        ;;

    check)

        echo -e "Running source code checker...\n"

        flake8 $BASE_DIR

        ;;

    shell)

        ipython

        ;;

    *)

        echo "Usage:"

        echo -e "  ./manage.sh <command>\n"

        echo "Available commands:"

        echo "  setup                                                Install dependencies"

        echo "  run                                                  Run the main script"

        echo "  test                                                 Run the test suit"

        echo "  check                                                Run source code checker"

        echo "  shell\
                                                Open an enhanced Interactive Python"

        ;;

esac
