#Take a grammar in BNF notation and turn into a list of lists
# such that each item in the list has the index number corresponding to its rule number,
# and the first item (list of lists) has as its first item the name of the rule, and followed by the 
# rules, e.g. [[type_specifier, INT, CHAR, VOID], [type_qualifier, CONST]] 
#TODO: would it be preferable to implement this as a list of dictionaries? E.g. 
# [{"number": 1, "name": type_specifier, "rules": INT, CHAR, VOID}, {....}] 
# How would this affect checking for pairwise disjointness (might take longer)
import re

def put_grammar_into_list():
  filename = raw_input("In what file is your grammar stored? ")
  rules = [] 
  rules_dict = {}
  with open(filename, 'r') as f:
    rule = []
    name = ""
    for line in f:
      line = line.replace("\n", "").replace(":", "").replace("|", "").replace("\t", "").replace("  ", " ")
      if re.search('[0-9]+\.', line) is not None:
        if len(rule) > 0 and len(name) > 0:
          rules.append(name)
          rules_dict[name] = rule 
          rule.append(re.split('[0-9]+\.', line)[1])
      else:
        if line!="" and line!=" ":
          rule.append(line)
          value.append(line)
  return rules_dict
  #new_filename = raw_input("Where would you like to store the grammar (now in list format)?")
  #with open(new_filename, 'w') as f:
  #  f.write(str(rules))


def check_if_pairwise_disjoint(l):
   print l     
   expanded_list = [] 

   return False 

if __name__=="__main__":
  l = put_grammar_into_list()
  disjoint = check_if_pairwise_disjoint(l)
  print disjoint  















