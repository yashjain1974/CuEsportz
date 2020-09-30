<--All about this project-->

1. Creating base of project...

2. creating an app for authentication purpose...
    1. urls mapping
    2. declaring functions in views
    3. creating models
    4. registring models for admin
    5. making migrations and deploying it
    6. creating superuser(username=admin, password=admin)

3. signup with registration form
    1. using csrf in form for security purpose
    2. defining action and methods in forms in 'registration.html'
    3. defining 'signUp' method in 'accounts.views' after that we can sign up in the web
    4. we are using initial mobile number as username for non staff user
    5. we are storing mob_no and refral code in different model
    6. password in different model and others details in User model
    7. Hashing password is mandatory ...(later)<<<--->>>(10)

4. signin with registration form
    1. there are three ways of signing in the web username, email and mob_no
    2. defining a function for signing with username, email and mobile
    3. authenticating with username using 'auth' model
    4. authenticating with email using ...(later)<<<--->>>(8)
    5. authenticating with mob_no using ...(later)<<<--->>>(8)

5. customizing admin page
    1. creating a method in accounts/models.py which return current mobile number
        1. creating '__str__(self)' method and returning mobile number
        2. you can access this value by using 'UserDetail.objects.get(id=object_id_var)'
    2. for changing titles of site, override variables in accounts.urls.py

6. loading all html files
    1. create templates directory in src
    2. put all html files in temlates
    3. adding temlates diectory in settings.py in templates list

7. loading static files it means load all java script, css files and images files.
    1. creating a static directory
    2. create 'STATICFILES_DIRS' in setting
    3. put all js, css and images files in static directory
    4. before every static files use '/static/' because these files are present in static file
        1. provide actual url or
        2. load all static files in the html file using {%load static%}
            1. use jinja syntax in all static files like {% static 'img_dir/img_name.jpg' %}
    
8. authenticating by mobile number
    1. getting mobile number from UserDetail model
    2. checking the mobile number with user entered mobile number and iterating through it ()<<<--->>>(9)
    3. if number matched then checking for password 
    4. we have a different model for password 
    5. (password must be hashed) if password matched then we can log in ()<<<-->>>(3.7)
    6. if number doesn't matched then user is not registered

9. we still don't know that how many users we have 
    1. countimng users
    2. creating a text file and set the total numbner of current user 
    3. total numbers means maximum id or id of last user
    4. every time a user created increment in it by 1

10. Hashing Password
    1. we are not using hashing we are using encryption here ()<<<--->>>(11)
    2. (documents are present in src/accounts/backends.py) ...

11. Encrypt password (later) ...
    1. generate key
    
12. generating username
    1. creating a function in backends.py
    2. (documents are available at accounts/backends.py)


