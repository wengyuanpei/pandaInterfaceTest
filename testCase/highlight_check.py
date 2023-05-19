import  requests
from time import sleep
token='Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxNjQwOTc2ODgyODYyOTg1MjE3Iiwic3ViIjoie1wiaWRcIjoxNjQwOTc2ODgyODYyOTg1MjE3LFwibW9iaWxlXCI6XCIrODYxNzM0NTA0MzM2NVwifSIsImV4cCI6MTY5OTg0MDQ3MH0.BQZ8VFcc2_LdnzQgr3ZRjxtLJ4DNVzinGjiq-yopfczA6KWFZz0Pc_CzaekPghRepkbSGmHGZljMGBpKNpPFjw'
header = {'Authorization':token}

UID=1640976882862985217

url='https://hear-pre.abctime.com/v1/highlights/level'



level_list=[0,1,2,3,4,5,6]
type_list=[2]
# 绘本总数查看
book_count=[]
for level in level_list:
    for type in type_list:

        data = {"level": level, "type": type, "uid": UID}

        rep_List=requests.post(url=url,json=data,headers=header)

        book_id=rep_List.json()['data']['book_list']

        if len(book_id) != 0:
            book_count.append(len(book_id))
        print('level:',level,'type:',type,'count:',len(book_id))

# print(book_count)
cover_null=[]
cover_null_id=[]
#获取没有封面的id
for level in level_list:
    data = {"level": level, "type": 2, "uid": UID}
    rep_List1 = requests.post(url=url, json=data, headers=header)
    rep_List2 = rep_List1.json()['data']['book_list']
    for id in range(0, len(rep_List2) - 1):
        idcoverbooknull = rep_List2[id]['classify_id']
        idcoverbooknull_name = rep_List2[id]['name']
        if rep_List2[id]['cover']=='':
            print(rep_List2[id])
            null_data=str(idcoverbooknull)+':'+str(idcoverbooknull_name)
            cover_null.append(null_data)
            cover_null_id.append(idcoverbooknull)
print('封面为空classify_id>>',cover_null)
print('封面为空classify_id>>',cover_null_id)




