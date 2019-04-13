html = '''h1="title start";
FOX Sports is dé live sportzender van Nederland. Iedere speelronde van de Eredivisie worden op FOX 

/* Record ID 1912828 */'''

left_border = '";\n'
right_border = '\n\n/*'

title = html[:html.find(left_border)+len(left_border)]
record = html[html.find(right_border):]

print(title, record)
