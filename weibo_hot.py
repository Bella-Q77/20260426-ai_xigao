import requests
from datetime import datetime

WEIBO_HOT_URL = "https://weibo.com/ajax/side/hotSearch"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://weibo.com/",
}

def get_weibo_hot_search(top_n=20):
    try:
        response = requests.get(WEIBO_HOT_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        hot_list = []
        realtime_list = data.get("data", {}).get("realtime", [])
        
        for idx, item in enumerate(realtime_list):
            if idx >= top_n:
                break
            
            word = item.get("word", "")
            hot_rank = idx + 1
            category = item.get("category", "")
            hot_num = item.get("num", 0)
            
            if item.get("is_commercial", 0) == 1:
                continue
            
            search_url = f"https://s.weibo.com/weibo?q={requests.utils.quote(word)}"
            
            hot_list.append({
                "rank": hot_rank,
                "title": word,
                "url": search_url,
                "category": category,
                "hot_value": hot_num,
                "source": "微博热搜"
            })
        
        return hot_list
    
    except Exception as e:
        print(f"获取微博热搜失败: {e}")
        return get_fallback_hot_search(top_n)

def get_fallback_hot_search(top_n=20):
    fallback_topics = [
        "育儿经验分享", "母婴好物推荐", "2024求职攻略", "十二星座运势",
        "春季护肤技巧", "健康饮食指南", "职场人际关系", "宠物日常",
        "旅行攻略推荐", "家居装修灵感", "学习方法分享", "健身减肥计划",
        "星座配对分析", "宝宝辅食制作", "面试技巧大全", "情感心理",
        "投资理财入门", "手账生活记录", "美食探店分享", "数码产品评测"
    ]
    
    hot_list = []
    for idx, topic in enumerate(fallback_topics[:top_n]):
        search_url = f"https://s.weibo.com/weibo?q={requests.utils.quote(topic)}"
        hot_list.append({
            "rank": idx + 1,
            "title": topic,
            "url": search_url,
            "category": "热门话题",
            "hot_value": 1000000 - idx * 50000,
            "source": "微博热搜(示例)"
        })
    
    return hot_list

if __name__ == "__main__":
    hot_data = get_weibo_hot_search(10)
    for item in hot_data:
        print(f"{item['rank']}. {item['title']} - {item['url']}")
