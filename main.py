import streamlit as st
import requests
import json
import time
import base64
import os

# 接口地址和鉴权信息
API_ENDPOINT = "https://api.klingai.com/v1/images/kolors-virtual-try-on"
ACCESS_TOKEN = ""
  # 请替换为您的有效令牌

def create_virtual_try_on_task(human_image, cloth_image, callback_url=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    data = {
        "model_name": "kolors-virtual-try-on-v1",
        "human_image": human_image,
        "cloth_image": cloth_image,
        "callback_url": callback_url
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    response_data = response.json()
    if response.status_code == 200:
        return response_data['data']['task_id']
    else:
        st.error(f"Error creating task: {response_data['message']}")
        return None

def get_virtual_try_on_task(task_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(f"{API_ENDPOINT}/{task_id}", headers=headers)
    response_data = response.json()
    if response.status_code == 200:
        return response_data['data']
    else:
        st.error(f"Error getting task: {response_data['message']}")
        return None

def image_to_base64(image_file):
    if image_file is None:
        st.error("No file uploaded.")
        return None
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# Streamlit 页面布局
st.title("AIGCLINK-KELING虚拟试穿应用")
st.write("上传人物图像和服装图像进行虚拟试穿。")

# 上传图片
human_image_file = st.file_uploader("选择人物图像 (JPEG/PNG)", type=["jpeg", "png"])
cloth_image_file = st.file_uploader("选择服装图像 (JPEG/PNG)", type=["jpeg", "png"])

if st.button("开始试穿"):
    if human_image_file and cloth_image_file:
        # 转换图像为 Base64
        human_image = image_to_base64(human_image_file)
        cloth_image = image_to_base64(cloth_image_file)

        if human_image and cloth_image:
            # 创建虚拟试穿任务
            task_id = create_virtual_try_on_task(human_image, cloth_image)
            if task_id:
                # 等待任务完成
                while True:
                    task_data = get_virtual_try_on_task(task_id)
                    if task_data and task_data['task_status'] in ['succeed', 'failed']:
                        break
                    time.sleep(5)
                print(task_data)
                # 显示结果
                if task_data and task_data['task_status'] == 'succeed':
                    if 'task_result' in task_data and 'images' in task_data['task_result'] and task_data['task_result']['images']:
                        image_url = task_data['task_result']['images'][0]['url']
                        st.image(image_url, caption='虚拟试穿结果', use_column_width=True)
                    else:
                        st.warning("未找到图像URL。")
                else:
                    st.warning("试穿任务失败,请重试。")
    else:
        st.warning("请上传所有必要的图片。")