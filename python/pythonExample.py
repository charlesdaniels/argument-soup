import argumentSoup
import sys 

SOUP = argumentSoup.argumentSoup("example argument soup", """ an example program
	used to demonstrate the functionality of the argument soup Python, 
	does not actually do anything at all""")
SOUP.addOption("example", 
	"argument", 
	aliases=["ex", "e"], 
	positionals=[{'name':'intOption', 'requiredType':int}], 
	help = "This is an example argument, it does not actually do anything")
SOUP.addOption("verbose", "flag")
SOUP.addOption('help', 'flag', help="""This command causes the help message to
	printed. It has a relatively long help message, to demonstrate and test
	correct line wrapping behavior for help text generation""", aliases=['h'])

parsedArguments = SOUP.parse(sys.argv)
if 'help' in parsedArguments['flags']:
	SOUP.printHelpMessage()

print(sys.argv)
print("argument soup parsed sys.argv like this: ", parsedArguments)