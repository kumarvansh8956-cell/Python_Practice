# String! a sequence of character under closed in qutes. It's a immutable datatype.
a = "hello python"
# we can find the length like this
print(len(a))
# We can call any specific charactor withim the given string using indexing
print(a[0:3])
# We can also call the charactor in reverse order using negative indexing
print(a[-1])
# We can also call the charactor in reverse order using negative indexing
print(a[-1::-1])
''' Here the legendary slicing confusing as hell, but not biggie.a[s_i:e_i:j_c].
here s_i is starting index,e_i is ending index and j_c is step or jump count. 
important note the charactor at e_i never return'''
print(a[0:10:2])
print(a[0:10:3])
print(a[0:10:4])
# The build in function for string in the python
print(a.capitalize()) # it capitalise the first charactor
print(a.casefold()) # it switch the case 
print(a.center(10)) # it give the space from front and set our string in center
print(a.center(10,"$")) # we can switch the blankspace with any specific charactor
print(a.count("l")) # count the repeation of any specific charactor or substring
print(a.lower()) # it switch to lowercase
print(a.strip()) # it remove leading and ladding blankspace or charactor
print(a.split(" ")) # it split the string from any position
print(a.replace("hello","hi")) # it replaace a string with another given one