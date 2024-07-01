import re

def restricted_markdown(value):
    value = " " + value + " "
    r = re.compile("<br/>")
    value = r.sub("¤", value)
    r = re.compile(r'<[a-z|0-9|/]+?>')
    value = r.sub('', value)
    r_spe = re.compile("¤")
    value = r_spe.sub("<br/>", value)
    r = re.compile(" ")
    value = r.sub("¤", value)
    r = re.compile("http(s){0,1}://")
    link_found = r.finditer(value)
    code_found = re.search(r'`(.){1,}`', value)
    r_bold = re.compile(r'\*\*([a-z|0-9]){1,}\*\*')
    bold_found = r_bold.search(value)
    if not bold_found:
        r_bold = re.compile(r'\_\_([a-z|0-9]){1,}\_\_')
        bold_found = r_bold.search(value)
    bold_iter = r_bold.finditer(value)
    r_italic = re.compile(r'([a-z|0-9|¤])\*([a-z|0-9]){1,}\*([a-z|0-9|¤])')
    italic_found = r_italic.search(value)
    if not italic_found:
        r_italic = re.compile(r'([a-z|0-9|¤])\_([a-z|0-9]){1,}\_([a-z|0-9|¤])')
        italic_found = r_italic.search(value)
    italic_iter = r_italic.finditer(value)
    value = " ".join(value)
    value = value.split(" ")
    if code_found:
        idx = [i for i, x in enumerate(value) if x == "`"]
        value[idx[0]] = "<code>"
        value[idx[1]] = "</code>"
        if len(idx) > 2:
            for i in range(2, len(idx)):
                if i % 2 != 0:
                    value[idx[i]] = "<code>"
                else:
                    value[idx[i]] = "</code>"
    if bold_found:
        for i in bold_iter:
            cur_ids = i.span()
            value[cur_ids[0]] = "<b>"
            value[cur_ids[0] + 1] = ""
            value[cur_ids[1] - 2] = "</b>"
            value[cur_ids[1] - 1] = ""
    if italic_found:
        for i in italic_iter:
            cur_ids = i.span()
            value[cur_ids[0] + 1] = "<i>"
            value[cur_ids[1] - 2] = "</i>"
    value[0] = ""
    value[-1] = ""
    dec_val = 0
    for i in link_found:
        cur_id = i.span()[0] - dec_val
        cnt = cur_id
        href_link = ""
        no_stop = True
        while no_stop and value[cnt]:
            if cnt == len(value) - 1:
                no_stop = False
            elif value[cnt] == "¤" or repr(value[cnt]) in ["'\\n'", "'\\r'"]:
                no_stop = False
            else:
                href_link += value[cnt]
                cnt += 1
        del value[cur_id + 1:cnt]
        dec_val += cnt - cur_id - 1
        value[cur_id] = "<a href = '" + href_link + "'>" + href_link + "</a>"
    value = "".join(value)
    value = r_spe.sub(" ", value)
    return value

print(restricted_markdown("**oui** *non* http://wikipedia.org and https://youtube.com and `code here` yes"))

