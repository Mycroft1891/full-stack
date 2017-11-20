# Units, Formats, Environments

[__<= GO BACK__](../README.md)

- [Quiz 1: Responsive Image](responsive-images.html)
- [Quiz 2: Make Site responsive](project/index.html)

The key to optimizing images is to keep the `smallest amount of pixels` as well as the `highest compression rate`

In order to make sure that the images scale only up to their full resolution and not more (it becomes pixelated), we can make use of `max-width: 100%`. Further more, if we want to work with margins with 2 or more images, we can use the `calc()` css funcitons:

```
/* property: calc(expression) */
width: calc(100% - 80px);
```


### Less used CSS attributes

For pixels and percentage independent image resizing, we can use the `viewport height` and `viewport width`. This ensures that the image adjusts according to the viewport's dimensions rather than the size of its container which can be set to something smaller.


### Vector Images vs Raster Images

When we use images have the option to choose between `vector images` and `raster images`. `raster images` are images like `.png` which are designed with a pixel width and height. `vector images` on the other hand store a set of instruction to construct the images with lines and colors. The power of `vector images` is that they can scale indefinitely which means they don't require any resizing.


### Compression, Optimization And Automation


> Use ImageMagick® to create, edit, compose, or convert bitmap images. It can read and write images in a variety of formats (over 200) including PNG, JPEG, JPEG-2000, GIF, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG. Use ImageMagick to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves.

> [Image Magic Quote](http://www.imagemagick.org/script/index.php)

As our image library grows, it becomes increasingly useful to have tools that automate the image resizing process for us. `Image Magic` and `Grunt` are such tools
