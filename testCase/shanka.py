import requests

from common.get_tlj_auth import *
import qrcode
from PIL import ImageFont, ImageDraw, Image

wordList=[[41532,'strawberry','aa'],
[41533,'lunch','aa'],
[41534,'peach','aa'],
[41535,'purple','aa'],
[41536,'bird','aa'],
[41537,'cat','aa'],
[41538,'lion','aa'],
[41539,'green','aa'],
[41540,'giraffe','aa'],
[41541,'grape','aa'],
[41542,'fish','aa'],
[41543,'monkey','aa'],
[41544,'seat','aa'],
[41545,'zebra','aa'],
[41546,'piano','aa'],
[41547,'block','aa'],
[41548,'panda','aa'],
[41549,'letter','aa'],
[41550,'fox','aa'],
[41551,'guitar','aa'],
[41552,'dress','aa'],
[41553,'tiger','aa'],
[41554,'worker','aa'],
[41555,'lemon','aa'],
[41556,'movie','aa'],
[41557,'gloves','aa'],
[41558,'mouse','aa'],
[41559,'letter','aa'],
[41560,'pear','aa'],
[41561,'river','aa'],
[41562,'pants','aa'],
[41563,'lake','aa'],
[41564,'father','aa'],
[41565,'bowl','aa'],
[41566,'shirt','aa'],
[41567,'peanut','aa'],
[41568,'voice','aa'],
[41569,'grandfather','aa'],
[41570,'market','aa'],
[41571,'shorts','aa'],
[41572,'love','aa'],
[41573,'grandmother','aa'],
[41574,'carrot','aa'],
[41575,'socks','aa'],
[41576,'mother','aa'],
[41577,'screen','aa'],
[41578,'bottle','aa'],
[41579,'sky','aa'],
[41580,'plant','aa'],
[41581,'egg','aa'],
[41582,'chicken','aa'],
[41583,'cow','aa'],
[41584,'duck','aa'],
[41585,'pig','aa'],
[41586,'bench','aa'],
[41587,'leaf','aa'],
[41588,'snake','aa'],
[41589,'frog','aa'],
[41590,'insect','aa'],
[41591,'moss','B'],
[41592,'moon','aa'],
[41593,'corn','aa'],
[41594,'jacket','aa'],
[41595,'butterfly','aa'],
[41596,'pumpkin','aa'],
[41597,'bunny','aa'],
[41598,'goldfish','aa'],
[41599,'farmer','aa'],
[41600,'crocodile','aa'],
[41601,'apple','aa'],
[41602,'cherry','aa'],
[41603,'gate','aa'],
[41604,'red','aa'],
[41605,'rainbow','aa'],
[41606,'rain','aa'],
[41607,'swimsuit','aa'],
[41608,'fence','aa'],
[41609,'tail','aa'],
[41610,'dirt','aa'],
[41611,'seed','C'],
[41612,'ladder','aa'],
[41613,'sandbox','aa'],
[41614,'ostrich','aa'],
[41615,'bridge','aa'],
[41616,'subway','aa'],
[41617,'tunnel','aa'],
[41618,'cookie jar','aa'],
[41619,'fridge','aa'],
[41620,'sink','aa'],
[41621,'trash can','aa'],
[41622,'snow','aa'],
[41623,'coat','aa'],
[41624,'hose','B'],
[41625,'fire','aa'],
[41626,'sled','B'],
[41627,'snowman','aa'],
[41628,'bus','aa'],
[41629,'truck','aa'],
[41630,'yellow','aa'],
[41631,'dark','C'],
[41632,'pencil','A'],
[41633,'play','A'],
[41634,'dad','A'],
[41635,'kitchen','A'],
[41636,'round','A'],
[41637,'write','A'],
[41638,'sleep','A'],
[41639,'up','A'],
[41640,'living room','A'],
[41641,'large','C'],
[41642,'brown','A'],
[41643,'pink','A'],
[41644,'down','A'],
[41645,'orange','A'],
[41646,'skip','A'],
[41647,'clean','A'],
[41648,'brother','A'],
[41649,'rock','A'],
[41650,'bathroom','A'],
[41651,'step','A'],
[41652,'look','A'],
[41653,'sister','A'],
[41654,'door','A'],
[41655,'dining room','A'],
[41656,'happy','A'],
[41657,'chin','A'],
[41658,'foot','A'],
[41659,'bike','A'],
[41660,'hall','A'],
[41661,'bedroom','A'],
[41662,'cheek','A'],
[41663,'small','A'],
[41664,'bake','A'],
[41665,'hair','A'],
[41666,'eye','A'],
[41667,'read','A'],
[41668,'hug','A'],
[41669,'mouth','A'],
[41670,'eyebrow','A'],
[41671,'blue','A'],
[41672,'plane','A'],
[41673,'nose','A'],
[41674,'chest','A'],
[41675,'smile','A'],
[41676,'gray','A'],
[41677,'friend','A'],
[41678,'toy','A'],
[41679,'sheep','A'],
[41680,'arm','A'],
[41681,'picture','C'],
[41682,'throw','A'],
[41683,'win','A'],
[41684,'one','A'],
[41685,'three','A'],
[41686,'seven','B'],
[41687,'five','A'],
[41688,'two','A'],
[41689,'draw','A'],
[41690,'carry','A'],
[41691,'cook','A'],
[41692,'run','A'],
[41693,'garden','aa'],
[41694,'ball','A'],
[41695,'jump','A'],
[41696,'food','A'],
[41697,'crawl','B'],
[41698,'nest','A'],
[41699,'gold','A'],
[41700,'belly','A'],
[41701,'long','A'],
[41702,'hamster','A'],
[41703,'roll','A'],
[41704,'cold','A'],
[41705,'hot','A'],
[41706,'straight','A'],
[41707,'hop','A'],
[41708,'kick','A'],
[41709,'fast','A'],
[41710,'pull','A'],
[41711,'push','A'],
[41712,'slow','A'],
[41713,'bee','A'],
[41714,'spin','A'],
[41715,'sit','A'],
[41716,'in','A'],
[41717,'out','A'],
[41718,'four','A'],
[41719,'lift','A'],
[41720,'hand','A'],
[41721,'body','A'],
[41722,'head','A'],
[41723,'wheel','A'],
[41724,'short','A'],
[41725,'black','A'],
[41726,'help','A'],
[41727,'smooth','B'],
[41728,'warm','A'],
[41729,'dry','A'],
[41730,'sour','A'],
[41731,'sweet','A'],
[41732,'bad','A'],
[41733,'slide','C'],
[41734,'outside','C'],
[41735,'mom','A'],
[41736,'fold','B'],
[41737,'act','B'],
[41738,'animal','B'],
[41739,'answer','B'],
[41740,'bread','B'],
[41741,'chew','B'],
[41742,'butter','B'],
[41743,'boat','B'],
[41744,'cave','B'],
[41745,'change','C'],
[41746,'bite','B'],
[41747,'secret','B'],
[41748,'sing','B'],
[41749,'six','B'],
[41750,'study','B'],
[41751,'ten','B'],
[41752,'sandwich','B'],
[41753,'police','B'],
[41754,'mushroom','B'],
[41755,'toothbrush','B'],
[41756,'plate','B'],
[41757,'paper','B'],
[41758,'milk','B'],
[41759,'umbrella','B'],
[41760,'math','B'],
[41761,'walk','B'],
[41762,'many','B'],
[41763,'log','B'],
[41764,'lettuce','B'],
[41765,'leg','B'],
[41766,'turtle','B'],
[41767,'cover','B'],
[41768,'glue','B'],
[41769,'hole','B'],
[41770,'tissue','B'],
[41771,'eight','B'],
[41772,'drive','B'],
[41773,'dig','B'],
[41774,'dance','B'],
[41775,'tent','B'],
[41776,'hide-and-seek','B'],
[41777,'low','B'],
[41778,'construction worker','B'],
[41779,'doctor','B'],
[41780,'police officer','B'],
[41781,'shoes','B'],
[41782,'room','B'],
[41783,'teddy bear','B'],
[41784,'school','B'],
[41785,'heavy','B'],
[41786,'deer','B'],
[41787,'jellyfish','B'],
[41788,'cheer','B'],
[41789,'house','B'],
[41790,'store','B'],
[41791,'cheese','B'],
[41792,'soda pop','B'],
[41793,'pass','C'],
[41794,'sugar','B'],
[41795,'beach','B'],
[41796,'teacher','B'],
[41797,'add','B'],
[41798,'paint','B'],
[41799,'hay','B'],
[41800,'oil','B'],
[41801,'soccer','B'],
[41802,'mud','B'],
[41803,'pond','B'],
[41804,'high','B'],
[41805,'firefighter','B'],
[41806,'nurse','B'],
[41807,'pilot','B'],
[41808,'hat','B'],
[41809,'flower','B'],
[41810,'pick','B'],
[41811,'time','B'],
[41812,'dog','B'],
[41813,'light','B'],
[41814,'far','B'],
[41815,'near','B'],
[41816,'wolf','B'],
[41817,'float','B'],
[41818,'tank','B'],
[41819,'game','B'],
[41820,'park','B'],
[41821,'picnic','B'],
[41822,'uniform','B'],
[41823,'share','B'],
[41824,'flour','B'],
[41825,'mix','B'],
[41826,'oven','B'],
[41827,'swing','B'],
[41828,'ride','B'],
[41829,'fun','B'],
[41830,'hike','B'],
[41831,'tomato','C'],
[41832,'ocean','C'],
[41833,'water','C'],
[41834,'elephant','C'],
[41835,'potato','C'],
[41836,'smart','C'],
[41837,'cloud','C'],
[41838,'chips','C'],
[41839,'mountain','C'],
[41840,'pizza','C'],
[41841,'cabbage','C'],
[41842,'avocado','C'],
[41843,'eggplant','C'],
[41844,'same','C'],
[41845,'bacon','C'],
[41846,'yogurt','C'],
[41847,'caring','C'],
[41848,'goose','C'],
[41849,'donkey','C'],
[41850,'shark','C'],
[41851,'eagle','C'],
[41852,'muffin','C'],
[41853,'toast','C'],
[41854,'creative','C'],
[41855,'interesting','C'],
[41856,'talented','C'],
[41857,'spider','C'],
[41858,'ice','C'],
[41859,'wind','C'],
[41860,'street','C'],
[41861,'birthday','C'],
[41862,'sharp','C'],
[41863,'wash','C'],
[41864,'pepper','C'],
[41865,'onion','C'],
[41866,'dinosaur','C'],
[41867,'bear','C'],
[41868,'forest','C'],
[41869,'winter','C'],
[41870,'spring','C'],
[41871,'summer','C'],
[41872,'jam','C'],
[41873,'popcorn','C'],
[41874,'city','C'],
[41875,'home','C'],
[41876,'balloon','C'],
[41877,'grow','C'],
[41878,'pork','C'],
[41879,'live','C'],
[41880,'owl','C'],
[41881,'koala','C'],
[41882,'find','C'],
[41883,'thin','C'],
[41884,'full','C'],
[41885,'count','C'],
[41886,'grass','C'],
[41887,'fruit','C'],
[41888,'zoo','C'],
[41889,'fall','C'],
[41890,'banana','C'],
[41891,'basketball','aa'],
[41892,'book','aa'],
[41893,'swim','A'],
[41894,'puzzle','A'],
[41895,'behind','A'],
[41896,'finger','C'],
[41897,'cake','C'],
[41898,'tree','aa'],
[41899,'colorful','aa'],
[41900,'move','C'],
[41901,'kind','C'],
[41902,'nine','B'],
[41903,'ear','A'],
[41904,'sad','C'],
[41905,'ant','C'],
[41906,'big','C'],
[41907,'box','C'],
[41908,'bucket','C'],
[41909,'car','C'],
[41910,'climb','C'],
[41911,'cup','C'],
[41912,'different','C'],
[41913,'eat','C'],
[41914,'feed','C'],
[41915,'fly','C'],
[41916,'ice cream','C'],
[41917,'funny','C'],
[41918,'have','C'],
[41919,'helpful','C'],
[41920,'make','C'],
[41921,'nice','C'],
[41922,'place','C'],
[41923,'quiet','C'],
[41924,'square','C'],
[41925,'tool','C'],
[41926,'tooth','C'],
[41927,'train','C'],
[41928,'want','C'],
[41929,'window','C'],
[41930,'wing','C'],
[41931,'woman','C']
]




