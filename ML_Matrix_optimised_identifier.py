#Project Using Matrix Chain Multiplication


#Function that returns the Cost/salar multiplications for the matrix multiplication using Dynamic Programming
def mCM(arrelem):
 
    #variable n is used here to calculate the size of array
    n = len(arrelem)
 
    # c[i,j] = minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i]M[i+1]...M[j] = M[i..j]

    # The cost is zero when multiplying one matrix
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    for length in range(2, n + 1):  #Iteration through Subsequence lengths
 
        for i in range(1, n - length + 2):
 
            j = i + length - 1
            c[i][j] = float('inf')
 
            k = i
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + arrelem[i - 1] * arrelem[k] * arrelem[j]
 
                if cost < c[i][j]:
                    c[i][j] = cost
 
                k = k + 1
 
    # return min cost to multiply Matrix[j+1]..Matrix[j]
    return c[1][n - 1]

if __name__ == '__main__':

    #initializing arrcost which will store the cost of all the sequences of each array's chain multiplication 
    arrcost=[] 

    #taking size of array for matrix as input
    nosize=int(input("How many numbers you want to store for the matrix chain multiplication?\n"))

    #storing elements in arrelem array
    arrelem=[]

    #asking the user for the number of sequences he/she want to check
    size=int(input("How many sequences you want to check to find the optimised one?\n"))

    #iterating till the number of sequences given as input by user 
    for z in range(size):
        # Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
        
        print("For Sequence No. {}".format(z+1)) #printing the sequence number
                
        #printing lines for better visibility
        print("---------------------------------------------------")

        #taking the elements in arrelem array to check for cost of the matrix chain
        for x in range(nosize):
            dims=int(input("Enter the elements "))
            arrelem.append(dims)
        
        #storing the cost in optmres variable and then appending it to arrcost array
        #This mechanism works till the number of sequences
        optmres=mCM(arrelem)
        arrcost.append(optmres)
        arrelem=[]

        #printing lines for better visibility
        print("---------------------------------------------------\n")

    #indexmin variable stores the index which have minimum value element
    indexmin=arrcost.index(min(arrcost))
    
    print("All the sequences with their operations are {} and among them ".format(arrcost))

    #sorting the array such that we get the minimum value at 0th index 
    arrcost.sort()
    
    print("Best sequence for the ML model that runs in least time will be the sequence no : {} and the no of operations will be {}".format(indexmin+1,arrcost[0]))


#Sample input and Output:
'''
How many numbers you want to store for the matrix chain multiplication?
5
How many sequences you want to check to find the optimised one?
3
For Sequence No. 1
---------------------------------------------------
Enter the elements 10
Enter the elements 12
Enter the elements 24
Enter the elements 36
Enter the elements 5
---------------------------------------------------

For Sequence No. 2
---------------------------------------------------
Enter the elements 5
Enter the elements 24
Enter the elements 12
Enter the elements 36
Enter the elements 10
---------------------------------------------------

For Sequence No. 3
---------------------------------------------------
Enter the elements 10
Enter the elements 36
Enter the elements 24
Enter the elements 5
Enter the elements 12
---------------------------------------------------

Best sequence for your ML model that runs in least time will be the sequence no : 2 and the no of operations will be 5400
'''