# classes and objects in python

## let us understand object oriented programming(oop) in python

oop in python consists of two main components

- classes
- objects

## classes

A class in python can be considered to be a representation or template or blueprint for a real world entity

### Let us look at a scenario

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

### Example(OBJECT AND CLASSES )

    class phone:
        def make_call(self):
            print("Making phone call...")
        def play_game(self):
            print("Playing game...")

In the code above we have:

- created a new class(phone ) using -> class phone:
- Inside we created two user-defined functions -> make_call and play_game
- make_cal() method is just printing out 'maing phone call...'
-play_game() method is just printing out 'playing game...'

### Now that we have created a class, we would have to move a stp further by creating an instance of the class(objects )

    p1=phone()
    p1.make_call()
    p1.play_game()

In the code above we are:

- creating a new object called as p1 with the command: p1=phone().
- if we would have to invoke the make_call method from the class we use:
  - p1.make_call()
- similarly, to invoke play_game() method from the phone class,we use ;
  - p1.play_game()

Now,that we have understood how to create a class and an object. Let us go ahead and add parameters to the methods of our class
    class Phone:

    def set_color(self,color):

        self.color=color

    def set_cost(self,cost):

        self.cost=cost

    def show_color(self):

        return self.color

    def show_cost(self):

        return self.cost

    def make_call(self):

        print(“Making phone call”)

    def play_game(self):

        print(“Playing Game”)
In the code above, we are creating 6 methods:

- set_color()
- set_cost()
- show_color()
- show_cost()
- make_call()
- play_game()

- set_color(): This method takes in two parameters: self and color. With the code self.
color=color, we are able to set a color to the attribute ‘color’.

- set_cost(): This method also takes in two parameters: self and cost. With the code: self.cost=cost, we are able to set a cost value to the attribute ‘cost’.

- show_color(): With this method, we are just returning the color of the phone.

- show_cost(): With this method, we are returning the cost of the phone.

- make_call(): With this method, we are simply printing out: “Making a phone call”.

- play_game(): With this method, we are printing out: “Playing Game”
