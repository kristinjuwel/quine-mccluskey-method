import globals
def multiplyMinterms(x,y): 
    '''
    Description:                        multiplies minterms and appends them on the list
    Arguments:
    x, y                                minterm inputs to multiply

    Returns:
    res                                 a refined list
    '''
    res = []
    for i in x:
        if i+"'" in y or (len(i) == 2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            res.append(i)
    return res

def multiplyExpressions(x,y):
    '''
    Description:                        multiplies expressions and appends them on the list
    Arguments:
    x,y                                 terms to multiply

    Returns:
    res                                 a refined list
    '''
    res = []
    for i in x:
        for j in y:
            temp = multiplyMinterms(i,j)
            res.append(temp) if len(temp) != 0 else None
    return res

def refineList(givenList,dontCareList):
    '''
    Description:                        removes the don't care terms from the list
    Arguments:
    givenList, dontCareList             position in the map

    Returns:
    res                                 a refined list
    '''
    res = []
    for i in givenList:
        if int(i) not in dontCareList:
            res.append(i)
    return res

def findEPI(primeChart):
    '''
    Description:                        finds essential prime implicants
    Arguments:
    primeChart                          prime implicants chart

    Returns:
    res                                 a refined list
    '''
    res = []
    for i in primeChart:
        if len(primeChart[i]) == 1:
            res.append(primeChart[i][0]) if primeChart[i][0] not in res else None
    return res

def findVariables(x, variable):
    '''
    Description:                        find variables in a minterm (For example, the minterm --01 has C' and D as variables)
    Arguments:
    x                                   position in the map

    Returns:
                                        variable list
    '''
    ascii = ord(variable)
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append(chr(i+ascii)+"'")
        elif x[i] == '1':
            var_list.append(chr(i+ascii))
    return var_list


def flattenList(x):
    '''
    Description:                        removes the don't care terms from the list
    Arguments:
    x                                   position in the map

    Returns:
    flattened_items                     a refined list
    '''
    flattened_items = []
    for i in x:
        flattened_items.extend(x[i])
    return flattened_items

def findMinterms(a):
    '''
    Description:                        finds which minterms are merged. For example, 10-1 is obtained by merging 9(1001) and 11(1011)
    Arguments:
    a                                   position in the map

    Returns:
    temp                                a temporary list
    '''
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a,2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
    temp = []
    for i in range(pow(2,gaps)):
        temp2,ind = a[:],-1
        for j in x[0]:
            if ind != -1:
                ind = ind+temp2[ind+1:].find('-')+1
            else:
                ind = temp2[ind+1:].find('-')
            temp2 = temp2[:ind]+j+temp2[ind+1:]
        temp.append(str(int(temp2,2)))
        x.pop(0)
    return temp

def compareMinterms(a,b):
    '''
    Description:                        function for checking if 2 minterms differ by 1 bit only
    Arguments:
    a, b                                minterm inputs to compare

    Returns:
    True, mismatch_index                boolean value (hindi ko alam)
    '''
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_index = i
            c += 1
            if c>1:
                return (False,None)
    return (True, mismatch_index)

def removeTerms(chart,terms):
    '''
    Description:                        removes minterms which are already covered from chart
    Arguments:
    _chart, terms                       chart, terms to check

    Returns:
                                        chart with removed redundant minterms
    '''
    for i in terms:
        for j in findMinterms(i):
            try:
                del chart[j]
            except KeyError:
                pass

# Primary grouping of minterms
def grouping(minterms, groups, size):
    '''
    Description:                        groups the primary minterms 
    Arguments:
    minterms, groups, size              the entered minterms plus dontCC, groupings, get size

    Returns:
    None
    '''
    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]
    # Primary grouping ends

#Primary group printing
def print_primary(groups):
    '''
    Description:                        print the primary groups
    Arguments:
    groups                              groupings of minterms

    Returns:
    None
    '''
    
    var3 = ''
    var1 = "\n\n\n\nGroup No.\tMinterms\tBinary of Minterms\n%s"%('='*43)
    for i in sorted(groups.keys()):
        var3 += "\n"+"%5d:"%i+"\n" # Prints group number
        for j in groups[i]:
            var3 +="\n"+"\t\t\t    %-20d\t%s"%(int(j,2),j)+"\n" # Prints minterm and its binary representation
        var3 += "\n"+'-'*43+ "\n"
    return var1+var3
    #Primary group printing ends

def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st
 
