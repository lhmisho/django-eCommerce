for creating a register form

Login user
    1) create form -- > LoginterForm() -- { usernam, password, password2}
    2) create view -- > login_page
    3) manage url  -- > path('login/', 'registration/login.html', context)
    4) manage template {{ form }}

Register User
    1) create form -- > RegisterForm() -- > { username, password, email}
        *)clean_username() --> check the user is already exists or not 
        *)clean_password() --> check the password is already exists or not 
    2) create view -- > register_page -- > 
    3) manage url -- > path('register/', 'registration/register.html', context)
    4) manage url -- > {{form}}
those are the basic concept 