import re

text = 'name_ = "The Building of the Transcontinental Railroad" ncaj_ =alksasdoandoasd'

start='name_ ='
end='ncaj_'
regex = rf"{s}\s*(.+?)\s*{end}"

matches = re.findall(regex, text)
for match in matches:
    print(match)