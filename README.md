# ITBC Final project - Ivan Tot

This is a payment tracker / budget planner app.  
This is not an e-banking app, just a transaction tracker offering various information to the user.   
The app should be able to allow login for users, who may have different roles. After login, a user should be able to access his money account. A single user can have one money account.  
Money account is curated by the user, so the balance is completely up to the user and has no relations whatsoever to a banking account, and the transactions logged by the user will only change the balance of the money account within the app.
Money account and user creation should be handled by the administrator.  
Users log financial transactions (payments) for their related money accounts (type of transaction can be input or output).
Users also can create a budget with categories, assigning a certain amount of funds to be available for a given time range, per category.  
The app should be able to provide information related to money account balance, remaining funds per category, spending and earning statistics of various sorts, spending habits, favorite shops…

## Installation

### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```
### Activate Virtual environment
Open terminal and navigate to project directory, than run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |

### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```
### Databse
Start MySQL server and execute all commands in **_init_db/init_db.sql_**

### Environment variables
1. Create new file **_.env_**
2. Copy all consts from **env-template** to **_.env_**
3. Assign values to const in .env file


## Run server
From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```

## Once in docs / postman
Use startup route to set up admin and basic roles  
`/api/admin/setup-admin`

## Other consideration
At the moment DIN and EUR are only supported currency in the application.  
Transaction deduct funds from money account.   
Budget is an arbitrary amount of money assigned by user to a category during a period of time. Not connected to money account.  
Transactions can be inbound and outbound by nature.  
There must be a vendor, budget and category as well as a user with a money account for a transaction to take place.


## Notable endpoints:  
-    `/api/budgets/get-budgets-funds-by-user-id`
-    `/api/transactions/get-transactions-in-time-by-user-id`
-    `/api/transactions/get-transactions-by-vendor-id`
-    `/api/transactions/get-spending-habits-user-id`
-    `/api/transactions/get_number_of_transactions_for_vendors_per_category`
-    `/api/transactions/get_favorite_vendors_per_category`
-    `/api/transactions/get-favorite-means-of-payment-by-user`
-    `/api/transactions/get-inbound-outbound-payments-by-user`



[//]: # (## Contributing)

[//]: # ()
[//]: # (Pull requests are welcome. For major changes, please open an issue first)

[//]: # (to discuss what you would like to change.)

## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)