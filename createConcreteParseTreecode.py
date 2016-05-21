import re
import json
#writing functions to write functions....trop meta! 

'''
Example1: (a grammar rule with a single rule in its RHS) 

rule:
define_directive
	: POUND DEFINE IDENTIFIER define_type 

function that should match this rule:
def match_define_directive(self):
    root = "define_directive"
    children = []
    children.append(match_pound()).append(match_define()).append(match_id()).append(match_define_type())
    return [root, children] 
'''

'''
think about terminals and nonterminals, when to update current token
Example2: (a grammar rule with multiple rules in its RHS)

rule:
4. define_type
	: NUM_CONST
	| STRING_LITERAL

function:
def match_define_type(self):
    root = "define_type"
    chidlren = []
    if currenttoken == "NUM_CONST":
        children.append(match_num_const())
    elif currenttoken == "STR_LIT":
        children.append(match_str_lit())
    return [root, children]


rule:
8. function_definition
	: declaration_list compound_statement
	| compound_statement

function:

def match_function_definition(self):
    root = "function_definition"
    children = []
    if currenttoken in terminaldict["declaration_list"]:
        children.append(match_declaration_list()).append(match_compound_statement())
    elif currenttoken in terminaldict["compound_statement"]
        children.append(match_compound_statement())
    return [root, children] 
'''

def make_concrete_tree_methods(reservedwords_dict, rulesdict):
#This function takes a dictoinary of rules for a grammar, the key being the name of the rule and the value being the right-hand side of the rule, and writes all the rules for generating the Concrete Parse Trees for this grammar (since they follow the same procedure).
  methods = [] 
  '''self argument included because Concrete Parse Tree implemented as class
     also trying to deal with the necessary whitespace in creating these python functions
     how to deal with 0 or more repitions? rule { rule } ???'''
  for key in rulesdict:
    thismethod = []
    rhs = rulesdict[key]
    whitespace = "  " 
    declaration = whitespace + "def match_" + key + "(self): \n"
    root = whitespace + whitespace + "root = \"" + key + "\" \n" 
    line1 = whitespace + whitespace + "children = [] \n"
    returnline = whitespace + whitespace + "return [root, children] \n"
    if len(rhs) > 1:
      #multiple rules (and thus, multiple if statements) --> rhs = [[rule1],[rule2],[rule3]]
      lines = []
      for line  in rhs:
        if is_terminal(line[0]):
          lines.append(whitespace + whitespace + "elif currenttoken == \"" + line[0]  +"\": \n")
          childrenline = whitespace + whitespace + whitespace + "children"
          for rule in line:
              if is_terminal(rule):
                terminalname = rule.lower()
                childrenline = childrenline + ".append(self.match_" + terminalname + "())" #TODO 
              else:
                childrenline = childrenline + ".append(self.match_" + rule  + "())" #TODO 
          lines.append(childrenline)
          lines.append("\n")
        else:
          lines.append(whitespace + whitespace + "elif currenttoken in terminaldict[\"" + line[0] + "\"]: \n")
          childrenline = whitespace + whitespace + whitespace + "children"
          for rule in line:
              if is_terminal(rule):
                terminalname = rule.lower()
                childrenline = childrenline + ".append(self.match_" + terminalname + "())" #TODO 
              else:
                childrenline = childrenline + ".append(self.match_" + rule  + "())" #TODO 
          childrenline = childrenline + "\n"
          lines.append(childrenline)
      thismethod.append(declaration)
      thismethod.append(root)
      thismethod.append(line1)
      thismethod.append(lines)
      thismethod.append(returnline)  
      thismethod.append("\n")
      methods.append(thismethod)
    else:
        #rhs = [[rule1]], e.g. rule1 = ["this", "that", "the", "other"] 
      rhs = rhs[0]
      childrenline = whitespace + whitespace + "children"
      #children.append(...all the match rules 
      for rule in rhs:
        if is_terminal(rule):
          terminalname = rule.lower()
          childrenline = childrenline + ".append(self.match_" + terminalname + "())" #TODO 
          #add the the currenttoken/rule to the (check that it matches?) and update
        else:
          childrenline = childrenline + ".append(self.match_" + rule + "())"
      childrenline = childrenline + "\n"
      thismethod.append(declaration)
      thismethod.append(root)
      thismethod.append(line1)
      thismethod.append(childrenline)
      thismethod.append(returnline)  
      thismethod.append("\n")
      methods.append(thismethod)
  return methods  
      
