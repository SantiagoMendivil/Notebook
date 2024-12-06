# Table of contents
- [Table of contents](#table-of-contents)
- [The span Tag](#the-span-tag)
- [Text Shadow](#text-shadow)

# The span Tag 
In order to make a specific part of our code special, or with a different style from an element, like a specific word in a paragraph, we use the span tag.

```html 
<h1>Click <span class="cta">here!</span></h1>
```

The text here! will be displayed with the stylings that we add to the cta class. 

# Text Shadow
```css 
h1 {
    text-shadow: 0px 0px black;
}
```

The first value is the offset of the horizontal line, the second value is the offset of the vertical line and the final value is the color of the shadow. 

We can use a fourth value that sets the shadow with some blur

```css 
h1 {
    text-shadow: -5px 5px 0px black;
}
```