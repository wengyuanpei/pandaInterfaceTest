

import json


def flatten_json_to_str(data):
    """将JSON键值对拼接为连续字符串"""
    result = []

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                # 处理嵌套字典或列表
                nested = flatten_json_to_str(value)
                if nested:  # 只有当嵌套结果非空时才添加
                    result.append(f"{key}{nested}")
            elif value is not None:  # 忽略None值
                # 特殊处理extra字段(已经是字符串的JSON)
                if key == "extra":
                    try:
                        extra_data = json.loads(value)
                        extra_str = flatten_json_to_str(extra_data)
                        result.append(f"{key}{extra_str}")
                    except json.JSONDecodeError:
                        result.append(f"{key}{value}")
                else:
                    result.append(f"{key}{value}")
    elif isinstance(data, list):
        for item in data:
            nested = flatten_json_to_str(item)
            if nested:
                result.append(nested)

    return "".join(result)

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

sc={
  "company": {
    "name": "未来科技",
    "founded": 2010,
    "departments": [
      {
        "name": "研发部",
        "employees": 50,
        "projects": [
          {
            "name": "AI助手",
            "status": "active",
            "milestones": {
              "phase1": "2022-03",
              "phase2": "2023-06"
            }
          }
        ]
      },
      {
        "name": "市场部",
        "budget": 1200000,
        "campaigns": {
          "current": "夏季促销",
          "upcoming": ["双十一", "黑五"]
        }
      }
    ],
    "financials": {
      "2022": {
        "revenue": 5000000,
        "profit": 1200000
      },
      "2023": {
        "revenue": 6200000,
        "profit": {
          "Q1": 300000,
          "Q2": 400000,
          "Q3": "预估中"
        }
      }
    }
  },
  "metadata": {
    "last_updated": "2023-07-15T08:30:00Z",
    "contacts": [
      {
        "type": "email",
        "value": "contact@futuretech.com"
      },
      {
        "type": "phone",
        "value": "+86 13800138000"
      }
    ]
  }
}
formatted_result = flatten_json_to_str(sc)
print(formatted_result)
