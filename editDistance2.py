import cython
@cython.cfunc
def editDistDP(str1, str2):
    m: cython.int = len(str1)
    n: cython.int = len(str2)
    # Create a table to store results of subproblems
    dp : list = []
    for x in range(m + 1):
        dp.append([0 for x in range(n + 1)])
 
    # Fill d[][] in bottom up manner
    i: cython.int
    j: cython.int
    for i in range(m + 1):
        for j in range(n + 1):
 
            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
 
    return dp[m][n]

class collation:
    def __init__(self,string):
        self.string = string

    def collate(self,str1,str2):
        str1Dist = editDistDP(str1,self.string)
        str2Dist = editDistDP(str2,self.string)
        if str1Dist < str2Dist:
            return 1
        elif str2Dist == str1Dist:
            return 0
        return -1

#print(collation("banana").collate("g","vvrvrg"))