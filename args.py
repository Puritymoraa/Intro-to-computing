def calculate_avg(accept_list):
    
    sum_of_numbers = sum(accept_list)
    number_of_items = len(accept_list)
    
    return sum_of_numbers / number_of_items

accept_list = [1,2,3,4,5]
print(calculate_avg(accept_list))

def calculate_average_2 (*args): #gathering arguments
    sum_of_numbers = sum(args)
    number_of_items = len(args)
    
    return sum_of_numbers / number_of_items

result  = calculate_average_2 (1,2,3,4,5)
print(result)

#concatenate some list

def concatenate_s(*args): #how we can join string together
    result = " ".join(args) #delimeter...that is what we specify before .join()
    
    return result
result = concatenate_s("Hello","Sally","!")
print (result)
    
    
    
#when you have a list as an argument, when you call the function, you have to have the name of your list as an argument
#when you have *name_of_variable as your paramenter, when you call a function, you can give multiple arguments to it. 