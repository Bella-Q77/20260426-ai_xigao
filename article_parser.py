import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

def parse_article_url(url):
    try:
        domain = urlparse(url).netloc
        
        if "weibo.com" in domain or "weibo.cn" in domain:
            return parse_weibo_article(url)
        elif "zhihu.com" in domain:
            return parse_zhihu_article(url)
        elif "bilibili.com" in domain or "b23.tv" in domain:
            return parse_bilibili_article(url)
        else:
            return parse_general_article(url)
    
    except Exception as e:
        print(f"解析文章URL失败: {e}")
        return get_default_style()

def parse_weibo_article(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        
        content = ""
        for script in soup.find_all("script"):
            if "render_data" in script.text:
                match = re.search(r'pageInfo":\s*(\{.*?\})', script.text)
                if match:
                    try:
                        import json
                        data = json.loads(match.group(1))
                        content = data.get("status", {}).get("text", "")
                    except:
                        pass
                break
        
        if not content:
            content = soup.get_text()
        
        style_info = analyze_content_style(content)
        style_info["source"] = "微博"
        
        return style_info
    
    except Exception as e:
        print(f"解析微博文章失败: {e}")
        return get_default_style()

def parse_zhihu_article(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        
        content_elem = soup.find("article") or soup.find(class_="RichContent-inner")
        content = content_elem.get_text() if content_elem else soup.get_text()
        
        style_info = analyze_content_style(content)
        style_info["source"] = "知乎"
        
        return style_info
    
    except Exception as e:
        print(f"解析知乎文章失败: {e}")
        return get_default_style()

def parse_bilibili_article(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        
        content_elem = soup.find(id="read-article-holder") or soup.find(class_="article-holder")
        content = content_elem.get_text() if content_elem else soup.get_text()
        
        style_info = analyze_content_style(content)
        style_info["source"] = "哔哩哔哩"
        
        return style_info
    
    except Exception as e:
        print(f"解析B站文章失败: {e}")
        return get_default_style()

def parse_general_article(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        
        for elem in soup(["script", "style", "nav", "header", "footer", "aside"]):
            elem.decompose()
        
        content_elem = soup.find("article") or soup.find("main") or soup.body
        content = content_elem.get_text() if content_elem else soup.get_text()
        
        style_info = analyze_content_style(content)
        style_info["source"] = "通用网页"
        
        return style_info
    
    except Exception as e:
        print(f"解析通用网页失败: {e}")
        return get_default_style()

def analyze_content_style(content):
    sentences = re.split(r'[。！？\n]', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    
    avg_sentence_length = sum(len(s) for s in sentences) / len(sentences) if sentences else 0
    
    has_emoji = any(ord(c) > 0x1F000 for c in content)
    
    has_hashtag = '#' in content
    
    has_list = any(marker in content for marker in ['\n- ', '\n1. ', '\n（1）', '、'])
    
    if avg_sentence_length < 15:
        sentence_style = "短句简洁"
    elif avg_sentence_length < 30:
        sentence_style = "中等长度"
    else:
        sentence_style = "长句详细"
    
    if has_emoji and has_hashtag:
        style_type = "社交媒体风格"
    elif has_list:
        style_type = "列表式科普风格"
    else:
        style_type = "叙事散文风格"
    
    paragraphs = content.split('\n\n')
    avg_paragraph_length = sum(len(p) for p in paragraphs) / len(paragraphs) if paragraphs else 0
    
    if avg_paragraph_length < 50:
        paragraph_style = "段落短小"
    elif avg_paragraph_length < 150:
        paragraph_style = "段落适中"
    else:
        paragraph_style = "段落较长"
    
    return {
        "style_type": style_type,
        "sentence_style": sentence_style,
        "paragraph_style": paragraph_style,
        "has_emoji": has_emoji,
        "has_hashtag": has_hashtag,
        "has_list": has_list,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_paragraph_length": round(avg_paragraph_length, 1),
        "content_length": len(content),
        "source": "未知"
    }

def get_default_style():
    return {
        "style_type": "通用科普风格",
        "sentence_style": "中等长度",
        "paragraph_style": "段落适中",
        "has_emoji": False,
        "has_hashtag": False,
        "has_list": True,
        "avg_sentence_length": 20,
        "avg_paragraph_length": 100,
        "content_length": 0,
        "source": "默认模板"
    }

if __name__ == "__main__":
    test_url = "https://weibo.com"
    style = parse_article_url(test_url)
    print("文章风格分析结果:")
    for key, value in style.items():
        print(f"{key}: {value}")
