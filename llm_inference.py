import json
import fire
from vllm import LLM, SamplingParams


def main(
    prompt_path: str = "",      # 输入的prompt路径，json格式
    response_path: str = "",    # 输出的response路径，json格式
    model_path: str = "",       # 模型路径，需要预先从huggingface下载保存到本地
    temperature: float = 0.0,   # LLM解码温度，温度越高LLM回答多样性越强
    top_p = 0.95,               # 解码采样top-p，
    max_tokens = 2048           # prompt + response的总token数（单词数）限制，防止爆显存。
):
    # 从json文件中加载prompt列表
    prompts = json.load(open(prompt_path, 'r'))

    # 加载LLM
    llm = LLM(model=model_path,
              max_model_len=max_tokens,
              gpu_memory_utilization=0.8)

    # 定义解码时的采样策略
    sampling_params = SamplingParams(temperature=temperature,
                                     top_p=top_p,
                                     max_tokens=max_tokens)

    # 执行LLM推理，得到回复
    responses = llm.generate(prompts, sampling_params)

    # 回复格式处理
    responses = [x.outputs[0].text for x in responses]

    # 以json格式存储回复到指定路径
    json.dump(responses,
              open(response_path, 'w', encoding='utf-8'),
              indent=2,
              ensure_ascii=False)


if __name__ == '__main__':
    fire.Fire(main)
