import requests

def get(url, params=None, headers=None):
    """发送 GET 请求并返回响应数据"""
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()  # 返回 JSON 格式的响应
    else:
        response.raise_for_status()  # 抛出异常以处理错误

def post(url, data=None, headers=None):
    """发送 POST 请求并返回响应数据"""
    response = requests.post(url, json=data, headers=headers)  # 使用 json 参数自动转换为 JSON
    if response.status_code in (200, 201):
        return response.json()  # 返回 JSON 格式的响应
    else:
        response.raise_for_status()  # 抛出异常以处理错误

