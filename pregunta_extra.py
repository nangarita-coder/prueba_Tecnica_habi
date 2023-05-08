import re

n = int(input("Ingrese el número de líneas del fragmento HTML: "))
html_lines = []
for i in range(n):
    html_lines.append(input("Ingrese la línea {}: ".format(i+1)))

html = "\n".join(html_lines)

pattern = r'(https?://)(?:www\.|ww2\.)?([a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,}){1,2})'

matches = re.findall(pattern, html)

domains = list(set([match[1] for match in matches]))

print(";".join(sorted(domains)))