def is_terminal(token):
    if re.search('[A-Z]', token) is not None:
      return True
    else:
      return False

def write_methods_for_reservedwords(reserved):
  methods = []
  for key in reserved:
    thismethod = []
    name = key.lower()
    thismethod = []
    whitespace = "  " 
    declaration = whitespace + "def match_" + name + "(self): \n"
    leaf = whitespace + whitespace + "leaf = [] \n"
    ifstatement = whitespace + whitespace + "if currenttoken == \"" + key +"\": \n"
    elsestatement = whitespace + whitespace + "else: \n"
    ifbody = whitespace + whitespace + whitespace + "currenttoken = self.get_token() \n"
    returntrue = whitespace + whitespace + whitespace + "return [\"" + key + "\"] \n"
    returnfalse = whitespace + whitespace + whitespace + "print \" Error! Unexpected token\" + currenttoken \n" + whitespace + whitespace + whitespace + "return False \n \n"
    thismethod.append(declaration)
    thismethod.append(leaf)
    thismethod.append(ifstatement)
    thismethod.append(ifbody)
    thismethod.append(returntrue)
    thismethod.append(elsestatement)
    thismethod.append(returnfalse)
    methods.append(thismethod)
  return methods 
   
def write_list_of_methods_to_file(methodslist, reservedmethods): 
    f = raw_input("Where do you want to write this file?")
    with open(f, 'w') as myfile:
        openingstring = "#Tree structure: [root, [child, child]] \nclass ConcreteParseTree(stringstream, mydict):\n  terminaldict = mydict\n  currenttoken = self.get_token() \n \n" 
        myfile.write(openingstring)
        for item in reservedmethods:
            if isinstance(item, list): 
              for rule in item:
                myfile.write(rule)
        for item in methods:
          if isinstance(item, list):
            for rule in item:
              if isinstance(rule, list):
                for thing in rule:
                  myfile.write(thing)
              else:
                myfile.write(rule)
          else:
            myfile.write(item)
        closingstring = "\n \nfrom lexicalanalyzer import LexicalAnalyzer\nif __name__ == \"__main__\":\n  f = raw_input(\"Where is your program?\")\n  with open(f, 'r') as myfile:\n    mystring = myfile.read()\n  x = LexicalAnalyzer(mystring)\n  tokens = x.tokenize()\n  dictname = raw_input(\"Where is the terminal dictionary stored?\")\n  terminaldict = {}\n  with open(dictname, 'r'):\n    terminaldict = eval(dictname.read())\n  ParseTree = ConcreteParseTree(tokens, terminaldict)\n  ParseTree.match_translation_unit()\n  return \"done\""
        myfile.write(closingstring)
        return "done"        

from lexicalanalyzer import LexicalAnalyzer
if __name__=="__main__":
  mystring = "empty string"
  x = LexicalAnalyzer(mystring)
  reserved = {}
  temp = x.reserved
  for key in temp:
    reserved[temp[key]] = key 
  
  #f = raw_input("Where is your rules dict stored?")
  f = "rulesdict.txt"
  with open(f, 'r') as myfile:
    mystring = myfile.read()
  rulesdict = eval(mystring) 
  methods = make_concrete_tree_methods(reserved, rulesdict)
  reservedmethods = write_methods_for_reservedwords(reserved)
  write_list_of_methods_to_file(methods, reservedmethods) 














