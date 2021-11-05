#Author: Nils Becker

import spacy

def evaluate(input):
    '''
    Returns whether an input string is a rule,
    template, assertion or none
    '''
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input)
    tokens = [token for token in doc]
    if tokens[0].dep_ == "compound" or tokens[0].dep_ == 'nsubj':
        return evaluateTemplate(tokens)
    if tokens[0].dep_ == "expl":
        return evaluateAssertion(tokens)
    if tokens[0].dep_ == "mark":
        return evaluateRule(tokens)
    return ("", False)


def evaluateTemplate(tokens):
    '''
    This method checks if the input is a template and if so, returns the rule
    '''
    nominator = tokens[0].text
    properties = [token.text for token in tokens if (token.dep_ == 'pobj' or token.dep_ == 'conj')]
    result = "(deftemplate: " + nominator + "\n\t"
    for property in properties:
        result = result +'(slot ' + property + ')'
    return result +")" , True

def evaluateAssertion(tokens):
    '''
    This method checks if the input is comparable to an assertion and if so, returns the assertion
    '''
    subsets = []
    buffer = []
    for token in tokens:
        buffer.append(token)
        if token.dep_ == 'punct' or token.dep_ == 'cc':
            subsets.append(buffer)
            buffer = []
    subsets.append(buffer)
    slotContent = ""
    result = "(assert("
    for subset in subsets:
        for token in subset:
            if token.dep_ == 'dobj' or token.dep_ == 'attr':
                result += token.text + "("
            if token.dep_ == 'appos' or token.dep_ == 'npadvmod' or token.dep_== 'oprd' or token.dep_ == 'amod':
                #slotContent = "'" + token.text + "'"
                slotContent = "'" + token.text + "')"
            if token.dep_ == 'pobj' or token.dep_ =='acl' or token.dep_ =='conj':
                #slot = token.lemma_
                result += token.lemma_ + "(" + slotContent 
    return result + "))", True

def evaluateRule(tokens):
    '''
    Checks if the input is a rule and if so, returns the rule
    '''
    subsets = []
    buffer = []
    for token in tokens:
        buffer.append(token)
        if token.dep_ == 'expl':
            subsets.append(buffer)
            buffer = []
    subsets.append(buffer)
    #get resulting assertions
    assertions = []
    for i in range(2, len(subsets)):
        if(evaluateAssertion(subsets[i])[1]):
            assertions.append(evaluateAssertion(subsets[i])[0])
    name = ""
    slot = ""
    content = ""
    for i in range (len(subsets[1])):
        if(subsets[1][i].dep_ == 'dobj'):
            name = subsets[1][i].text
        if(subsets[1][i].dep_ == 'acl' or subsets[1][i].dep_ == 'pobj'):
            slot = subsets[1][i].lemma_
        if(subsets[1][i].dep_ == 'oprd' or subsets[1][i].dep_ == 'amod'):
            content = subsets[1][i].text
    result =  "(defrule rule:\n\t(" + name + "(" + slot + "('" + content +"'))  =>  "
    for assertion in assertions:
        result += assertion+" " 
    return result+")", True

#Input/Output
'''
Sample Inputs:
    House template has properties of roof, garden, and balcony.
    There exists a house with a big roof, a small garden and a wide balcony
    Roof template has properties of color.
    There exists a roof with a red color.
    There exists a roof with a black color.
    If there exists a roof with black color then there exists a roof with a yellow color.   
'''
kb = []
while True:
    inp = input("Insert a rule, an template or an assertion (enter 'q' to stop extending): ")
    if(inp == "q"):
        break
    result = evaluate(inp)
    if(result[1]):
        print("In CLIPS your input would translate to:\n"+str(result[0]))
        kb.append(result[0])
    else:
        print("Wrong Syntax")
    
print("\nYou have collected:")
for content in kb:
    print(content)
