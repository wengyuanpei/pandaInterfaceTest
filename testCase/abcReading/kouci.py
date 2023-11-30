import random

checkWordsList=['ame',
                'ake',
                'ate',
                'ade',
                'abe',
                'ape',
                'afe',
                'ale',
                'ave',
                'ime',
                'ine',
                'ipe',
                'ike',
                'ome',
                'one',
                'ope',
                'ube',
                'ule',
                'une',
                'ute',
                'ai',
                'ay',
                'ee',
                'ea',
                'y',
                'ey',
                'igh',
                'ie',
                'oa',
                'ow',
                'ue',
                'ui',
                'ew',
                'oo',
                'bl',
                'cl',
                'br',
                'cr',
                'fl',
                'gl',
                'fr',
                'gr',
                'pl',
                'sl',
                'dr',
                'tr',
                'sm',
                'sn',
                'sp',
                'sw',
                'st',
                'sh',
                'ch',
                'tch',
                'ph',
                'wh',
                'th',
                'ck',
                'qu',
                'ng',
                'nk',
                'nd',
                'nt',
                'it',
                'mp',
                'sk',
                'sc',
                'spr',
                'str',
                'spl',
                'squ',
                'ar',
                'ir',
                'ur',
                'er',
                'or',
                'ou',
                'ow',
                'oi',
                'oy',
                'u',
                'au',
                'aw',
                'all',
                'wa',
                'or',
                'oar',
                'are',
                'air',
                'ea',
                'ear',
                'eer',
                'a',
                'e',
                'i',
                'o',
                'u',
                'kn',
                'wr',
                'ture',
                'sure',
                'tion',
                'sion',
                'ous',
                'ful']

lenth34= []
lenth2=[]
lenth1=[]
for i in checkWordsList:
    if len(i) >2:
        lenth34.append(i)
    if len(i) ==2:
        lenth2.append(i)
    if len(i) ==1:
        lenth1.append(i)

words='marbles'
if len(words) >=7:
    print('命中7')
    for cici in checkWordsList:
        if cici in words:
            wen=words.replace(cici,'___')
            print(wen)
            break
        else:
            print('无法命中扣词，降级或扣一个')
            break
elif 4 <= len(words) < 7:
    print('命中46')
    for cici in checkWordsList:
        if cici in words:
            wen = words.replace(cici, '__')
            print(wen)
        else:
            print('无法命中扣词，降级或扣一个')
            break
elif len(words) < 4:
    print('命中13')
    for cici in checkWordsList:
        if cici in words:
            wen = words.replace(cici, '_')
            print(wen)
        else:
            print('无法命中扣词，降级或扣一个')
            break
else:
    print('随机1个')
    a = words[random.randint(1, len(words) - 1)]
    wen = words.replace(a, '_')
    print(wen)
