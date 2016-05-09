#format of data structure is:
# {"name_of_rule": ["first_rule", "second_rule", ... , "last_rule"], "name..." : [...]}
# format of auxiliary list:
# ["name_of_rule", "name_of_rule", ... , "name_of_rule"] --the index of the name is the rule's number

import re
import json


def build_concrete_trees(rules_dict, start, visited, trees):
  visited[start] = 1
  trees = expand_root(rules_dict, start, visited)
  count = 0
  for key in visited:
    if visited[key] == 1:
        count += 1
        #print expand_root(rules_dict, key, visited, trees)
  if count < len(visited):
    print trees 
  else:
    return trees 

def expand_root(rules_dict, root, visited):
    if is_nonterminal(root) == True: # 'a'..................... ..b
        rhs = rules_dict[root] #[.,[b,B],.].......................[[C],[D]]
        visited[root] = 1 #a visited..............................b visited
        expanded = [] # [[a,[[b,[C]],B]],[a[[b,[D]],B]]...........[[b,[C]],[b,[D]]]
        for rule in rhs: # [.],[b,B],[.]..........................[C],[D] 
          expandedrule = []
          for value in rule:# b, B................................C,D
            if is_nonterminal(value) == True: #b(True), B(False...C(False),D(False)
              tree = expand_root(rules_dict, value, visited) #b --> [[b,[C]],[b,[D]]]
              if value == "b":
                print tree 
              #if expandedrule already has something in it (let's say a terminal character)
              orig = expandedrule
              if len(expandedrule) > 0:
                expandedrule = []
                for expanded_thing in tree:#[b,[C]], [b,[D]]
                  expandedrule = expandedrule + origtree.append(expanded_thing)
              else: #nothing before this rule/flattree is empty
                for expanded_thing in tree: #[C],[D]
                  expandedrule.append(expanded_thing)
            else: # the value is a Terminal........................[C],[D]
              print value
              if len(expandedrule) > 0: #flat tree there for a reason
                orig = expandedrule
                expandedrulel.append(orig.append(value))
                for thing in orig:
                  flattree = flattree + orig.append(value)
                  
          print flattree
          expanded.append(flattree) #[C],[D] ... expanded = [[C],[D]]....[B]
        trees = []
        for child in expanded:
          tree = [root] #'b'
          tree.append(child) #[b,[C]]...[[b,[D]]
          trees.append(tree)
        return trees
    else:
        #print "terminal"
        #print root
        return root

def is_nonterminal(token):
    if re.search('[a-z]', token) is not None:
      return True
    else:
      return False

if __name__=="__main__":
  name = raw_input("Where is the complete dictionary of rules and their right hand sides saved?")
  with open(name, 'r') as f:
    rules_dict = eval(f.read())
            expandedrule.append(orig.append(value))
  visited = {}
  for key in rules_dict:
    visited[key] = 0
  start = raw_input("What is the name of the topmost rule in your grammar?")
  trees = build_concrete_trees(rules_dict, start, visited, [])
  #print "results: "
  #for l in trees: print l











