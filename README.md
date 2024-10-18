# KLing API 使用指南

人人都可以创建 AI 虚拟试穿应用，每个电商网站、线下实体店都可以拥有自己的虚拟试穿。

## 步骤

1. 在 KLing 的 API 控制台获取 `as` 和 `ak`。
2. 配置 `as` 和 `sk` 到 `virtual_try_on.py` 中：
   ```python
   ak = ""  # 填写 access key
   sk = ""  # 填写 secret key

3、执行以下命令以获取 api_token：
python virtual_try_on.py

4、将获取的 api_token 配置到 main.py 的第 8、9 行：

API_ENDPOINT = "https://api.klingai.com/v1/images/kolors-virtual-try-on"
ACCESS_TOKEN = <获取api_token>

5、执行以下命令以访问应用：
streamlit run main.py
访问 localhost:8501。
