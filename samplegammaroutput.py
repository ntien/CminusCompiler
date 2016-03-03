'''
#not pairwise disjoint
1. nonterminala
	: A nonterminalb1
    | nonterminalb2 A
    | B21 nonterminalb3
RHS1: {A}, RHS2: {B21, B22}, RHS3: {B21}


#not pairwise disjoint
2. nonterminalb1
    : nonterminalc2 nonterminalc2
    | nonterminalc3 nonterminalb2
RHS1: {C2, C3}, RHS2: {C2, C3} 


3. nonterminalb2
	: B21 nonterminalc1
    | B22 nonterminalc2  
RHS1: {B21}, RHS2:{B22}


#pairwise disjoint
4. nonterminalb3
	: B31 nonterminalc1 
    | B32 nonterminalc2
    | B33 nonterminalc1 nonterminalc2
RHS1: {B31}, RHS2: {B32}, RHS3: {B33} 


#not pairwise disjoint
5. nonterminalc1
    : C1 C2
    | C1 nonterminalc2
RHS1: {C1}, RHS2: {C1}


#pairwise disjoint
6. nonterminalc2
    : C2 C3
    | C3 C2
RHS1: {C2}, RHS2: {C3}

#not pairwise disjoint
7. nonterminalc3
    : nonterminalc2 C3
    | C3
RHS1: {C2, C3}, RHS2: {C3} 

'''