#获取dev 手机号token
token=tljlogIn(15444444444)

UId=tljlogInUid(15444444444)

Kid=Uid=str(UId)
uid=Uid



header={"Authorization":token,
        "User-Uid":Uid,
        "Kid-Uid":Kid}


url='https://hear-dev.abctime.com/v1/flashcard/get_word_info'



# data={"level":"aa","version_code":20230601,"word":"letter","word_id":41559,"uid":1607331624148455426}







def shankaTest(id):

    # id = input("请输入闪卡，数字0-399：")

    id =id
    dataa=wordList[int(id)]
    idd=dataa[0]
    wordd=dataa[1]
    levell=dataa[2]
    data = {"level": levell, "version_code": 20230601, "word": wordd, "word_id": idd, "uid": 1607331624148455426}
    qrdata={"cardType":1,"cardInfo":{"level":levell,"versionCode":20230601,"word":wordd,"wordId":idd}}
    qr = qrcode.QRCode(version=2,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       )
    qr.add_data(qrdata)
    qr.make(fit=True)
    Img=qr.make_image()
    # print(Img)
    Img.save(r"C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\闪卡图片\闪卡第%d张%s.png" %(id,wordd))


    img = Image.open(r"C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\闪卡图片\闪卡第%d张%s.png" %(id,wordd))
    print(img.size)
    draw = ImageDraw.Draw(img)
    # print(draw)
    ttfront = ImageFont.truetype('msyh.ttc', 40,0)  # 字体文件msyh.ttc，需要查找下载
    content = wordd
    width_w, height_h = ttfront.getsize(content)

    # # font = ImageFont.truetype ('arial.ttf', font_size)
    # ascent, descent = ttfront.getmetrics ()
    # (width, baseline), (offset_x, offset_y) = ttfront.getsize(content)
    # print((width, baseline), (offset_x, offset_y))

    print(content)
    draw.text(((650-width_w)/2, 600), content, font=ttfront)  # 文字位置，正文内容，文字RGB颜色，字体
    img.save(r"C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\闪卡图片\闪卡第%d张%s.png" %(id,wordd))

    req=requests.post(url=url,json=data,headers=header)
    print(req.json())

