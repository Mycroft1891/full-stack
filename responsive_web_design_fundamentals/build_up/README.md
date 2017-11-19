# Building Up

[__<= GO BACK__](../README.md)

- [Quiz 1: Media Queries](breakpoints.html)

## Course Notes:

We can add media queries to apply certain css only when the width is greater or smaller than the specified one:

```
<link rel="stylesheet" media="screen and (min-width: 500px)" href="style.css">
```

or in our css:

```
@media screen and (min-width: 1px) and (max-width: 400px) {
  body {
    background-color: red;
  }
}
```

> Picking breakpoints is more of an art than a science.

> Udacity Quote

## Libraries, Frameworks and Modules

There are several libraries, frameworks and modules to create responsive design:

- [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [Bootstrap](https://getbootstrap.com/)
- [PureCSS](https://purecss.io/)
- [Kube](https://imperavi.com/kube/)
- [Materialize](http://materializecss.com/)
- [Bulma](https://bulma.io/)
