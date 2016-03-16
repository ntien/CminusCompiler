#format of data structure is:
# {"name_of_rule": ["first_rule", "second_rule", ... , "last_rule"], "name..." : [...]}
# format of auxiliary list:
# ["name_of_rule", "name_of_rule", ... , "name_of_rule"] --the index of the name is the rule's number

import re

def put_grammar_into_list():
#This function takes a grammar in BNF notation and turns it into a dictionary, the key being the name of the rule and the value being the right-hand side of the rule. Additionally, this function puts the name of each rule into a list in order, such that the index of the rule in the list corresponds to the rule's number (+1)'''
  filename = raw_input("In what file is your grammar stored? ")
  rules = [] 
  rules_dict = {}
  visited_dict = {} 
  with open(filename, 'r') as f:
    rule = []
    name = ""
    for line in f:
      line = line.replace("\n", "").replace(":", "").replace("|", "").replace("\t", "").replace("  ", " ")
      if re.search('[0-9]+\.', line) is not None:
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
            if item !="" and item !=" ":
              item = item.strip()
              temp.append(item)
          rule.append(temp)
  return rules_dict, rules, visited_dict

#this only checks rules that are called, eventually, by the first rule ("start")
def check_if_pairwise_disjoint(rules_dict):
#This function takes the dictionary of rules and checks that the first terminal of each rule's right-hand-side-rules are different (pairwise disjoint)''' 
#first: build set of all first tokens of each rule and put into dictionary
#then: check that the right-hand-sides of each rule has disjoint sets
  first_tokens_of_each_rule = build_set_of_right_side_terminals(rules_dict, {})
  for key in rules_dict:
    rhs = rules_dict[key] #rhs = right hand side
    terminals = []
    for item in rhs:
      for element in item:
        if is_terminal(element):
          terminals.append(element)   
        else:  
          
           
   first_tokens_of_each_rule = build_set_of_right_side_terminals(rules_dict, start, {})
   print first_tokens_of_each_rule[1]
   return False 

def build_set_of_right_side_terminals(rules_dict, start, terminal_dict):
    right_hand_side = rules_dict[start]
    terminals = []
    for item in right_hand_side:
      if is_terminal(item[0]):
        terminals.append(item[0])
      else:
        nextlevel = build_set_of_right_side_terminals(rules_dict, item[0], terminal_dict)
        #flattened_list = [item for sublist in nextlevel[0] for item in sublist] 
        terminals = terminals + nextlevel[0]
        for key in nextlevel[1]:
          terminal_dict[key] = nextlevel[1][key]
    terminal_dict[start] = terminals
    return terminals, terminal_dict


def is_terminal(token):
    if re.search('[A-Z]', token) is not None:
      return True
    else:
      return False


if __name__=="__main__":
  l = put_grammar_into_list()
  disjoint = check_if_pairwise_disjoint(l[0])















