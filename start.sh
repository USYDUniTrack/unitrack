#!/bin/bash

# Check if a virtual environment is active
if [[ "$VIRTUAL_ENV" != "" ]]; then
    # Deactivate the virtual environment
    deactivate
    echo "Virtual environment deactivated."
else
    echo "No virtual environment is currently active."
fi

source venv/bin/activate
python manage.py runserver
