# RegEx

## Settings

| Setting                         | Description                      |
| ------------------------------- | -------------------------------- |
| `re.match(pattern, string)`     | First match in string from start |
| `re.search(pattern, string)`    | First match in string            |
| `re.findall(pattern, string)`   | Find all matches in string       |
| `re.sub(pattern, repl, string)` | Replace all matches in string    |
| `re.compile(pattern, flags=0)`  | Compile `str` to RegEx object    |

## Meta Characters

| Meta Character | Description                                        | Example |
| -------------- | -------------------------------------------------- | ------- |
| `[ ]`          | Match any character in the brackets                | [a-c]   |
| `[^ ]`         | Match any character except in [ ]                  | [^5]    |
| `\`            | Escape character to escape class or specific match | \d      |
| `\d`           | Escape character for digits                        | \d      |
| `\w`           | Escape character for word characters               | \w      |
| `\s`           | Escape character for whitespace                    | \s      |
| `\S`           | Escape character for non-whitespace                | \S      |
| `*`            | Character occurs 0 or more times                   | a\*     |
| `+`            | Character occurs 1 or more times                   | a+      |
| `?`            | Character occurs 0 or 1 times                      | a?      |
| `{n}`          | Character occurs exactly n times                   | a{3}    |
| `{n,}`         | Character occurs n or more times                   | a{3,}   |
| &#124;         | Either or                                          | a\|b    |

## Flags

| Flag   | long name       | Description                                 |
| ------ | --------------- | ------------------------------------------- |
| `re.A` | `re.ASCII`      | ASCII only matching                         |
| `re.I` | `re.IGNORECASE` | Case insensitive matching                   |
| `re.M` | `re.MULTILINE`  | Multiline matching                          |
| `re.S` | `re.DOTALL`     | . special character, matches all characters |
| `re.X` | `re.VERBOSE`    | Verbose RegEx                               |
| `re.L` | `re.LOCALE`     | Matching based on locale language           |

## Common Patterns

Remove redundant whitespaces

```python
text = "if     you    want    to    remove    redundant    whitespaces"
re.sub(r"\s+", " ", text)

# >>> 'if you want to remove redundant whitespaces'
```

Remove special characters

```python
text = "remove # special @@ characters % ..."
re.sub(r"[^a-zA-Z0-9]+", "", text)

## >>> 'remove special characters'
```

Keep only numeric/alphabetic characters

```python
text = "numbers 123 and letters abc"
re.sub(r"[^a-zA-Z]+", "", text)
re.sub(r"[^0-9]+", "", text)

# >>> 'numbersandletters'
# >>> '123'
```

Get URLs from text

```python
text = "This is a text with a URL www.google.com and another URL https://www.zhaw.ch"
re.findall(r"https?://\S+|www\.\S+", text)

# >>> ['www.google.com', 'https://www.zhaw.ch']
```

Get email addresses from text

```python
text = "This is a text with an email hallo@gmail.com"
re.findall("[\w\.-]+@[\w\.-]+\.\w+", text)

# >>> ['hallo@gmailcom']
```

Get HTML tags from text

```python
text = "This is a text with a <b>bold</b> tag and a <a href='https://www.zhaw.ch'>link</a>"
re.findall(r"<.*?>", text)

# >>> ['<b>', '</b>', '<a href='https://www.zhaw.ch'>', '</a>']
```

Remove HTML tags from text

```python
text = "This is a text with a <b>bold</b> tag and a <a href='https://www.zhaw.ch'>link</a>"
re.sub(r"<.*?>", "", text)

# >>> 'This is a text with a bold tag and a link'
```
