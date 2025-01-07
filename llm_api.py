from random import randint
import json
from http import client

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]


def prompt_llm(prompt, model_name="gpt-4o-mini"):
    random_agent = user_agents[randint(0, len(user_agents) - 1)]

    conn = client.HTTPSConnection("api2.aigcbest.top")
    """
    这个地方填主站或者其他分站的网址，35.aigcbest.top的分站便宜，但是模型只有gpt-4o系列的。
    api2.aigcbest.top 里面比较全 但是比较贵
    """

    payload = json.dumps({
        "model": model_name,
        "temperature": 0,
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}]
    })

    headers = {
        'Accept': 'application/json',
        'Authorization': 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  # 这个地方填申请的令牌(API TOKEN)
        'User-Agent': random_agent,
        'Content-Type': 'application/json'
    }
    # 这块User-Agent的random_agent是我加的，不换容易被封或者报错，可能会慢一点

    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    response = res.read()
    response_utf8 = response.decode('utf-8')
    return json.loads(response_utf8)['choices'][0]['message']['content']


if __name__ == '__main__':

    user_inputs = 'hello, who are you?'
    response = prompt_llm(prompt=user_inputs, model_name='gpt-4o-mini')
    print(response)
