import sys
import os

abs_path = os.path.abspath( __file__ )
dir_path = os.path.dirname( abs_path )

newfile_name = "testing.md"
newfile_path = os.path.join( dir_path , newfile_name )
