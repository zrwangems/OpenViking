---
type: simulink-block
title: 'DQPSK Modulator Baseband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'dqpskmodulatorbaseband'
documentation_source_path: 'ref/dqpskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# DQPSK Modulator Baseband

## 端口

R2025b 中未提供文档。

## 参数

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用差分正交相移键控方法进行调制

DQPSK Modulator Baseband 模块使用差分正交相移键控方法进行调制。输出是调制信号的基带表示。

输入必须是离散时间信号。有关每个模块端口支持的数据类型的信息，请参阅支持的数据类型。

### 整数值信号和二进制值信号

当您将 **Input type** 参数设置为 `Integer` 时，有效输入值为 0、1、2 和 3。在这种情况下，模块接受标量或列向量输入信号。如果第一个输入为 *m*，则调制符号为

exp(jθ + jπm/2)

其中 θ 表示 **Phase rotation** 参数。如果后续输入为 *m*，则调制符号为前一个调制符号乘以 exp(jθ + jπm/2)。

当您将 **Input type** 参数设置为 `Bit` 时，输入包含二进制值对。在这种情况下，模块接受长度为偶数的列向量。下图显示了模块为计算当前符号而用来乘以前一个符号的复数，具体取决于您将 **Constellation ordering** 参数设置为 `Binary` 还是 `Gray`。下图假设您将 **Phase rotation** 参数设置为 π/4；在其他情况下，两个示意图将相应地旋转。

下图显示了当您将 **Phase rotation** 参数设置为 π/4 时，DQPSK 调制方法的信号星座图。箭头指示从每个符号到下一个符号的四种可能转移。`Binary` 和 `Gray` 选项确定每个输入值对与哪种转移相关联。

更一般地，如果 **Phase rotation** 参数的形式为 π/k，其中 *k* 为某个整数，则信号星座图有 2*k* 个点。
