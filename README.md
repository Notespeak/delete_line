# Delete_line
A very simple python script that allows users to delete a particular file. 
# Installation
1. Download the script
2. chmod +x delete_line.py
3. Add the script to back.rc : ''' echo 'alias delete_line="~/your/path/to/sciptdelete_line.py"' >> ~/.bashrc '''
4. Run '''source ~/.bashrc'''
# Usage
Now you can use the delete_line command to delete a specific line from a file. For example, to delete line 56 from the /Users/example file, you would run:

bash
Copy code
delete_line /Users/example 56