# l1 核对
#
# data_l1={"level":1,"type":2,"uid":1640976882862985217}
#
# rep_l1=requests.post(headers=header,url=url,json=data_l1)
#
# book_list=rep_l1.json()['data']['book_list']
# print(book_list)
# # print(len(book_list))
#
# id_list=[]
# id_name=[]
#
# for id in range(0,len(book_list)-1):
#
#     idlistbook=book_list[id]['classify_id']
#     idlistbook_name=book_list[id]['name']
#     adname=str(idlistbook)+':'+str(idlistbook_name)
#     print(adname)
#
#     id_list.append(adname)
#     id_name.append(idlistbook_name)
#     # id_name
# print(id_list)
# tru_list=[2859,
# 2422,
# 2421,
# 2425,
# 2426,
# 2427,
# 2430,
# 2432,
# 2433,
# 2435,
# 2447,
# 2424,
# 2428,
# 2429,
# 2431,
# 2423,
# 2434,
# 2655,
# 2438,
# 2889,
# 2439,
# 2440,
# 2437,
# 2441,
# 2443,
# 2444,
# 2445,
# 2442,
# 2446,
# 2971,
# 2972,
# 2973,
# 2974,
# 2979,
# 3301,
# 3310,
# 2946,
# 2947,
# 2957,
# 2976,
# 2975,
# 3163,
# 3298,
# 3314,
# 3319,
# 3334,
# 3238,
# 3264,
# 2937,
# 3060,
# 3061,
# 3062,
# 3070,
# 3071,
# 3072,
# 3073,
# 3074,
# 3076,
# 3083,
# 3084,
# 3085,
# 3086,
# 3088,
# 3111,
# 3116,
# 3118,
# 3119,
# 3120,
# 3123,
# 3125,
# 3126,
# 3127,
# 3161,
# 3164,
# 3165,
# 3166,
# 3169,
# 3171,
# 3172,
# 3173,
# 3192,
# 3193,
# 3195,
# 3196,
# 3211,
# 3212,
# 3213,
# 3214,
# 3215,
# 3220,
# 3228,
# 3229,
# 3233,
# 3235,
# 3239,
# 3263,
# 3265,
# 3269,
# 3270,
# 3274,
# 3275,
# 3278,
# 3279,
# 3280,
# 3288,
# 3292,
# 3293,
# 3294,
# 3295,
# 3296,
# 3297,
# 3299,
# 3300,
# 3302,
# 3303,
# 3311,
# 3312,
# 3313,
# 3315,
# 3316,
# 3317,
# 2932,
# 3335,
# 3336,
# 3337,
# 3338,
# 3339,
# 3340,
# 3345,
# 3346,
# 3347,
# 3348,
# 3350,
# 3349,
# 3351,
# 3352,
# 3353,
# 3354,
# 3361,
# 3366,
# 3367,
# 3368,
# 3369,
# 3370,
# 3371,
# 3372,
# 3373,
# 3375,
# 3379,
# 3385,
# 3387,
# 3388,
# 3389,
# 3390,
# 3391,
# 3392,
# 3393,
# 3398,
# 3399,
# 3405,
# 3406,
# 3407,
# 3408,
# 3416,
# 3418,
# 3421,
# 3422,
# 3423,
# 3424,
# 3425,
# 3426,
# 3431,
# 3475,
# 3478,
# 3168,
# 2859,
# 2724,
# 2455,
# 2454,
# 2453,
# 2456,
# 2457,
# 2458,
# 2459,
# 2650,
# 2718,
# 2722,
# 2723,
# 2735,
# 2736,
# 3019,
# 3050,
# 3262,
# 2448,
# 2449,
# 2451,
# 3053,
# 2452,
# 2450,
# 2466,
# 2469,
# 2471,
# 2472,
# 2473,
# 2474,
# 2475,
# 2476,
# 2477,
# 2460,
# 2462,
# 2464,
# 2465,
# 2461,
# 2467,
# 2468,
# 2737,
# 2991,
# 2993,
# 2996,
# 2998,
# 3002,
# 3010,
# 3017,
# 3022,
# 3025,
# 3027,
# 3029,
# 3034,
# 3045,
# 3095,
# 3096,
# 3097,
# 3174,
# 3175,
# 3177,
# 3179,
# 3455,
# 3456,
# 2463,
# 3014,
# 2470,
# 2852,
# 2871,
# 2982,
# 2984,
# 2986,
# 2987,
# 2988,
# 2989,
# 2997,
# 3004,
# 3008,
# 3042,
# 3043,
# 3044,
# 3056,
# 3058,
# 3099,
# 3100,
# 3101,
# 3102,
# 3103,
# 3106,
# 3108,
# 3110,
# 3134,
# 3135,
# 3140,
# 3144,
# 3146,
# 3147,
# 3148,
# 3149,
# 3150,
# 3151,
# 3152,
# 3155,
# 3181,
# 3184,
# 3191,
# ]
# name=["Airplane",
# "Dot and Dan",
# "Animal Families",
# "Family",
# "Thanksgiving Dinner",
# "Feelings",
# "A Park Rangers Day",
# "What Friends Do",
# "Goal",
# "Beach Baby",
# "Gulp",
# "Careful",
# "Sharing",
# "Girls and Boys",
# "Together",
# "Day and Night",
# "My Day",
# "Buff Ducks",
# "Hello Spot",
# "I Can!",
# "I Say",
# "Happy",
# "Hugs and Kisses",
# "Go Go Go",
# "Pumpkin Pie",
# "Community Helpers",
# "Gardening",
# "Baby Feelings",
# "Who Shares",
# "Blue",
# "Five Little Ducks",
# "Beach Day",
# "Fish!",
# "Splash",
# "Ours",
# "Give to Our Center",
# "The Tooth Fairy",
# "Bouncy",
# "I Can Hop",
# "Food from the Farm",
# "Baby Bunny’s Train",
# "First Steps",
# "We Can Clean!",
# "Making Tacos",
# "Fun With Baby",
# "My Toy",
# "Traveling with Teddy",
# "Uh-Oh!",
# "The Timbertoes: Hunting for Honey",
# "Nap Time",
# "I Love Words",
# "Nighty-Nighty, Baby Bunny",
# "A Book for Baby ' Roo",
# "A Very Long Car Ride",
# "All Kinds of Baskets",
# "Babies-Everywhere!",
# "Baby Band",
# "Baby Bunny and the Storm",
# "Baby Bunny in Autumn",
# "Baby Bunny in the Snow",
# "Baby Bunny Sings Along",
# "Baby Play",
# "Baby's Mealtime",
# "Barnyard-Breakfast",
# "Bath Time for Baby Bunny",
# "Beds",
# "Big Red Slide",
# "Bunny Hop",
# "Bus Ride",
# "Busy Day",
# "Busy Town",
# "Counting Sheep",
# "Daddy's Home",
# "Flying High",
# "Four Fun Chicks",
# "Guess Where I'm Hiding",
# "Here I Am",
# "Houses",
# "Knock, Knock",
# "Little Wagon",
# "Lullabies All Around",
# "Mirror Baby",
# "Monkey Baby",
# "My Best Day",
# "My Picture",
# "Noisy Zoo",
# "At the Zoo",
# "October Fun",
# "On a Roll",
# "On the Farm",
# "Pickups",
# "Reading-Together",
# "Snowman and Friends",
# "Springtime",
# "Twice as Nice",
# "Twins at the Table",
# "Walk to Daddy",
# "Watch Them Go",
# "We Love To...",
# "What I Like",
# "When They Grow Up",
# "Where Do You Nap?",
# "Where Has Ava Gone?",
# "Where Is Baby Bunny?",
# "Where's Teddy?",
# "Where's Your Belly Button?",
# "Who Is...",
# "Who Says ' Boo'?",
# "You Can Read...",
# "Your Wonderful Body",
# "Caring for Your Dog",
# "Our Home",
# "I Can Do It",
# "How Can We Share?",
# "How We Treat Others?",
# "The Stream",
# "New Year's Eve",
# "Holidays",
# "Just Like Me",
# "The Pig",
# "The X-Ray",
# "Friends!",
# "How I Feel",
# "The Timbertoe: A Chilly Adventure",
# "The Timbertoe: A Heartfelt Surprise",
# "The Timbertoe: A New Game",
# "The Timbertoe: A Pumpkin Party",
# "The Timbertoe: A Rare Sighting",
# "The Timbertoes: A Summer Treat",
# "The Timbertoes: A Tasty Treat",
# "The Timbertoes: An Autumn Surprise",
# "The Timbertoes: Backyard Game",
# "The Timbertoes: Building a Tower",
# "The Timbertoes: Building a Pet Door",
# "The Timbertoes: Canoe Adventure",
# "The Timbertoes: Creature Concert",
# "The Timbertoes: Doggy Distraction",
# "The Timbertoes: Fall Harvest",
# "The Timbertoes: Fix-It Day",
# "The Timbertoes: Garden Thieves",
# "The Timbertoes: Helping Hands",
# "The Timbertoes: Long-Distance Calling",
# "The Timbertoes: Making a Splash",
# "The Timbertoes: May Day Fun",
# "The Timbertoes: Muddy Clues",
# "The Timbertoes: Night Creatures",
# "The Timbertoes: Pa's Latest Invention",
# "The Timbertoes: Planting Potatoes",
# "The Timbertoes: Practice Makes Perfect",
# "The Timbertoes: Pumpkin Problem",
# "The Timbertoes: Rafting",
# "The Timbertoes: Raking Leaves",
# "The Timbertoes: River Slide",
# "The Timbertoes: Sap's Running!",
# "The Timbertoes: Sign of Spring",
# "The Timbertoes: Skis for Everyone!",
# "The Timbertoes: Snow and Sun",
# "The Timbertoes: Snow Play",
# "The Timbertoes: Spring is Coming",
# "The Timbertoes: Squiggly Pretzels",
# "The Timbertoes: Star Gazing",
# "The Timbertoes: Stuck Indoors",
# "The Timbertoes: Tent Trouble",
# "The Timbertoes: The Grasshopper",
# "The Timbertoes: The Mysterious Moon",
# "The Timbertoes: Tommy Gets Fit",
# "The Timbertoes: Tommy's Hat",
# "The Timbertoes: Walk in the Snow",
# "The Timbertoes: What's for Dinner?",
# "The Timbertoes: Who's Quickest?",
# "The Timbertoes: Winter Wonderful!",
# "The Timbertoes: Wishing for Spring",
# "JUNGLE ABC",
# "POLAR WORDS",
# "Hello, Hat",
# "Airplane",
# "New Friends",
# "Red",
# "Farm 123",
# "Green",
# "Yellow",
# "Winging It",
# "It's My Turn",
# "Get Moving",
# "A Ship and Shells",
# "My Grandpa",
# "Moving Day",
# "A Neighborhood Garden",
# "A Good Home",
# "The Beans Plants",
# "At a Street Fair",
# "Giants of the Sea",
# "Jack and Jill",
# "How Do Animals Use Their Voice and Sounds",
# "How Do Animals Use Their Wings",
# "How Do Animals Use Their Flippers",
# "I Go to the Dentist",
# "I'm the Boss",
# "How Do Animals Use Their Mouths",
# "Who Stole the Veggies",
# "Let's Get Pizza",
# "What's in a Tree",
# "What's in a Log",
# "What's in a Hole",
# "What's Inside a Cave",
# "Getting Your Zzzzs",
# "Clean Hands Dirty Hands",
# "What's in a Shell",
# "The Sound I Love Best",
# "Clean Teeth Dirty Teeth",
# "Peekaboo Spot",
# "Ocean Colors",
# "Love Is",
# "In The Big City",
# "Achoo",
# "Building A Playground",
# "The Game",
# "The Right Pet for Carl",
# "Stone Soup",
# "Who Can Get the Cheese?",
# "Losing Your Dog",
# "Sharing With Luke",
# "Keep It Clean",
# "Teamwork",
# "Pigs in My Garden",
# "We Give Thanks",
# "Do You Have Good Manners?",
# "It's Our School",
# "Feet!",
# "Samantha",
# "I Quit!",
# "My Computer Pal",
# "My Family Album",
# "Things We Like",
# "Together and Alone",
# "What Is a Friend?",
# "Good Night",
# "Hi, Ho, Teddy-O",
# "Fabulous Food",
# "It's Hard to Wait",
# "Sleepyheads Snooze",
# "Basketball",
# "Run Swim Fly",
# "Pet Show",
# "The Little Red Hen",
# "Cat, Dog, Dog",
# "The Basketball Game",
# "The Birthday Party",
# "Jade and Jamal",
# "Recess with Rosie",
# "Three Is Not a Crowd",
# "Dog Wash",
# "Labor Day",
# "Tricking Mr. Brown",
# "Fairness",
# "The Unhappy Troll",
# "Kickball",
# "What Will Sherman Shoot?",
# "Crystl's Crystls",
# "The Mice",
# "Salad Time!",
# "Little Bee Wants to Help",
# "Clay Today!",
# "Special Person Day",
# "Spider Spin",
# "Theodore",
# "How Would You Feel?",
# "I Can't Help Now",
# "All About Broken Bones",
# "Davy Duck's Grumpy Day",
# "My New Sister",
# "Dinosaur",
# "When We Were One",
# "The Big Race",
# "Do You See Chameleon?",
# "Tom's New Class",
# "The Family Show",
# "Maps Are Flat, Globes Are Round",
# "North, South, East, and West",
# "Waterways",
# "Keys and Symbols on Maps",
# ]
#
#
# #列表数据对比
# #等级配置表和代码跑出的数据差集对比
# diff_book_d=set(tru_list).difference(set(id_list))
#
# print(diff_book_d)
#
# #代码抛出数据和配置表差集
# diff_book_a=set(id_list).difference(set(tru_list))
# print(diff_book_a)
#
# diff=set(id_name).difference(set(name))
# print('名字差异：',diff)