# shankaTest()


for i in range(1):
    shankaTest(i)
    print("################################第"+str(i)+"张图片以生成########################################")




#手动输识别
# shankaTest()






def qrTest():
    qrdata ={"level": 'C', "version_code": 20230601, "word": "wordd", "word_id": 55555, "uid": 1607331624148455426}
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4
    )
    qr.add_data(qrdata)
    qr.make(fit=True)
    Img = qr.make_image()
    Img.save(r"C:\Users\zhang\Desktop\pandaInterfaceTest\testCase\闪卡图片\测试图片.png")
    print('测试图片生成成功！！')



# shankaTest()


# qrTest()



def check_mp3(id):
    url_info='https://hear-dev.abctime.com/v1/flashcard/get_word_test'
    dataa = wordList[int(id)]

    idd = dataa[0]
    wordd = dataa[1]
    levell = dataa[2]
    data = {"level":levell,"word_id":idd,"uid":1668498425131692033}

    respose=requests.post(url=url_info,json=data,headers=header)
    # print(respose.json()['data']['exercises'][2])
    resposes=respose.json()['data']['exercises']
    return resposes,idd,wordd,levell

errorList=[]
# for ai in range(50):
#     for i in range(244,245):
#             try:
#                 data_response=check_mp3(i)[0]
#                 print('单词：'+check_mp3(i)[2])
#                 for ii in range(len(data_response)):
#                     for iii in range(len(data_response[ii]['itemRespList'])):
#                         mp3Info=data_response[ii]['itemRespList'][iii]['audioResource']
#                         print(mp3Info)

                        # if mp3Info[-3:] == "mp3":
                        #     print(mp3Info[-3:])
                        #     print('OK!')
                        # else:
                        #     errorList.append([check_mp3(i)[1],check_mp3(i)[2],check_mp3(i)[3]])
                        #     continue
            # except:
            #     print(check_mp3(i)[0])

