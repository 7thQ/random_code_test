what each file does:

rewrite.py - fix scrapped table
filter.py - filter out from the fix scrapped table leaves bank       
test.py - turn key strokes into musical notes
addcolumns.py - Add columns   like phone and email   
google.py - googleApi to build rest of addres              
tojson.py - Convert usable data to format for text
convert.py - music shit         
create_excel.py - test code to make excel sheet      
removeUnknown.py - filters Number column 
telegram_monitor.py - watchs for pnc attempts and adds to json file credentials must run the venv needs the telly python package 
json_watcher.py - watches for data in the credentials file and loads it to the bank mobile app run together with tellgram one but each much be on its own termianl 
telegram_sender.py - send leads to person on telly right now it set up for MR.shelby to Mike larry