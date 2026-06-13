from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
token = str(input("Enter your token: "))
ACCESS_TOKEN = token
creds = Credentials(token=ACCESS_TOKEN)
service = build('drive', 'v3', credentials=creds)
ID = str(input("Enter file ID: "))
file = service.files().get(
    fileId=ID,
    fields='owners,createdTime,modifiedTime,name'
).execute()

print("File name:", file.get('name'))
print("Owners:", file.get('owners'))
print("Created:", file.get('createdTime'))
print("Edited:", file.get('modifiedTime'))
