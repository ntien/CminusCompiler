#Tree structure: [root, [child, child]] 
class ConcreteParseTree(tokens, mydict):
  self.symboltabe = {} 
  self.terminaldict = mydict
  self.stream = tokens 
  #structure of tokens:
  #[(id_num, "ID", string),(id_num, "STR_LIT", string),(id_num, reserved_word, string)]
  self.currenttoken = self.stream[0] #need to start here
  self.index = 1 #since currenttoken has already been initalized at self.stream[0]
  self.id_to_define = ''
  self.id_type = ''
  self.id_value = ''

  def get_token(self):
    self.currenttoken = self.stream[index]
    self.index += 1

  def reset_id(self):
    self.id_to_define = ''    
    self.id_type = ''
    self.id_value = ''

  def match_close_bracket(self): 
    if self.currenttoken[1] == "CLOSE_BRACKET": 
      self.get_token() 
      return ["CLOSE_BRACKET"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_const(self): 
    if self.currenttoken[1] == "CONST": 
      self.get_token() 
      return ["CONST"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_dec_op(self): 
    if self.currenttoken[1] == "DEC_OP": 
      self.get_token() 
      return ["DEC_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_neg(self): 
    if self.currenttoken[1] == "NEG": 
      self.get_token() 
      return ["NEG"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_void(self): 
    if self.currenttoken[1] == "VOID": 
      self.get_token() 
      return ["VOID"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_open_bracket(self): 
    if self.currenttoken[1] == "OPEN_BRACKET": 
      self.get_token() 
      return ["OPEN_BRACKET"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_char(self): 
    if self.currenttoken[1] == "CHAR": 
      self.get_token() 
      return ["CHAR"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_inc_op(self): 
    if self.currenttoken[1] == "INC_OP": 
      self.get_token() 
      return ["INC_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_while(self): 
    if self.currenttoken[1] == "WHILE": 
      self.get_token() 
      return ["WHILE"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 

  def match_eq_op(self): 
    if self.currenttoken[1] == "EQ_OP": 
      self.get_token() 
      return ["EQ_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_lop_gop_leop_geop(self): 
    if self.currenttoken[1] == "L_OP": 
      self.get_token() 
      return ["L_OP"] 
    elif self.currenttoken[1] == "G_OP": 
      self.get_token() 
      return ["G_OP"] 
    elif self.currenttoken[1] == "LE_OP": 
      self.get_token() 
      return ["LE_OP"] 
    elif self.currenttoken[1] == "GE_OP": 
      self.get_token() 
      return ["GE_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_return(self): 
    if self.currenttoken[1] == "RETURN": 
      self.get_token() 
      return ["RETURN"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_sizeof(self): 
    if self.currenttoken[1] == "SIZEOF": 
      self.get_token() 
      return ["SIZEOF"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_plusminus(self): 
    if self.currenttoken[1] == "PLUS":
      self.get_token() 
      return ["PLUS"] 
    elif self.currenttoken[1] == "MINUS": 
      self.get_token() 
      return ["MINUS"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_leop(self): 
    if self.currenttoken[1] == "LE_OP": 
      self.get_token() 
      return ["LE_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_semicolon(self): 
    if self.currenttoken[1] == "SEMICOLON": 
      self.get_token() 
      #return ["SEMICOLON"] 
      return []
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_gop(self): 
    if self.currenttoken[1] == "G_OP": 
      self.get_token() 
      return ["G_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_pos(self): 
    if self.currenttoken[1] == "POS": 
      self.get_token() 
      return ["POS"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_or_op(self): 
    if self.currenttoken[1] == "OR_OP": 
      self.get_token() 
      return ["OR_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_open_brace(self): 
    if self.currenttoken[1] == "OPEN_BRACE": 
      self.get_token() 
      return ["OPEN_BRACE"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_open_paren(self): 
    if self.currenttoken[1] == "OPEN_PAREN": 
      self.get_token() 
      return ["OPEN_PAREN"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_comma(self): 
    if self.currenttoken[1] == "COMMA": 
      self.get_token() 
      #return ["COMMA"] 
      return []
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_ptr_op(self): 
    if self.currenttoken[1] == "PTR_OP": 
      self.get_token() 
      return ["PTR_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_if(self): 
    if self.currenttoken[1] == "IF": 
      self.get_token() 
      return ["IF"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_address_op(self): 
    if self.currenttoken[1] == "ADDRESS_OP": 
      self.get_token() 
      return ["ADDRESS_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_multdividemod(self): 
    if self.currenttoken[1] == "MULT"
      self.get_token() 
      return ["MULT"]
    elif self.currenttoken[1] == "DIVIDE":
      self.get_token() 
      return ["DIVIDE"]
    elif self.currenttoken[1] == "MOD": 
      self.get_token() 
      return ["MOD"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_define(self): 
    if self.currenttoken[1] == "DEFINE": 
      self.get_token() 
      return ["DEFINE"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_typedef(self): 
    if self.currenttoken[1] == "TYPEDEF": 
      self.get_token() 
      return ["TYPEDEF"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_divide(self): 
    if self.currenttoken[1] == "DIVIDE": 
      self.get_token() 
      return ["DIVIDE"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_for(self): 
    if self.currenttoken[1] == "FOR": 
      self.get_token() 
      return ["FOR"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_enum(self): 
    if self.currenttoken[1] == "ENUM": 
      self.get_token() 
      return ["ENUM"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_period(self): 
    if self.currenttoken[1] == "PERIOD": 
      self.get_token() 
      return ["PERIOD"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_else(self): 
    if self.currenttoken[1] == "ELSE": 
      self.get_token() 
      return ["ELSE"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_and_op(self): 
    if self.currenttoken[1] == "AND_OP": 
      self.get_token() 
      return ["AND_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_zero(self): 
    if self.currenttoken[1] == "ZERO": 
      self.get_token() 
      return ["ZERO"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_geop(self): 
    if self.currenttoken[1] == "GE_OP": 
      self.get_token() 
      return ["GE_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_assign_op(self): 
    if self.currenttoken[1] == "ASSIGN_OP": 
      self.get_token() 
      return ["ASSIGN_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_close_brace(self): 
    if self.currenttoken[1] == "CLOSE_BRACE": 
      self.get_token() 
      return ["CLOSE_BRACE"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_identifier(self): 
    if self.currenttoken[1] == "IDENTIFIER": 
      self.get_token() 
      return ["IDENTIFIER"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_close_paren(self): 
    if self.currenttoken[1] == "CLOSE_PAREN": 
      self.get_token() 
      return ["CLOSE_PAREN"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_string_literal(self): 
    if self.currenttoken[1] == "STRING_LITERAL": 
      self.get_token() 
      return ["STRING_LITERAL"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_eq_opne_op(self): 
    if self.currenttoken[1] == "EQ_OP":
      self.get_token() 
      return ["EQ_OP"] 
    elif self.currenttoken[1] == "NE_OP": 
      self.get_token() 
      return ["NE_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_pound(self): 
    if self.currenttoken[1] == "POUND": 
      self.get_token() 
      return ["POUND"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_struct(self): 
    if self.currenttoken[1] == "STRUCT": 
      self.get_token() 
      return ["STRUCT"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_int(self): 
    if self.currenttoken[1] == "INT": 
      self.get_token() 
      return ["INT"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_epsilon(self): 
    if self.currenttoken[1] == "EPSILON": 
      self.get_token() 
      return ["EPSILON"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_type_name(self): 
    if self.currenttoken[1] == "TYPE_NAME": 
      self.get_token() 
      return ["TYPE_NAME"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_num_const(self): 
    if self.currenttoken[1] == "NUM_CONST": 
      self.get_token() 
      return ["NUM_CONST"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_lop(self): 
    if self.currenttoken[1] == "L_OP": 
      self.get_token() 
      return ["L_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_break(self): 
    if self.currenttoken[1] == "BREAK": 
      self.get_token() 
      return ["BREAK"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_continue(self): 
    if self.currenttoken[1] == "CONTINUE": 
      self.get_token() 
      return ["CONTINUE"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_not(self): 
    if self.currenttoken[1] == "NOT": 
      self.get_token() 
      return ["NOT"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_pointer(self): 
    if self.currenttoken[1] == "POINTER": 
      self.get_token() 
      return ["POINTER"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_ne_op(self): 
    if self.currenttoken[1] == "NE_OP": 
      self.get_token() 
      return ["NE_OP"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_mod(self): 
    if self.currenttoken[1] == "MOD": 
      self.get_token() 
      return ["MOD"] 
    else: 
      print "Error! Unexpected token" + self.currenttoken 
      return False 
 
  def match_expression_statement(self): 
    root = "expression_statement" 
    children = [] 
    if self.currenttoken[1] == "SEMICOLON": 
      children.append(self.match_semicolon())
    elif self.currenttoken[1] in terminaldict["expression"]: 
      children.append(self.match_expression()).append(self.match_semicolon())
    return [root, children] 

  def match_external_next(self): 
    root = "external_next" 
    children = [] 
    children.append(self.match_choose_declarator()).append(self.match_external_next2())
    return [root, children] 

  def match_optional_pointer(self): 
    root = "optional_pointer" 
    children = [] 
    if self.currenttoken[1] in terminaldict["pointer"]: 
      children.append(self.match_pointer())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_choose_declarator_next3(self): 
    root = "choose_declarator_next3" 
    children = [] 
    children.append(self.match_choose_declarator())
    children = children + self.match_possible_direct_declarator_next()
    return [root, children] 

  def match_unary_expression(self): 
    root = "unary_expression" 
    children = [] 
    if self.currenttoken[1] in terminaldict["postfix_expression"]: 
      children.append(self.match_postfix_expression())
    elif self.currenttoken[1] == "INC_OP": 
      children.append(self.match_inc_op()).append(self.match_unary_expression())
    elif self.currenttoken[1] == "DEC_OP": 
      children.append(self.match_dec_op()).append(self.match_unary_expression())
    elif self.currenttoken[1] in terminaldict["unary_operator"]: 
      children.append(self.match_unary_operator()).append(self.match_unary_expression())
    elif self.currenttoken[1] == "SIZEOF": 
      children.append(self.match_sizeof()).append(self.match_unary_expression_sizeof())
    return [root, children] 

  def match_type_qualifier(self): 
    root = "type_qualifier" 
    children = [] 
    children.append(self.match_const())
    return [root, children] 

  def match_struct_specifier_next(self): 
    root = "struct_specifier_next" 
    children = [] 
    if self.currenttoken[1] == "IDENTIFIER": 
      children.append(self.match_identifier()).append(self.match_struct_specifier_cont())
    elif self.currenttoken[1] == "OPEN_BRACE": 
      children.append(self.match_open_brace()).append(self.match_struct_declaration_list()).append(self.match_close_brace())
    return [root, children] 

  def match_unary_expression_sizeof_cont(self): 
    root = "unary_expression_sizeof_cont" 
    children = [] 
    if self.currenttoken[1] in terminaldict["type_specifier"]: 
      children.append(self.match_type_specifier()).append(self.match_close_paren())
    elif self.currenttoken[1] == "IDENTIFIER": 
      children.append(self.match_identifier()).append(self.match_close_paren())
    return [root, children] 

  def match_parameter_declaration_next(self): 
    root = "parameter_declaration_next" 
    children = [] 
    if self.currenttoken[1] in terminaldict["pointer"]: 
      children.append(self.match_pointer()).append(self.match_choose_declarator())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_initializer(self): 
    root = "initializer" 
    children = [] 
    if self.currenttoken[1] in terminaldict["assignment_expression"]: 
      children.append(self.match_assignment_expression())
    elif self.currenttoken[1] == "OPEN_BRACE": 
      children.append(self.match_open_brace()).append(self.match_zero()).append(self.match_close_brace())
    return [root, children] 

  def match_direct_declarator_next1(self): 
    root = "direct_declarator_next1" 
    children = [] 
    if self.currenttoken[1] in terminaldict["pointer"]: 
      children.append(self.match_pointer()).append(self.match_direct_declarator()).append(self.match_close_paren())
    elif self.currenttoken[1] in terminaldict["parameter_list"]: 
      children.append(self.match_parameter_list()).append(self.match_close_paren()).append(self.match_direct_declarator())
    elif self.currenttoken[1] in terminaldict["identifier_list"]: 
      children.append(self.match_identifier_list()).append(self.match_close_paren()).append(self.match_direct_declarator())
    elif self.currenttoken[1] == "CLOSE_PAREN": 
      children.append(self.match_close_paren()).append(self.match_direct_declarator())
    return [root, children] 

  def match_enumerator_list(self): 
    root = "enumerator_list" 
    children = [] 
    children.append(self.match_identifier())
    children = children + self.match_possible_comma_identifier()
    return [root, children] 

  def match_external_init_declarator_list(self): 
    root = "external_init_declarator_list" 
    children = [] 
    children.append(self.match_init_declarator())
    children = children + self.match_possible_comma_choose_declarator_init_declarator()
    return [root, children] 

  def match_struct_declaration_list(self): 
    root = "struct_declaration_list" 
    children = [] 
    children.append(self.match_struct_declaration())
    children = children + self.match_possible_struct_declaration()
    return [root, children] 

  def match_postfix_expression_next_brace(self): 
    root = "postfix_expression_next_brace" 
    children = [] 
    if self.currenttoken[1] == "CLOSE_PAREN": 
      children.append(self.match_close_paren())
    elif self.currenttoken[1] in terminaldict["argument_expression_list"]: 
      children.append(self.match_argument_expression_list()).append(self.match_close_paren())
    return [root, children] 

  def match_pointer(self): 
    root = "pointer" 
    children = [] 
    children.append(self.match_pointer()).append(self.match_pointer_next())
    return [root, children] 

  def match_additive_expression(self): 
    root = "additive_expression" 
    children = [] 
    children.append(self.match_multiplicative_expression())
    children = children + self.match_possible_plusminus_multiplicative_expression()
    return [root, children] 

  def match_external_declaration(self): 
    root = "external_declaration" 
    children = [] 
    if self.currenttoken[1] in terminaldict["type_specifier"]: 
      children.append(self.match_type_specifier()).append(self.match_external_next())
    elif self.currenttoken[1] in terminaldict["choose_declarator"]: 
      children.append(self.match_choose_declarator()).append(self.match_function_definition())
    elif self.currenttoken[1] in terminaldict["type_qualifier"]: 
      children.append(self.match_type_qualifier()).append(self.match_type_specifier()).append(self.match_init_declarator_list()).append(self.match_semicolon())
      #match_possible will return, if there are more of this rule, a list of the rules that will be combined with the children list (cannot append, because that will put them in their own list within the children list 
      children = children + self.match_possible_declaration_specifiers_semicolon()
    elif self.currenttoken[1] == "TYPEDEF": 
      children.append(self.match_typedef()).append(self.match_type_specifier()).append(self.match_semicolon())
      children = children + self.match_possible_declaration_specifiers_semicolon()
    return [root, children] 

  def match_type_specifier(self): 
    root = "type_specifier" 
    children = [] 
    if self.currenttoken[1] == "VOID": 
      children.append(self.match_void())
    elif self.currenttoken[1] == "CHAR": 
      children.append(self.match_char())
    elif self.currenttoken[1] == "INT": 
      children.append(self.match_int())
    elif self.currenttoken[1] in terminaldict["struct_specifier"]: 
      children.append(self.match_struct_specifier())
    elif self.currenttoken[1] == "TYPE_NAME": 
      children.append(self.match_type_name())
    return [root, children] 

  def match_compound_statement(self): 
    root = "compound_statement" 
    children = [] 
    children.append(self.match_open_brace()).append(self.match_compound_statement_next())
    return [root, children] 

  def match_choose_declarator_next1(self): 
    root = "choose_declarator_next1" 
    children = [] 
    if self.currenttoken[1] == "CLOSE_PAREN": 
      children.append(self.match_close_paren()).append(self.match_choose_declarator_next3())
    elif self.currenttoken[1] in terminaldict["parameter_list"]: 
      children.append(self.match_parameter_list()).append(self.match_close_paren()).append(self.match_choose_declarator_next3())
    elif self.currenttoken[1] in terminaldict["pointer"]: 
      children.append(self.match_pointer()).append(self.match_choose_declarator()).append(self.match_close_paren())
    elif self.currenttoken[1] in terminaldict["identifier_list"]: 
      children.append(self.match_identifier_list()).append(self.match_close_paren()).append(self.match_choose_declarator())
    return [root, children] 

  def match_choose_declarator_next2(self): 
    root = "choose_declarator_next2" 
    children = [] 
    if self.currenttoken[1] in terminaldict["logical_or_expression"]: 
      children.append(self.match_logical_or_expression()).append(self.match_close_bracket()).append(self.match_choose_declarator_next3())
    elif self.currenttoken[1] == "CLOSE_BRACKET": 
      children.append(self.match_close_bracket()).append(self.match_choose_declarator_next3())
    return [root, children] 

  def match_type_name(self): 
    root = "type_name" 
    children = [] 
    children.append(self.match_type_qualifier_specifier()).append(self.match_type_name_next())
    return [root, children] 

  #TODO: possibly add ID's to symbol table here 
  def match_choose_declarator(self): 
    root = "choose_declarator" 
    children = [] 
    if self.currenttoken[1] == "IDENTIFIER": 
      children.append(self.match_identifier())
    elif self.currenttoken[1] in terminaldict["choose_declarator_next"]: 
      children.append(self.match_choose_declarator_next())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_postfix_expression(self): 
    root = "postfix_expression" 
    children = [] 
    children.append(self.match_primary_expression())
    children = children + self.match_possible_postfix_expression_next()
    return [root, children] 

  def match_compilerdir_or_external_declaration(self): 
    root = "compilerdir_or_external_declaration" 
    children = [] 
    if self.currenttoken[1] in terminaldict["define_directive"]: 
      children.append(self.match_define_directive())
    elif self.currenttoken[1] in terminaldict["external_declaration"]: 
      children.append(self.match_external_declaration())
    return [root, children] 

  def match_pointer_next(self): 
    root = "pointer_next" 
    children = [] 
    if self.currenttoken[1] in terminaldict["type_qualifier"]: 
      children.append(self.match_type_qualifier()).append(self.match_optional_pointer())
    elif self.currenttoken[1] in terminaldict["pointer"]: 
      children.append(self.match_pointer())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_unary_expression_sizeof(self): 
    root = "unary_expression_sizeof" 
    children = [] 
    children.append(self.match_open_paren()).append(self.match_unary_expression_sizeof_cont())
    return [root, children] 

  def match_relational_expression(self): 
    root = "relational_expression" 
    children = [] 
    children.append(self.match_additive_expression())
    children = children + self.match_possible_lop_gop_leop_geop_additive_expression()
    return [root, children] 

  def match_statement(self): 
    root = "statement" 
    children = [] 
    if self.currenttoken[1] in terminaldict["compound_statement"]: 
      children.append(self.match_compound_statement())
    elif self.currenttoken[1] in terminaldict["selection_statement"]: 
      children.append(self.match_selection_statement())
    elif self.currenttoken[1] in terminaldict["iteration_statement"]: 
      children.append(self.match_iteration_statement())
    elif self.currenttoken[1] in terminaldict["jump_statement"]: 
      children.append(self.match_jump_statement())
    return [root, children] 

  def match_direct_abstract_declarator_next(self): 
    root = "direct_abstract_declarator_next" 
    children = [] 
    if self.currenttoken[1] == "OPEN_BRACKET": 
      children.append(self.match_open_bracket()).append(self.match_direct_abstract_declarator_next())
    elif self.currenttoken[1] == "OPEN_PAREN": 
      children.append(self.match_open_paren()).append(self.match_direct_abstract_declarator_next1())
    return [root, children] 

  def match_struct_declarator_list(self): 
    root = "struct_declarator_list" 
    children = [] 
    children.append(self.match_choose_declarator()).append(self.match_comma()).append(self.match_choose_declarator())
    return [root, children] 

  def match_direct_declarator(self): 
    root = "direct_declarator" 
    children = [] 
    if self.currenttoken[1] == "IDENTIFIER": 
      children.append(self.match_identifier())
    elif self.currenttoken[1] == "OPEN_PAREN": 
      children.append(self.match_open_paren()).append(self.match_direct_declarator_next1())
    elif self.currenttoken[1] == "OPEN_BRACKET": 
      children.append(self.match_open_bracket()).append(self.match_direct_declarator_next2())
    return [root, children] 

  def match_unary_operator(self): 
    root = "unary_operator" 
    children = [] 
    if self.currenttoken[1] == "ADDRESS_OP": 
      children.append(self.match_address_op())
    elif self.currenttoken[1] == "POINTER": 
      children.append(self.match_pointer())
    elif self.currenttoken[1] == "POS": 
      children.append(self.match_pos())
    elif self.currenttoken[1] == "NEG": 
      children.append(self.match_neg())
    elif self.currenttoken[1] == "NOT": 
      children.append(self.match_not())
    return [root, children] 

  def match_type_qualifier_specifier(self): 
    root = "type_qualifier_specifier" 
    children = [] 
    if self.currenttoken[1] in terminaldict["type_qualifier"]: 
      children.append(self.match_type_qualifier()).append(self.match_type_specifier())
    elif self.currenttoken[1] in terminaldict["type_specifier"]: 
      children.append(self.match_type_specifier())
    return [root, children] 

  def match_define_directive(self): 
    root = "define_directive" 
    children = [] 
    children.append(self.match_pound()).append(self.match_define()).append(self.match_identifier()).append(self.match_define_type())
    return [root, children] 

  def match_struct_declaration(self): 
    root = "struct_declaration" 
    children = [] 
    children.append(self.match_type_specifier()).append(self.match_struct_declarator_list()).append(self.match_semicolon())
    return [root, children] 

  #TODO: put id's into symbol table 
  def match_assignment_expression(self): 
    root = "assignment_expression" 
    children = [] 
    children.append(self.match_unary_expression())
    children = children + self.match_possible_assign_op_assignment_expression()
    return [root, children] 

  def match_parameter_declaration(self): 
    root = "parameter_declaration" 
    children = [] 
    children.append(self.match_declaration_specifiers()).append(self.match_parameter_declaration_next())
    return [root, children] 

  def match_multiplicative_expression(self): 
    root = "multiplicative_expression" 
    children = [] 
    children.append(self.match_unary_expression())
    children = children + self.match_possible_multdividemod_unary_expression()
    return [root, children] 

  def match_define_type(self): 
    root = "define_type" 
    children = [] 
    if self.currenttoken[1] == "NUM_CONST": 
      children.append(self.match_num_const())
    elif self.currenttoken[1] == "STRING_LITERAL": 
      children.append(self.match_string_literal())
    return [root, children] 

  def match_argument_expression_list(self): 
    root = "argument_expression_list" 
    children = [] 
    children.append(self.match_assignment_expression())
    children = children + self.match_possible_comma_assignment_expression()
    return [root, children] 

  def match_iteration_statement(self): 
    root = "iteration_statement" 
    children = [] 
    children.append(self.match_while()).append(self.match_open_paren()).append(self.match_expression()).append(self.match_close_paren()).append(self.match_statement())
    return [root, children] 

  def match_selection_statement(self): 
    root = "selection_statement" 
    children = [] 
    children.append(self.match_if()).append(self.match_open_paren()).append(self.match_expression()).append(self.match_close_paren()).append(self.match_statement()).append(self.match_selection_statement_next())
    return [root, children] 

  def match_postfix_expression_next(self): 
    root = "postfix_expression_next" 
    children = [] 
    if self.currenttoken[1] == "OPEN_BRACKET": 
      children.append(self.match_open_bracket()).append(self.match_expression()).append(self.match_close_bracket())
    elif self.currenttoken[1] == "OPEN_PAREN": 
      children.append(self.match_open_paren()).append(self.match_postfix_expression_next_brace())
    elif self.currenttoken[1] == "PERIOD": 
      children.append(self.match_period()).append(self.match_identifier())
    elif self.currenttoken[1] == "PTR_OP": 
      children.append(self.match_ptr_op()).append(self.match_identifier())
    elif self.currenttoken[1] == "INC_OP": 
      children.append(self.match_inc_op())
    elif self.currenttoken[1] == "DEC_OP": 
      children.append(self.match_dec_op())
    return [root, children] 

  def match_equality_expression(self): 
    root = "equality_expression" 
    children = [] 
    children.append(self.match_relational_expression())
    children = children + self.match_possible_eq_opne_op_relational_expression()
    return [root, children] 

  #TODO
  def match_primary_expression(self): 
    root = "primary_expression" 
    children = [] 
    if self.currenttoken[1] == "IDENTIFIER": 
      if self.id_type != '':
        self.id_to_define = self.currenttoken[2] #currenttoken = (id_num, "IDENTIFIER", id_value)
      children.append(self.match_identifier()
    elif self.currenttoken[1] == "NUM_CONST": 
      if self.id_type !='' and self.id_to_define != '':
        self.id_value = currenttoken[2]
      children.append(self.match_num_const())
    elif self.currenttoken[1] == "STRING_LITERAL": 
      if self.id_type !='' and self.id_to_define != '':
        self.id_value = currenttoken[2]
      children.append(self.match_string_literal())
    elif self.currenttoken[1] == "OPEN_PAREN": 
      children.append(self.match_open_paren()).append(self.match_expression()).append(self.match_close_paren())
    return [root, children] 

  #TODO: put id's in symbol table 
  def match_declaration_specifiers(self): 
    root = "declaration_specifiers" 
    children = [] 
    if self.currenttoken[1] in terminaldict["type_qualifier_specifier"]: 
      children.append(self.match_type_qualifier_specifier()).append(self.match_init_declarator_list())
    elif self.currenttoken[1] == "TYPEDEF": 
      children.append(self.match_typedef()).append(self.match_type_specifier())
    return [root, children] 

  def match_declaration(self): 
    root = "declaration" 
    children = [] 
    children.append(self.match_declaration_specifiers()).append(self.match_semicolon())
    children = children + self.match_possible_declaration_specifiers_semicolon()
    return [root, children] 

  def match_struct_specifier_cont(self): 
    root = "struct_specifier_cont" 
    children = [] 
    if self.currenttoken[1] == "OPEN_BRACE": 
      children.append(self.match_open_brace()).append(self.match_struct_declaration_list()).append(self.match_close_brace())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_logical_and_expression(self): 
    root = "logical_and_expression" 
    children = [] 
    children.append(self.match_equality_expression())
    children = children + self.match_possible_and_op_equality_expression()
    return [root, children] 

  def match_init_declarator_list(self): 
    root = "init_declarator_list" 
    children = [] 
    children.append(self.match_choose_declarator()).append(self.match_init_declarator())
    children = children + self.match_possible_comma_choose_declarator_init_declarator()
    return [root, children] 

  def match_identifier_list(self): 
    root = "identifier_list" 
    children = [] 
    children.append(self.match_identifier())
    children = children + self.match_possible_comma_identifier()
    return [root, children] 

  def match_jump_statement(self): 
    root = "jump_statement" 
    children = [] 
    if self.currenttoken[1] == "CONTINUE": 
      children.append(self.match_continue()).append(self.match_semicolon())
    elif self.currenttoken[1] == "BREAK": 
      children.append(self.match_break()).append(self.match_semicolon())
    elif self.currenttoken[1] in terminaldict["expression_statement"]: 
      children.append(self.match_expression_statement())
    return [root, children] 

  def match_function_definition(self): 
    root = "function_definition" 
    children = [] 
    if self.currenttoken[1] in terminaldict["declaration_list"]: 
      children.append(self.match_declaration_list()).append(self.match_compound_statement())
    elif self.currenttoken[1] in terminaldict["compound_statement"]: 
      children.append(self.match_compound_statement())
    return [root, children] 

  def match_external_next2(self): 
    root = "external_next2" 
    children = [] 
    if self.currenttoken[1] in terminaldict["external_init_declarator_list"]: 
      children.append(self.match_external_init_declarator_list()).append(self.match_semicolon())
      children = children + self.match_possible_declaration_specifiers_semicolon()
    elif self.currenttoken[1] in terminaldict["function_definition"]: 
      children.append(self.match_function_definition())
    return [root, children] 

  def match_parameter_list(self): 
    root = "parameter_list" 
    children = [] 
    children.append(self.match_parameter_declaration()).append(self.match_comma())
    children = children + self.match_possible_comma_parameter_declaration()
    return [root, children] 

  def match_type_name_next(self): 
    root = "type_name_next" 
    children = [] 
    if self.currenttoken[1] in terminaldict["pointer"]: 
      children.append(self.match_pointer()).append(self.match_choose_declarator())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_compound_statement_next(self): 
    root = "compound_statement_next" 
    children = [] 
    if self.currenttoken[1] == "CLOSE_BRACE": 
      children.append(self.match_close_brace())
    elif self.currenttoken[1] in terminaldict["statement_list"]: 
      children.append(self.match_statement_list()).append(self.match_close_brace())
    elif self.currenttoken[1] in terminaldict["declaration_list"]: 
      children.append(self.match_declaration_list()).append(self.match_compound_statement_next1())
    return [root, children] 

  def match_struct_specifier(self): 
    root = "struct_specifier" 
    children = [] 
    children.append(self.match_struct()).append(self.match_struct_specifier_next())
    return [root, children] 

  def match_direct_abstract_declarator_next1(self): 
    root = "direct_abstract_declarator_next1" 
    children = [] 
    if self.currenttoken[1] == "CLOSE_PAREN": 
      children.append(self.match_close_paren())
    elif self.currenttoken[1] in terminaldict["parameter_list"]: 
      children.append(self.match_parameter_list()).append(self.match_close_paren())
    return [root, children] 

  def match_direct_declarator_next2(self): 
    root = "direct_declarator_next2" 
    children = [] 
    if self.currenttoken[1] in terminaldict["logical_or_expression"]: 
      children.append(self.match_logical_or_expression()).append(self.match_close_bracket()).append(self.match_direct_declarator())
    elif self.currenttoken[1] == "CLOSE_BRACKET": 
      children.append(self.match_close_bracket()).append(self.match_direct_declarator())
    return [root, children] 

  def match_declaration_list(self): 
    root = "declaration_list" 
    children = [] 
    children.append(self.match_declaration())
    children = children + self.match_possible_declaration()
    return [root, children] 

  def match_selection_statement_next(self): 
    root = "selection_statement_next" 
    children = [] 
    if self.currenttoken[1] == "ELSE": 
      children.append(self.match_else()).append(self.match_statement())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_enum_specifier(self): 
    root = "enum_specifier" 
    children = [] 
    children.append(self.match_enum()).append(self.match_open_brace()).append(self.match_enumerator_list()).append(self.match_close_brace())
    return [root, children] 

  def match_direct_abstract_declarator(self): 
    root = "direct_abstract_declarator" 
    children = [] 
    if self.currenttoken[1] == "CLOSE_BRACKET": 
      children.append(self.match_close_bracket())
    elif self.currenttoken[1] in terminaldict["logical_or_expression"]: 
      children.append(self.match_logical_or_expression()).append(self.match_close_bracket())
    return [root, children] 

  def match_choose_declarator_next(self): 
    root = "choose_declarator_next" 
    children = [] 
    if self.currenttoken[1] == "OPEN_PAREN": 
      children.append(self.match_open_paren()).append(self.match_choose_declarator_next1())
    elif self.currenttoken[1] == "OPEN_BRACKET": 
      children.append(self.match_open_bracket()).append(self.match_choose_declarator_next2())
    return [root, children] 

  def match_translation_unit(self): 
    root = "translation_unit" 
    children = [] 
    children.append(self.match_compilerdir_or_external_declaration())
    children = children + self.match_possible_compilerdir_or_external_declaration()
    return [root, children] 

  #TODO: put id's into symbol table 
  def match_init_declarator(self): 
    root = "init_declarator" 
    children = [] 
    if self.currenttoken[1] == "EQ_OP": 
      children.append(self.match_assign_op()).append(self.match_initializer())
    elif self.currenttoken[1] == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_statement_list(self): 
    root = "statement_list" 
    children = [] 
    children.append(self.match_statement())
    children = children + self.match_possible_statement()
    return [root, children] 

  def match_expression(self): 
    root = "expression" 
    children = [] 
    children.append(self.match_assignment_expression())
    children = children + self.match_possible_comma_assignment_expression()
    return [root, children] 

  def match_logical_or_expression(self): 
    root = "logical_or_expression" 
    children = [] 
    children.append(self.match_logical_and_expression())
    children = children + self.match_possible_or_op_equality_expression()
    return [root, children] 

  def match_possible_declaration_specifiers_semicolon(self):
    children =  []
    if self.currenttoken[1] in terminaldict["declaration_specifiers"]:
      children.append(match_declaration_specifiers).append(match_semicolon)
      children = children + self.match_possible_declaration_specifiers_semicolon()
      return children 
    else:
      return [] 
      
  def match_possible_compilerdir_or_external_declaration(self):
    children = []
    if self.currenttoken[1] in terminaldict["compilerdir_or_external_declaration"]:
      children.append(self.match_compilerdir_or_external_declaration())
      children = children + self.match_possible_compilerdir_or_external_declaration()
      return children
    else:
      return []

  def match_possible_comma_choose_declarator_init_declarator(self):
    children = []
    if self.currenttoken[1] == "COMMA":
      children.append(self.match_comma()).append(self.match_choose_declarator()).append(self.match_init_declarator())
      children = children + self.match_possible_comma_choose_declarator_init_declarator()
      return children
    else:
      return []

  def match_possible_comma_parameter_declaration(self):
    children = []
    if self.currenttoken[1] == "COMMA":
      children.append(self.match_comma()).append(self.match_parameter_declaration())
      children = children + self.match_possible_comma_parameter_declaration()
      return children
    else:
      return []

  def match_possible_direct_declarator_next(self):
    children = []
    if self.currenttoken[1] in terminaldict["direct_declarator_next"]:
      children.append(self.match_direct_declarator_next())
      children = children + self.match_possible_direct_declarator_next()
      return children
    else:
      return []

  def match_possible_comma_identifier(self):
    children = []
    if self.currenttoken[1] == "COMMA":
      children.append(self.match_comma()).append(match_identifier())
      children = children + self.match_possible_comma_identifier()
      return children
    else:
      return []

  def match_possible_struct_declaration(self):
    children = []
    if self.currenttoken[1] in terminaldict["struct_declaration"]:
      children.append(self.match_struct_declaration())
      children = children + self.match_possible_struct_declaration()
      return children
    else:
      return []

  def match_possible_postfix_expression_next(self):
    children = []
    if self.currenttoken[1] in terminaldict["postfix_expression_next"]:
      children.append(self.match_postfix_expression_next())
      children = children + self.match_possible_postfix_expression_next()
      return children
    else:
      return []

  def match_possible_comma_assignment_expression(self):
    children = []
    if self.currenttoken[1] == "COMMA":
      children.append(self.match_comma()).append(self.match_assignment_expression())
      children = children + self.match_possible_comma_assignment_expression()
      return children
    else:
      return []


  def match_possible_multdividemod_unary_expression(self):
    children = []
    if self.currenttoken[1] == "MULT" or self.currenttoken == "DIV" or self.currenttoken == "MOD":
      children.append(self.match_multdividemod()).append(self.match_unary_expression())
      children = children + self.match_possible_multdivmod_unary_expression())
      return children
    else:
      return []

  def match_possible_plusminus_multiplicative_expression(self):
    children = []
    if self.currenttoken[1] == "PLUS" or self.currenttoken == "MINUS":
      children.append(self.match_plusminus()).append(self.match_multiplicative_expression())
      children = children + self.match_possible_plusminus_multiplicative_expression()
      return children
    else:
      return []

  def match_possible_lop_gop_leop_geop_additive_expression(self):
	# (L_OP|G_OP|LE_OP|GE_OP)
    children = []
    if self.currenttoken[1] == "L_OP" or self.currenttoken == "G_OP" or self.currenttoken == "LE_OP" or self.currenttoken == "GE_OP":
      children.append(self.match_lop_gop_leop_geop()).append(self.match_additive_expression())
      children = children + self.match_possible_eq_opne_op_relational_expression()
      return children 
    else:
      return []

  def match_possible_eq_opne_op_relational_expression(self): 
	#relational_expression { (EQ_OP|NE_OP) relational_expression }
    children = []
    if self.currenttoken[1] == "EQ_OP" or self.currenttoken == "NE_OP":
      children.append(self.match_eq_opne_op()).append(self.match_relational_expression())
      children = children + self.match_possible_eq_opne_op_relational_expression()
      return children
    else:
      return []

  def match_possible_and_op_equality_expression(self):
	#equality_expression { AND_OP equality_expression }
    children = []
    if self.currenttoken[1] == "AND_OP":
      children.append(self.match_and_op()).append(self.match_equality_expression())
      children = children + self.match_possible_and_op_equality_expression()
      return children
    else:
      return []

  def match_possible_or_op_equality_expression(self):
	#logical_and_expression { OR_OP logical_and_expression }
     children = []
    if self.currenttoken[1] == "OR_OP":
      children.append(self.match_or_op()).append(self.match_equality_expression())
      children = children + self.match_possible_or_op_equality_expression()
      return children
    else:
      return []

  def match_possible_assign_op_assignment_expression(self):
	#unary_expression { EQ_OP assignment_expression }
    children = []
    if self.currenttoken[1] == "EQ_OP":
      children.append(self.match_assign_op()).append(self.match_assignment_expression())
      children = children + self.match_possible_assign_op_assignment_expression()
      return children
    else:
      return []

  def match_possible_statement(self):
	#statement { statement }
    children = []
    if self.currenttoken[1] in terminaldict["statement"]:
      children.append(self.match_statement())
      children = children + self.match_possible_statement()
      return children
    else:
      return []

  def match_possible_declaration(self):
	#declaration { declaration }
    children = []
    if self.currenttoken[1] in terminaldict["declaration"]:
      children.append(self.match_declaration())
      children = children + self.match_possible_declaration()
      return children
    else:
      return []

 
from lexicalanalyzer import LexicalAnalyzer
if __name__ == "__main__":
  f = raw_input("Where is your program?")
  with open(f, 'r') as myfile:
    mystring = myfile.read()
  x = LexicalAnalyzer(mystring)
  tokens = x.tokenize()
  dictname = raw_input("Where is the terminal dictionary stored?")
  terminaldict = {}
  with open(dictname, 'r'):
    terminaldict = eval(dictname.read())
  ParseTree = ConcreteParseTree(tokens, terminaldict)
  ParseTree.match_translation_unit()
  return "done"
