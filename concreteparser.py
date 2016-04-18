import shlex 
keywords = ["POUND", "DEFINE", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", "POS", "NEG", "ADDRESS_OP", "POINTER", "INC_OP", "DEC_OP", "MULT", "DIVIDE", "MOD", "NOT", "SIZEOF", "IF", "WHILE", "RETURN", "CONTINUE", "BREAK", "SEMICOLON", "IDENTIFIER", "CONSTANT", "STRING_LITERAL"
reserved = ["#", "DEFINE", "(", ")", "{", "}", "+", "-", "*", "TYPEDEF",   

#Tree structure: [root, [child, child]]

class ConcreteParseTree(stringstream, mydict):
  stream = shlex.shlex(stringstream) 
  terminaldict = mydict
  currenttoken = stream.get_token()

  def match_translation_unit(self):
    root = "translation_unit"
    child = match_compiler_or_external_declaration()
    if currenttoken != "":
        match_translation_unit()
    else:
        return [root, [child]]



  def  match_compiler_or_external_declaration(self):
    if currenttoken == "#":
        root = "#"
        return [root, [match_define_directive()]]
    elif currenttoken in terminaldict["external_declaration"]:
        root = "external_declaration"
        return [root, [match_external_declaration()]]
    else:
        return False 
    
  def match_define_directive(self):
    currenttoken = stream.get_token()
    if currenttoken == "DEFINE":
      root = "DEFINE"
      return [root, [match_define_type()]
    else:
      return False 
    
  def match_define_type(self):
    #if stream.get_token() == "CONST":
      #If define directive is finished, should call translation unit again?
    #elif stream.get_token() == "STRING_LITERAL":
    currenttoken = stream.get_token()
    if currenttoken == "CONST":
        leaf = "CONST"
        currenttoken = stream.get_token()
        return [leaf]
    elif currenttoken == "STRING_LITERAL":
        leaf = "STRING_LITERAL"
        currenttoken = stream.get_token()
        return [leaf]
    else:
      return False   


  def match_external_declaration(self):
    if currenttoken in terminaldict["type_specifier"]:
        match_type_specifier()
        match_external_next()
    elif currenttoken in terminaldict["choose_declarator"]:
        match_choose_declarator()
        match_function_definition()
    elif currenttoken in terminaldict["type_qualifier"]:
        match_type_qualifier()
        match_type_specifier()
        match_init_declarator_list()
        match_semicolon()
        match_possible_declaration_specifiers_and_semicolon()
    elif currenttoken == "TYPEDEF":
        #possibly need to update token here
        currenttoken = stream.get_token()
        match_type_specifier()
        match_semicolon()
        match_possible_declaration_specifiers_and_semicolon()
    else:
        return False  

  def match_type_qualifier_specifier(self):
    if currenttoken in terminaldict["type_qualifier"]:
      match_type_qualifier()
      match_type_specifier()
    elif currenttoken in terminaldict["type_specifier"]:
      match_type_specifier()
    else:
      return False 


  def match_type_specifier(self)
    if currenttoken == "VOID":
        currenttoken = stream.get_token()
    elif currenttoken == "CHAR":
        currenttoken = stream.get_token()
    elif currenttoken == "INT":
        currenttoken = stream.get_token()
    elif currenttoken == "TYPE_NAME":
        currenttoken = stream.get_token()
    elif currenttoken in terminaldict["struct_specifier"]:
        currenttoken = stream.get_token()
    else:
      return False

  def match_external_next(self):
    if currenttoken in terminaldict["choose_declarator"]:
        match_choose_declarator()
        match_external_next2()
    else:
        return False

  def match_external_next2(self):
    if currenttoken in terminaldict["external_init_declarator"]:
        match_external_init_declarator_list()
        match_semicolon()
        match_possible_declaration_specifiers_and_semicolon()
    elif currenttoken in terminaldict["function_definition"]:
        match_function_definition()
    else:
        return False

  def match_external_init_declarator_list(self):
    if currenttoken in terminaldict["init_declarator"]:
        match_init_declarator()
        match_possible_comma_choose_declarator_init_declarator()
    else:
        return False

  def match_choose_declarator(self):
    if currenttoken in terminaldict["choose_declarator_next"]:
        match_choose_declarator_next()
    elif currenttoken == "IDENTIFIER":
        currenttoken = stream.get_token()
    else:
        currenttoken == stream.get_token()
          
  def match_choose_declarator_next(self):
    if currenttoken == "(":
      currenttoken = stream.get_token()
      match_choose_declarator_next1()
    elif currenttoken == "[":
      currenttoken = stream.get_token()
      match_choose_declarator_next2()
    else:
      return False 

  def match_choose_declarator_next1(self):
    if currenttoken == ")":
      currenttoken = stream.get_token()
      match_choose_declarator_next3()
    elif currenttoken in terminaldict["parameter_list"]:
        match_parameter_list()
        match_close_paren()
        match_choose_declarator_next3()
    elif currenttoken in terminaldict["pointer"]:
        match_pointer()
        match_choose_declarator()
        match_close_paren()
    elif currenttoken in terminaldict["identifier_list"]:
        match_identifier_list()
        match_close_paren()
        match_choose_declarator()

  
  def match_choose_declarator_next2(self):
    if currenttoken in terminaldict["logical_or_expression"]:
      match_logicial_or_expression()
      match_close_bracket()
      match_choose_declarator_next3()
    elif currenttoken in "]":
      currenttoken = stream.get_token()
      match_choose_declarator_next3()

  def match_choose_declarator_next3(self):
    if currenttoken in terminaldict["choose_declarator"]:
      match_choose_declarator()
      match_possible_direct_declarator_next()
    else:
      return False    


  def match_function_definition(self):
    if currenttoken in terminaldict["declaration_list"]:
        match_declaration_list()
        match_compound_statement()
    elif currenttoken in terminaldict["compound_statement"]:
        match_compound_statement()
    else:
        return False

  def match_type_qualifier(self):
    if currenttoken == "CONST":
      currenttoken = stream.get_token()
    else:
      return False

  def match_init_declarator_list(self):
    if currenttoken in terminaldict["choose_declarator"]:
      match_choose_declarator()
      match_init_declarator()
      match_possible_comma_choose_declarator_init_declarator()
    else:
      return False
  
  def match_init_declarator(self):
    if currenttoken == "=":
        currenttoken = stream.get_token()
        match_initializer()
    else:
        currenttoken = stream.get_token()

  def match_initializer(self):
    if currenttoken in terminaldict["assignment_expression"]:
      match_assignment_expression()
    elif currenttoken == "[":
      currenttoken = stream.get_token():
      match_zero()
      match_close_brace()
    else:
      return False
    
  def match_semicolon(self):
    if currenttoken == ";":
        currenttoken = stream.get_token()
    else:
        return False

  def match_possible_declaration_specifiers_and_semicolon(self):
    # {declaration_specifiers SEMICOLON }
    if currenttoken in terminaldict["declaration_specifiers"]:
        match_declaration_specifiers()
        match_semicolon()
        match_possible_declaration_specifiers_and_semicolon()
    else:
        currenttoken = stream.get_token() 

  def match_possible_comma_choose_declarator_init_declarator(self):
    # { COMMA choose_declarator init_declarator }
    if currenttoken in ",":
        match_choose_declarator()
        match_init_declarator()
        match_possible_comma_choose_declarator_init_declarator()
    else:
        currenttoken = stream.get_token() 

  def match_pointer(self):
    if currenttoken == "*":
        currenttoken = stream.get_token()
        match_pointer_next()
    else:
        return False

  def match_pointer_next(self):
    if currenttoken in terminaldict["type_qualifier"]:
      match_type_qualifier()
      match_optional_pointer()
    elif currenttoken in terminaldict["pointer"]:
       match_pointer() 
    else:
        currenttoken = stream.get_token()

  def match_optional_pointer(self):
    if currenttoken in terminaldict["pointer"]:
      match_pointer()
    else:
      currenttoken = stream.get_token()
  
  def match_parameter_list(self):
    if currenttoken in terminaldict["parameter_declaration"]:
        match_parameter_declaration()
        match_possible_comma_parameter_declaration()
    else:
        return False

  def match_parameter_declaration(self):
    if currenttoken in terminaldict["declaration_specifiers"]:
        match_declaration_specifiers()
        match_parameter_declaration_next()
    else:
        return False

  def match_possible_comma_parameter_declaration(self):
    # { COMMA parameter_declaration }


  def parameter_declaration_next(self):
    if currenttoken in terminaldict["pointer"]:
      match_pointer()
      match_choose_declarator()
    else:
      currenttoken = stream.get_token()

  def match_identifier_list(self):
    if currenttoken = "IDENTIFIER":
        currenttoken = stream.get_token()
        match_possible_comma_id()
    else:
        return False

  def match_possible_comma_id(self):
    # { COMMA IDENTIFIER }
    if currenttoken == ",":
        currenttoken = stream.get_token()
        match_id()
        match_possible_comma_id()
    else:
        currenttoken = stream.get_token()
	
  def match_zero(self):
    if currenttoken == "0":
        currenttoken = stream.get_token()
    else:
        return False


  def match_close_brace(self):
    if currenttoken == "}":
        currenttoken = stream.get_token()
    else:
        return False

  def match_close_paren(self):
    if currenttoken == ")":
        currenttoken = stream.get_token()
    else:
        return False

  #TODO
  def match_id(self):

  def match_possible_direct_declarator_next()
    # { direct_declarator_next }
    if currenttoken in terminaldict["direct_declarator_next"]:
      match_direct_declarator_next()
      match_possible_direct_declarator_next()
    else:
        currenttoken = stream.get_token()
  
  def match_assignment_expression(self):
    if currenttoken in terminaldict["unary_expression"]:
        match_unary_expression()
    else:
        return False

  def match_possible_eq_assignment_expression(self):
    # { EQ_OP assignment_expression }
    if currenttoken == "=":
        currenttoken = stream.get_token()
        match_assignment_expression()
        match_possible_eq_assignment_expression()
    else:
        currenttoken = stream.get_token()
	
  def match_declaration_specifiers(self):
    if currenttoken in terminaldict["type_qualifier_specifier"]:
      match_type_qualifier_specifier()
      match_init_declarator_list()
    elif currenttoken == "TYPEDEF":
      currenttoken = stream.get_token()
      match_type_specifier()
    else:
      return False

  def match_direct_declarator_next(self):
    if currenttoken == "IDENTIFIER":
        currenttoken = stream.get_token()
    elif currenttoken == "(":
        currenttoken = stream.get_token()
        match_direct_declarator_next1()
    elif currenttoken == "[":
        currenttoken = stream.get_token()
        match_direct_declarator_next2()
    else:
        return False

  def match_direct_declarator_next1(self):    
    if currenttoken in terminaldict["pointer"]:
        match_pointer()
        match_direct_declarator()
        match_close_paren()
    elif currenttoken in terminaldict["parameter_list"]:
        match_parameter_list()
        match_close_paren()
        match_direct_declarator()
    elif currenttoken in terminaldict["identifier_list"]:
        match_identifier_list()
        match_close_paren()
        match_direct_declarator()
    elif currenttoken == ")":
        currenttoken = stream.get_token()
        match_direct_declarator()
    else:
        return False

  def match_direct_declarator_next2(self):
    if currenttoken in terminaldict["logical_or_expression"]:
        match_logical_or_expression()
        match_close_bracket()
        match_direct_declarator()
    elif currenttoken == "]":
        currenttoken = stream.get_token()
        match_direct_declarator()
    else:
        return False

  def match_unary_expression(self):
    if currenttoken in terminaldict["postfix_expression"]:
        match_postfix_expression()
    elif currenttoken == "+":
        currenttoken = stream.get_token()
        match_unary_expression()
    elif currenttoken == "-":
        currenttoken = stream.get_token()
        match_unary_expression()
    elif currenttoken in terminaldict["match_unary_operator"]:
        match_unary_operator()
        match_unary_expression()
    elif currenttoken == "SIZEOF":
        currenttoken = stream.get_token()
        match_unary_expression_sizeof()
    else: 
        return False 

  def match_postfix_expression(self):
    if currenttoken in terminaldict["primary_expression"]:
      match_primary_expression()
      match_possible_postfix_expression_next()
    else:
      return False   

  def match_unary_operator(self):
    if  currenttoken == "&":
        currenttoken = stream.get_token()
    elif currenttoken == "*":
        currenttoken = stream.get_token()
    elif currenttoken == "+":
        currenttoken = stream.get_token()
    elif currenttoken == "-":
        currenttoken = stream.get_token()
    elif currenttoken == "!":
        currenttoken = stream.get_token()
    else:
        return False
	

  def match_unary_expression_sizeof(self): 
    if currenttoken == "(":
        currenttoken = stream.get_token()
        match_unary_expression_sizeof_cont()
    else:
        return False

  def match_unary_expression_sizeof_cont(self):
    if currenttoken in terminaldict["type_specifier"]:
        match_type_specifier()
        match_close_paren()
    elif currenttoken == "IDENTIFIER":
        currenttoken = stream.get_token()
        match_close_paren()
    else:
        return False

  def match_primary_expression()
    if currenttoken == "IDENTIFIER":
        currenttoken = stream.get_token()
    elif currenttoken == "CONST":
        currenttoken = stream.get_token()
    elif currenttoken == "STRING_LITERAL":
        currenttoken = stream.get_token()
    elif currenttoken == "(":
        currenttoken = stream.get_token()
        match_expression()
        match_close_paren()
    else:
        return False 
    
  def match_possible_postfix_expression_next(self):
    # { postfix__expression_next }
    if currenttoken in terminaldict["post_expression_next"]:
        match_postfix_expression_next()
        match_possible_postfix_expression_next()

  def match_postfix_expression_next(self):
    if currenttoken == "[":
        currenttoken = stream.get_token()
        match_expression()
        match_close_bracket()
    elif currenttoken == "(":
        currenttoken = stream.get_token()
        match_postfix_expression_next_brace()
    elif currenttoken == ".":
        currenttoken = stream.get_token()
        match_id()
    elif currenttoken == "*":
        currenttoken = stream.get_token()
        match_id()
    elif currenttoken == "+":
        currenttoken = stream.get_token()
    elif currenttoken == "-":
        currenttoken = stream.get_token()
    else:
        return False 
  
  def match_postfix_expression_next_brace(self):
    if currenttoken == ")":
        currenttoken = stream.get_token()
    elif currenttoken in terminaldict["argument_expression_list"]:
	    match_argument_expression_list()
        match_close_paren()
    else:
        return False 

  def match_argument_expression_list(self):
    if currenttoken in terminaldict["assignment_expression"]:
        match_possible_comma_assignment_expression()
    else:
        return False

  def match_assignment_expression(self):


  def match_possible_comma_assignment_expression(self):
    #{ COMMA assignment_expression }



  def match_compound_statement(self):

if __name__ == "__main__"
  filename = raw_input("Where is your program stored?")
  myfile = open(name, "r")
  stream = myfile.read()
  myfile.close()
  dictname = raw_input("Where is the terminal dictionary stored?")
  myfile = open(dictname, "r")
  mydict = myfile.read()
  myfile.close()
  acceptor = Acceptor(stream, mydict)
  acceptor.match_translation_unit()
