# DriveTool by Soulf
## What does this program do?

DriveTool extracts metadata from Google documents, even when they're not publicly visible. In the future, I plan to create a program that downloads a document and adds metadata. The resulting document contains metadata, even though it was initially private.

## How to install

1. `Git clone https://github.com/SoulfalProger/DriveTool.git` 
2. `cd drivetool`
3. `pip install -r requirements.txt`
4. `python main.py`

## How to use

1. Go to developers.google.com/oauthplayground
2. Drive API v3 → https://www.googleapis.com/auth/drive.metadata.readonly
3. Authorize APIs → Exchange token
4. Copy and save the access_token

For example you have the document link:
https://drive.google.com/file/d/blabalbalv1blabalbla/view?usp=sharing

blabalbalv1blabalbla <-- This is file ID
