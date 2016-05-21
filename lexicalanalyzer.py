
import re
class LexicalAnalyzer():

  def __init__(self, string):
    self.raw = string
    #list of all accepted tokens
    self.reserved = {";":"SEMICOLON",
                        "(":"OPEN_PAREN",
                        ")":"CLOSE_PAREN",
                        "[":"OPEN_BRACKET",
                        "]":"CLOSE_BRACKET",
                        "{":"OPEN_BRACE",
                        "}":"CLOSE_BRACE",
                        "#":"POUND",
                        "*":"STAR|MULT|POINTER",
                        "&":"ADDRESS_OP",
                        "=":"ASSIGN_OP",
                        "==":"EQ_OP",
                        "<=":"LE_OP",
                        ">=":"GE_OP",
                        "<":"L_OP",
                        ">":"G_OP",
                        "!":"NOT",
                        "!=":"NE_OP",
                        "define":"DEFINE",
                        "const":"CONST",
                        "string":"STRING_LITERAL",
                        "int":"INT",
                        "typedef":"TYPEDEF",
                        "void":"VOID",
                        "char":"CHAR",
                        "typename":"TYPE_NAME",
                        "if":"IF",
                        "while":"WHILE",
                        "for":"FOR",
                        "else":"ELSE",
                        "continue":"CONTINUE",
                        "break":"BREAK",
                        "return":"RETURN",
                        "+":"PLUS",
                        "-":"MINUS",
                        "/":"DIVIDE",
                        "%":"MOD",
                        ".":"PERIOD",
                        "++":"INC_OP",
                        "--":"DEC_OP",
                        "": "EPSILON",
                        "tempsizeof": "SIZEOF",
                        "tempid":"IDENTIFIER",
                        "1":"ZERO",
                        ",":"COMMA",
                        "*":"POINTER",
                        "+|-":"PLUSMINUS",
                        "<|>|<=|>=": "L_OPG_OPLE_OPGE_OP",
                        "+":"POS",
                        "-":"NEG",
                        "*|/|%":"MULTDIVIDEMOD",
                        "tempnum":"NUM_CONST",
                        "**":"PTR_OP",
                        "*":"POINTER",
                        "=|!=":"EQ_OPNE_OP",
                        "&&":"AND_OP",
                        "||":"OR_OP",
                        "struct":"STRUCT",
                        "enum":"ENUM"}
    self.literaltable = {} #only used for # DEFINE variables
    self.tokens = []

    self.define = False
    self.defineName = ""
    #pattern match
    #creat symbol table

  def tokenize(self):
      mystring = re.sub("\s+",' ', self.raw).strip()
      word = "" 
      match = False
      unique_id = 0
      i = 0 
      while i < len(mystring)-1:
        letter = mystring[i]
        new = word + letter
        #new should either be a reserved word, a numeric constant, a string literal, or an identifier
        if self.is_valid_token(new):
            match = True
            word = new
            i = i + 1
        else: # new is not valid: adding this letter made a valid token invalid, or didn't change an invalid token
          if letter == " ":
            if match == True:
              #TODO: add token to list 
              if word == "DEFINE":
                self.define = True
              if word in self.literaltable:
                word = self.literaltable[word]
              self.tokens.append(self.create_token(word, unique_id))
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
              self.tokens.append(self.create_token(word, unique_id))
              unique_id = unique_id + 1
              word = ""
              if self.is_valid_token(letter) == False:
                match = False
            else: #adding letter to already invalid word, so keep going
              i = i + 1
              word = new 
              match = False 
      return self.tokens    

  def is_valid_token(self, string):
        if len(string) != "":
          if string in self.reserved:
            return True 
          elif self.is_number(string):
            return True
          elif self.is_id(string):
            return True
          elif self.is_string_literal(string):
            return True
          else:
            return False 
        else:
            print "What"
            return False 

  def create_token(self, string, id_num):
        if string != "":
          if string in self.reserved:
            return (id_num, self.reserved[string], string)

          elif self.is_number(string):
              if self.define == True and len(self.defineName) > 0:
                self.set_defined_var(string, "NUM_CONST")
              #if an identifier came right before this, then this could be its number value
              return (id_num, "NUM_CONST", string)

          elif self.is_id(string):
            if self.define == True:
              self.defineName = string 
            return (id_num, "IDENTIFIER", string)

          elif self.is_string_literal(string):
            if self.define == True and len(self.defineName) > 0:
              self.set_defined_var(string, "STRING_LITERAL") 
            return (id_num, "STRING_LITERAL", string)
          else:
            print "Error! \n"
            print string
            return False
        else:
            print "NO"
            return False 

  def is_number(self, string):
        if re.match("\d+", string) != None and re.match("\d", string[0]) != None:
          for letter in string:
            if re.match("\d+", letter) == None:
              return False
          return True
        else:
            return False

  def is_id(self, string):
        if re.match("[a-zA-Z]", string[0]):
          for letter in string:
            if re.match("\d+", letter) == None and re.match("[a-zA-Z]", letter) == None:
              return False
          return True
        else:
          return False 

  def is_string_literal(self, string):
        if len(string) > 1:  
          if (string[0] == "\'" and string[-1] == "\'") or (string[0] == "\"" and string[-1] == "\""):
            return True
          else:
            return False
        else:
          return False
     
  def set_defined_var(self, string, vartype):
      literaltable[self.defineName] = (string, vartype)
      self.define = False
      self.defineName = ""

if __name__=="__main__":
    f = raw_input("Where is your program?")
    mystring = ""
    with open(f, 'r') as myfile:
      mystring = myfile.read()
    x = LexicalAnalyzer(mystring)
    x.tokenize() 
