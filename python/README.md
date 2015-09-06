# argument soup Python implementation reference 

# Basic usage
## Argv
`argumentSoup.argmentSoup.parse()` accepts a list of strings in the same format as sys.argv, so no special modification is required in order to use argument soup with sys.argv 

## For interactive interpreters 
Argument soup will not extract your commands from user input; you will need to do that and split your input on your own. Here is an example of how this could be accomplished...

```python
while True:
	userInput = input('> ')
	splitInput = userInput.split(userInput) 
	command = splitInput[0] # extract command and store a copy
	splitInput = splitInput[1:] # discard command
	options = argumentSoupInstance.parse(splitInput) # parse options
```

# Data structures 

## `argumentSoup.argumentSoup.addOption()` positional structure
This is used for the `positionals` argument of `addOption()` to specify positional options following an argument. 

`positionals` is a list containing dicts, where each dict contains two fields: `name`, containing the name of the option (used for generation of help messageS), and `requiredType`, which is the class type required as a positional option to the argument. 

**NOTE**: `requiredType` should be an actual class (eg. `int`), NOT a string (eg. `int`)

**NOTE**: you should not add positionals to flags, they will cause argumentSoup to error 

## `argumentSoup.argumentSoup.parse()` return structure 
This is used as the return value for `parse()`. This structure is a dict containing two fields. 

`arguments`, which is a list of lists. Each list in `arguments` contains one or more elements, the first element is always the name of the argument, with each further element being a valid positional option for that argument, cast to it's required type (if any). 

`flags`, which is a list of strings, each being a flag which was detected by argumentSoup. If a flag is not present in `flags`, it was not in the input of `parse()`. 

# Example of usage
```python
import argumentSoup # import the library
argumentSoupInstance = argumentSoup.argumentSoup('myprogramname',"""this is a 
brief description of my program""") # instantiate an argumentSoup instance 
argumentSoupInstance.addOption("verbose", # option name 
	"flag", # type (flag or argument)
	aliases = ["v","verb"], # aliases 
	help = """causes the program to generate verbose output """) # help message
argumentSoupInstance.addOption('inputFile',
	'argument',
	aliases = ['i'],
	positionals = [{'name':'inputFilePath','requiredType':None}],
	help = """Specifies the input file for the application via a single positional argument to '-inputFile'. Example usage: 'myprogram - inputFile /path/to/file'""")
argumentSoupInstance.printHelpMessage() 
```

This gives the output:
```
          myprogramname
 
 
this is a brief description of my program
 
 
--verbose (v, verb)
    causes the program to generate verbose output
-inputFile [inputFilePath] (i)
    Specifies the input file for the application via a single positional
    argument to '-inputFile'. Example usage: 'myprogram - inputFile
    /path/to/file'

```

# Class and function reference 
## `argumentSoup` 
### Constructor
Takes two string arguments, `name`, the name of the program, and `headerMessage`, a brief message describing the program, in that order.

### `def addOption(this, name, optionType, aliases=[], positionals = [],help = ""):`

|argument|expected type|description|default|
|--------|-------------|-----------|-------|
| `name` | string | the name of the option | N/A | 
| `optionType` | string | `'argument'` or `'flag'` indicating the type of option | N/A | 
| `aliases` | list of strings | list of aliases for this option | `[]` |
| `positionals` |  `argumentSoup.argumentSoup.addOption()` positional structure | specifies positional options accepted by this argument, , *must* be empty if `optionType` is `flag` | `[]` | 
| `help` | string | string containing the help message for the argument or flag, note that newlines and whitespace longer than 1 space will be ignored | `""` | 

|return type|description|condition|
|-----------|-----------|---------|
|`None`|N/A|always|

|exceptions|cause| 
|----------|-----|
| `ValueError` | attempted to create a flag which takes a positional option |

Used to add options to the argument soup instance for future parsing. 

### `def resolveAlises(this, toResolve):` 
|argument|expected type|description|default|
|--------|-------------|-----------|-------|
| `toResolve` | list of strings | list of strings in the same format as `sys.argv` which will be scanned for aliases | N/A | 


|return type|description|condition|
|-----------|-----------|---------|
| list of strings | list of strings in the same format as `sys.argv` which has had any aliases replaced with their full names | always |

|exceptions|cause| 
|----------|-----|
| none | N/A | 

Internal function used for resolving aliases, not indented for use outside of `argumentSoup.argumentSoup`.


### `def parse(this, toParse):` 
|argument|expected type|description|default|
|--------|-------------|-----------|-------|
| `toParse` | list of strings | list of strings in the same format as `sys.argv` which will be scanned for aliases | N/A | 


|return type|description|condition|
|-----------|-----------|---------|
| `argumentSoup.argumentSoup.parse()` return structure  | the final output of argument soup | always |

|exceptions|cause| 
|----------|-----|
| `TypeError`| an option was passed with `--`, but is not a flag | 
| `ValueError` | an option was passed with `--` or `-`, but was not found in the `argumentSoup` instance | 
| `TypeError` | an option was passed with `-`, but is not an argument | 

**NOTE**: any exceptions thrown by the class in `requiredType` by also be thrown during typecasting. 

The function which performs the functionality of argument soup. Parses arguments and returns the extracted and appropriately type-casted results thereof. 

### `def printHelpMessage(this):`
|argument|expected type|description|default|
|--------|-------------|-----------|-------|
| | | | |

|return type|description|condition|
|-----------|-----------|---------|
| `None` | N/A | always | 

|exceptions|cause| 
|----------|-----|
| | |

Prints out the help message for the argumentSoup implementation as described by the argument soup spec. 




