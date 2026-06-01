# list,tuple,dictionary&set
List = [1,0.2,True,"hello"] # this is a list
Tuple_1 = 1,0.2,True,"hello"  # this is a tuple. its also can declare as tuple = (1,0.2,True,"hello")
Tuple_2 = (1,0.2,True,"hello")
Dic = {"key":"value","vansh":99}
Set = {1,0.2,True,"hello"}

# type checking
print(type(List), type(Tuple_2), type(Tuple_1), type(Dic),type(Set))
Ty_ty =type(Set)
print( type(Ty_ty))
# fetching the items
print(List[0],List[1]) # both tuple and list use indexing.
print(Tuple_1[0],Tuple_1[1]) # we can fetch their item using indexing like string
print(Dic["key"]) # distionary does not have indexing. we fetch its items by the help of key
# set also does not have indexing nor key. we use ' in ' with loop or type convertion for fetch it item
L_s = list(Set)
print(L_s[0])

# method for data strutures
'''----------------------xxxxxxxxxxxx-----------------------------'''
# for list
print("Original List:", List)

List.append("new_item")        # add element
List.remove(True)              # remove element (True treated as 1 in Python)
List.insert(1, "inserted")     # insert at index
popped = List.pop()            # remove last element

print("Updated List:", List)
print("Popped from List:", popped)

# for tuple

print("\nTuple_1:", Tuple_1)
print("Count of 1:", Tuple_1.count(1))
print("Index of 'hello':", Tuple_1.index("hello"))


# TUPLE 2 (with brackets)
Tuple_2 = (1, 0.2, True, "hello")

print("\nTuple_2:", Tuple_2)
print("Same as Tuple_1? ->", Tuple_1 == Tuple_2)
# for dictionary

print("\nOriginal Dictionary:", Dic)

Dic["AI"] = "ML"              # add new key-value
Dic.update({"vansh": 100})    # update value

print("Keys:", Dic.keys())
print("Values:", Dic.values())
print("Items:", Dic.items())

print("Get vansh:", Dic.get("vansh"))

removed = Dic.pop("key")      # remove key
print("After pop:", Dic)


# for set
print("\nOriginal Set:", Set)
Set.add("new")                 # add element
Set.discard(0.2)              # remove safely
Set.update([10, 20])          # add multiple items

print("Updated Set:", Set)

another_set = {1, "hello", 50}

print("Union:", Set.union(another_set))
print("Intersection:", Set.intersection(another_set))
print("Difference:", Set.difference(another_set))