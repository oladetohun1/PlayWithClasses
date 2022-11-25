# classes and objects in python

## let us understand object oriented programming(oop) in python

oop in python consists of two main components

- classes
- objects

## classes

A class in python can be considered to be a representation or template or blueprint for a real world entity

- ### Let us look at a scenario

if we take a real world entity(class ) 'phone'

The class would have two things associated with it;

- properties
- Behaviours

#### properties: The class(phone ) would have certain properties associated with it such as

- color
- cost
- battery life

#### Behaviour: Simiarly, the class(phone ) would have certain behaviours associated with it such as

- Making a call
- Watching a Video
- playing games

N.B: When the properties and behaviour are combined together we have a class

## Objects

An object in python can be considered to be specific instance of a class.

So if PHONE is a class, then samsung, iphone and Nokia would be specific instance of the class or in other words 'Objects of the class'

### Example

    class phone:
        def make_call(self):
            print("Making phone call...")
        def play_game(self):
            print("Playing a game...")

In the code above we have:

- created a new class(phone ) using -> class phone:
- Inside we created two user-defined functions -> make_call and play_game

Now that we have created a class, we would have to move a stp further by creating an instance of the class(objects )
