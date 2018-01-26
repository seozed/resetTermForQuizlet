# resetTermForQuizlet
一个可以重置Quizle下一个单词集所有解释和图像卡片的脚本

#how to use?
# resetTermForQuizlet

一个可以重置Quizle下一个单词集所有解释和图像卡片的脚本

# how to use?

1. 登录你的[Quizlet](https://quizlet.com/)

2. 打开浏览器的开发者工具，选择**Network**选项卡；

3. 选择一个请求，复制为cUrl COMMAND；

4. 打开https://curl.trillworks.com/ ，粘贴你的curl COMMAND，这个网站会把你的cUrl转换为python代码。

5. 打开`resetTermForQuizlet.py`, 把cookies和header，粘贴到脚本当中，同时设置你的单词集ID。它看起来应该是这样的

   ```python
   if __name__ == '__main__':
       cookies = {
           '__cfduid': 'xxxxxxx',
           'qi5': 'xxxxxx',
           'fs': 'xxxxxxx',
           'qlts': 'xxxxxxxx',
           '__qca': 'xxxxxx',
           '_ga': 'xxxxxxxx',
           '__gads': 'xxxxxxxx',
           'qtkn': 'xxxxxxxx',
           'app_session_first_start': '1',
           'app_session_id': 'xxxxxxxx',
       }

       headers = {
           'Host': 'quizlet.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.5,zh-HK;q=0.3',
           'Referer': 'https://quizlet.com/',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
           'DNT': '1',
           'Pragma': 'no-cache',
           'Cache-Control': 'no-cache',
           'CS-Token': 'xxxxxxxxxx',
           # 请确保头部拥有CS-Token
       }

       q = QAuto(cookies=cookies, headers=headers)
       q.resetImageAndDefinitionForAllTerm(256182221)

   ```

   ​

6. 运行这个脚本

```
$python resetTermForQuizlet.py
able reset done.
about reset done.
...
```
