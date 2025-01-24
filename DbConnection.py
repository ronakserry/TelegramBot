
import os 
from dotenv import load_dotenv
load_dotenv() 
from typing import Final  

DbServer:Final=os.getenv("DbServer")
DbName:Final=os.getenv("DbName")
ConnStr=f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DbServer};DATABASE={DbName};'