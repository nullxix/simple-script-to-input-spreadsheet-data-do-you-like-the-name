# Installing (mac)

### run this command
brew install python


### do this
'''bash
function sheet(){
  pushd /path/to/install/dir
  python3 cli.py "$@"
  popd
}
export -f sheet
'''

in either ~/.bash_profile or ~/.zshenv  
(change /path/to/install/dir to match where you cloned this too)

### run this command:
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


### go to this url and click the blue button
https://developers.google.com/sheets/api/quickstart/python

take the 'credentials.json' file, 
save it as 'google-api-credentials.json' in the installation directory (the one with main.py)

# Configure the Spreadsheet

create a config.py file, copy everything from example_config.py into it.
mess around with the properties in there to set up different spreadsheets.

"test" <--- this can be replaced with whatever name you want. You'll use this to call the spreadsheet later
"id" <--- found in the spreadsheet url between /d/ and /edit 

for 
https://docs.google.com/spreadsheets/d/1s11c-vbUR7BLABLABLAAa6RbGVCZ2yII/edit#gid=0  
the id is  
"1s11c-vbUR7BLABLABLAAa6RbGVCZ2yII"  

"tab" <-- there's different tabs at the bottom of the spreadsheet, you copy+paste the tab name for the tab you want to modify.

"columns" <--- used to create the prompts for filling up columns in the spreadsheet. If you have 7 columns you want to fill, this needs 7 strings in it.  

The first time you run the script, you'll be prompted to sign into a google account to give permissions. The account won't like this and will give you scary warnings. Ignore them, the account is weak and cowardly.


# Using

sheet <name> [number-of-rows-to-add>]  

number of rows is optional, default is 1


