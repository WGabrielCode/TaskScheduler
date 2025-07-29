import os
import subprocess
import datetime

Repo_path = os.path.dirname( os.path.abspath( __file__ ) )
#print( os.path.abspath( __file__ ) , "\n" , Repo_path )
Readme_file = os.path.join( Repo_path , "README.md" )
Commit_message = "Commit nr : "

