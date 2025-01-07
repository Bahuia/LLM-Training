# COIN 新生科研培训指南

## 大语言模型基础知识


### 提示工程（Prompt Engineering）

先导知识：无

#### 可视化实验平台
推荐使用Poe（https://poe.com）平台进行带有可视化界面的提示工程简单实验，便于零基础同学熟悉LLM使用方式。该平台需要注册，免费版可以使用国内外多种不同来源的LLM，包括Llama系列，Gemini系列，GPT系列，QWen系列等。

1. 登录后，平台首页如下所示，选择红框中提供的官方LLM创建bot：
![](figure/poe1.png)
2. 在下方输入框中输入prompt，LLM给出相应回复（下图中使用模型为gpt-4o，需要订阅，gpt-3.5-turbo支持免费访问）
![](figure/poe2.png)

#### 批量API访问实验平台
推荐使用钱多多API平台（https://api2.aigcbest.top）进行可以批量访问的提示工程实验，用于帮助进阶的同学使用相应的LLM api处理大批量数据，便于在研究数据集上实验。注：该网站需要充值，按每次查询大模型的内容量计费，但是相比于大模型的官方API便宜，且不需要翻墙可以使用国外的多个LLM。

各个模型的价目表：https://api2.aigcbest.top/pricing 
如果使用常用的gpt-3.5-turbo模型，一共生成1M token（一百万个单词或汉字）的回复，仅需1.5美元。

#### 资料汇总

* 提示工程总结博客： https://www.promptingguide.ai
可以快速了解提示工程的定义与各种类别以及对应论文。

* 