# Rodrigo Alcover
# Program GUI 2/7/2022
# CIS 226-23199 Advanced Python Programming

'''
On the terminal:

python3 -m venv venv
. venv/bin/activate
pip install Flask
export FLASK_APP=hello.py
flask run
* Running on http://127.0.0.1:5000/
pip install pytest
pytest
 
'''

from ageleapyears import age_leap_years

def test_age_leap_years():
    assert age_leap_years("01","01","2020") == 2