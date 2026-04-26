from flask import Flask, render_template, request, jsonify
from weibo_hot import get_weibo_hot_search
from article_parser import parse_article_url
from article_generator import generate_article, get_available_categories

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hot-search', methods=['GET'])
def hot_search():
    try:
        top_n = request.args.get('top_n', 20, type=int)
        hot_data = get_weibo_hot_search(top_n)
        
        return jsonify({
            'success': True,
            'data': hot_data,
            'source': '微博热搜',
            'count': len(hot_data)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/parse-article', methods=['POST'])
def parse_article():
    try:
        data = request.get_json()
        url = data.get('url', '')
        
        if not url:
            return jsonify({
                'success': False,
                'error': '请提供文章链接'
            }), 400
        
        style_info = parse_article_url(url)
        
        return jsonify({
            'success': True,
            'data': style_info
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/generate-article', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        category = data.get('category', '默认')
        style_info = data.get('style_info', None)
        
        if not topic:
            return jsonify({
                'success': False,
                'error': '请提供文章主题'
            }), 400
        
        result = generate_article(topic, category, style_info)
        
        return jsonify({
            'success': True,
            'data': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/categories', methods=['GET'])
def categories():
    cats = get_available_categories()
    return jsonify({
        'success': True,
        'data': cats
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
