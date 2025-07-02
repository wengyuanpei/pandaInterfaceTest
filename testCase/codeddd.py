import json



def traverse_json(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print("  " * indent + f"Key: {key}")
            traverse_json(value, indent + 1)
    elif isinstance(data, list):
        for item in data:
            traverse_json(item, indent + 1)
    else:
        print("  " * indent + f"Value: {data}")


if __name__ == '__main__':
    js = {
        "ab_study_flow3": 1,
        "again_coin": 5,
        "challenges_id": 208,
        "continue_true_num": 0,
        "cost_time": 1,
        "extra": "{\"allCount\":0,\"challengeRate\":1,\"correctCount\":0,\"currentCorrectCount\":0,\"maxCorrentCount\":0,\"maxScore\":0,\"openCount\":0}",
        "false_num": 0,
        "is_again": "false",

        "proportion": 25,
        "repair_date": 0,
        "score": 0,
        "stage": -1,
        "stage_num": 3,
        "stage_type": 1,
        "true_num": 0,
        "true_proportion": 0,
        "uid": 73279,
        "video_urls": []}
    traverse_json(js)

