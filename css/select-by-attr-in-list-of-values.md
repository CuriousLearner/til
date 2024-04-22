# Select by attr in list of values

You can select an element in the DOM having an attribute with list of values.

By using the `[attr~='foo']` selector, it only select elements where the attribute contains the string "foo", and also takes into consideration that the element should contain an attr value in a space separated list.

Example:

```html
<div attr='en-us foo bar' />
```

can be selected with

```css
[attr~='foo'] { font-size:smaller; }
```

If you want to select value with dash separated, you may do:

```css
/* value in a dash-separated list, e.g., "-" (U+002D) */
[attr|='en'] { font-size:smaller; }
```
