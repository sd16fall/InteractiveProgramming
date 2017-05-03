# Technical Review Reflection
by Charlie Weiss

### Feedback and Decisions
My key questions were presented and answered as follows:
- **How do I make this time-based, rather than counter-based, which changes depending on the system?**

There are two ways to do this: 
1) Set a goal for frames per second. Check how much time has passed since the last update, and if too little time has passed, tell it to wait until enough time has and update then.
2) Check current time, and position objects according to that time. This requires mathematically obtaining the desired postions for objects depending on each movement, which can be a pain. Good for multiplayer games and punishing players for having slow computers, since it will make the game very skippy. It's not necessary for this game.

- **How do I clean up object declarations?**

You can write a function for this! Remember DRY-- Don't Repeat Yourself! (And its wonderful counterpart WET-- Write Everything Twice). If you're copying and pasting a lot, you're probably wrong.

- **How do I easily generate new levels?**

This actually answers the above question as well. You can make a simply function that defines new objects, and has spaces to input something like width, height, and position. This function can load a text file, that you have previously created, that contains all this information. Pickle is a tool for this.

There was also interesting feedback for questions that came up during the review, such as

- **How do I create collisions on shapes other than a rectangle?**

So, rectangles are the standard, so you don't really need to worry about this. However, if you were to, you could overlay the object views on top of each other and check for interaction using something like exor. Have an image, add another image to it, take that image away, and there should be a bit of white space left. Check the resulting image with the original-- if there is nothing there, there is no collision, and if there is, then there was a collision!

**Going forward**
I will definitely be taking the advice on level generation, and implementing the first time-based solution the next time I return to this. Thanks guys!

### Review Process Reflection
I think the review went quite well! I had a good time presenting my project and getting feedback on it. I provided the right amount of context for the project, so the feedback was very useful, and I will be using the majority of it (eventually). I can work on managing time more effectively, which I can improve by actually being aware I should do that. Oh well, tangents are fun!

Cheers, and have a great summer!
Charlie
