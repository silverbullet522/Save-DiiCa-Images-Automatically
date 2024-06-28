from mitmproxy import http
import json
import os

select = input("输入1：选择保存DiiCa\n输入2：选择保存Liella/LiyuuCollection\n")
if select == "1":
    monitored_url = "https://diica-api-utoniq.graphcdn.app/"
    print("正在保存DiiCa的响应...")
elif select == "2":
    monitored_url = "https://api-utoniq.graphcdn.app/"
    print("正在保存Liella/LiyuuCollection的响应...")
else:
    print("输入错误，请重新输入")


# 保存响应的目录
output_dir = "responses"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def response(flow: http.HTTPFlow) -> None:
    # 检查请求的 URL
    if flow.request.pretty_url.startswith(monitored_url):
        # 解析请求内容
        try:
            request_json = json.loads(flow.request.text)
            if request_json.get("operationName") == "CollectionDetail":
                # 构建文件名
                file_name = os.path.join(output_dir, f"{flow.request.timestamp_start}.json")
                # 保存响应内容
                with open(file_name, 'w') as f:
                    json.dump(flow.response.json(), f, indent=2)
        except (json.JSONDecodeError, AttributeError):
            pass

# 入口函数
addons = [
    response
]
