# COIN 新生大语言模型培训指南


## 提示工程（大语言模型入门）

### 知识储备要求
* 熟悉Python编程语言

### 可视化实验平台
推荐使用Poe（https://poe.com）
平台进行带有可视化界面的提示工程简单实验，便于零基础同学熟悉LLM使用方式。该平台需要注册，免费版可以使用国内外多种不同来源的LLM，包括Llama系列，Gemini系列，GPT系列，QWen系列等。

1. 登录后，平台首页如下所示，选择红框中提供的官方LLM创建bot：
![](figure/poe1.png)
2. 在下方输入框中输入prompt，LLM给出相应回复（下图中使用模型为gpt-4o，需要订阅，gpt-3.5-turbo支持免费访问）
![](figure/poe2.png)

### 批量API访问实验平台
推荐使用钱多多API平台（https://api2.aigcbest.top）
进行可以批量访问的提示工程实验，用于帮助进阶的同学使用相应的LLM api处理大批量数据，便于在研究数据集上实验。注：该网站需要充值，按每次查询大模型的内容量计费，但是相比于大模型的官方API便宜，且不需要翻墙可以使用国外的多个LLM。

各个模型的价目表：https://api2.aigcbest.top/pricing 
如果使用常用的gpt-3.5-turbo模型，一共生成1M token（一百万个单词或汉字）的回复，仅需1.5美元。

### 资料汇总

* 提示工程总结博客： https://www.promptingguide.ai
可以快速了解提示工程的定义与各种类别以及对应论文。


## 神经网络模型基础

本节内容需要结合Pytorch教程学习

### 知识储备要求
* 数学基础知识：线性代数，微积分，概率统计，离散数学
* 机器学习基础：监督学习和无监督学习，过拟合和欠拟合，模型评估指标（如准确率、精确率、召回率、F1 分数），交叉验证

### 传统神经网络

#### CNN模型
原理讲解：https://zhuanlan.zhihu.com/p/156926543

#### RNN/LSTM/GRU模型
原理讲解：https://zhuanlan.zhihu.com/p/123211148

### Transformer模型

Transformer是一种深度学习模型架构，最初由Google团队在2017年提出。它专为处理序列数据（如自然语言）而设计，并在自然语言处理任务中表现出色，后来也广泛应用于计算机视觉、语音处理等领域。目前，几乎所有熟知的LLM都基于这一架构。

* 原论文连接：https://arxiv.org/abs/1706.03762
* 对Transformer的代码注解：https://nlp.seas.harvard.edu/2018/04/03/attention.html
哈佛NLP组对Transformer的基本功能的简单实现。阅读其代码与注解，可以深入理解transformer中的attention机制与位置编码的具体实现。

### 传统预训练模型

预训练模型（Pre-trained Models）是近年来人工智能领域，特别是自然语言处理（NLP）和计算机视觉（CV）领域的核心技术之一。它通过在大规模数据上进行预训练，学习通用的特征表示，然后可以通过微调（fine-tuning）或迁移学习（transfer learning）来适应具体任务。

#### BERT
BERT是由Google在2018年提出的一种基于Transformer架构的自然语言处理模型，旨在通过双向的上下文学习方法来理解语言的深层含义。
* 原论文链接：https://arxiv.org/abs/1810.04805
* 原理讲解：https://zhuanlan.zhihu.com/p/46652512

#### GPT
GPT是一种基于深度学习的自然语言处理模型，由 OpenAI 开发。它的核心技术是 Transformer 架构，这是一种在处理序列数据（如文本）方面非常高效的神经网络结构。也是目前ChatGPT系列的模型的原型。
* 原论文链接：https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
* 原理讲解：https://zhuanlan.zhihu.com/p/636915538

#### T5
T5 是由谷歌在2019年提出的一种基于Transformer的自然语言处理预训练模型。T5的核心创新在于将几乎所有的自然语言处理任务统一为文本到文本的形式，即将输入和输出都看作字符串，从而简化了任务的定义和模型的设计。

* 原论文链接：https://arxiv.org/abs/1910.10683
* 原理讲解：https://zhuanlan.zhihu.com/p/88438851

