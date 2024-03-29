import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# The name of the file that contains our credentials.
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get Sales Figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")
        
        data_str = input("Enter your data here: ")
        
        sales_data = data_str.split(",")
        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data
    
def validate_data(values):
	"""
	Inside the try, converts all string values into integers.
	Raises ValueError if strings cannot be converted into int,
	or if there aren't exactly 6 values.
	"""
	try:
				[int(value) for value in values]             
				if len(values) != 6:
					raise ValueError(
					f"Exactly 6 values required, you provided {len(values)}"
					)
	except ValueError as e:
				print(f"Invalid data: {e}, please try again.\n")
				return False
	return True
      
data = get_sales_data()