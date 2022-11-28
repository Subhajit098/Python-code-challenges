# Statement: We are required to find the function that returns the prime factors of a given integer in the form of a list .
# Sample Test Case: 
# Input: 630
# Output: [ 2, 3, 3, 5, 7 ]

def get_prime_factors(num):
    evenList=[]
    i=2
    while(i<=num):
      if(num%i==0):
        evenList.append(i)
        num=num/i
      else:
          i=i+1  
    return evenList
      

num=int(input("Enter: "))
print(get_prime_factors(num))