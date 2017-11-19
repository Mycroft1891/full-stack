# Common Responsive Patterns

[__<= GO BACK__](../README.md)

- [Quiz 1: Mostly Fluid blank CSS](pattern-mostly-fluid-quiz-blankcss.html)
- [Quiz 2: Build Home Town App Part 2](Start/index.html)

There are several CSS design patterns but some of the most widely used ones are:

- [column drop](#column-drop)
- [mostly fluid](#mostly-fluid)
- [layout shifter](#layout-shifter)
- [off canvas](#off-canvas)

In some cases a project only uses one of these design patterns or a combination of 2 or more.

### Column Drop

At its smallest breakpoint the individual containers are stacked horizontally. As the screen width increases, the containers start stack vertically more and more until it reaches the max width and starts adding margins on both sides.

### Mostly Fluid

This design pattern is very similar to `Column Drop` except that the containers are much more fluid meaning that they change more from breakpoint to breakpoint.

### Layout Shifter

Similar to how `Column` and `Mostly Fluid` this design pattern adjust at different breakpoints. The key difference with this design pattern is that with each breakpoint the layout of the site completely changes rather than pushing itms down.

### Off Canvas

The `off canvas` design pattern hides content that the user accesses less frequently off the canvas. This is usually used to hide the menu and use a menu 'hamburger' button to transition the `off canvas` content in/out again.
