# PyExtAndMarkdown

Set of functions to specifically convert Markdown to HTML in Python, omiting certain tags/symbols for example.

## restricted_markdown

Allow to convert Markdown like synthax text to html omiting all tags apart `<br/>`, `<i></i>`, `<b></b>` and all links those beginning by `https://` or `http://` (no local links).

You can choose wich tags to keep in an list argument called `allowed_l`

# Dependencies

- re

## Function

`restricted_markdown(value, allowed_l = ["code", "weblinks", "bold", "italic", "breakline"], never_value = "¤")`

## Arguments

- `value` is tyhe input string
- `allowed_l` is the list containing all the allowed tags
- `never_value` is a string that won't be used in the text `value`

## Examples:

``print(restricted_markdown("**oui** *non* http://wikipedia.org and https://youtube.com and `code here` <br/> yes"))``

Output:

`<p><b>oui</b> <i>non</i> <a href = 'http://wikipedia.org'>http://wikipedia.org</a> and <a href = 'https://youtube.com'>https://youtube.com</a> and <code>code here</code> <br/> yes</p>`

=========================

``print(restricted_markdown(value = "**oui** *non* http://wikipedia.org and https://youtube.com and `code here` <br/> yes",
      allowed_l = ["italic"]))``

Output:

``<p>**oui** <i>non</i> http://wikipedia.org and https://youtube.com and `code here`  yes</p>``
