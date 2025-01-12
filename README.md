# COIN 新生大语言模型培训一期


## 提示工程

### 知识储备要求
* 熟悉Python编程语言

### 主要学习资料
* [提示工程总结](https://www.promptingguide.ai/zh)
可以快速了解提示工程的定义与各种类别以及对应论文。
主要阅读Introduction与Prompting Techniques两个章节。
请将学习到的Prompt形式利用以下的实验平台进行实验。
* [《大语言模型》](LLM.pdf) 主要学习第十章

### 可视化实验平台
推荐使用Poe（https://poe.com）
平台进行带有可视化界面的提示工程简单实验，便于零基础同学熟悉LLM使用方式。该平台需要注册，免费版可以使用国内外多种不同来源的LLM，包括Llama系列，Gemini系列，GPT系列，QWen系列等。

1. 登录后，平台首页如下所示，选择红框中提供的官方LLM创建bot：
![](figure/poe1.png)
2. 在下方输入框中输入prompt，LLM给出相应回复（下图中使用模型为gpt-4o，需要订阅，gpt-3.5-turbo支持免费访问）
![](figure/poe2.png)

### 批量API访问实验平台
推荐使用钱多多API平台（https://api2.aigcbest.top）
进行可以批量访问的提示工程实验，使用相应的公开LLM api处理大批量数据，便于在研究数据集上实验。注：该网站需要充值，按每次查询大模型的内容量计费，但是相比于大模型的官方API便宜，且不需要翻墙可以使用国外的多个LLM。

各个模型的价目表：https://api2.aigcbest.top/pricing 
如果使用常用的gpt-3.5-turbo模型，一共生成1M token（一百万个单词或汉字）的回复，仅需1.5美元。

### LLM本地化部署进行实验


### 资料汇总

* [清华LLM公开课](https://www.bilibili.com/video/BV1UG411p7zv?buvid=XU11F2D1F1B6721741676EA71D3F31356C54F&from_spmid=playlist.playlist-detail.0.0&is_story_h5=false&mid=w7mFjjzdrDXbKb0J8YwY7g%3D%3D&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=00d7fb01-933c-42b3-89c7-7db4d68bd324&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1725711243&unique_k=HMZ3qGQ&up_id=493282299&wxfid=o7omF0RtW5yr6BgHzKzhtWiTIqNQ&share_times=2&_unique_id_=8e3bd8bb-c73e-43b4-b8fa-a40e89a44691&code=081C9dll2fDEQe44dlnl2sFU4u1C9dlx&state=&spm_id_from=333.788.videopod.episodes) 主要学习4-1到4-10以及4-16内容。
* [Prompt模版对LLM的影响](https://mp.weixin.qq.com/s/OFwqmnB8Qoq-am-OrRstIQ) 
* [微软开源PromptWizard：自动prompt工具](https://mp.weixin.qq.com/s/_0gERIijVNOlQuhmGv5mOg)
* [RePrompt：提示词自动化优化策略](https://mp.weixin.qq.com/s/R6ZsMZwiHNGcfVowUwPvaQ)
* [自动优化LLM流水线](https://mp.weixin.qq.com/s/oog-dCmWFqT6IAC06pIESA)
* [从最少到最多的提示可在大型语言模型中实现复杂的推理](https://mp.weixin.qq.com/s/HX0p0nTmtgOsgzNM8rT_SA)
* [把ICL和IWL双重学习同时写进提示词](https://mp.weixin.qq.com/s/xkSVSD017xaohG3V-1oRow)
* [知识图谱提示激发大型语言模型中的思维图](https://mp.weixin.qq.com/s/Q9qAHmzMjiWvZg8reTw7dQ)
* [通过结构化数据提升大型语言模型推理能力](https://mp.weixin.qq.com/s/wE60z0HtC2um7Wt5ScG-PQ)
