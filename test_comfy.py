import requests
import json

# 加载你的 workflow.json
with open('modules/aigc_pipeline/workflow.json', 'r', encoding='utf-8') as f:
    workflow = json.load(f)

# 设置提示词
workflow['6']['inputs']['text'] = 'a cute cat'
workflow['7']['inputs']['text'] = 'ugly'

# 提交
response = requests.post('http://127.0.0.1:8188/prompt', json={'prompt': workflow})
print(response.json())