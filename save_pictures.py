import json
import os
import requests

def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_image(path,image_uri, title):
    try:
        # 构造文件的完整路径
        file_path = f"{path}/{title}.png"

        # 检查文件是否已经存在
        if os.path.exists(file_path):
            print(f"文件已存在，跳过：{file_path}")
            return

        # 如果文件不存在，继续下载
        response = requests.get(image_uri)
        response.raise_for_status()

        # 确保保存图片的目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"图片已保存：{file_path}")
    except requests.RequestException as e:
        print(f"下载图片失败：{e}")

def save_description(path, description):
    try:
        # 构造文件的完整路径
        file_path = f"{path}/description.txt"

        # 检查文件是否已经存在
        if os.path.exists(file_path):
            print(f"描述文件已存在，跳过：{file_path}")
            return

        # 确保保存描述的目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 保存描述到文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(description)

        print(f"描述文件已保存：{file_path}")
    except Exception as e:
        print(f"保存描述文件失败：{e}")
def main(data):
    # JSON数据中的图片保存路径字段是`description`字段
    path = data['data']['collection']['title'].strip()

    # 保存描述文件
    description = data['data']['collection']['description']
    save_description(path, description)

    # 保存封面图片
    cover_uri = data['data']['collection']['thumbnail']['uri']
    save_image(path, cover_uri, "cover")

    # 遍历集合中的每一项
    for item in data['data']['collection']['collectionItems']['edges']:
        if item is not None:
            node = item['node']
            # 获取图片的uri
            image_uri = node['item']['thumbnail']['front']['uri']
            # 获取标题
            title = node['item']['title']
            # 保存图片
            save_image(path, image_uri, title)

def process_json_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            # 加载JSON数据
            data = load_json_data(file_path)
            # 处理数据
            main(data)

if __name__ == "__main__":
    # 指定包含JSON文件的目录路径
    directory_path = 'responses'
    process_json_files(directory_path)