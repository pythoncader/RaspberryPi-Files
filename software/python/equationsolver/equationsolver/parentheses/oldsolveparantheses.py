import equationsolver.terms.terms as terms
def parantheses(halftermslist):
    paranthesesterms_indexes = []
    runtime = 0
    myparanthesesterm = []
    for i in range(0, len(halftermslist)): #find all of the terms with parantheses and add them to a list
        if '(' in halftermslist[i]:
            paranthesesterms_indexes.append(i)

    for i in range(0, len(paranthesesterms_indexes)): #loop through the parantheses terms
        paranthesesterm_inner = []
        multiplied = []
        paranthesesterm = halftermslist[paranthesesterms_indexes[i]] #string of parantheses term
        paranthesesterm_index = i #index of paranthesesterm in terms list
        paranthesesterm = list(paranthesesterm)
        print(paranthesesterm)

        
        while '(' in paranthesesterm:
            if runtime == 0:
                num_of_parantheses = 0
                myparanthesesterm.extend(paranthesesterm)

            if '*' == myparanthesesterm[0]:
                multiplied.append([True, num_of_parantheses])
                del myparanthesesterm[0]

            del myparanthesesterm[0]
            del myparanthesesterm[-1]

            print(paranthesesterm)

            if '(' in myparanthesesterm:
                paranthesesterm_inner.extend(terms.termer(myparanthesesterm, True))
                print("line 30:", paranthesesterm_inner)

                myparanthesesterm = []
                myparanthesesterm.extend(paranthesesterm_inner)
            break