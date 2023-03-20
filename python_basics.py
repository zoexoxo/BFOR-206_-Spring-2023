#####
# This script will demonstrate some of the basic operations in
# python, like if statements, for loops and functions
#####

# %% create a basic function

def new_function():
    pass

#pass allows it to ignore it without giving us an error when we run it

# %% run new function

new_function()


# %%

def func2(arg1):
#This function accepts an argument and prints them out

    print("The argument is", arg1)

# %% fun fuc2
func2("Hello World")
func2()

# %%

def func3(arg1, arg2=True):
    if arg2:
        print("arg2 is True!")
    print("arg1 is", arg1)

#%%
func3('test')
func3('test2, False')

#use named arguments
print(' example with named args:')
func3(arg2=True, arg1=123)
# %%
def add_numbers(a, b):
#this number adds two numbers together
    result = a + b

    return result

#%%
c = add_numbers(2,123)


# %%
assert add_numbers(2,2) == 4
assert add_numbers(4, -1) == 3
assert add_numbers(3.2, 1.4) == 4.6

# %% lab preparation

my_list = ['Hello', 'BFOR', '206', None, 'Bye']

#%% for loop over list
for item in my_list:
    print(item)

#%% hint for today's lab
a=None

if a:
    print('a has a variiable', a)
else:
    print('a is none')

#%%
for i in range(len(my_list)):
    print('the value of i is', i)
    print('the value of my_list at i is', my_list[i])



# %%
