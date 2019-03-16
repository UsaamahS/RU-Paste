# RU-Paste
USAAMAH SAEED & ROMEL RAMKISSOON

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

#### Screenshots

##### Home page
![image](https://user-images.githubusercontent.com/43759716/54469364-71564f80-476d-11e9-96c3-29df1e80ba7f.png)

##### HTTPS support 
![image](https://user-images.githubusercontent.com/43759716/54469396-c5613400-476d-11e9-8bb3-fd253ce3db28.png)

##### Admin login portal
![image](https://user-images.githubusercontent.com/43759716/54469403-de69e500-476d-11e9-8348-4f1429c330fc.png)

##### Admin permissions
![image](https://user-images.githubusercontent.com/43759716/54469431-428ca900-476e-11e9-9128-3cf3130eebf0.png)

##### Admin's ability to view users 
![image](https://user-images.githubusercontent.com/43759716/54469442-67811c00-476e-11e9-9fc4-1c664d91443c.png)

##### Profile View
![image](https://user-images.githubusercontent.com/43759716/54469452-854e8100-476e-11e9-9d94-4b578b95f44b.png)

##### Password Reset
![image](https://user-images.githubusercontent.com/43759716/54469460-9b5c4180-476e-11e9-8e19-3c9235a7d29e.png)
![image](https://user-images.githubusercontent.com/43759716/54469473-d2325780-476e-11e9-9b8f-79996eaa9293.png)

##### Upload file
![image](https://user-images.githubusercontent.com/43759716/54469481-e5ddbe00-476e-11e9-8f3d-8f4a2105ddff.png)

##### Syntax highlighting
![image](https://user-images.githubusercontent.com/43759716/54469487-01e15f80-476f-11e9-952a-d2323366782e.png)

##### Downloading files
![image](https://user-images.githubusercontent.com/43759716/54469491-17ef2000-476f-11e9-8abf-142cd2059b53.png)

##### Search posts
![image](https://user-images.githubusercontent.com/43759716/54469496-2d644a00-476f-11e9-8818-dd8c2be75d5f.png)

##### Markdown Rendering
![image](https://user-images.githubusercontent.com/43759716/54469505-3b19cf80-476f-11e9-8db5-97c3569eecf4.png)

##### Creating a paste
![image](https://user-images.githubusercontent.com/43759716/54469511-597fcb00-476f-11e9-9c88-d5a508a77370.png)

##### Crontab for backups
![image](https://user-images.githubusercontent.com/43759716/54469552-cd21d800-476f-11e9-917f-59b453c1fb7d.png)

##### Password encryption
![image](https://user-images.githubusercontent.com/43759716/54469591-46b9c600-4770-11e9-8ace-35b1d6d82e07.png)

