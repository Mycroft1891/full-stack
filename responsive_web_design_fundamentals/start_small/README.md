# Starting Small

[__<= GO BACK__](../README.md)

## [Lesson Project: Redesign Website](Start/index.html)

When designed responsive web sites it is important to understand the difference between hardware pixels and the Device Pixel Ratio

> The device pixel ratio is the ratio between physical pixels and logical pixels. For instance, the iPhone 4 and iPhone 4S report a device pixel ratio of 2, because the physical linear resolution is double the logical linear resolution.


A key part is too always define the viewport which gives the browser instructions on how to control the page's dimensions and scaling.

> The viewport is the user's visible area of a web page.
>
>The viewport varies with the device, and will be smaller on a mobile phone than on a computer screen.
>
Before tablets and mobile phones, web pages were designed only for computer screens, and it was common for web pages to have a static design and a fixed size.

## Things to note:

- The `width=device-width` part sets the width of the page to follow the screen-width of the device (which will vary depending on the device).

- The `initial-scale=1.0` part sets the initial zoom level when the page is first loaded by the browser.

- It is important to set the width of elements using relative units like `% or em` rather than `px or mm` which can overflow.
