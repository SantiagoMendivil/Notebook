# Table of contents
- [Table of contents](#table-of-contents)
- [Google Fonts](#google-fonts)
  - [@font-face](#font-face)
  - [@font-face tips](#font-face-tips)

# Google Fonts
In order to specify a font from the google fonts api, we have to follow the next steps: 

1. Go into the Google Fonts webpage 
2. Select or search for the desired font 
3. Copy and paste the html code for the font. 
4. In the css file add the font family to the elements that you want to have that font. 

**NOTE**: If the font is in a parent element like body or html, we can use the `inherit` attribute in order to set that same font into the selected children element. This because the children elements don't inherit the font from the parent element. 

```css 
body {
    font-family: 'Orbitron', sans-serif;
}

div {
    font-family: inherit;
}
```

## @font-face 
if we download the font from another website that is not Google Fonts, we would need to drag and drop the font in the project and set the following code: 

```css 
@font-face {
    src: url("path/to/font");
    font-family: name-for-font;
}
```

## @font-face tips 
- Limit yourself to two or three fonts per page 
- Consider using newer font formats like WOFF2.  