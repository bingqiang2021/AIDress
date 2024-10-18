KLing API：人人都可以创建AI虚拟试穿应用，每个电商网站、线下实体店都可以拥有自己的虚拟试穿

1、在kling的API控制台获取as和ak
2、配置as和sk到virtual_try_on.py中
ak = "" # 填写access key
sk = "" # 填写secret key

3、执行：python virtual_try_on.py，获取api_token
4、将获取的api_token配置到main.py的第8、9行：
API_ENDPOINT = "https://api.klingai.com/v1/images/kolors-virtual-try-on"
ACCESS_TOKEN = <获取api_token>

5、执行streamlit run  main.py即可访问localhost:8501访问

youtube链接：https://www.youtube.com/watch?v=ClyI32_zsRY
b站链接：https://www.bilibili.com/video/BV1eMC2YNEyA/
