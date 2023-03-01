# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list, start_index, end_index) -> list:
    output_list = []

    i = start_index

    while(i < end_index and i < len(input_list)):
        output_list.append(input_list[i])
    
    return output_list

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list, step_size) -> list:
    result = []
    for i in range(0, len(input_list), step_size):
        result.add(input_list[i])
    return result

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list : list) -> bool:
    for i in range(0, len(input_list), 1):
        for j in range(len(input_list)-1, 0, -1):
            if j != i:
                if input_list[i]==input_list[j]:
                    return False
    return True

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list : list) -> list:
    result = []

    for sub_list in input_list:
        for x in sub_list:
            result.append(x)

    return result

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args) -> list:
    result = []
    for l in args:
        result = result + l
    return result

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list : list) -> list:
    result = []
    for sub_tuple in input_list:
        sub_result=()
        for i in range(len(sub_tuple)-1, 0, -1):
            sub_result = sub_result + sub_tuple[i]
        result.append(sub_result)

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_tuplicates(input_list : list) -> list:
    for i in range(0, len(input_list), 1):
        for j in range(len(input_list)-1, 0, -1):
            if j != i:
                if input_list[i]==input_list[j]:
                    input_list.remove(input_list[i])
    return input_list

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list : list) -> list:
    result = []

    for i in range(input_list):
        subresult=[]
        for i in range[input_list[i]]:
            subresult.append(0)
        result.append(subresult)

    for i in range(input_list):
        for j in range(input_list[i]):
            result[i][j]=input_list[j][i]
    
    return result

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list : list, chunk_size : int) -> list:
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i:i + chunk_size]
    return input_list

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict) -> dict:
    result = {}
    for d in dict:
        result.update(d)
    return result

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list : list) -> dict:
    even = []
    odd = []
    for x in input_list:
        if x & 1:
            odd.append(x)
        else:
            even.append(x)

    return {'even' : even, 'odd' : odd}

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict : dict) -> dict:
    result = {}
    for key, value in input_dict.items():
        mean = 0
        for x in value:
            mean = mean + x
        result[key] = mean / len(value)
    return result

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


