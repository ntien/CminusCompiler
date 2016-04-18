#list of all accepted tokens
reserved = {";":"SEMICOLON","(":"OPEN_PAREN",")":"CLOSE_PAREN","[":"OPEN_BRACKET","]":"CLOSE_BRACKET","{":"OPEN_BRACE","}":"CLOSE_BRACE", "#":"POUND","*":"STAR|MULT|POINTER", "&":"ADDRESS_OP", "=":"ASSIGN_OP","==":"EQ_OP", "<=":"LE_OP", ">=":"GE_OP", "<":"L_OP",">":"G_OP","!":"NOT", "!=":"NE_OP", "define":"DEFINE", "const":"CONST", "string":"STRING_LITERAL", "int":"INT", "typedef":"TYPEDEF", "void":"VOID", "char":"CHAR", "typename":"TYPE_NAME", "if":"IF", "while":"WHILE", "for":"FOR", "else":"ELSE", "continue":"CONTINUE", "break":"BREAK", "return":"RETURN", "+":"PLUS", "-":"MINUS", "/":"DIVIDE", "%":"MOD", ".":"PERIOD", "++":"INC_OP","--":"DEC_OP"}


#pattern match
#creat symbol table

import re
def tokenize():
  f = raw_input("Where is your program?")
  with open(f, 'r') as myfile:
    mystring = myfile.read()
  mystring = re.sub("\s+",' ', mystring).strip()
  tokens = []
  word = "" 
  match = False
  unique_id = 0
  i = 0 
  while i < len(mystring)-1:
    letter = mystring[i]
    new = word + letter
    #new should either be a reserved word, a numeric constant, a string literal, or an identifier
    if is_valid_token(new):
        match = True
        word = new
        i = i + 1
    else: # new is not valid: adding this letter made a valid token invalid, or didn't change an invalid token
      if letter == " ":
        if match == True:
          #TODO: add token to list 
          tokens.append(create_token(word, unique_id))
          unique_id = unique_id + 1
          i = i + 1
          word = ""
          match = False
        else:
          print "ERROR :0 \n"
          print new
          i = i + 1
          word = ""
          match = False
      else: #letter is not a space
        if match == True: #the word was valid before the new letter was added, so add old word to tokens
        #and start over
          tokens.append(create_token(word, unique_id))
          unique_id = unique_id + 1
          word = ""
          if is_valid_token(letter) == False:
            match = False
        else: #adding letter to already invalid word, so keep going
          i = i + 1
          word = new 
          match = False 
  return tokens    


def is_valid_token(string):
    if len(string) != "":
      if string in reserved:
        return True 
      elif re.match("\d+", string) != None and re.match("\d", string[0]) != None:
        for letter in string:
          if re.match("\d+", letter) == None:
            return False
        return True
      elif re.match("[a-zA-Z]", string[0]) != None:
        for letter in string:
          if re.match("\d", letter) == None and re.match("[a-zA-Z]", letter) == None:
            return False
        return True
      elif len(string) > 1:
        if (string[0] == "\'" and string[-1] == "\'") or (string[0] == "\"" and string[-1] == "\""):
          return True
        else:
          return False
      else:
        return False
    else:
        print "What"

def create_token(string, id_num):
    if string != "":
      if string in reserved:
        return (id_num, reserved[string], string)
      elif re.match("\d+", string) != None and re.match("\d", string[0]) != None:
        for letter in string:
          if re.match("\d+", letter) == None:
            print "Fourth Error! \n"
            print string
            return False
        return (id_num, "NUM_CONST", string)
      elif re.match("[a-zA-Z]", string[0]):
        for letter in string:
          if re.match("\d+", letter) == None and re.match("[a-zA-Z]", letter) == None:
            print "Fifth Error! \n"
            print string
            return False
        return (id_num, "IDENTIFIER", string)
      elif len(string) > 1:  
        if (string[0] == "\'" and string[-1] == "\'") or (string[0] == "\"" and string[-1] == "\""):
          return (id_num, "STRING_LITERAL", string)
      else:
        print "Sixth Error! \n"
        print string
        return False
    else:
        print "NO"

if __name__=="__main__":
    print tokenize()    
