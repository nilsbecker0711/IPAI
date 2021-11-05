import ast
import nltk

formula = input("Input arithmetic expression: ")
grammar = nltk.CFG.fromstring("""
                                S -> S OP1 S | S OP2 S | E
                                E -> NUM | '(' S ')'
                                OP1 -> '*' | '/'
                                OP2 -> '-'| '+'
                                NUM ->'0' | '1'| '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' |  """ )  
parser = nltk.ChartParser(grammar)
trees = list(parser.parse(formula.split()))  
for tree in trees:
    print("Formula structure:\n", tree)


restore = ast.parse(formula, "", "eval")
#print(tree.fields_)

