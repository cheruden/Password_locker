# Password Locker
### by :cheruiyot Dennis

#### To clone project to your local computer and run it follow the following instructions.

### Setup
> Install these first:
* Python3.8
* pip
* pyperclip
* xclip

 

 >1. `` git clone git remote add origin https://github.com/cheruden/Password_locker``
>2. ``cd Password_locker``
>3. To run the app,  use  ``` python3.8 run.py ```
>4. To run tets use ``` python3.8 test_user_cred.py ```




## Technologies used
* Python3.8


| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: na** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |


### Cloning
* In your terminal:
        
        $ git clone https://github.com/cheruden/Password_locker.git``
        $ cd Password_locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py