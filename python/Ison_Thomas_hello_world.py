# 1. TASK: print "Hello World"
print("Hello World!")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
name2 = "Thomas"

print("Hello", name,"!")    # with a comma
print("Hello", name2,"!")
print("Hello " + name + "!")    # with a +
print("Hello " + name2 + "!")

# 3. print "Hello 42!" with the number in a variable
name = "42"
num = "25"

print("Hello " , name, "!")    # with a comma
print("Hello " + name + "!")    # with a +    -- this one should give us an error!
print("Hello " , num, "!")
print("Hello " + num + "!")


# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
fave_food3 = "burgers"
fave_food4 = "lasagna"

print("I love to eat {} and {}.".format(fave_food1, fave_food2) ) # with .format()
print("I love to eat {} and {}.".format(fave_food3, fave_food4) )
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string
print(f"I love to eat {fave_food3} and {fave_food4}.")