# Printing and processing of Prime Implicant chart
def prime_charts(enter_minterms, all_prime, enter_dontCC, variable):
    '''
    Description:                        last function for printing and processing of Prime Implicant chart
    Arguments:
    enter_minterms, all_prime,          The minterms that was inputed, the dont care conditions,
    enter_dontCC                        and all the prime implicants calculated 

    Returns:
    Printed output                      Returns the prime implicants and the primary answer                                  
    '''
    sz = len(str(enter_minterms[-1])) # The number of digits of the largest minterm
    chart = {}
    tuple1 = '\n\n\nPrime Implicants chart:\n\n    Minterms\n'+'='*(len(enter_minterms)*(sz+1)+16)
    str1 = convertTuple(tuple1) + "\n"
    str2 = ''
    strlength = len(enter_minterms)
    str5 = []

    for i in all_prime:
        merged_minterms,y = findMinterms(i), 0
        end =''    
        tuple2 ="         %-26s"%', '.join(merged_minterms), end            
        str2 += convertTuple(tuple2)
        str5 = [' - ']* strlength
        for j in refineList(merged_minterms,enter_dontCC):
            x = enter_minterms.index(int(j))*(sz+2) # The position where we should put 'X'
            str5[enter_minterms.index(int(j))] = ' X '
            

            y = x + sz
            try:
                chart[j].append(i) if i not in chart[j] else None # Add minterm in chart
            except KeyError:
                chart[j] = [i]
        str2 += ''.join(str5)
        str2 += '\n'+'-'*(len(enter_minterms)*(sz+1)+16)+ "\n"
    # Printing and processing of Prime Implicant chart ends


    EPI = findEPI(chart) # Finding essential prime implicants
    tuple3 = "\nEssential Prime Implicants: "+', '.join(str(i) for i in EPI)
    str3 = convertTuple(tuple3)+"\n"
    removeTerms(chart,EPI) # Remove EPI related columns from chart

    if(len(chart) == 0): # If no minterms remain after removing EPI related columns
        final_result = [findVariables(i, variable) for i in EPI] # Final result with only EPIs
    else: # go for further simplification
        P = [[findVariables(j, variable) for j in chart[i]] for i in chart]
        while len(P)>1: # Keep multiplying until we get the SOP form of P
            P[1] = multiplyExpressions(P[0],P[1])
            P.pop(0)
        final_result = [min(P[0],key=len)] # Choosing the term with minimum variables from P
        final_result.extend(findVariables(i, variable) for i in EPI) # Adding the EPIs to final solution
    tuple4 = '\n\nSolution: F = '+' + '.join(''.join(i) for i in final_result)
    str4 = convertTuple(tuple4)+"\n"
    return str1 + str2 + str3 +str4

#Main Function
def driver(variable,minterms, dontCare, sizing):
    '''
    Description:                        The main function is the one responsible for setting up the
                                        tabluar method program., initializing the minterms and calling
                                        the functions within the program                             
    Arguments:
    None         

    Returns:
    None
    '''
    try:
        #for entering given
        enter_minterms = [int(i) for i in minterms.strip().split()]
        
        enter_dontCC = [int(i) for i in dontCare.strip().split()]
        enter_minterms.sort()
        minterms = enter_minterms + enter_dontCC
        minterms.sort()
        sizing = int(sizing)
        if (sizing == 7 or sizing == 8):
            size = len(bin(minterms[-1]))-1
        elif(sizing>8):
            tempo = sizing - 8
            size = len(bin(minterms[-1])) + tempo
        else: 
            size = len(bin(minterms[-1]))-2
        groups, all_prime = {}, set()

        #Function call for primary grouping of minterms
        grouping(minterms, groups, size)   
        #Function call for primary group printing
        globals.var4 = print_primary(groups)

        # Process for creating tables and finding prime implicants starts
        num = 1
        while True:
            tmp = groups.copy()
            groups, key, marked, should_stop = {}, 0, set(), True
            l = sorted(list(tmp.keys()))

            for i in range(len(l)-1):
                for j in tmp[l[i]]: # Loop which iterates through current group elements
                    for k in tmp[l[i+1]]: # Loop which iterates through next group elements
                        compared = compareMinterms(j,k) # Compare the minterms
                        if compared[0]: # If the minterms differ by 1 bit only
                            try:
                                # Put a '-' in the changing bit and add it to corresponding group
                                groups[key].append(j[:compared[1]]+'-'+j[compared[1]+1:]) if j[:compared[1]]+'-'+j[compared[1]+1:] not in groups[key] else None 
                            except KeyError:
                                # If the group doesn't exist, create the group at first and then put a '-' in the changing bit and add it to the newly created group
                                groups[key] = [j[:compared[1]]+'-'+j[compared[1]+1:]] 
                            should_stop = False
                            marked.add(j) # Mark element j
                            marked.add(k) # Mark element k
                key += 1

            local_unmarked = set(flattenList(tmp)).difference(marked) # Unmarked elements of each table
            all_prime = all_prime.union(local_unmarked) # Adding Prime Implicants to global list
            # Printing Prime Implicants of current table
            globals.space = "\n\n"
            globals.status = "STATUS OF EACH TABLE:\n"
            tuple = "\nUnmarked elements(Prime Implicants) of table "+ str(num) +":\n",None if len(local_unmarked)==0 else ', '.join(local_unmarked) +'.'
            globals.unmarked1 += convertTuple(tuple)+"\n"
            
            
            if should_stop: # If the minterms cannot be combined further
                # Print all prime implicants
                tuple02 = "\n\nAll Prime Implicants: ",None if len(all_prime)==0 else ', '.join(all_prime) 
                globals.txt2 = convertTuple(tuple02)
                break

            # Printing of all the next groups starts
            vari3 = ''
            vari1 = "\n\n\n\nGroup No.             Minterms            Binary of Minterms\n"
            vari2 = '='*43+"\n"
            for i in sorted(groups.keys()):
                vari3 += "     %5d:"%i+ "\n" # Prints group number
                for j in groups[i]:
                    vari3 += "\t\t\t\t%-24s     %s"%(','.join(findMinterms(j)),j)+"\n" # Prints minterms and its binary representation
                vari3 +=  "\n"+'-'*43+ "\n"
            globals.vari4 += vari1+vari2+vari3
            
            num += 1
            # Printing of all the next groups ends
        # Process for creating tables and finding prime implicants ends



        #Function call for printing and processing of Prime Implicant chart
        globals.chart = prime_charts(enter_minterms, all_prime, enter_dontCC, variable)
    except Exception as e:
        globals.error = "\n\n\nStill wrong combination was inputed ! ! ! !"
    


"""#Run
if __name__ == "__main__":

    main()
    """