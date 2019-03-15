# RU-Paste
RU-Paste is a Django based Pastebin delvoped by students for an assignment. The aim of RU-Paste is to be secure, and be a lightweight application that can be deployed on multiple servers.


#### Key Features!
  - Appealing visual design
  - Private Posts
  - Text File Uploads
  - Raw and rendered files
  - Supports syntax highlighting as well as markdown rendering
  - Ability to search support
  - Full HTTPS support via TLS
  - Data stored on disk is encrypted
  - Schelduled backups
#### User layout
RU-Paste has 4 tiers of users:

  - Vistors
    - Can create a new User account 
    - Can login
    - Can perform a password reset
  - Users
    - Users can list, search, create, edit, update and delete their own Posts.
    - Can edit, update and delete their account and profile
    - Users are able to upload text files as posts.
  - Admins
    - Can list, search, create, edit, update, delete Users. 
    - administrator interface and functions are not be visible by Users or Visitors
    - Login from a special administrator portal 
  - SuperUsers
    - Can do all functions of the above users, aswell as do tasks related to maintenance and configuration of RU-Paste

#### Post Features
- Can be marked as Public or Private
- Posts work similarly to pastebin (a raw and rendered window) with the option to download the raw post as a text file.
- User should be able to configure a post expiration date. 
- Posts can have titles.
- The main/home page displays the 10 most recent posts. 

#### Dependencies and requirements

- Django - Web-Framework
- Python3 - cuz python > everything
- Bootstrap - Becuase css is hard
- Django-crispy-forms - For sweet crispy forms
- Django-pygments - Syntax highlighting Library
- Markdown - Rendering library for Markdown
- Mistune - Markdown parsing
- Pillow -  Python Imaging Library
- pyOpenSSL - Python based wrapper for OpenSSL library
- Werkzueg - WSGI utility library for Python

#### Installation

After installing the above requirements clone or download the repo. 

```sh
$ cd ru-paste
$ python manage.py runserver #note this runs the server without HTTPS support
$ python manage.py runserver_plus --cert certname #runs server with HTTPS
```
By Default the server runs on localhost:8000 for non https and https://127.0.0.1:8000 for HTTPS
