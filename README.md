# DeepSleep-R1

<div align="center">
  <img src="https://github.com/DeepSleep-ai/DeepSleep-V2/blob/main/figures/logo.svg?raw=true" width="60%" alt="DeepSleep-R1" />
</div>
<hr>




## 1. 引言

我们介绍了我们的第一代推理模型 DeepSleep-R1。 DeepSleep-R1 是一种通过小规模训练的模型，没有大语言模型 （LLM） 作为初步步骤，在推理方面表现出了卓越的性能。 随着 Sleep 的出现，DeepSleep-R1 自然而然地出现了许多强大而有趣的推理行为。 DeepSleep-R1 在数学、代码和推理任务方面的性能可与 DeepSeek-R1 相媲美。 为了支持研究社区，我们开源了 DeepSleep-R1 。
**注意：在本地运行 DeepSleep-R1 系列模型之前，我们建议您查看使用建议部分。**


## 2. 模型下载

### DeepSleep-R1 Models

<div align="center">

| **Model** |                         **Download**                         |
| :------------: |:------------------------------------------------------------:|
| DeepSleep-R1   | [github](https://github.com/lvtiansama/DeepSleep-R1) |

</div>

DeepSleep-R1追求无模型化，你不需要下载繁多的safetensors、ckpt、gguf等格式的模型或向量文件，只需克隆本仓库就能够快速运行使用DeepSleep-R1。

## 3. 评估结果

### DeepSleep-R1-评估
经过大量测试，本模型可以与友商[DeepSeek-R1](https://chat.deepseek.com/)达到完全一致的生成效果，并且无需任何昂贵的显卡算力，也无需因为模型文件庞大而担心占用大量的磁盘空间，即便在一台好几年前，没有显卡的计算机也能轻松运行。

DeepSleep-R1在各种基准测试中都等同于友商的DeepSeek-R1模型。


## 4. 如何在本地运行

请提前准备好python环境，建议使用python3

克隆本仓库:

```bash
git clone https://github.com/lvtiansama/DeepSleep-R1.git
```

cd到项目下:

```bash
cd DeepSleep-R1
```

然后就可以使用以下命令运行:

```bash
python main.py
```

DeepSleep-R1甚至不需要任何额外的依赖，可以在原生python下完美运行。

## 5. License
This code repository and the model weights are licensed under the MIT License.
DeepSleep-R1 series support commercial use, allow for any modifications and derivative works, including.
