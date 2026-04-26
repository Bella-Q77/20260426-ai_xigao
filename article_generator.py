import random
from datetime import datetime

CATEGORY_TEMPLATES = {
    "育儿": {
        "intro_templates": [
            "作为一名宝爸/宝妈，今天想和大家聊聊关于{topic}的那些事儿。在育儿的道路上，我们都是不断学习的新手。",
            "关于{topic}，相信很多家长都有自己的困惑。今天我就来分享一下我的心得体会。",
            "最近很多朋友问我关于{topic}的问题，今天整理了一些实用的经验分享给大家。"
        ],
        "sections": [
            {
                "title": "为什么要重视{topic}",
                "points": [
                    "首先，{topic}对于孩子的成长发育至关重要",
                    "很多家长容易忽视这一点，但实际上影响深远",
                    "专家建议，越早关注{topic}效果越好"
                ]
            },
            {
                "title": "实用建议与方法",
                "points": [
                    "第一点：要保持耐心，循序渐进",
                    "第二点：观察孩子的反应，灵活调整",
                    "第三点：结合孩子的个性特点来实施",
                    "第四点：定期评估效果，及时优化"
                ]
            },
            {
                "title": "常见误区提醒",
                "points": [
                    "误区一：急于求成，给孩子太大压力",
                    "误区二：盲目跟风，不考虑实际情况",
                    "误区三：缺乏持续性，三天打鱼两天晒网"
                ]
            }
        ],
        "conclusion_templates": [
            "总之，{topic}需要家长们用心对待。希望今天的分享能够帮助到大家，祝每个宝宝都能健康快乐成长！",
            "育儿之路漫漫，关于{topic}还有很多值得探讨的地方。欢迎大家在评论区交流分享自己的经验。",
            "以上就是关于{topic}的一些心得体会。如果觉得有用，记得点赞收藏哦！"
        ],
        "emojis": ["👶", "❤️", "💡", "✨", "🌟", "🌸", "🌈", "🎈"],
        "hashtags": ["#育儿经验#", "#宝妈分享#", "#科学育儿#", "#育儿日记#"]
    },
    "母婴": {
        "intro_templates": [
            "怀孕和产后的这段时间，妈妈们最关心的就是{topic}了。今天来聊聊我的亲身体验。",
            "作为过来人，关于{topic}我有一些实用的建议想分享给新手妈妈们。",
            "很多准妈妈问我关于{topic}的问题，今天整理了一篇超详细的攻略。"
        ],
        "sections": [
            {
                "title": "关于{topic}你需要知道",
                "points": [
                    "怀孕期间，{topic}的变化是正常的生理反应",
                    "了解这些知识，可以帮助你更好地应对",
                    "有疑问一定要及时咨询医生或专业人士"
                ]
            },
            {
                "title": "好物推荐清单",
                "points": [
                    "必备好物一：选择舒适透气的产品",
                    "必备好物二：口碑好的大品牌更放心",
                    "必备好物三：根据不同阶段及时更换",
                    "避坑提醒：这些产品真的不推荐购买"
                ]
            },
            {
                "title": "日常护理小贴士",
                "points": [
                    "保持清洁卫生是第一位的",
                    "注意观察身体的变化信号",
                    "定期产检，及时了解情况",
                    "保持良好的心态也很重要哦"
                ]
            }
        ],
        "conclusion_templates": [
            "以上就是关于{topic}的全部内容了。希望每位妈妈都能轻松度过这段特别的时光！",
            "关于{topic}还有什么想了解的，欢迎在评论区留言。祝所有准妈妈和妈妈们身体健康！",
            "如果觉得这篇分享有用，记得点赞收藏转发给需要的朋友哦！"
        ],
        "emojis": ["🤰", "👶", "💝", "🌸", "✨", "🎀", "💫", "🌈"],
        "hashtags": ["#母婴好物#", "#孕期日记#", "#产后恢复#", "#新手妈妈#"]
    },
    "求职": {
        "intro_templates": [
            "最近收到很多私信问关于{topic}的问题，作为过来人，我整理了一些实用经验分享给大家。",
            "找工作是每个职场人都会经历的阶段，关于{topic}，这些经验你一定要知道！",
            "今天来聊聊大家最关心的{topic}，全是干货，建议收藏！"
        ],
        "sections": [
            {
                "title": "关于{topic}的核心认知",
                "points": [
                    "首先要明确自己的定位和目标",
                    "了解市场行情和行业发展趋势",
                    "知己知彼，才能做出正确的选择"
                ]
            },
            {
                "title": "具体操作指南",
                "points": [
                    "第一步：准备一份亮眼的简历",
                    "第二步：针对性地投递岗位",
                    "第三步：面试前的充分准备",
                    "第四步：面试中的沟通技巧",
                    "第五步：面试后的跟进与复盘"
                ]
            },
            {
                "title": "避坑指南",
                "points": [
                    "这些常见误区一定要避免",
                    "不要盲目投递，要有针对性",
                    "薪资谈判的技巧你知道吗？",
                    "试用期这些权益一定要维护"
                ]
            }
        ],
        "conclusion_templates": [
            "以上就是关于{topic}的全部内容。希望大家都能找到心仪的工作！",
            "求职路上，{topic}是非常重要的一环。如果还有疑问，欢迎在评论区交流。",
            "祝大家都能拿到满意的offer！觉得有用记得点赞收藏哦！"
        ],
        "emojis": ["💼", "🎯", "💡", "📈", "✨", "🚀", "💪", "🌟"],
        "hashtags": ["#求职经验#", "#面试技巧#", "#职场干货#", "#找工作#"]
    },
    "星座": {
        "intro_templates": [
            "大家好！今天来聊聊{topic}，看看最近的运势如何。",
            "关于{topic}，近期有哪些值得注意的地方呢？一起来看看吧！",
            "很多朋友私信问关于{topic}的运势，今天就来详细解析一下。"
        ],
        "sections": [
            {
                "title": "整体运势分析",
                "points": [
                    "近期整体运势呈现上升趋势",
                    "事业方面可能会有新的机遇",
                    "感情方面需要多一些沟通",
                    "财运方面保持稳定即可"
                ]
            },
            {
                "title": "各方面详细解析",
                "points": [
                    "事业运：把握机会，稳步前行",
                    "感情运：主动沟通，增进理解",
                    "财运：稳健投资，避免冲动",
                    "健康运：注意休息，劳逸结合"
                ]
            },
            {
                "title": "好运小贴士",
                "points": [
                    "幸运色：柔和的色彩能带来好运",
                    "幸运数字：这些数字近期很有缘分",
                    "宜：保持积极心态，主动出击",
                    "忌：犹豫不决，过度焦虑"
                ]
            }
        ],
        "conclusion_templates": [
            "以上就是关于{topic}的全部解析。运势仅供参考，最重要的还是保持积极的心态！",
            "关于{topic}你有什么感受呢？欢迎在评论区分享。祝大家好运连连！",
            "喜欢星座运势的朋友们记得关注哦，定期更新最新运势解析！"
        ],
        "emojis": ["⭐", "✨", "🌟", "💫", "🔮", "🌙", "☀️", "🌈"],
        "hashtags": ["#星座运势#", "#十二星座#", "#运势解析#", "#每日运势#"]
    },
    "默认": {
        "intro_templates": [
            "今天想和大家聊聊{topic}这个话题。",
            "关于{topic}，相信很多人都有自己的看法。",
            "最近关于{topic}的讨论很多，我也来分享一下我的观点。"
        ],
        "sections": [
            {
                "title": "关于{topic}的几点思考",
                "points": [
                    "首先，我们要理解{topic}的核心是什么",
                    "其次，要看到事物的多面性",
                    "最后，结合实际情况做出判断"
                ]
            },
            {
                "title": "具体分析",
                "points": [
                    "从不同角度来看这个问题",
                    "分析其中的利弊得失",
                    "探讨可能的解决方案",
                    "总结一些实用的建议"
                ]
            }
        ],
        "conclusion_templates": [
            "以上就是关于{topic}的全部内容。感谢阅读！",
            "关于{topic}你有什么看法呢？欢迎在评论区交流。",
            "如果觉得这篇文章有用，记得点赞收藏哦！"
        ],
        "emojis": ["✨", "💡", "🌟", "📝", "🌈", "🎯", "💪", "🎉"],
        "hashtags": ["#干货分享#", "#知识分享#", "#经验交流#"]
    }
}

