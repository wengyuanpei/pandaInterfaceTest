import re
import xlwt
file=r"C:\Users\zhang\Desktop\听力机testproject-deep.xml"

f = open(file,encoding="utf-8")
texttall=f.read()
f.close()

testcase=re.findall("<testcase.*?</testcase>",texttall,re.S)
# print(testcase)


book=xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet=book.add_sheet("frist",cell_overwrite_ok=True)
titlelist=["用例名称","概要","步骤","操作","预期"]
for i  in range(0,len(titlelist)):
    sheet.write(0,i,titlelist)

r=1
for case in testcase:
    title=re.findall('name="(.*?)">',case,re.S)[0]
    # print(title)
    sheet.write(r,0,title)
    sumrry=re.findall("<summary><!\[CDATA\[(.*?)]]></summary>",case,re.S)[0]
    # print(sumrry)
    sumrry=sumrry.replace('<p>','').replace('<p>','').replace('&ldquo;','"').replace('&ldquo;','"').replace('&nbsp;','"')
    # print(sumrry)
    sheet.write(r,1,sumrry)
    stepes=re.findall("<step>.*?</step>",case,re.S)
    i=1
    for step in stepes:
        print(step)
        action=re.findall("<actions><!\[CDATA(.*?)]></actions>",step,re.S)[0]
        print('action:',action)
        action=action.replace('<p>','').replace('<p>','').replace('&ldquo;','"').replace('&ldquo;','"').replace('&nbsp;','"')
        print("action:",action)
        expected=re.findall(r"<expectedresults><!\[CDATA(.*?)]></expectedresults>",step,re.S)[0]
        print(expected)
        expected = expected.replace('<p>', '').replace('<p>', '').replace('&ldquo;', '"').replace('&ldquo;', '"').replace('&nbsp;', '"')
        print(expected)
        print('写入2')
        sheet.write(r,2,i)
        print('写入3')
        sheet.write(r,3,action)
        print('写入4')
        sheet.write(r,4,expected)
        i+=1
        r+=1
    print("\n")
book.save(r'C:\Users\zhang\Desktop\Casefortingliji.xlsx')