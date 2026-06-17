# ShoppingListApp

A shopping list web-app

## Description

A simple Django-backed web application that allows the user to add items to a shopping list that persists between sessions. The user can add from a pre-defined inventory of global and user-created items.

The user can add custom tags to items to organise them and items can be toggled between two states to indicate bought/ not bought status.

The user can search the inventory to find items to add to their shopping list.

The app automatically tracks totals for the shopping list, broken down by tag and bought status.

Users can log in via username and password or Google Login.

**Note:** This project has been shipped with a pre-populated `db.sqlite3` for demo purposes. I am aware that committing a database file isn't best practice for projects (it should normally be excluded via `.gitignore`), but I have included it here so the app works out of the box without extra setup and full functionality can be demonstrated. I have added a few images into media for the global inventory items. Shipping in debug mode.

**Demo Account:**
The database is shipped with a demo account already created with a pre-existing shopping list with assigned tags, to demonstrate functionality.

Username: demo_account
Password: root

**Key Dependencies:**
Django>=6.0
django-allauth>=65.18
django-colorfield>=0.14

### Installing
1. Clone the repository
```
git clone https://github.com/google-london-apprenticeships/DL-ZachE.git
cd DL-ZachE
```
2. Create virtual environment
```
python -m venv venv
source venv/bin/activate
``` 

3. Install dependencies
```
pip install -r requirements.txt
```

4. (Optional) If you want to test the program, you may wish to create a superuser.

```
python manage.py createsuperuser
```
And follow the instructions in terminal to create a super user.


### Dependencies
Requires Django (developed using Django v6.0.6)
Tested on Arch Linux (kernel 7.0.10-arch1-1)
Developed using Python 3.14.5

### Executing Program
Simply host the application. To do so locally:
1. Navigate to /ShoppingListApp
2. Run the following

```
python manage.py runserver 
```

3. Visit local IP address in browser
```
http://127.0.0.1:{port number goes here}/
```
8000: http://127.0.0.1:8000/

### Updating after changes

Note: Edits to models and underlying db are not propagated by default. If changes are made to project files, migration may be required. If you encounter errors run the following:

```
python manage.py makemigrations
python manage.py migrate
```

## Author
Zach David Edwards

## Version History
0.1
Initial Release

## License

This project is licenced under the MIT License:

Copyright (c) 2026 Zach David Edwards

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
