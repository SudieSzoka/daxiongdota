import os
import requests
import json

def fetch_webhook_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_data(data, directory='data'):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for user in data:
        user_id = user.get('user_id')
        if not user_id:
            continue  # 跳过没有 user_id 的记录
        
        user_file = os.path.join(directory, f'{user_id}.json')
        
        # 读取现有数据
        if os.path.exists(user_file):
            with open(user_file, 'r', encoding='utf-8') as f:
                try:
                    user_data = json.load(f)
                except json.JSONDecodeError:
                    user_data = []
        else:
            user_data = []
        
        # 添加新记录
        new_records = user.get('records', [])
        user_data.extend(new_records)
        
        # 保存回文件
        with open(user_file, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=4)

def main():
    webhook_url = os.getenv('WEBHOOK_URL')
    data = fetch_webhook_data(webhook_url)
    save_data(data)

if __name__ == "__main__":
    main()