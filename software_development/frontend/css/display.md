# Table of contents
- [Table of contents](#table-of-contents)
- [inline](#inline)
- [block](#block)
  - [Center with margins and one element (block)](#center-with-margins-and-one-element-block)
  - [Center with margins and more elements (inline)](#center-with-margins-and-more-elements-inline)
- [align-items](#align-items)
- [flex-direction](#flex-direction)

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


# align-items
The align-items align the content in the vertical line to a specific positios such as with justify content.

```css 
.container {
    display: flex; 
    justify-content: center; 
    align-items: center; 
}
```

If the parent div doesn't have a height, the children divs will fit all the y-axis space that they could have. Specify a height if using align-items

# flex-direction
The items can be positioned in different ways like start, center, end, etc. but if we want to change the direction of the children divs, we should use flex-direction in order to change their position. 


```css 
.container {
    display: flex; 
    flex-direction: column; 
    justify-content: center; 
    align-items: center; 
}
```