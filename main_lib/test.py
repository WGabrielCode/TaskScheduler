import sys
import os

abs_path = os.path.abspath( __file__ )
dir_path = os.path.dirname( abs_path )

newfile_name = "testing.md"
newfile_path = os.path.join( dir_path , newfile_name )

def add_to_file( newfile_path , x ,  mode = "a" ) :
	#if not os.path.exists( )
	with open( newfile_path , mode ) as f :
		f.write( x + "\n" )

def new_num() :
	"""
	if not os.path.isfile( newfile_path ) :
		return 1
	"""
	file = open( newfile_path , "r" )

	if os.path.getsize( newfile_path ) == 0 : return 1

	for line in file :
		pass
	print( int( line.split()[0] ) + 1 )

new_line = str( new_num() ) + " day"

add_to_file( newfile_path , new_line )