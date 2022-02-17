# Rodrigo Alcover
# Program GUI 2/7/2022
# CIS 226-23199 Advanced Python Programming

'''
On the terminal:
To run the program.
python3 -m venv venv
. venv/bin/activate
pip install pytest
pytest
 
'''


from  ageleapyears import add
#Importing the module from the main file

def test_add():
    assert add(7, 1) == 8