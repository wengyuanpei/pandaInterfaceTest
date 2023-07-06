import requests
from  common.finish_plan import *

header={'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjA3MzE0NjQ0NjU3OTUwNzIxIiwic3ViIjoie1wiaWRcIjoxNjA3MzE0NjQ0NjU3OTUwNzIxLFwibW9iaWxlXCI6XCIrODYxODM4NDI1MzUwNlwifSIsImV4cCI6MTcwMzUwMDc3N30.mN98tokSAFBflTS27rRTwhf8AAcHWAlF76-bqhoJxMZz-eg0HwYrLGgHKriRBf0A2ySf83MN6JKN3gri493xpw'}
baseurl=urlenverment(1)#dev环境

def getplaninfo(nextt,uid):

    url=baseurl+'v1/study/plan-info-new'
    data={"next":nextt,"uid":uid}
    rep=requests.post(url=url,json=data,headers=header)

    print('RAZ数据：' + str(rep.json()['data']['read_book']))
    print('磨耳朵数据：'+str(rep.json()['data']['listen_info']))
    print('AI对话数据：' + str(rep.json()['data']['oral_training']))

    planid=rep.json()['data']['user_plan_id']
    lisen=rep.json()['data']['listen_info']['user_plan_id']

    return planid,lisen



def getlevelinfo():

    levellisturl='v1/ai-oral-training/get-level-list'



    url=baseurl+levellisturl

    levellist=requests.get(url=url,headers=header)
    list_level=levellist.json()['data']['level_list']
    # print(levellist.json()['data']['level_list'])
    return list_level


def get_scene_id(levelid):
    list_info = 'v1/ai-oral-training/get-list'
    url=baseurl+list_info
    data={
    "level_id": levelid,
    "uid": 1399976013499392001
}
    get_scene_id_rp=requests.post(url=url,json=data,headers=header)
    scene_id_list=get_scene_id_rp.json()['data']['scene_list']

    return scene_id_list




def getwordinfo(scene_id):

    wordslist = 'v1/ai-oral-training/key-words'
    url =baseurl+wordslist
    date={"scene_id":scene_id,"uid":1399976013499392001}

    wordinfoget=requests.post(url=url,json=date,headers=header)
    wordinfo=wordinfoget.json()['data']['word_list']
    return wordinfo


def getsentenceinfo(scene_id):

    sentencelist='v1/ai-oral-training/sentence'
    url =baseurl+sentencelist

    date={"scene_id":scene_id,"uid":1399976013499392001}

    dialogueinfoget=requests.post(url=url,json=date,headers=header)
    dialogueinfo=dialogueinfoget.json()['data']['dialogue_list']
    return dialogueinfo



if __name__ == '__main__':

    listlevel=getlevelinfo()

    worderrorlist=[]
    for num in range(len(listlevel)):
        level=listlevel[num]['level_id']

        datalist=get_scene_id(level)
        for datanum in range(len(datalist)):

            scene_id=datalist[datanum]['scene_id']

            word=getwordinfo(scene_id)
            for wordnum in range(len(word)):
                word_info1 = word[wordnum]['word_id']
                word_info2 = word[wordnum]['word']
                word_info3 = word[wordnum]['word_phonetic']
                word_info4 = word[wordnum]['word_translation']
                word_info5 = word[wordnum]['word_audio']
                if word_info1 =="" or word_info2 =="" or word_info3 =="" or word_info4 =="" or word_info5 =="":
                    worderrorlist.append([level,scene_id,'word'])

                    break
                else:
                    print('ID为%d单词数据正常！' % scene_id )





            sentence=getsentenceinfo(scene_id)
            for dialoguenum in range(len(sentence)):
                sentence = sentence[dialoguenum]['sentence_list']
                for i in range(len(sentence)):
                    sentenceend=sentence[i]

                    sentence1=sentenceend['role_id']
                    sentence2 = sentenceend['content']
                    sentence3 = sentenceend['content_audio']
                    # print('对话数据:',sentence1,sentence2,sentence3)
                    if sentence1=="" or sentence2=="" or sentence3=="" :
                        worderrorlist.append([level,scene_id,'sentenc'])

                        break
                    else:
                        print('ID为%d对话数据正常！' % scene_id)




    print(worderrorlist)

