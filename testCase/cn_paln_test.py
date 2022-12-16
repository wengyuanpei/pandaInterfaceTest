

#语文定级计划上报接口
import requests
from time import sleep


list_plan=[["char_id",4],
["char_id",5],
["char_id",8],
["char_id",11],
["char_id",12],
["char_id",14],
["char_id",15],
["char_id",16],
["char_id",17],
["char_id",18],
["char_id",19],
["char_id",20],
["char_id",22],
["char_id",23],
["char_id",26],
["char_id",27],
["char_id",29],
["char_id",29],
["char_id",31],
["char_id",32],
["char_id",33],
["char_id",34],
["char_id",38],
["char_id",40],
["char_id",41],
["char_id",44],
["char_id",46],
["char_id",53],
["char_id",60],
["char_id",72],
["char_id",74],
["char_id",76],
["char_id",77],
["char_id",86],
["char_id",88],
["char_id",97],
["char_id",108],
["char_id",118],
["char_id",140],
["char_id",146],
["char_id",152],
["char_id",183],
["char_id",204],
["char_id",212],
["char_id",254],
["lesson_id",31],
["lesson_id",32],
["lesson_id",33],
["lesson_id",34],
["lesson_id",35],
["lesson_id",36],
["lesson_id",37],
["lesson_id",38],
["lesson_id",39],
["lesson_id",40],
["lesson_id",41],
["lesson_id",42],
["lesson_id",43],
["lesson_id",44],
["lesson_id",45],
["ideo_id",2397],
["ideo_id",2389],
["ideo_id",2380],
["ideo_id",2374],
["ideo_id",2366],
["ideo_id",2359],
["ideo_id",2352],
["ideo_id",2344],
["ideo_id",2336],
["ideo_id",2329],
["ideo_id",2322],
["ideo_id",2316],
["ideo_id",2311],
["ideo_id",2305],
["ideo_id",2298],
["ideo_id",2233],
["ideo_id",2361],
["ideo_id",2340],
["ideo_id",2332],
["ideo_id",2324],
["ideo_id",2319],
["ideo_id",2313],
["ideo_id",2308],
["ideo_id",2297],
["ideo_id",2292],
["ideo_id",2286],
["ideo_id",2262],
["ideo_id",2246],
["ideo_id",2240],
["ideo_id",2194],
["char_id",21],
["char_id",37],
["char_id",42],
["char_id",43],
["char_id",47],
["char_id",51],
["char_id",52],
["char_id",54],
["char_id",62],
["char_id",63],
["char_id",67],
["char_id",80],
["char_id",89],
["char_id",95],
["char_id",98],
["char_id",107],
["char_id",113],
["char_id",116],
["char_id",117],
["char_id",119],
["char_id",122],
["char_id",133],
["char_id",137],
["char_id",143],
["char_id",145],
["char_id",164],
["char_id",165],
["char_id",170],
["char_id",171],
["char_id",199],
["char_id",219],
["char_id",255],
["char_id",269],
["char_id",279],
["char_id",280],
["char_id",284],
["char_id",299],
["char_id",336],
["char_id",574],
["char_id",590],
["char_id",708],
["char_id",774],
["char_id",964],
["char_id",1039],
["lesson_id",46],
["lesson_id",47],
["lesson_id",48],
["lesson_id",49],
["lesson_id",50],
["lesson_id",51],
["lesson_id",52],
["lesson_id",53],
["lesson_id",54],
["lesson_id",55],
["lesson_id",56],
["lesson_id",57],
["lesson_id",58],
["lesson_id",59],
["lesson_id",60],
["ideo_id",2291],
["ideo_id",2285],
["ideo_id",2280],
["ideo_id",2273],
["ideo_id",2267],
["ideo_id",2261],
["ideo_id",2254],
["ideo_id",2247],
["ideo_id",2239],
["ideo_id",2218],
["ideo_id",2275],
["ideo_id",2158],
["ideo_id",2196],
["ideo_id",2171],
["ideo_id",2177],
["ideo_id",2942],
["ideo_id",2888],
["ideo_id",2882],
["ideo_id",2876],
["ideo_id",2894],
["ideo_id",2930],
["ideo_id",2936],
["ideo_id",2783],
["ideo_id",2779],
["ideo_id",2774],
["ideo_id",2769],
["ideo_id",2607],
["ideo_id",2603],
["ideo_id",2600],
["ideo_id",2599],
["char_id",25],
["char_id",64],
["char_id",65],
["char_id",75],
["char_id",82],
["char_id",83],
["char_id",106],
["char_id",110],
["char_id",114],
["char_id",121],
["char_id",125],
["char_id",132],
["char_id",134],
["char_id",135],
["char_id",139],
["char_id",150],
["char_id",161],
["char_id",167],
["char_id",169],
["char_id",190],
["char_id",215],
["char_id",239],
["char_id",241],
["char_id",271],
["char_id",278],
["char_id",317],
["char_id",346],
["char_id",535],
["char_id",586],
["char_id",611],
["char_id",614],
["char_id",655],
["char_id",724],
["char_id",745],
["char_id",751],
["char_id",820],
["char_id",902],
["char_id",978],
["char_id",1018],
["char_id",1054],
["lesson_id",61],
["lesson_id",62],
["lesson_id",63],
["lesson_id",64],
["lesson_id",65],
["lesson_id",66],
["lesson_id",67],
["lesson_id",68],
["lesson_id",69],
["lesson_id",70],
["lesson_id",71],
["lesson_id",72],
["lesson_id",73],
["lesson_id",74],
["lesson_id",75],
["ideo_id",8277],
["ideo_id",8276],
["ideo_id",8278],
["ideo_id",8279],
["ideo_id",8281],
["ideo_id",8280],
["ideo_id",8282],
["ideo_id",8283],
["ideo_id",8285],
["ideo_id",8286],
["ideo_id",8287],
["ideo_id",8284],
["ideo_id",8288],
["ideo_id",8291],
["ideo_id",8290],
["ideo_id",8289],
["ideo_id",8292],
["ideo_id",8295],
["ideo_id",8293],
["ideo_id",8294],
["ideo_id",8296],
["ideo_id",8299],
["ideo_id",8297],
["ideo_id",8298],
["ideo_id",8304],
["ideo_id",8307],
["ideo_id",8305],
["ideo_id",8306],
["ideo_id",8310],
["ideo_id",8309],
["ideo_id",8308],
["ideo_id",8311],
["ideo_id",1679],
["ideo_id",1757],
["ideo_id",1721],
["ideo_id",1686],
["ideo_id",1743],
["ideo_id",1750],
["ideo_id",1734],
["ideo_id",1728],
["ideo_id",1713],
["ideo_id",1700],
["ideo_id",1771],
["ideo_id",1672],
["ideo_id",1642],
["ideo_id",1663],
["ideo_id",1649],
["char_id",73],
["char_id",87],
["char_id",102],
["char_id",103],
["char_id",120],
["char_id",134],
["char_id",141],
["char_id",155],
["char_id",161],
["char_id",172],
["char_id",213],
["char_id",221],
["char_id",225],
["char_id",226],
["char_id",229],
["char_id",230],
["char_id",231],
["char_id",253],
["char_id",261],
["char_id",266],
["char_id",266],
["char_id",270],
["char_id",281],
["char_id",288],
["char_id",295],
["char_id",317],
["char_id",321],
["char_id",332],
["char_id",367],
["char_id",535],
["char_id",548],
["char_id",570],
["char_id",580],
["char_id",635],
["char_id",740],
["char_id",753],
["char_id",816],
["char_id",984],
["char_id",1043],
["char_id",1049],
["char_id",1055],
["char_id",1079],
["lesson_id",5],
["lesson_id",7],
["lesson_id",8],
["lesson_id",9],
["lesson_id",10],
["lesson_id",11],
["lesson_id",12],
["lesson_id",13],
["lesson_id",14],
["lesson_id",16],
["lesson_id",17],
["lesson_id",18],
["lesson_id",19],
["lesson_id",20],
["lesson_id",21],
["ideo_id",8315],
["ideo_id",8312],
["ideo_id",8314],
["ideo_id",8313],
["ideo_id",8317],
["ideo_id",8319],
["ideo_id",8318],
["ideo_id",8316],
["ideo_id",8322],
["ideo_id",8321],
["ideo_id",8320],
["ideo_id",8323],
["ideo_id",8330],
["ideo_id",8329],
["ideo_id",8328],
["ideo_id",8331],
["ideo_id",8334],
["ideo_id",8332],
["ideo_id",8333],
["ideo_id",8335],
["ideo_id",8339],
["ideo_id",8338],
["ideo_id",8336],
["ideo_id",8337],
["ideo_id",8343],
["ideo_id",8340],
["ideo_id",8341],
["ideo_id",8342],
["ideo_id",1698],
["ideo_id",1689],
["ideo_id",1681],
["ideo_id",1670],
["ideo_id",1659],
["ideo_id",1650],
["ideo_id",1644],
["ideo_id",2038],
["ideo_id",2044],
["ideo_id",2031],
["ideo_id",2021],
["ideo_id",2014],
["ideo_id",2006],
["ideo_id",1998],
["ideo_id",1991],

]





