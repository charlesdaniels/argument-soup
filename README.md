# Project on Hiatus
This project is on indefinite haiatus, and is no longer updated.  

# Introduction
Argument soup is a project to create a consistent, portable, multi-lingual argument parsing library for argv and interactive command shell parsing. The first implementation will be written in python, but I hope to add C, C++, and Java versions in the future. 

The motivation for this library is to create a consistent argument experience between applications, even those written in different language. I am tired of having to read a different help format for every application, and having to remember which programs want `--verbose`, `-v`, `--v`, `verbose`, and so on. 

# Specification
## Introduction
This section contains a technical specification for an argumentSoup compliant implementation. 

## Overview 
Argument soup will look for two types of options in an argv array (or split string), `arguments` and `flags`.

`flags` always begin with `--`, and may be up to 253 characters in length (but no less than one character in length), excluding the leading `--`. Flags are followed by exactly zero positional options, and always toggle a boolean option from False to True. For example, `--verbose` is a valid flag. `--foo` would toggle the value `foo` from False to True, and `--foo bar` would be interpreted the same as `--foo`. 

`arguments` always begin with `-`, and may be up to 254 characters in length, but no less than one character in length, excluding the `-`. Arguments may be followed by one or more positional options. The argumentSoup implementation should provide a method by which to specify the minimum and maximum number of positional options for an argument, as well as the type of each positional option (int, float, string, etc.). 

`positional options` follow arguments, and are order-sensitive and space-delineated. Positional options may be up to 255 characters in length, but no less than one character in length. Positional options not preceded by an argument, or preceded by an argument which has already consumed it's maximum number of positional arguments are ignored and discarded. 

## Examples 

|input|output|
|-----|------|
| '--verbose' | verbose=True | 
| '-intValue 7' | intValue = 7 | 
| '-inputFile /foo/bar -twoFloats 6.7 9.0 --verbose' | inputFile = '/foo/bar', twoFloats = [6.7,9.0], verbose=True| 

## Aliases 
All implementations should have a method by which to specify aliases, for example aliasing `v` to `verbose`. 

## Help message generation 
All implementations should have a method by which to generate and print a help message. A help message begins with a title, which may be up to 255 characters in length, and a header message, which may be up to 8192 characters in length. The title should be centered, with each line being 60 characters long, preceded and succeeded by 10 characters of whitespace. The title should be followed by two lines of whitespace, then the header message should be printed, left aligned, with each line being 80 characters in length or less. 

The header message should be followed by two lines of whitespace, then documentation for all flags and arguments. Flags and argument should be printed sequentially, sorted alphabetically, and separated by one line of whitespace. Said documentation should not exceed 80 characters in width. Documentation strings should not exceed 8192 characters in length. 

Option documentation begins with one or more lines containing...

* the argument or flag, including preceding `-` or `--`
* a list of positional options, separated by spaces. Option names are surrounded by brackets (`[]`). Options of a specific type are preceded by that type and a colon (eg. `int:`, `float:`) 
* documentation strings begin on the next line, and are indented by four spaces. Documentation strings are left-aligned, and do not exceed 80 characters per line, including indent. 
* positional options are referred to like `[option]` within documentation strings. It is acceptable to leave out type specifiers like `int:` from the documentation strings. (note that this point is convention, and is not enforced by argument soup)

### Example
```
         my really cool program


This is my really cool program. This is a header message, where I explain all
the neat things that my programs can do. In this space, I can use up to 8192
characters for this purpose 


--verbose (v, aliasForVerbose)
    Makes the program display verbose output. Note how the documentation string
    is left justified, indented by one tab (4 spaces), and is no more than 80
    characters in length, including said tab. 

-someargument [option] int:[integer option] (s, sa, aliasForArgument)
	This argument gives my program an option, which is referred to in this
	documentation string as [option]. Argument soup will error if 
	[integer option] is not an integer. Notice how [integer option] is not
	wrapped even though it contains a space. Also notice how we can leave out 
	the "int:" in the documentation string. 
```

## Language specific differences 
As every programming language is different, argument soup implementations are allowed the following freedoms to make porting easier...

* arguments may be limited one positional option, if desired (to avoid having to use arbitrarily sized lists for results) 
* implementations may support any or no type specifiers 
* argument, flag, and other string lengths with explicitly defined limits may be permitted larger sizes if desired, so long as they support at least the size specified (eg. documentation strings can be arbitrarily long, so long as they support at least 8192 characters). 
* additional features may be added on a per-implementation basis, so long as the previous described features are preserved
* implementations may expose parsing results through any means desired (eg. hash table, pointers, etc.) 
* no specific form of logging, error handling, or exception handling is required
