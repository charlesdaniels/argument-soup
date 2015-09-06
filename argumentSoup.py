class argumentSoup:
	def __init__(this):
		options = {} 

	def addOption(this, name, type, aliases=[], positionals = []):
		# adds a new option to this instance for parsing 

		# name - the name of the option (eg. 'verbose')
		# type - the type of option ('flag' or 'argument') 
		# aliases - list of string aliases for the option (eg. ['v'])
		# positionals - list of dicts containing positional argument information
		# example: [{'name':'targetFile', 'requiredType':None},
		#			{'name':'favoriteNumber', 'requiredType':int}]
		# NOTE: positionals is order-sensitive! 
		# NOTE: 'type' should be the actual class type, eg. int, not 'int' 

		# no return value 

		raise(NotImplementedError)

	def parse(this, toParse):
		# parses the list toParse, which is an order-sensitive list of arguments in
		# the same format as sys.argv

		# eg. ['--verbose','-inputfile foobar.txt']

		# returns a dict containing a list of arguments and flags, as specified
		# in the argument soup spec. 

		# eg. {'flags':'verbose','arguments':{'inputfile':'foobar.txt'}}

		raise(NotImplementedError)