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

R2025b 中未记录。

## 参数

**Signal constellation**
:   一个实数或复数向量，列出星座点。

**输出类型**
:   确定模块产生整数还是整数的二进制表示。

    如果将此参数设置为 `Integer`，模块产生整数。

    如果将此参数设置为 `Bit`，当 **Decision type** 设置为 `Hard decision` 时，模块为每个符号产生一组 K 位，称为*二进制字*。如果 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio`，模块分别输出逐位 LLR 和近似 LLR。

**Decision type**
:   指定在解调期间使用硬判决、LLR 还是近似 LLR。有关详细信息，请参阅 Hard- vs. Soft-Decision Demodulation。

    要启用此参数，请将 **输出类型** 设置为 `Bit`。

**Variance source**
:   当将此参数设置为 `Dialog` 时，可以在 **Variance** 参数中指定噪声方差。当将此选项设置为 `Port` 时，模块上会出现一个端口，通过该端口可以输入噪声方差。

    要启用此参数，请将 **Decision type** 设置为 `Approximate log-likelihood ratio` 或 `Log-likelihood ratio`。

**Variance**
:   当 **Variance source** 设置为 `Dialog` 时，此参数出现，并指定输入信号中的噪声方差。此参数在 normal 模式、Accelerator 模式和 Rapid Accelerator 模式下可调。对于定点输入，此参数不可调。

    如果使用 Simulink® Coder™ 快速仿真 (RSIM) 目标构建 RSIM 可执行文件，则可以在不重新编译模型的情况下调整该参数。这对于蒙特卡洛仿真非常有用，在此类仿真中，您需要以不同的噪声量多次运行仿真（可能在多台计算机上）。

    精确 LLR 算法使用有限精度算术计算指数。对于涉及非常大正负幅值的计算，精确 LLR 算法会产生：

    - 如果噪声方差是非常大的值，则为 `Inf` 或 `-Inf`
    - 如果噪声方差和信号功率都是非常小的值，则为 `NaN`

    近似 LLR 算法不计算指数。可以通过使用近似 LLR 算法来避免 `Inf`、`-Inf` 和 `NaN` 结果。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 使用代码生成时，对于定点输入，**Variance** 参数不可调。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 QAM 调制数据

General QAM Demodulator Baseband 模块解调使用正交幅度调制调制的信号。输入是调制信号的基带表示。

输入必须是离散时间复信号。**Signal constellation** 参数通过在一个长度为 *M* 的复数向量中列出星座点来定义星座。模块将 **Signal constellation** 向量中的第 *m* 个点映射到整数 *m*-1。

此模块接受标量或列向量输入信号。有关每个模块端口支持的数据类型的信息，请参阅此页面上的 Supported Data Types 表。
