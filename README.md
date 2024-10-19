# KLing API 使用指南

人人都可以创建 AI 虚拟试穿应用，每个电商网站、线下实体店都可以拥有自己的虚拟试穿。
## 步骤
[![My Video](https://i9.ytimg.com/vi/ClyI32_zsRY/mqdefault.jpg?v=67123096&sqp=COyUzLgG&rs=AOn4CLDQ74qnFyXnFyGHPcdaDDJpqJCSBA)](https://www.youtube.com/watch?v=ClyI32_zsRY&t=1s)


1. 在 KLing 的 API 控制台获取 `as` 和 `ak`。
2. 配置 `as` 和 `sk` 到 `virtual_try_on.py` 中：
   ```python
   ak = ""  # 填写 access key
   sk = ""  # 填写 secret key

3、执行以下命令以获取 api_token：
python virtual_try_on.py

4. 将获取的 `api_token` 配置到 `main.py` 的第 8、9 行：
   ```python
   API_ENDPOINT = "https://api.klingai.com/v1/images/kolors-virtual-try-on"
   ACCESS_TOKEN = <获取api_token>
   
5. 执行以下命令以访问应用：
   ```bash
   streamlit run main.py

## 相关链接

- YouTube链接：[点击这里](https://www.youtube.com/watch?v=ClyI32_zsRY)
- B站链接：[点击这里](https://www.bilibili.com/video/BV1eMC2YNEyA/)
