---
type: simulink-block
title: 'eSpeak Text to Speech'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'espeaktexttospeech'
documentation_source_path: 'supportpkg/raspberrypi_ref/espeaktexttospeech.html'
language: zh-CN
chinese_source: worker-translation
---

# eSpeak Text to Speech

## 端口

### 输入

### **ASCII text** — 输入 ASCII 文本字符向量

该模块接受一个数组，该数组会按以下格式转换为其 ASCII 等价形式：`uint8('character vector')`。例如，你可以将 `uint8('Hello world')` 或 `uint8('1 2
3')` 发送到该模块的输入端口。但是，如果你将 `[1 2
3]` 发送到输入，则该模块不执行任何操作。

**数据类型：** `uint8`

## 参数

在 R2025b 中未记录。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

在默认音频设备上将文本转换为语音

使用 eSpeak Text to Speech 模块，通过 eSpeak 语音合成器将文本转换为语音。该模块通过连接到 Raspberry Pi® 板的默认音频设备输出合成语音。

如果你在主计算机上仿真包含 eSpeak Text to Speech 模块的模型，而未在 Raspberry Pi 板上运行该模型，则该模块会产生零值（或无输出）。有关详细信息，请参阅“模块在仿真中产生零值或不执行任何操作”。你必须在外部模式（Monitor & Tune）下使用此模块，或者将模型部署到 Raspberry Pi 板上，才能听到语音合成器的输出。

当你在外部模式下运行包含该模块的模型时，该模块会自动启动一个后台进程，将输入文本转换为其对应的 ASCII 值。转换结束后，该模块即可转换另一个输入文本数组。如果输入文本与当前正在转换的文本重叠，则该模块会启动多个并发运行的后台进程。尽管 Linux® 声音驱动程序会混合来自这些进程的声音，但生成的输出不理想。并发运行过多进程会产生错误。