## PyTorch教程

PyTorch 是一个开源的深度学习框架，由 Meta（原 Facebook）开发并维护。它以动态计算图和灵活易用为特点，广泛应用于学术研究和工业实践。

PyTorch 提供了一整套工具，用于构建和训练神经网络，包括：

- **自动微分**：通过动态计算图自动计算梯度，便于实现复杂模型和调试。
- **灵活性**：支持动态调整网络结构，适合研究和实验。
- **GPU 加速**：轻松利用 GPU 提升计算效率。
- **丰富的生态系统**：包括高层封装库（如 TorchVision、TorchText、TorchAudio 等）和工具（如 Lightning、HuggingFace 等）。

PyTorch是目前最广泛使用的深度学习框架之一。

### 知识储备要求
* 熟悉Python编程语言
* 熟悉深度学习算法，经典神经网络模型结构

### 资料汇总
* 官方文档：https://pytorch.org/tutorials/
* 中文文档：https://pytorch123.com
* Pytorch实用教程：https://tingsongyu.github.io/PyTorch-Tutorial-2nd/

## HuggingFace

HuggingFace包含了Transformers库，Dataset库和Model库。
Transformers 是一个Python（主要基于Pytorch）库，用于自然语言处理。它包含了多种以transformer模型为基础架构的预训练模型相关代码，如BERT、GPT、RoBERTa、T5、llama家族等。这些模型可以很容易地用于自然语言理解和生成任务。
Dataset库提供了快速、高效的方式来下载、预处理和加载NLP数据集。
Model库运营着一个模型中心，这是一个共享和发现预训练模型的平台。用户可以上传自己训练的模型，或者下载别人分享的模型，应用于不同的机器学习任务。

### 知识储备要求
* 熟悉Python编程语言，Pytorch框架
* 熟悉各种神经网络模型结构以及预训练模型架构原理

### 资料汇总
* 官方网址：https://huggingface.co

很多经典的PLM（LLM），数据集，都会上传到该网站，开源供研究者下载。

目前，可以从 https://huggingface.co/docs/transformers/index
中查找到目前几乎所有的PLM的代码实现，学习相关模型的具体实现与API调用接口，方便后续对模型架构进行修改。

## 大语言模型进阶学习

### 知识储备要求：
* 熟悉Python编程语言，Pytorch框架
* 熟悉各种神经网络模型结构以及预训练模型架构原理
* 熟悉HuggingFace的Transfromers代码实现，以及常用API接口

### 主要学习资料

