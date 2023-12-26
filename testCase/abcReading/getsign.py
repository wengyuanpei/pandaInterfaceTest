from common.abcSign import *

aaa={
	"book_nums": 2,
	"cid": 11,
	"uid": 63439,
	"year": 1,
	"sign": "20bd78fa5dd5eb65c7c480fb54e655f906e26df2fbefe8d3fc7748a14cbac685"
}

a='a3478fc914a48eaa30bb137d3c0987b038481b4c5a26d7ef92582523c537f82b'

data = 'uid=11940857&rank_type=3&time_type=3&content_id=3&size=20&timestamp=1703493897'

aaa1={
	"book_nums": 2,
	"cid": 11,
	"uid": 63439,
	"year": 1}


dataaa={'uid':11940857,'rank_type':3,'time_type':3,'content_id':3,'size':20,'timestamp':1703494662}
sign=getSignEnd(aaa1,'dev')
print(sign)


