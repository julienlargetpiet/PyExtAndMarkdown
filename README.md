# PyExtAndMarkdown

Set of functions to specifically convert Markdown to HTML in Python, omiting certain tags/symbols for example.

## restricted_markdown

Allow to convert Markdown like synthax text to html omiting all tags apart `<br/>`, `<i></i>`, `<b></b>` and all links those beginning by `https://` or `http://` (no local links).

## Examples:

`print(restricted_markdown("**oui** *non* http://wikipedia.org and https://youtube.com and `code here` yes"))`

Output:

`<b>oui</b> <i>non</i> <a href = 'http://wikipedia.org'>http://wikipedia.org</a> and <a href = 'https://youtube.com'>https://youtube.com</a> and <code>code here</code> yes`
`

