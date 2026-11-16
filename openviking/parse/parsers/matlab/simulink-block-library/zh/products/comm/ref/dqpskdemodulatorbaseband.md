---
type: simulink-block
title: 'DQPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Phase Modulation'
documentation_page: 'dqpskdemodulatorbaseband'
documentation_source_path: 'ref/dqpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# DQPSK Demodulator Baseband

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

对 DQPSK 调制数据进行解调

DQPSK Demodulator Baseband 模块对使用差分正交相移键控方法调制的信号进行解调。输入是调制信号的基带表示。

输入必须是离散时间复信号。输出取决于当前符号与前一个符号之间的相位差。由于不存在前一个符号，模块输出的第一个整数（如果您将 **Output type** 参数设置为 `Bit`，则为第一个二进制对）采用零初始条件。

此模块接受标量或列向量输入信号。有关各模块端口支持的数据类型的信息，请参阅“支持的数据类型”。

### 输出和星座图类型

当您将 **Output type** 参数设置为 `Integer` 时，模块将相位差

θ + πm/2

映射到 *m*，其中 θ 表示 **Phase rotation** 参数，*m* 为 0、1、2 或 3。

当您将 **Output type** 参数设置为 `Bit` 时，输出包含二进制值对。对于 **Constellation ordering** 参数为 `Binary` 或 `Gray` 的情况，DQPSK Modulator Baseband 模块的参考页说明了哪些相位差映射到每个二进制对。
