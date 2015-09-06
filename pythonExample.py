import argumentSoup
import sys 

SOUP = argumentSoup.argumentSoup()
SOUP.addOption("example", 
	"argument", 
	aliases=["ex", "e"], 
	positionals=[{'name':'intOption', 'requiredType':int}], 
	help = "This is an example argument, it does not actually do anything")
SOUP.addOption("verbose", "flag")

print(SOUP.parse(['-example', '46', 'bar', '--verbose']))