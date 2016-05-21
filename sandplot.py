
  def match_possible_declaration_specifiers_semicolon(self):
    children =  []
    if currenttoken in terminaldict["declaration_specifiers"]:
      children.append(match_declaration_specifiers).append(match_semicolon)
      children = children + self.match_possible_declaration_specifiers_semicolon()
      return children 
    else:
      return [] 
      
  def match_possible_compilerdir_or_external_declaration(self):
    children = []
    if currenttoken in terminaldict["compilerdir_or_external_declaration"]:
      children.append(self.match_compilerdir_or_external_declaration())
      children = children + self.match_possible_compilerdir_or_external_declaration()
      return children
    else:
      return []

  def match_possible_comma_choose_declarator_init_declarator(self):
    children = []
    if currenttoken == "COMMA":
      children.append(self.match_comma()).append(self.match_choose_declarator()).append(self.match_init_declarator())
      children = children + self.match_possible_comma_choose_declarator_init_declarator()
      return children
    else:
      return []

  def match_possible_comma_parameter_declaration(self):
    children = []
    if currenttoken == "COMMA":
      children.append(self.match_comma()).append(self.match_parameter_declaration())
      children = children + self.match_possible_comma_parameter_declaration()
      return children
    else:
      return []

  def match_possible_direct_declarator_next(self):
    children = []
    if currenttoken in terminaldict["direct_declarator_next"]:
      children.append(self.match_direct_declarator_next())
      children = children + self.match_possible_direct_declarator_next()
      return children
    else:
      return []

  def match_possible_comma_identifier(self):
    children = []
    if currenttoken == "COMMA":
      children.append(self.match_comma()).append(match_identifier())
      children = children + self.match_possible_comma_identifier()
      return children
    else:
      return []

  def match_possible_struct_declaration(self):
    children = []
    if currenttoken in terminaldict["struct_declaration"]:
      children.append(self.match_struct_declaration())
      children = children + self.match_possible_struct_declaration()
      return children
    else:
      return []

  def match_possible_postfix_expression_next(self):
    children = []
    if currenttoken in terminaldict["postfix_expression_next"]:
      children.append(self.match_postfix_expression_next())
      children = children + self.match_possible_postfix_expression_next()
      return children
    else:
      return []

  def match_possible_comma_assignment_expression(self):
    children = []
    if
    if currenttoken == "COMMA":
      children.append(self.match_comma()).append(self.match_assignment_expression())
      children = children + self.match_possible_comma_assignment_expression()
      return children
    else:
      return []


  def match_possible_multdividemod_unary_expression(self):
    children = []
    if
    if currenttoken == "MULT" or currenttoken == "DIV" or currenttoken == "MOD":
      children.append(self.match_multdividemod()).append(self.match_unary_expression())
      children = children + self.match_possible_multdivmod_unary_expression())
      return children
    else:
      return []

  def match_possible_plusminus_multiplicative_expression(self):
    children = []
    if
    if currenttoken == "PLUS" or currenttoken == "MINUS":
      children.append(self.match_plusminus()).append(self.match_multiplicative_expression())
      children = children + self.match_possible_plusminus_multiplicative_expression()
      return children
    else:
      return []

  def match_possible_lop_gop_leop_geop_additive_expression(self):
	# (L_OP|G_OP|LE_OP|GE_OP)
    children = []
    if currenttoken == "L_OP" or currenttoken == "G_OP" or currenttoken == "LE_OP" or currenttoken == "GE_OP":
      children.append(self.match_lop_gop_leop_geop()).append(self.match_additive_expression())
      children = children + self.match_possible_eq_opne_op_relational_expression()
      return children 
    else:
      return []

  def match_possible_eq_opne_op_relational_expression(self): 
	#relational_expression { (EQ_OP|NE_OP) relational_expression }
    children = []
    if currenttoken == "EQ_OP" or currenttoken == "NE_OP":
      children.append(self.match_eq_opne_op()).append(self.match_relational_expression())
      children = children + self.match_possible_eq_opne_op_relational_expression()
      return children
    else:
      return []

  def match_possible_and_op_equality_expression(self):
	#equality_expression { AND_OP equality_expression }
    children = []
    if currenttoken == "AND_OP":
      children.append(self.match_and_op()).append(self.match_equality_expression())
      children = children + self.match_possible_and_op_equality_expression()
      return children
    else:
      return []

  def match_possible_or_op_equality_expression(self):
	#logical_and_expression { OR_OP logical_and_expression }
     children = []
    if currenttoken == "OR_OP":
      children.append(self.match_or_op()).append(self.match_equality_expression())
      children = children + self.match_possible_or_op_equality_expression()
      return children
    else:
      return []

  def match_possible_eq_op_assignment_expression(self):
	#unary_expression { EQ_OP assignment_expression }
    children = []
    if currenttoken == "EQ_OP":
      children.append(self.match_eq_op()).append(self.match_assignment_expression())
      children = children + self.match_possible_eq_op_assignment_expression()
      return children
    else:
      return []

  def match_possible_statement(self):
	#statement { statement }
    children = []
    if
    if currenttoken in terminaldict["statement"]:
      children.append(self.match_statement())
      children = children + self.match_possible_statement()
      return children
    else:
      return []

  def match_possible_declaration(self):
	#declaration { declaration }
    children = []
    if currenttoken in terminaldict["declaration"]:
      children.append(self.match_declaration())
      children = children + self.match_possible_declaration()
      return children
    else:
      return []

