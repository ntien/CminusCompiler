#Tree structure: [root, [child, child]] 
class ConcreteParseTree(stringstream, mydict):
  terminaldict = mydict
  currenttoken = self.get_token() 
 
  def match_close_bracket(self): 
    leaf = [] 
    if currenttoken == "CLOSE_BRACKET": 
      currenttoken = self.get_token() 
      return ["CLOSE_BRACKET"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_const(self): 
    leaf = [] 
    if currenttoken == "CONST": 
      currenttoken = self.get_token() 
      return ["CONST"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_dec_op(self): 
    leaf = [] 
    if currenttoken == "DEC_OP": 
      currenttoken = self.get_token() 
      return ["DEC_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_neg(self): 
    leaf = [] 
    if currenttoken == "NEG": 
      currenttoken = self.get_token() 
      return ["NEG"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_void(self): 
    leaf = [] 
    if currenttoken == "VOID": 
      currenttoken = self.get_token() 
      return ["VOID"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_open_bracket(self): 
    leaf = [] 
    if currenttoken == "OPEN_BRACKET": 
      currenttoken = self.get_token() 
      return ["OPEN_BRACKET"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_char(self): 
    leaf = [] 
    if currenttoken == "CHAR": 
      currenttoken = self.get_token() 
      return ["CHAR"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_inc_op(self): 
    leaf = [] 
    if currenttoken == "INC_OP": 
      currenttoken = self.get_token() 
      return ["INC_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_while(self): 
    leaf = [] 
    if currenttoken == "WHILE": 
      currenttoken = self.get_token() 
      return ["WHILE"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_eq_op(self): 
    leaf = [] 
    if currenttoken == "EQ_OP": 
      currenttoken = self.get_token() 
      return ["EQ_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_l_opg_ople_opge_op(self): 
    leaf = [] 
    if currenttoken == "L_OPG_OPLE_OPGE_OP": 
      currenttoken = self.get_token() 
      return ["L_OPG_OPLE_OPGE_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_return(self): 
    leaf = [] 
    if currenttoken == "RETURN": 
      currenttoken = self.get_token() 
      return ["RETURN"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_sizeof(self): 
    leaf = [] 
    if currenttoken == "SIZEOF": 
      currenttoken = self.get_token() 
      return ["SIZEOF"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_plusminus(self): 
    leaf = [] 
    if currenttoken == "PLUSMINUS": 
      currenttoken = self.get_token() 
      return ["PLUSMINUS"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_le_op(self): 
    leaf = [] 
    if currenttoken == "LE_OP": 
      currenttoken = self.get_token() 
      return ["LE_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_semicolon(self): 
    leaf = [] 
    if currenttoken == "SEMICOLON": 
      currenttoken = self.get_token() 
      return ["SEMICOLON"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_g_op(self): 
    leaf = [] 
    if currenttoken == "G_OP": 
      currenttoken = self.get_token() 
      return ["G_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_pos(self): 
    leaf = [] 
    if currenttoken == "POS": 
      currenttoken = self.get_token() 
      return ["POS"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_or_op(self): 
    leaf = [] 
    if currenttoken == "OR_OP": 
      currenttoken = self.get_token() 
      return ["OR_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_open_brace(self): 
    leaf = [] 
    if currenttoken == "OPEN_BRACE": 
      currenttoken = self.get_token() 
      return ["OPEN_BRACE"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_open_paren(self): 
    leaf = [] 
    if currenttoken == "OPEN_PAREN": 
      currenttoken = self.get_token() 
      return ["OPEN_PAREN"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_comma(self): 
    leaf = [] 
    if currenttoken == "COMMA": 
      currenttoken = self.get_token() 
      return ["COMMA"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_ptr_op(self): 
    leaf = [] 
    if currenttoken == "PTR_OP": 
      currenttoken = self.get_token() 
      return ["PTR_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_if(self): 
    leaf = [] 
    if currenttoken == "IF": 
      currenttoken = self.get_token() 
      return ["IF"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_address_op(self): 
    leaf = [] 
    if currenttoken == "ADDRESS_OP": 
      currenttoken = self.get_token() 
      return ["ADDRESS_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_multdividemod(self): 
    leaf = [] 
    if currenttoken == "MULTDIVIDEMOD": 
      currenttoken = self.get_token() 
      return ["MULTDIVIDEMOD"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_define(self): 
    leaf = [] 
    if currenttoken == "DEFINE": 
      currenttoken = self.get_token() 
      return ["DEFINE"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_typedef(self): 
    leaf = [] 
    if currenttoken == "TYPEDEF": 
      currenttoken = self.get_token() 
      return ["TYPEDEF"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_divide(self): 
    leaf = [] 
    if currenttoken == "DIVIDE": 
      currenttoken = self.get_token() 
      return ["DIVIDE"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_for(self): 
    leaf = [] 
    if currenttoken == "FOR": 
      currenttoken = self.get_token() 
      return ["FOR"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_enum(self): 
    leaf = [] 
    if currenttoken == "ENUM": 
      currenttoken = self.get_token() 
      return ["ENUM"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_period(self): 
    leaf = [] 
    if currenttoken == "PERIOD": 
      currenttoken = self.get_token() 
      return ["PERIOD"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_else(self): 
    leaf = [] 
    if currenttoken == "ELSE": 
      currenttoken = self.get_token() 
      return ["ELSE"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_and_op(self): 
    leaf = [] 
    if currenttoken == "AND_OP": 
      currenttoken = self.get_token() 
      return ["AND_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_zero(self): 
    leaf = [] 
    if currenttoken == "ZERO": 
      currenttoken = self.get_token() 
      return ["ZERO"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_ge_op(self): 
    leaf = [] 
    if currenttoken == "GE_OP": 
      currenttoken = self.get_token() 
      return ["GE_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_assign_op(self): 
    leaf = [] 
    if currenttoken == "ASSIGN_OP": 
      currenttoken = self.get_token() 
      return ["ASSIGN_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_close_brace(self): 
    leaf = [] 
    if currenttoken == "CLOSE_BRACE": 
      currenttoken = self.get_token() 
      return ["CLOSE_BRACE"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_identifier(self): 
    leaf = [] 
    if currenttoken == "IDENTIFIER": 
      currenttoken = self.get_token() 
      return ["IDENTIFIER"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_close_paren(self): 
    leaf = [] 
    if currenttoken == "CLOSE_PAREN": 
      currenttoken = self.get_token() 
      return ["CLOSE_PAREN"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_string_literal(self): 
    leaf = [] 
    if currenttoken == "STRING_LITERAL": 
      currenttoken = self.get_token() 
      return ["STRING_LITERAL"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_eq_opne_op(self): 
    leaf = [] 
    if currenttoken == "EQ_OPNE_OP": 
      currenttoken = self.get_token() 
      return ["EQ_OPNE_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_pound(self): 
    leaf = [] 
    if currenttoken == "POUND": 
      currenttoken = self.get_token() 
      return ["POUND"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_struct(self): 
    leaf = [] 
    if currenttoken == "STRUCT": 
      currenttoken = self.get_token() 
      return ["STRUCT"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_int(self): 
    leaf = [] 
    if currenttoken == "INT": 
      currenttoken = self.get_token() 
      return ["INT"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_epsilon(self): 
    leaf = [] 
    if currenttoken == "EPSILON": 
      currenttoken = self.get_token() 
      return ["EPSILON"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_type_name(self): 
    leaf = [] 
    if currenttoken == "TYPE_NAME": 
      currenttoken = self.get_token() 
      return ["TYPE_NAME"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_num_const(self): 
    leaf = [] 
    if currenttoken == "NUM_CONST": 
      currenttoken = self.get_token() 
      return ["NUM_CONST"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_l_op(self): 
    leaf = [] 
    if currenttoken == "L_OP": 
      currenttoken = self.get_token() 
      return ["L_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_break(self): 
    leaf = [] 
    if currenttoken == "BREAK": 
      currenttoken = self.get_token() 
      return ["BREAK"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_continue(self): 
    leaf = [] 
    if currenttoken == "CONTINUE": 
      currenttoken = self.get_token() 
      return ["CONTINUE"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_not(self): 
    leaf = [] 
    if currenttoken == "NOT": 
      currenttoken = self.get_token() 
      return ["NOT"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_pointer(self): 
    leaf = [] 
    if currenttoken == "POINTER": 
      currenttoken = self.get_token() 
      return ["POINTER"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_ne_op(self): 
    leaf = [] 
    if currenttoken == "NE_OP": 
      currenttoken = self.get_token() 
      return ["NE_OP"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_mod(self): 
    leaf = [] 
    if currenttoken == "MOD": 
      currenttoken = self.get_token() 
      return ["MOD"] 
    else: 
      print " Error! Unexpected token" + currenttoken 
      return False 
 
  def match_expression_statement(self): 
    root = "expression_statement" 
    children = [] 
    if currenttoken == "SEMICOLON": 
      children.append(self.match_semicolon())
    if currenttoken in terminaldict["expression"]: 
      children.append(self.match_semicolon())
    return [root, children] 

  def match_external_next(self): 
    root = "external_next" 
    children = [] 
    children.append(self.match_choose_declarator()).append(self.match_external_next2())
    return [root, children] 

  def match_optional_pointer(self): 
    root = "optional_pointer" 
    children = [] 
    if currenttoken in terminaldict["pointer"]: 
      children.append(self.match_pointer())
    if currenttoken == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_choose_declarator_next3(self): 
    root = "choose_declarator_next3" 
    children = [] 
    children.append(self.match_choose_declarator()).append(self.match_direct_declarator_next())
    return [root, children] 

  def match_unary_expression(self): 
    root = "unary_expression" 
    children = [] 
    if currenttoken in terminaldict["postfix_expression"]: 
      children.append(self.match_postfix_expression())
    if currenttoken == "INC_OP": 
      children.append(self.match_unary_expression())
    if currenttoken == "DEC_OP": 
      children.append(self.match_unary_expression())
    if currenttoken in terminaldict["unary_operator"]: 
      children.append(self.match_unary_expression())
    if currenttoken == "SIZEOF": 
      children.append(self.match_unary_expression_sizeof())
    return [root, children] 

  def match_type_qualifier(self): 
    root = "type_qualifier" 
    children = [] 
    children.append(self.match_const())
    return [root, children] 

  def match_struct_specifier_next(self): 
    root = "struct_specifier_next" 
    children = [] 
    if currenttoken == "IDENTIFIER": 
      children.append(self.match_struct_specifier_cont())
    if currenttoken == "OPEN_BRACE": 
      children.append(self.match_close_brace())
    return [root, children] 

  def match_unary_expression_sizeof_cont(self): 
    root = "unary_expression_sizeof_cont" 
    children = [] 
    if currenttoken in terminaldict["type_specifier"]: 
      children.append(self.match_close_paren())
    if currenttoken == "IDENTIFIER": 
      children.append(self.match_close_paren())
    return [root, children] 

  def match_parameter_declaration_next(self): 
    root = "parameter_declaration_next" 
    children = [] 
    if currenttoken in terminaldict["pointer"]: 
      children.append(self.match_choose_declarator())
    if currenttoken == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_initializer(self): 
    root = "initializer" 
    children = [] 
    if currenttoken in terminaldict["assignment_expression"]: 
      children.append(self.match_assignment_expression())
    if currenttoken == "OPEN_BRACE": 
      children.append(self.match_close_brace())
    return [root, children] 

  def match_direct_declarator_next1(self): 
    root = "direct_declarator_next1" 
    children = [] 
    if currenttoken in terminaldict["pointer"]: 
      children.append(self.match_close_paren())
    if currenttoken in terminaldict["parameter_list"]: 
      children.append(self.match_direct_declarator())
    if currenttoken in terminaldict["identifier_list"]: 
      children.append(self.match_direct_declarator())
    if currenttoken == "CLOSE_PAREN": 
      children.append(self.match_direct_declarator())
    return [root, children] 

  def match_enumerator_list(self): 
    root = "enumerator_list" 
    children = [] 
    children.append(self.match_identifier()).append(self.match_comma()).append(self.match_identifier())
    return [root, children] 

  def match_external_init_declarator_list(self): 
    root = "external_init_declarator_list" 
    children = [] 
    children.append(self.match_init_declarator()).append(self.match_comma()).append(self.match_choose_declarator()).append(self.match_init_declarator())
    return [root, children] 

  def match_struct_declaration_list(self): 
    root = "struct_declaration_list" 
    children = [] 
    children.append(self.match_struct_declaration()).append(self.match_struct_declaration())
    return [root, children] 

  def match_postfix_expression_next_brace(self): 
    root = "postfix_expression_next_brace" 
    children = [] 
    if currenttoken == "CLOSE_PAREN": 
      children.append(self.match_close_paren())
    if currenttoken in terminaldict["argument_expression_list"]: 
      children.append(self.match_close_paren())
    return [root, children] 

  def match_pointer(self): 
    root = "pointer" 
    children = [] 
    children.append(self.match_pointer()).append(self.match_pointer_next())
    return [root, children] 

  def match_additive_expression(self): 
    root = "additive_expression" 
    children = [] 
    children.append(self.match_multiplicative_expression()).append(self.match_plusminus()).append(self.match_multiplicative_expression())
    return [root, children] 

  def match_external_declaration(self): 
    root = "external_declaration" 
    children = [] 
    if currenttoken in terminaldict["type_specifier"]: 
      children.append(self.match_external_next())
    if currenttoken in terminaldict["choose_declarator"]: 
      children.append(self.match_function_definition())
    if currenttoken in terminaldict["type_qualifier"]: 
      children.append(self.match_semicolon())
    if currenttoken == "TYPEDEF": 
      children.append(self.match_semicolon())
    return [root, children] 

  def match_type_specifier(self): 
    root = "type_specifier" 
    children = [] 
    if currenttoken == "VOID": 
      children.append(self.match_void())
    if currenttoken == "CHAR": 
      children.append(self.match_char())
    if currenttoken == "INT": 
      children.append(self.match_int())
    if currenttoken in terminaldict["struct_specifier"]: 
      children.append(self.match_struct_specifier())
    if currenttoken == "TYPE_NAME": 
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
    if currenttoken == "CLOSE_PAREN": 
      children.append(self.match_choose_declarator_next3())
    if currenttoken in terminaldict["parameter_list"]: 
      children.append(self.match_choose_declarator_next3())
    if currenttoken in terminaldict["pointer"]: 
      children.append(self.match_close_paren())
    if currenttoken in terminaldict["identifier_list"]: 
      children.append(self.match_choose_declarator())
    return [root, children] 

  def match_choose_declarator_next2(self): 
    root = "choose_declarator_next2" 
    children = [] 
    if currenttoken in terminaldict["logical_or_expression"]: 
      children.append(self.match_choose_declarator_next3())
    if currenttoken == "CLOSE_BRACKET": 
      children.append(self.match_choose_declarator_next3())
    return [root, children] 

  def match_type_name(self): 
    root = "type_name" 
    children = [] 
    children.append(self.match_type_qualifier_specifier()).append(self.match_type_name_next())
    return [root, children] 

  def match_choose_declarator(self): 
    root = "choose_declarator" 
    children = [] 
    if currenttoken == "IDENTIFIER": 
      children.append(self.match_identifier())
    if currenttoken in terminaldict["choose_declarator_next"]: 
      children.append(self.match_choose_declarator_next())
    if currenttoken == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_postfix_expression(self): 
    root = "postfix_expression" 
    children = [] 
    children.append(self.match_primary_expression()).append(self.match_postfix_expression_next())
    return [root, children] 

  def match_compilerdir_or_external_declaration(self): 
    root = "compilerdir_or_external_declaration" 
    children = [] 
    if currenttoken in terminaldict["define_directive"]: 
      children.append(self.match_define_directive())
    if currenttoken in terminaldict["external_declaration"]: 
      children.append(self.match_external_declaration())
    return [root, children] 

  def match_pointer_next(self): 
    root = "pointer_next" 
    children = [] 
    if currenttoken in terminaldict["type_qualifier"]: 
      children.append(self.match_optional_pointer())
    if currenttoken in terminaldict["pointer"]: 
      children.append(self.match_pointer())
    if currenttoken == "EPSILON": 
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
    children.append(self.match_additive_expression()).append(self.match_l_opg_ople_opge_op()).append(self.match_additive_expression())
    return [root, children] 

  def match_statement(self): 
    root = "statement" 
    children = [] 
    if currenttoken in terminaldict["compound_statement"]: 
      children.append(self.match_compound_statement())
    if currenttoken in terminaldict["selection_statement"]: 
      children.append(self.match_selection_statement())
    if currenttoken in terminaldict["iteration_statement"]: 
      children.append(self.match_iteration_statement())
    if currenttoken in terminaldict["jump_statement"]: 
      children.append(self.match_jump_statement())
    return [root, children] 

  def match_direct_abstract_declarator_next(self): 
    root = "direct_abstract_declarator_next" 
    children = [] 
    if currenttoken == "OPEN_BRACKET": 
      children.append(self.match_direct_abstract_declarator_next())
    if currenttoken == "OPEN_PAREN": 
      children.append(self.match_direct_abstract_declarator_next1())
    return [root, children] 

  def match_struct_declarator_list(self): 
    root = "struct_declarator_list" 
    children = [] 
    children.append(self.match_choose_declarator()).append(self.match_comma()).append(self.match_choose_declarator())
    return [root, children] 

  def match_direct_declarator(self): 
    root = "direct_declarator" 
    children = [] 
    if currenttoken == "IDENTIFIER": 
      children.append(self.match_identifier())
    if currenttoken == "OPEN_PAREN": 
      children.append(self.match_direct_declarator_next1())
    if currenttoken == "OPEN_BRACKET": 
      children.append(self.match_direct_declarator_next2())
    return [root, children] 

  def match_unary_operator(self): 
    root = "unary_operator" 
    children = [] 
    if currenttoken == "ADDRESS_OP": 
      children.append(self.match_address_op())
    if currenttoken == "POINTER": 
      children.append(self.match_pointer())
    if currenttoken == "POS": 
      children.append(self.match_pos())
    if currenttoken == "NEG": 
      children.append(self.match_neg())
    if currenttoken == "NOT": 
      children.append(self.match_not())
    return [root, children] 

  def match_type_qualifier_specifier(self): 
    root = "type_qualifier_specifier" 
    children = [] 
    if currenttoken in terminaldict["type_qualifier"]: 
      children.append(self.match_type_specifier())
    if currenttoken in terminaldict["type_specifier"]: 
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

  def match_assignment_expression(self): 
    root = "assignment_expression" 
    children = [] 
    children.append(self.match_unary_expression()).append(self.match_eq_op()).append(self.match_assignment_expression())
    return [root, children] 

  def match_parameter_declaration(self): 
    root = "parameter_declaration" 
    children = [] 
    children.append(self.match_declaration_specifiers()).append(self.match_parameter_declaration_next())
    return [root, children] 

  def match_multiplicative_expression(self): 
    root = "multiplicative_expression" 
    children = [] 
    children.append(self.match_unary_expression()).append(self.match_multdividemod()).append(self.match_unary_expression())
    return [root, children] 

  def match_define_type(self): 
    root = "define_type" 
    children = [] 
    if currenttoken == "NUM_CONST": 
      children.append(self.match_num_const())
    if currenttoken == "STRING_LITERAL": 
      children.append(self.match_string_literal())
    return [root, children] 

  def match_argument_expression_list(self): 
    root = "argument_expression_list" 
    children = [] 
    children.append(self.match_assignment_expression()).append(self.match_comma()).append(self.match_assignment_expression())
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
    if currenttoken == "OPEN_BRACKET": 
      children.append(self.match_close_bracket())
    if currenttoken == "OPEN_PAREN": 
      children.append(self.match_postfix_expression_next_brace())
    if currenttoken == "PERIOD": 
      children.append(self.match_identifier())
    if currenttoken == "PTR_OP": 
      children.append(self.match_identifier())
    if currenttoken == "INC_OP": 
      children.append(self.match_inc_op())
    if currenttoken == "DEC_OP": 
      children.append(self.match_dec_op())
    return [root, children] 

  def match_equality_expression(self): 
    root = "equality_expression" 
    children = [] 
    children.append(self.match_relational_expression()).append(self.match_eq_opne_op()).append(self.match_relational_expression())
    return [root, children] 

  def match_primary_expression(self): 
    root = "primary_expression" 
    children = [] 
    if currenttoken == "IDENTIFIER": 
      children.append(self.match_identifier())
    if currenttoken == "NUM_CONST": 
      children.append(self.match_num_const())
    if currenttoken == "STRING_LITERAL": 
      children.append(self.match_string_literal())
    if currenttoken == "OPEN_PAREN": 
      children.append(self.match_close_paren())
    return [root, children] 

  def match_declaration_specifiers(self): 
    root = "declaration_specifiers" 
    children = [] 
    if currenttoken in terminaldict["type_qualifier_specifier"]: 
      children.append(self.match_init_declarator_list())
    if currenttoken == "TYPEDEF": 
      children.append(self.match_type_specifier())
    return [root, children] 

  def match_declaration(self): 
    root = "declaration" 
    children = [] 
    children.append(self.match_declaration_specifiers()).append(self.match_semicolon()).append(self.match_declaration_specifiers()).append(self.match_semicolon())
    return [root, children] 

  def match_struct_specifier_cont(self): 
    root = "struct_specifier_cont" 
    children = [] 
    if currenttoken == "OPEN_BRACE": 
      children.append(self.match_close_brace())
    if currenttoken == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_logical_and_expression(self): 
    root = "logical_and_expression" 
    children = [] 
    children.append(self.match_equality_expression()).append(self.match_and_op()).append(self.match_equality_expression())
    return [root, children] 

  def match_init_declarator_list(self): 
    root = "init_declarator_list" 
    children = [] 
    children.append(self.match_choose_declarator()).append(self.match_init_declarator()).append(self.match_comma()).append(self.match_choose_declarator()).append(self.match_init_declarator())
    return [root, children] 

  def match_identifier_list(self): 
    root = "identifier_list" 
    children = [] 
    children.append(self.match_identifier()).append(self.match_comma()).append(self.match_identifier())
    return [root, children] 

  def match_jump_statement(self): 
    root = "jump_statement" 
    children = [] 
    if currenttoken == "CONTINUE": 
      children.append(self.match_semicolon())
    if currenttoken == "BREAK": 
      children.append(self.match_semicolon())
    if currenttoken in terminaldict["expression_statement"]: 
      children.append(self.match_expression_statement())
    return [root, children] 

  def match_function_definition(self): 
    root = "function_definition" 
    children = [] 
    if currenttoken in terminaldict["declaration_list"]: 
      children.append(self.match_compound_statement())
    if currenttoken in terminaldict["compound_statement"]: 
      children.append(self.match_compound_statement())
    return [root, children] 

  def match_external_next2(self): 
    root = "external_next2" 
    children = [] 
    if currenttoken in terminaldict["external_init_declarator_list"]: 
      children.append(self.match_semicolon())
    if currenttoken in terminaldict["function_definition"]: 
      children.append(self.match_function_definition())
    return [root, children] 

  def match_parameter_list(self): 
    root = "parameter_list" 
    children = [] 
    children.append(self.match_parameter_declaration()).append(self.match_comma()).append(self.match_parameter_declaration())
    return [root, children] 

  def match_type_name_next(self): 
    root = "type_name_next" 
    children = [] 
    if currenttoken in terminaldict["pointer"]: 
      children.append(self.match_choose_declarator())
    if currenttoken == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_compound_statement_next(self): 
    root = "compound_statement_next" 
    children = [] 
    if currenttoken == "CLOSE_BRACE": 
      children.append(self.match_close_brace())
    if currenttoken in terminaldict["statement_list"]: 
      children.append(self.match_close_brace())
    if currenttoken in terminaldict["declaration_list"]: 
      children.append(self.match_compound_statement_next1())
    return [root, children] 

  def match_struct_specifier(self): 
    root = "struct_specifier" 
    children = [] 
    children.append(self.match_struct()).append(self.match_struct_specifier_next())
    return [root, children] 

  def match_direct_abstract_declarator_next1(self): 
    root = "direct_abstract_declarator_next1" 
    children = [] 
    if currenttoken == "CLOSE_PAREN": 
      children.append(self.match_close_paren())
    if currenttoken in terminaldict["parameter_list"]: 
      children.append(self.match_close_paren())
    return [root, children] 

  def match_direct_declarator_next2(self): 
    root = "direct_declarator_next2" 
    children = [] 
    if currenttoken in terminaldict["logical_or_expression"]: 
      children.append(self.match_direct_declarator())
    if currenttoken == "CLOSE_BRACKET": 
      children.append(self.match_direct_declarator())
    return [root, children] 

  def match_declaration_list(self): 
    root = "declaration_list" 
    children = [] 
    children.append(self.match_declaration()).append(self.match_declaration())
    return [root, children] 

  def match_selection_statement_next(self): 
    root = "selection_statement_next" 
    children = [] 
    if currenttoken == "ELSE": 
      children.append(self.match_statement())
    if currenttoken == "EPSILON": 
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
    if currenttoken == "CLOSE_BRACKET": 
      children.append(self.match_close_bracket())
    if currenttoken in terminaldict["logical_or_expression"]: 
      children.append(self.match_close_bracket())
    return [root, children] 

  def match_choose_declarator_next(self): 
    root = "choose_declarator_next" 
    children = [] 
    if currenttoken == "OPEN_PAREN": 
      children.append(self.match_choose_declarator_next1())
    if currenttoken == "OPEN_BRACKET": 
      children.append(self.match_choose_declarator_next2())
    return [root, children] 

  def match_translation_unit(self): 
    root = "translation_unit" 
    children = [] 
    children.append(self.match_compilerdir_or_external_declaration()).append(self.match_compilerdir_or_external_declaration())
    return [root, children] 

  def match_init_declarator(self): 
    root = "init_declarator" 
    children = [] 
    if currenttoken == "EQ_OP": 
      children.append(self.match_initializer())
    if currenttoken == "EPSILON": 
      children.append(self.match_epsilon())
    return [root, children] 

  def match_statement_list(self): 
    root = "statement_list" 
    children = [] 
    children.append(self.match_statement()).append(self.match_statement())
    return [root, children] 

  def match_expression(self): 
    root = "expression" 
    children = [] 
    children.append(self.match_assignment_expression()).append(self.match_comma()).append(self.match_assignment_expression())
    return [root, children] 

  def match_logical_or_expression(self): 
    root = "logical_or_expression" 
    children = [] 
    children.append(self.match_logical_and_expression()).append(self.match_or_op()).append(self.match_logical_and_expression())
    return [root, children] 


 
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
