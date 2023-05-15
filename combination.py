import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arrayEins, arrayZwei, axis = None):
   
   arrayEins = arrayEins.reshape((1,6))
   arrayZwei = arrayZwei.reshape((1,4))
   if axis == None:
       axis = 0

   if arrayEins.shape[axis] == arrayZwei.shape[axis]:
      neu = np.append(arrayEins,arrayZwei)
      return neu
   else:
      raise TypeError("The combination is not possible") 
   
   

    
  


if __name__ == "__main__":
    # use this for your own testing!
   
   a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
   b = np.ones((2,2))

   #result = combination(a,b)
   #print(result)
