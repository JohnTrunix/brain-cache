# CSS Structured Content

## Links[^1]

```html
<a href="https://www.w3schools.com">This is a link</a>
```

```css
a {
    color: blue;
    text-decoration: none;
    cursor: pointer;
}
```

-   `a:link` - unvisited link
-   `a:visited` - visited link
-   `a:hover` - mouse over link
-   `a:active` - selected link

## Lists[^2]

```html
<ul>
    <li>a</li>
    <li>b</li>
    <li>c</li>
</ul>
```

-   `ul` - unordered list
-   `ol` - ordered list

```css
ul {
    list-style-type: square;
}
```

## Tables[^3]

```html
<table>
    <tr>
        <th>A</th>
        <th>B</th>
        <th>C</th>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
</table>
```

```css
table {
    border-collapse: collapse;
    width: 100%;
}

th,
td {
    border: 1px solid #ddd;
    padding: 8px;
}

th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #4caf50;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #ddd;
}
```

## Forms

## Images

## Iframes

[^1]: [CSS Links](https://www.w3schools.com/css/css_link.asp){target=\_blank}
[^2]: [CSS Lists](https://www.w3schools.com/css/css_list.asp){target=\_blank}
[^3]: [CSS Tables](https://www.w3schools.com/css/css_table.asp){target=\_blank}
