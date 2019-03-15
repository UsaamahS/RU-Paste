# RU-Paste
RU-Paste is Django based Pastebin delvoped by students for an assignment. The aim of RU-Paste is to be secure, and be a lightweight application that can be deployed on multiple servers.


##### Key Features!
  - Appealing visual design
  - Private Posts
  - Text File Uploads
  - Raw and rendered files
  - Supports syntax highlighting as well as markdown rendering
  - Ability to search support
  - Full HTTPS support via TLS
  - Data stored on disk is encrypted
  - Schelduled backups
##### User layout
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
