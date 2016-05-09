import re
import json
#writing functions to write functions....trop meta! 

def match_define_directive(self):
    currenttoken = stream.get_token()
    if currenttoken == "DEFINE":
      root = "DEFINE"
      return [root, [match_define_type()]
    else:
      return False 
   
def make_concrete_tree_methods(rulesdict):
#This function takes a dictoinary of rules for a grammar, the key being the name of the rule and the value being the right-hand side of the rule, and writes all the rules for generating the Concrete Parse Trees for this grammar (since they follow the same procedure).
  methods = [] 
  '''self argument included because Concrete Parse Tree implemented as class
     also trying to deal with the necessary whitespace in creating these python functions
     how to deal with 0 or more repitions? rule { rule } ???'''
  for key in rulesdict:
    declaration = "  def match_" + key + "(self):"
    rhs = rules_dict[key]
    if len(rhs) > 1:
        #multiple if statements 
    else:
      line1 = " 
        if len(rule) > 0 and len(name) > 0:
          name = name.strip()
          rules.append(name)
          rules_dict[name] = rule
          visited_dict[name] = 0
        name = re.split('[0-9]+\.', line)[1]
        rule = []
      else:
        if line!="" and line!=" ":
          temptemp = line.split(" ")
          temp = []
          for item in temptemp:
            item = item.replace("{","").replace("}","").replace("(","").replace(")","").strip()
            if item !="" and item !=" ":
              temp.append(item)
          if temp !="" and temp != " ":
            rule.append(temp)
    if len(rule) > 0 and len(name) > 0:
      name = name.strip()
      rules.append(name)
      rules_dict[name] = rule
      visited_dict[name] = 0
  return rules_dict, rules, visited_dict

#this only checks rules that are called, eventually, by the first rule ("start")

def check(rules_dict, rules, visited_dict):
  multiple_rules = True
  for i in xrange(len(rules)):
     if is_terminal(rules[i]) == True:
       multiple_rules = False
       return "Only one rule, it appears"
  if not multiple_rules:
    return check_if_pairwise_disjoint(rules_dict, rules[0], visited_dict)



def check_if_pairwise_disjoint(rules_dict, start, visited):
#This function takes the dictionary of rules and checks that the first terminal of each rule's right-hand-side-rules are different (pairwise disjoint)''' 
#first: build set of all first tokens of each rule and put into dictionary
#then: check that the right-hand-sides of each rule has disjoint sets
   terminals = build_terminals_dict(rules_dict, start, {}, visited)
   terminal_dict = terminals[0]
   for key in terminal_dict:
     if len(set(terminal_dict[key])) < len(terminal_dict[key]):
       print key + " has " + str(terminal_dict[key]) + " terminals, which are not disjoint \n" 
   
   filename = raw_input("Where would you like to save the terminal dictionary to?")
   with open(filename, 'w') as f:
     json.dump(terminal_dict, f)
   return False 


def build_terminals_dict(rules_dict, start, terminal_dict, visited):
  thislevel = build_terminals_dict_recurse(rules_dict, start, terminal_dict, visited)
  terminal_dict = thislevel[1]
  visited = thislevel[2]
  count = 0
  for key in visited:
      count += 1
      if visited[key] == 0:
        return build_terminals_dict(rules_dict, key, terminal_dict, visited)
  if count == len(visited):
    return terminal_dict, visited

def build_terminals_dict_recurse(rules_dict, start, terminal_dict, visited):
  rhs = rules_dict[start]
  terminals = []
  if visited[start] != 1:
    visited[start] = 1
    for each_rule in rhs:
      if len(each_rule) > 0:
        first = each_rule[0]
        if is_terminal(first):
          terminals.append(first)
        else:
          recurse = build_terminals_dict_recurse(rules_dict, first, terminal_dict, visited)
          terminals = terminals + recurse[0]
          terminal_dict = merge_dicts(terminal_dict, recurse[1])
          visited = merge_dicts(visited, recurse[2])
    if len(terminals) < 1:
      print start 
    terminal_dict[start] = terminals
  else:
    terminals = terminal_dict[start]
  return terminals, terminal_dict, visited


def merge_dicts(merge_to, merge_from):
  for key in merge_from:
    merge_to[key] = merge_from[key]
  return merge_to

def is_terminal(token):
    if re.search('[A-Z]', token) is not None:
      return True
    else:
      return False


if __name__=="__main__":
  f = raw_input("Where is your rules_dict stored?")
  with open(f, 'r') as myfile:
    mystring = myfile.read()
  rulesdict = eval(mystring) 
  make_concrete_tree_methods(rulesdict)
    














