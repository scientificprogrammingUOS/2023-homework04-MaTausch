import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if not type(loc) is int and not type(loc) is float:
            raise TypeError("The Argument isn`t a number")   
    if not type(scale) is int and not type(scale) is float:
            raise TypeError("The Argument isn`t a number") 
    if not type(lower_bound) is int and not type(lower_bound) is float:
            raise TypeError("The Argument isn`t a number") 
    if not type(upper_bound) is int and not type(upper_bound) is float:
            raise TypeError("The Argument isn`t a number") 
    if upper_bound < lower_bound:
            raise TypeError("Do you even know what upper and lower means?!") 
    
    gaussian_array = np.random.normal(loc = loc, scale = scale, size = 100)
    #print(gaussian_array)
    lower = gaussian_array < upper_bound
    upper = gaussian_array > lower_bound
    gaussian_array = gaussian_array[lower & upper]
    print(gaussian_array)
    mean = 0
    for gau in gaussian_array:
        mean = mean + gau
        #print(mean)

    mean = mean/len(gaussian_array)
    print (mean)
    std = np.std(gaussian_array)

    tupel = (mean, std)
    return tupel


if __name__ == "__main__":
    # use this for your own testing!

    gaussian_analysis(1,2,3,4)
