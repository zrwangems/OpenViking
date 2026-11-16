---
type: simulink-block
title: 'General QAM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'generalqamdemodulatorbaseband'
documentation_source_path: 'ref/generalqamdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# General QAM Demodulator Baseband

## 端口

R2025b 中未提供文档。

## 参数

**Signal constellation**
:   列出星座点的实数或复数向量。

**Output type**
:   确定模块是输出整数还是输出整数的二进制表示。

    如果将此参数设置为 `Integer`，模块将输出整数。

    如果将此参数设置为 `Bit`，当 **Decision type** 设置为 `Hard decision` 时，模块会为每个符号输出一组 K 个比特，称为*二进制字*。如果 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio`，模块将分别输出逐比特 LLR 和近似 LLR。

**Decision type**
:   指定在解调过程中使用硬判决、LLR 还是近似 LLR。有关详细信息，请参阅硬判决解调与软判决解调。

    要启用此参数，请将 **Output type** 设置为 `Bit`。

**Variance source**
:   将此参数设置为 `Dialog` 时，可以在 **Variance** 参数中指定噪声方差。将此选项设置为 `Port` 时，模块上会出现一个端口，可通过该端口输入噪声方差。

    要启用此参数，请将 **Decision type** 设置为 `Approximate log-likelihood ratio` 或 `Log-likelihood ratio`。

**Variance**
:   当 **Variance source** 设置为 `Dialog` 时，会显示此参数，用于指定输入信号中的噪声方差。此参数在正常模式、加速模式和快速加速模式下可调。对于定点输入，此参数不可调。

    如果使用 Simulink® Coder™ 快速仿真 (RSIM) 目标来构建 RSIM 可执行文件，则无需重新编译模型即可调整该参数。这对于蒙特卡罗仿真很有用，在这类仿真中，您需要使用不同的噪声量多次运行仿真（可能在多台计算机上）。

    精确 LLR 算法使用有限精度算术计算指数。对于涉及绝对值非常大的正数或负数的计算，精确 LLR 算法会产生以下结果：

    - 如果噪声方差非常大，则产生 `Inf` 或 `-Inf`
    - 如果噪声方差和信号功率都非常小，则产生 `NaN`

    近似 LLR 算法不计算指数。通过使用近似 LLR 算法，可以避免出现 `Inf`、`-Inf` 和 `NaN` 结果。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用注意事项和限制：

- 使用代码生成时，对于定点输入，**Variance** 参数不可调。

## 版本历史

**在 R2006a 之前推出**

## 描述

对 QAM 调制数据进行解调

General QAM Demodulator Baseband 模块对采用正交幅度调制方式调制的信号进行解调。输入是调制信号的基带表示。

输入必须是离散时间复信号。**Signal constellation** 参数通过在长度为 *M* 的复数向量中列出星座点来定义星座。模块将 **Signal constellation** 向量中的第 *m* 个点映射为整数 *m*-1。

此模块接受标量或列向量输入信号。有关每个模块端口支持的数据类型的信息，请参阅本页中的“支持的数据类型”表。
