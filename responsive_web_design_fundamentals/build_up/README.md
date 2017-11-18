# Building Up

[__<= GO BACK__](../README.md)

- [Quiz 1: Media Queries](breakpoints.html)

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