list_plan_id=[
983,
984,
985,
986,
987,
988,
989,
990,
991,
992,
993,
994,
995,
996,
997,
998,
999,
1000,
1001,
1002,
1003,
1004,
1005,
1006,
1007,
1008,
1009,
1010,
1011,
1012,
1013,
1014,
1015,
1016,
1017,
1018,
1019,
1020,
1021,
1022,
1023,
1024,
1025,
1026,
1027,
1028,
1029,
1030,
1031,
1032,
1033,
1034,
1035,
1036,
1037,
1038,
1039,
1040,
1041,
1042,
1043,
1044,
1045,
1046,
1047,
1048,
1049,
1050,
1051,
1052,
1053,
1054,
1055,
1056,
1057,
1058,
1059,
1060,
1061,
1062,
1063,
1064,
1065,
1066,
1067,
1068,
1069,
1070,
1071,
1072,
1073,
1074,
1075,
1076,
1077,
1078,
1079,
1080,
1081,
1082,
1083,
1084,
1085,
1086,
1087,
1088,
1089,
1090,
1091,
1092,
1093,
1094,
1095,
1096,
1097,
1098,
1099,
1100,
1101,
1102,
1103,
1104,
1105,
1106,
1107,
1108,
1109,
1110,
1111,
1112,
1113,
1114,
1115,
1116,
1117,
1118,
1119,
1120,
1121,
1122,
1123,
1124,
1125,
1126,
1127,
1128,
1129,
1130,
1131,
1132,
1133,
1134,
1135,
1136,
1137,
1138,
1139,
1140,
1141,
1142,
1143,
1144,
1145,
1146,
1147,
1148,
1149,
1150,
1151,
1152,
1153,
1154,
1155,
1156,
1157,
1158,
1159,
1160,
1161,
1162,
1163,
1164,
1165,
1166,
1167,
1168,
1169,
1170,
1171,
1172,
1173,
1174,
1175,
1176,
1177,
1178,
1179,
1180,
1181,
1182,
1183,
1184,
1185,
1186,
1187,
1188,
1189,
1190,
1191,
1192,
1193,
1194,
1195,
1196,
1197,
1198,
1199,
1200,
1201,
1202,
1203,
1204,
1205,
1206,
1207,
1208,
1209,
1210,
1211,
1212,
1213,
1214,
1215,
1216,
1217,
1218,
1219,
1220,
1221,
1222,
1223,
1224,
1225,
1226,
1227,
1228,
1229,
1230,
1231,
1232,
1233,
1234,
1235,
1236,
1237,
1238,
1239,
1240,
1241,
1242,
1243,
1244,
1245,
1246,
1247,
1248,
1249,
1250,
1251,
1252,
1253,
1254,
1255,
1256,
1257,
1258,
1259,
1260,
1261,
1262,
1263,
1264,
1265,
1266,
1267,
1268,
1269,
1270,
1271,
1272,
1273,
1274,
1275,
1276,
1277,
1278,
1279,
1280,
1281,
1282,
1283,
1284,
1285,
1286,
1287,
1288,
1289,
1290,
1291,
1292,
1293,
1294,
1295,
1296,
1297,
1298,
1299,
1300,
1301,
1302,
1303,
1304,
1305,
1306,
1307,
1308,
1309,
1310,
1311,
1312,
1313,
1314,
1315,
1316,
1317,
1318,
1319,
1320,
1321,
1322,
1323,
1324,
1325,
1326,
1327,
1328,
1329,
1330,
1331,
1332,
1333,
1334,
1335,
1336,
1337,
1338,
1339,
1340,
1341,
1342,
1343,
1344,
1345,
1346,
1347,
1348,
1349,
1350,
1351,
1352,
1353,
1354,
1355,
1356,
1357,
1358,
1359,
1360,
1361,
1362,
1363,
1364,
1365,
1366,
1367,
1368,
1369,
1370,
1371,
1372,
1373,
1374,
1375,
1376,
1377,
1378,
1379,
1380,
1381,
1382,
1383,
1384,
1385,
1386,
1387,
1388,
1389,
1390,
1391,
1392,
1393,
1394,
1395,
1396,
1397,
1398,
1399,
1400,
1401,
1402,
1403,
1404,
1405,
1406,
1407,
1408,
1409,
1410,
1411,
1412,
1413,
1414,
1415,
1416,
1417,
1418,
1419,
1420,
1421,
1422,
1423,
1424,
1425,
1426,
1427,
1428,
1429,
1430,
1431,
1432,
1433,
1434,
1435,
1436,
1437,
1438,
1439,
1440,
1441,
1442,
1443,
1444,
1445,
1446,
1447,
1448,
1449,
1450,
1451,
1452,
1453,
1454,
1455,
1456,
1457,
1458,
1459,
1460,
1461,
1462,
1463,

]





