# Full Responsiveness

[__<= GO BACK__](../README.md)

1. [Quiz 1: Final Responsive Overhaul](../units_formats_environments/project/index.html)

Up until now we did as much we could to reduce the image size and reduce response time but there is actually something we can do to give the browser more information about the image we have using `srcset`

## SRCSET

`srcset` lets us specify different resolution images that the browser can load for lower or higher resolution devices. If there are browsers that do not support this attribute, it is ignored and the default `src` attribute is used.

To read more about srcset visit: [Srcset and Sizes](http://ericportis.com/posts/2014/srcset-sizes/)

## Sizes attribute

The sizes attribute gives the browser information about the display size of an image element – it does not actually cause the image to be resized. That's done in CSS!

PS: For a practical implementation of these concepts, attributes and options, take a look at the course HTML:

[__Final Project__](../units_formats_environments/project/index.html)
