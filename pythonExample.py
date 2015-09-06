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

print(SOUP.parse(['-example', '46', 'bar', '--verbose']))
SOUP.printHelpMessage()