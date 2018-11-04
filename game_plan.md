
# Mad Libs Game Plan
## User Story
As a user, I'll be prompted to enter a noun, verb, or adjective. After the program processes my inputs, I'll be able to view a complete story that features my words in designated places throughout.

## What I need?
- Story Template (probably a string)
- Blank spaces (objects? something to manage these)
- Prompt for user's input, must specify part of speech
- Generate complete story
- Display complete story

## Code requirements
- Variable assignment
- Function definitions
- Core data types: strings, integers, floats
- Collection types: lists, tuples, dictionary

### MVP
**Create story/poem**
```print ("roses are {color}}")
print ("{plural noun} are blue")
print ("I love {celebrity}")
```

**Variables**
```
material = input("Enter a Material: ")
noun = input("Enter a Noun: ")
name = input("Enter a Name: ")

print ("roses are " + color)
print (plural_noun + " are blue")
print ("I love " + celebrity)
```

**Story Snippet**
```print (""" ~ A Memoir ~

Every once in a while,
My """ + material + " slippers end up on the " + noun + ". \n" +
name.upper() + """ knows EXACTLY
How they got there,
But won't spill the beans.
Life is hard enough.
```

### Shortcomings...
- Too many variables?
- I need a way to check if 2 inputs are the same?
- Can I randomize inputs of same type?
- What about .replace() ?
- This looks messy and just a lot
- There must be a better way than using 3 quotes so many times.
- I'll try using lists? Dictionary?

### Try Using Lists and Dictionaries
```def get_nouns(num_nouns):
nouns_list = []
for i in range(num_nouns):
    noun = input("Type a noun: ")
    nouns_list.append(noun)
return nouns_list
```
```word_dict = {}
word_dict["nouns"] = get_nouns(num_nouns)
```

## Stretch Challenges
- Randomize the words of the same type (ie shuffle the 5 nouns)).
- Use a dictionary to generate the words.
- Use a different data structure to store words.
- Build with TDD
- Use the system module (for accessing command-line arguments)