* [《大语言模型》](LLM.pdf)
强烈推荐的一本关于LLM的学习资料，但需要配合前面的基础知识进行学习。
此书与本教程的内容有较多重叠，可以对先前知识完成补全。
可以重点学习第六、七、八、九章。
* [清华LLM公开课](https://www.bilibili.com/video/BV1UG411p7zv?buvid=XU11F2D1F1B6721741676EA71D3F31356C54F&from_spmid=playlist.playlist-detail.0.0&is_story_h5=false&mid=w7mFjjzdrDXbKb0J8YwY7g%3D%3D&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=00d7fb01-933c-42b3-89c7-7db4d68bd324&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1725711243&unique_k=HMZ3qGQ&up_id=493282299&wxfid=o7omF0RtW5yr6BgHzKzhtWiTIqNQ&share_times=2&_unique_id_=8e3bd8bb-c73e-43b4-b8fa-a40e89a44691&code=081C9dll2fDEQe44dlnl2sFU4u1C9dlx&state=&spm_id_from=333.788.videopod.episodes)
系统的了解大模型的历史、原理和前沿进展。
* [GPT系列论文精读](https://www.bilibili.com/video/BV1AF411b7xQ)
* [Llama3.1论文精读](https://www.bilibili.com/video/BV1WM4m1y7Uh/)

### 主要论文
* GPT3：https://arxiv.org/abs/2005.14165
* InstructGPT：https://arxiv.org/pdf/2203.02155
* RLHF：https://www.cs.utexas.edu/~ai-lab/pubs/ICML_IL11-knox.pdf
* Llama：https://arxiv.org/abs/2302.13971
* Llama2：https://arxiv.org/abs/2307.09288
* GPT-4：https://arxiv.org/abs/2303.08774
* O1：https://openai.com/index/learning-to-reason-with-llms/
* Llama3：https://arxiv.org/abs/2407.21783
* Prompt：https://dl.acm.org/doi/pdf/10.1145/3560815
* LoRA：https://arxiv.org/abs/2106.09685
* PPO：https://arxiv.org/pdf/1707.06347
* DPO：https://arxiv.org/abs/2305.18290

### LLM训练推理实验平台

[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)是一个github开源项目，集成了二十多个llama家族模型的相关代码。这些代码包含pre-training，supervised fine-tuning，Reward Modeling，DPO等LLM中的基本阶段。通过该框架，可以在不深入了解每个模型的底层实现的前提下，快速上手微调模型。使用时与huggingface提供的模型结合使用。具体操作请参考项目首页的README。

以下README提供了当前版本下，各种训练方式的指令，需要熟悉。
https://github.com/hiyouga/LLaMA-Factory/blob/main/examples/README.md

在科研中，如果不涉及更改LLM的结构，例如修改attention机制，增加MOE等，一般直接调用这些API指令即可完成对模型的各种训练需求，其中重点需要掌握Lora Supervised Fine-Tuning（应用最广泛）。

### 预训练
预训练通常非常吃资源，实验室通常难以完成，因此资料主要以了解为主。

* [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
* [LLM训练技术讲解](https://zhuanlan.zhihu.com/p/636270877)

### Prompt技术

* Prompt对LLM的影响：https://mp.weixin.qq.com/s/OFwqmnB8Qoq-am-OrRstIQ
* COT：https://arxiv.org/abs/2201.11903
* PromptWizard：https://mp.weixin.qq.com/s/_0gERIijVNOlQuhmGv5mOg
* RePrompt：https://mp.weixin.qq.com/s/R6ZsMZwiHNGcfVowUwPvaQ
* DSPy：https://mp.weixin.qq.com/s/oog-dCmWFqT6IAC06pIESA
* Least-to-Most：https://mp.weixin.qq.com/s/HX0p0nTmtgOsgzNM8rT_SA
* ICL：https://mp.weixin.qq.com/s/xkSVSD017xaohG3V-1oRow
* 知识图谱prompt：https://mp.weixin.qq.com/s/Q9qAHmzMjiWvZg8reTw7dQ
* 结构化语言prompt：https://mp.weixin.qq.com/s/wE60z0HtC2um7Wt5ScG-PQ

### 检索生成增强

* 一文读懂RAG：https://www.zhihu.com/tardis/zm/art/675509396?source_id=1003
* 同济RAG综述：https://arxiv.org/abs/2312.10997
* PDF解析RAG：https://mp.weixin.qq.com/s/OJgKzoLMw_SZ-9petsAyYA
* 现有RAG框架总结：https://mp.weixin.qq.com/s/4AEC-JWccUgNLP1xp9RgVw
* Search-O1：https://mp.weixin.qq.com/s/gqnGyMM_KYYwDbHyWkIIuw
自主知识检索新框架
* GraphRAG：https://github.com/microsoft/graphrag
* LightRAG：https://github.com/HKUDS/LightRAG

### LLM Agent
* LLM Agent综述：https://arxiv.org/abs/2308.11432
* LangChain：https://www.langchain.com
* Language Agent：https://yusu.substack.com/p/language-agents

### LLM推理加速
* vLLM：https://qiankunli.github.io/2024/07/07/vllm.html
最广泛使用的大模型推理加速范式
* Falcon：https://mp.weixin.qq.com/s/QfNiSWyGThJyw2IEY5Ltvg
* Retrival-Attention：https://mp.weixin.qq.com/s/AhYvVpCHCeJalaKkkFsWMQ

### LLM可解释性
* 程序性知识：https://mp.weixin.qq.com/s/udRoUMDzDpfApi5xymFk9w