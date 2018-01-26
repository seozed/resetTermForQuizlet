import requests
import json
import time


class QAuto(object):
    def __init__(self, cookies, headers):
        self.session = requests.Session()
        self.session.cookies = requests.utils.cookiejar_from_dict(cookie_dict=cookies)
        self.session.headers.update(headers)

    def get_terms(self, set_id):
        url = "https://quizlet.com/{id}/edit".format(id=set_id)
        response = self.session.get(url)
        flag = "window.createSetData = "
        start_coord = response.text.index(flag) + len(flag)
        end_coord = response.text[start_coord:].index('};') + start_coord + 1
        text = response.text[start_coord:end_coord]
        item = json.loads(text)
        return item['terms']

    def get_definition(self, word, form_lang='en', to_lang='zh-CN'):
        """
        获取单词解释

        """
        url = f"https://quizlet.com/webapi/3.2/suggestions/definition?corroboration=1&defLang={to_lang}&limit=10&localTermId=-1&word={word}&wordLang={form_lang}"
        response = self.session.get(url)
        item = response.json()
        try:
            return item['responses'][0]['data']['suggestions']['suggestions']
        except KeyError as e:
            return e

    def get_image(self, word):
        url = f"https://quizlet.com/webapi/3.2/images/search?query={word}&perPage=52&languages=%5B%22en%22%2C%22zh-CN%22%5D"
        response = self.session.get(url)
        item = response.json()
        images = item['responses'][0]['models']['image']
        return images

    def set_image(self, termId, imageId, imageCode):
        """
        修改一个单词的图像
        :param termId: 单词ID
        :type termId: int
        :param imageId: 图片ID
        :type imageId: int
        :param imageCode: 图像代码
        :type imageCode: int
        :return:
        :rtype:
        """
        timestamp = int(round(time.time() * 1000))
        data = '{"data":[{"termId":%s,"definitionImageId":%s,"definitionImageCode":"%s"}],"requestId":"%s:termImage:op-seq-0"}' % (
            termId, imageId, imageCode, timestamp)
        response = self.session.post("https://quizlet.com/webapi/3.2/term-images/save?_method=PUT", data=data)
        item = response.json()
        return item

    def set_definition(self, setId, termId, definition):
        """
        设置一个单词的释义
        :param setId: 单词集ID
        :type setId: int
        :param termId: 单词ID
        :type termId: int
        :param definition: 单词解释
        :type definition: str
        :return:
        :rtype:
        """
        timestamp = int(round(time.time() * 1000))
        data = '{"data":[{"setId":%s,"id":%s,"definition":"%s"}],"requestId":"%s:term:op-seq-0"}' % (
            setId, termId, definition, timestamp)
        data = data.encode('utf-8')
        response = self.session.post("https://quizlet.com/webapi/3.2/terms/save?_method=PUT", data=data)
        return response.json()

    def resetImageAndDefinitionForAllTerm(self, setId):
        terms = self.get_terms(setId)
        for term in terms:
            setId = term['setId']
            termId = term['id']
            word = term['word']

            # set term definition
            response = q.get_definition(word=word)
            try:
                definition = response.pop()['text']
                self.set_definition(setId=setId, termId=termId, definition=definition)

                # set term image
                images = self.get_image(word)
                imageId = images[0]['id']
                imageCode = images[0]['code']
                self.set_image(termId, imageId, imageCode)

                msg = "{word} reset done.".format(word=word)
                print(msg)

            except IndexError as e:
                msg = "{word} error: {err}".format(word=word, err=e)


if __name__ == '__main__':
    cookies = {
        '__cfduid': 'xxxxx',
        'qi5': 'xxxxxxxxxxxxxx',
        'fs': 'xxxxxxxxxxxxxx',
        'qlts': 'xxxxxxxxxxxxxx--VcAw',
        '__qca': 'P0-xxxxxxxxxxxxxx-xxxxxxxxxxxxxx',
        '_ga': 'GA1.2.xxxxxxxxxxxxxx.1516845245',
        '__gads': 'ID=7cd98e1b86049e8f:T=1516845244:S=xxxxxxxxxxxxxx',
        'qtkn': 'xxxxxxxxxxxxxx',
        'app_session_first_start': '1',
        'app_session_id': '3614e9a2xxxxxxxxxxxxxx24ce-4035-a7f8-eec11b5201b7',
    }

    headers = {
        'Host': 'quizlet.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.5,zh-HK;q=0.3',
        'Referer': 'https://quizlet.com/256182221/edit',
        'CS-Token': 'xxxxxxxx',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    setId = 256182221

    q = QAuto(cookies=cookies, headers=headers)
    q.resetImageAndDefinitionForAllTerm(setId)