# errorList=list(set(errorList))
# print(errorList)


# 查看异常单词的扣词问题
# for i in range(50):
#     # print(check_mp3(108))
#     aa=check_mp3(244)[0][2]['contentResp']['content']
#     if str(aa).find('_')!=4 and str(aa).find('_')!=8:
#
#         print(aa+"位置在"+str(str(aa).find('_')))
#     else:
#         print(aa+'扣位置错误！！！！！！！！！！！！！！！！')

# ####################################pre 环境##################################################

pre_header={"Authorization":'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTcwMjI3NjU3MH0.e6CLa06064efURGTB9K0SmGdLMf1joGLrPhDGvUZt-SHBY9ZRTlWijLItbWrmrNP6TWovbAoXR8MW9Sfbk6VCA',
        "User-Uid":'1640976882862985217',
        "Kid-Uid":'1640976882862985217'}
def check_mp3_pre(id):
    url_info='https://hear-pre.abctime.com/v1/flashcard/get_word_test'
    dataa = wordList[int(id)]

    idd = dataa[0]
    wordd = dataa[1]
    levell = dataa[2]
    data = {"level":levell,"word_id":idd,"uid":1640976882862985217}

    respose=requests.post(url=url_info,json=data,headers=pre_header)
    # print(respose.json()['data']['exercises'][2])
    resposes=respose.json()['data']['exercises']
    return resposes,idd,wordd,levell

# errorList1=[]
#
# for i in range(400):
#         try:
#             data_response=check_mp3_pre(i)[0]
#             print('单词：'+check_mp3(i)[2])
#             for ii in range(len(data_response)):
#                 for iii in range(len(data_response[ii]['itemRespList'])):
#                     mp3Info=data_response[ii]['itemRespList'][iii]['audioResource']
#                     print(mp3Info)
#
#                     if mp3Info[-3:] == "mp3":
#                         # print(mp3Info[-3:])
#                         print('OK!')
#                     else:
#                         errorList1.append([check_mp3(i)[1],check_mp3(i)[2],check_mp3(i)[3]])
#                         continue
#         except:
#             print(check_mp3(i)[0])
# print(errorList1)