def generate_article(topic, category, style_info=None):
    if style_info is None:
        style_info = {}
    
    template = CATEGORY_TEMPLATES.get(category, CATEGORY_TEMPLATES["默认"])
    
    intro = random.choice(template["intro_templates"]).format(topic=topic)
    conclusion = random.choice(template["conclusion_templates"]).format(topic=topic)
    
    sections_content = []
    for section in template["sections"]:
        section_title = section["title"].format(topic=topic)
        points = section["points"]
        
        section_content = f"## {section_title}\n\n"
        for i, point in enumerate(points, 1):
            formatted_point = point.format(topic=topic)
            if style_info.get("has_emoji", False):
                emoji = random.choice(template["emojis"])
                section_content += f"{emoji} {formatted_point}\n\n"
            elif style_info.get("has_list", True):
                section_content += f"{i}. {formatted_point}\n\n"
            else:
                section_content += f"{formatted_point}\n\n"
        
        sections_content.append(section_content)
    
    title = generate_title(topic, category)
    
    if style_info.get("has_emoji", False):
        intro = random.choice(template["emojis"]) + " " + intro
        conclusion = random.choice(template["emojis"]) + " " + conclusion
    
    if style_info.get("has_hashtag", False):
        hashtags = " ".join(template["hashtags"][:3])
        conclusion += "\n\n" + hashtags
    
    article = f"# {title}\n\n"
    article += f"{intro}\n\n"
    article += "".join(sections_content)
    article += conclusion
    
    return {
        "title": title,
        "content": article,
        "category": category,
        "topic": topic,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def generate_title(topic, category):
    title_templates = [
        "关于{topic}，你一定要知道的几件事",
        "{topic}超全攻略！建议收藏",
        "干货分享：{topic}详解",
        "过来人告诉你关于{topic}的真相",
        "关于{topic}，这些经验太有用了",
        "{topic}入门到精通，看这一篇就够了",
        "为什么我说{topic}很重要？",
        "{topic}常见问题解答",
        "亲测有效的{topic}经验分享",
        "关于{topic}的深度解析"
    ]
    
    return random.choice(title_templates).format(topic=topic)

def get_available_categories():
    return list(CATEGORY_TEMPLATES.keys())

if __name__ == "__main__":
    result = generate_article("宝宝辅食添加", "育儿", {"has_emoji": True, "has_hashtag": True})
    print(result["content"])
