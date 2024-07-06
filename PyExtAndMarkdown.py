import re

def restricted_markdown(value, allowed_l = ["code", "weblinks", "bold", "italic", "breakline"], never_value = "¤"):
    r = re.compile(never_value)
    value = r.sub("", value)
    value = " " + value + " "
    r_spe = re.compile(never_value)
    if "breakline" in allowed_l:
        r = re.compile("<br/>")
        value = r.sub("¤", value)
        r = re.compile(r'<[A-Z|a-z|0-9|/]+?>')
        value = r.sub('', value)
        value = r_spe.sub("<br/>", value)
    else:
        r = re.compile(r'<[a-z|0-9|/]+?>')
        value = r.sub('', value)
    r = re.compile(" ")
    value = r.sub(never_value, value)
    value2 = value
    value = " ".join(value)
    value = value.split(" ")
    if "code" in allowed_l:
        code_found = re.search(r'`(.){1,}`', value2)
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
    if "bold" in allowed_l:
        r_bold = re.compile(r'\*\*([A-Z|a-z|0-9]){1,}\*\*')
        bold_found = r_bold.search(value2)
        if not bold_found:
            r_bold = re.compile(r'\_\_([A-Z|a-z|0-9]){1,}\_\_')
            bold_found = r_bold.search(value2)
        bold_iter = r_bold.finditer(value2)
        if bold_found:
            for i in bold_iter:
                cur_ids = i.span()
                value[cur_ids[0]] = "<b>"
                value[cur_ids[0] + 1] = ""
                value[cur_ids[1] - 2] = "</b>"
                value[cur_ids[1] - 1] = ""
    if "italic" in allowed_l:
        r_italic = re.compile(r'([A-Z|a-z|0-9|¤])\*([A-Z|a-z|0-9]){1,}\*([A-Z|a-z|0-9|¤])')
        italic_found = r_italic.search(value2)
        if not italic_found:
            r_italic = re.compile(r'([A-Z|a-z|0-9|¤])\_([A-Z|a-z|0-9]){1,}\_([A-Z|a-z|0-9|¤])')
            italic_found = r_italic.search(value2)
        italic_iter = r_italic.finditer(value2)
        if italic_found:
            for i in italic_iter:
                cur_ids = i.span()
                value[cur_ids[0] + 1] = "<i>"
                value[cur_ids[1] - 2] = "</i>"
    value[0] = ""
    value[-1] = ""
    if "weblinks" in allowed_l:
        r = re.compile("http(s){0,1}://")
        link_found = r.finditer(value2)
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
    return "<p>" + value + "</p>"

print(restricted_markdown("**oui** *non* http://wikipedia.org and https://youtube.com and `code here` <br/> yes"))
