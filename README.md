# resetTermForQuizlet
一个可以重置Quizle下一个单词集所有解释和图像卡片的脚本

#how to use?
1. 登录你的Quizlet
2. 打开浏览器的开发者工具，选择Network选项卡；
3. 选择一个请求，复制为cUrl COMMAND；
4. 打开https://curl.trillworks.com/ ，粘贴你的curl COMMAND，这个网站会把你的cUrl转换为python代码。
5. 复制其中的cookies和header，粘贴到脚本当中，并设置需要重置的单词集ID
6. 运行这个脚本```
$python resetTermForQuizlet.py
able reset done.
about reset done.
```

