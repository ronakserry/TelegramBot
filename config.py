import os 
from dotenv import load_dotenv
load_dotenv() 
from typing import Final 

BotToken:Final = os.getenv("BotTOken")
BotUsername:Final = os.getenv("BotUsername")
AdminId:Final = os.getenv("AdminId")
CustomerId:Final =os.getenv("CustomerId")
TransactionId:Final=os.getenv("TransacrionId")
AccountId:Final=os.getenv("AccountId")
ChannelId:Final=os.getenv("ChannelId")
Data="data.json"