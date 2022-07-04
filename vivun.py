# some cypress script for front end of hero
# 2 focused engineers for smoke testing & automatic release

# Input: 
x = [1, 2, 3,None, None, None, None]    
y = [2, 4, 6, 100] 
      

def merge_lists(A, B):
  A_vals = [i for i in A if i is not None]
  indx_a = len(A_vals) - 1 # last non empty element B
  indx_b = len(B) - 1 # last element of B
  indx_current = len(A) - 1 # current working element
  while indx_a >= 0 and indx_b >= 0:
    if A[indx_a] < B[indx_b]:
      A[indx_current] = B[indx_b]
      indx_b -= 1
      indx_current -= 1
    
    else:
      A[indx_a + 1] = A[indx_a]
      A[indx_a] = None
      indx_a -= 1
      indx_current -= 1
   

merge_lists(x,y)
print(x)


'''final interview

alex sets ml strategy
vivun solves attention, engineers want to work on what's cool; salespeople don't unerstand how product works
what are the most imprtant thins for eng to do bases on salespoeple

customer says i wish for this feature, salespoeple take notes - "customer needs geocoding for targeted ads"
" i want zipcode targeting"
all is location based targeting

then you can take those to engineer to say what is most wanted. join

sum $$ for each feature. 
bayesian 
try to figure out causal structure of how deals work 
    environmental factors (competition)
    timing
    doing test drive, proof of value
    
    '''