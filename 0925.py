
mylist = [ 45, 20, 21, 50, 10, 8, 9, 7, 10]
def bubble(A):
    length = len(A) - 1
    unsorted = True

    while unsorted:
    	for i in range(0,length):
		    unsorted = False
		    if A[i] > A[i + 1]:
			    hold = A[i + 1]
			    A[i + 1] = A[i]
			    A[i] = hold
			    print A
		    else:
			    unsorted = True
print bubble(mylist)


