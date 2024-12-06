# Table of contents
- [Table of contents](#table-of-contents)
- [inline](#inline)
- [block](#block)
  - [Center with margins and one element (block)](#center-with-margins-and-one-element-block)
  - [Center with margins and more elements (inline)](#center-with-margins-and-more-elements-inline)

# inline
Using display inline it will display all the elements right beside each other. 

```css
img {
    display: inline;
}
```

# block
Using display bloc it will display all the elements one on top of each other. 

Nothing can be placed beside one of these block elements. Basically it makes the elements to place one on top of each other without excuses. 

```css
img {
    display: block;
}
```

## Center with margins and one element (block)
1. We need to use the display block. 
2. Must have a width. 
3. Margin left/right auto


```css
.container {
    display: block;
    width: 200px;
    margin-left: auto;
    margin-right: auto;
}
```

## Center with margins and more elements (inline)
Using **flexbox**. If we have a div of divs we just add: 

```css 
.nav-wrapper {
    display: flex; 
    justify-content: center;
}
```

The **justify-content** attribute can be set to: 

- **start**: Align all the items from left to right. 
- **end**: Align all the items from right to left. 
- **center**: Align all the items in the center. 
- **space-between**: Align all the items with strict space from each other. 