S_plan_resorse=[1,2,3]
url="https://hear.abctime.com/v1/study-cn/finish-plan"
header={  "Content-Type": "application/json;charset=UTF-8"}
# data={"event_id":3,"user_plan_id":2335,"uid":1561969032355688449}
uid_18384243506=1562629060075102209  #

aa=1
for i_S1_w,plan_id_s in list_plan_id,list_plan:
    aa+=1
    if aa == 7:
        break
    for i_S1_w_event_id in (1, 2, 3):
        data = {"event_id": i_S1_w_event_id, "user_plan_id": i_S1_w, "uid": uid_18384243506}
        sleep(2)
        print('请求参数：', data)
        reqsts = requests.post(url=url, headers=header, json=data)
        print('S1字卡学习完成上报：', reqsts.text)
        # 获取当日推荐学习内容
        plan_url = "https://hear.abctime.com/v1/study-cn/plan-info"
        data_plan = {"uid": uid_18384243506}
        plan_req = requests.post(url=plan_url, headers=header, json=data_plan)
        plan_next_day = plan_req.json()["data"]["user_plan_info"]["ch_character"][plan_id_s[0]]
        if plan_next_day == str(plan_id_s[1]):
            print('当日推荐计划与预期一致')
        else:
            print('当日推荐计划与预期一致,IDs:',plan_id_s[1])

