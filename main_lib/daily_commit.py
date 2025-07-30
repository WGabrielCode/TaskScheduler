import sys
import os
from collections import deque

abs_path = os.path.abspath( __file__ )
dir_path = os.path.dirname( abs_path )

newfile_name = "testing.md"
newfile_path = os.path.join( dir_path , newfile_name )

def add_to_file( newfile_path , x ,  mode = "a" ) :
	#if not os.path.exists( )
	with open( newfile_path , mode ) as f :
		f.write( x + "\n" )

def new_num() :

	# file does not exist :
	if not os.path.isfile( newfile_path ):
		return 1

	# file does not contain any lines of information
	if os.path.getsize( newfile_path ) == 0 : return 1

	# checking the last number in file
	def get_last_line_deque( filepath ) :
		with open( filepath, 'r' ) as f :
			last_line = deque( f, maxlen = 1 ).pop().strip()
		return last_line

	# outdated
	"""
	def get_last_line_for( filepath ) :
		file = open( newfile_path, "r" )
		for line in file :
			pass
		return line
	"""

	return int( get_last_line_deque(newfile_path).split()[0] ) + 1

add_to_file( newfile_path , str( new_num() ) + " day" )


