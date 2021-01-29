import equationsolver.terms.terms as terms
def parentheses(halftermslist):
    parenthesesterms = []

    for i in range(0, len(halftermslist)): #find all of the terms with parentheses and add them to a list
        if '(' in halftermslist[i]:
            parenthesesterms.append(halftermslist[i])
            print("\nline 8:", parenthesesterms)

    parentheses = {}

    for i in range(0, len(parenthesesterms)):
        parentheses[1] = {"term": list(parenthesesterms[i]), "index": i, "multiplied": False}
        print("\nline 14", parentheses)

        level = 1
        
        while True:
            if '*' == parentheses[level]["term"][0]:
                parentheses[level]["multiplied"] = True
                del parentheses[level]["term"][0]

            del parentheses[level]["term"][0]
            del parentheses[level]["term"][-1]

            parentheses[level]["term"] = terms.termer(parentheses[level]["term"], True)

            print("\nline 25", parentheses)

            for term in range(0, len(parentheses[level]["term"])):
                if '(' in parentheses[level]["term"][term]:
                    parentheses[lastlevel+0.001] = {"term": parentheses[level]["term"][term], "index": term, "multiplied": False}
                    print(parentheses)
                    lastlevel += 0.001
            break
                
            