#'''def print_name(name): #name here is parameter
    #print(name)

#print_name('Alex') #Alex here is argus'''

''' def foo(a,b,*args,**kwargs): 
    print(a,b)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key,kwargs[key])'''

#foo(1,2,3,4,5,six = 6, seven = 7)

#foo(1,2,3,4)

def foo(a,b,*,c,d): #after *, its keyword only parameter
    print(a,b,c,d)

foo(1,2,c=3,d=4)