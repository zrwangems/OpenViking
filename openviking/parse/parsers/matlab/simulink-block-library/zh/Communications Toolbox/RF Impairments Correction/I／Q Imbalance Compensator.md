---
type: simulink-block
title: 'I/Q Imbalance Compensator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'iqimbalancecompensator'
documentation_source_path: 'ref/iqimbalancecompensator.html'
language: zh-CN
chinese_source: worker-translation
---

# I/Q Imbalance Compensator

## 端口

R2025b 中未提供文档。

## 参数

**补偿器系数来源**
:   将补偿器系数的来源指定为 `Estimated from input signal` 或 `Input port`。
    如果设置为 `Estimated from input signal`，补偿器会根据输入信号计算系数。
    如果设置为 `Input port`，则禁用所有其他属性，并且您必须通过输入端口提供系数。
    默认值为 `Estimated from input signal`。

**初始补偿器系数**
:   指定内部算法用于补偿 I/Q 不平衡的初始系数。默认值为 `0+0j`。

**自适应步长来源**
:   将自适应步长的来源指定为 `Property` 或 `Input port`。
    如果设置为 `Property`，请在 **自适应步长** 字段中指定步长。
    如果设置为 `Input port`，则必须通过输入端口指定步长。默认值为 `Property`。

**自适应步长**
:   将自适应算法的步长指定为实数标量。仅当 **自适应步长来源**
    设置为 `Property` 时，此参数才可用。
    默认值为 `0.00001`。

**系数自适应输入端口**
:   选中此复选框可创建一个输入端口，允许信号控制自适应过程。
    如果选中此复选框且输入信号为 `true`，则更新估计的补偿系数。
    如果未启用自适应端口或输入信号为 `false`，则补偿系数保持不变。
    默认情况下，不选中此复选框。

**估计系数输出端口**
:   选中此复选框可通过输出端口提供估计的补偿系数。默认情况下，不选中此复选框。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2014b 中推出**

## 描述

补偿同相分量与正交分量之间的不平衡

I/Q Imbalance Compensator 可减轻调制信号的同相分量与正交分量之间的幅度和相位不平衡所造成的影响。
支持的调制方案包括 OFDM、M-PSK 和 M-QAM，其中 M > 2。

此模块最多支持三个输入端口，其中一个用于输入信号。
当您将 **补偿器系数来源** 参数设置为 `Estimated from input signal` 时，会启用两个附加输入端口。
第一个附加输入端口在您将 **自适应步长来源** 参数设置为 `Input port` 时启用，
第二个附加输入端口在您选中 **系数自适应输入端口** 复选框时启用。
这两个选项彼此独立。此外，您可以选中 **估计系数输出端口** 复选框，
以创建一个可选输出端口，通过该端口提供估计的补偿器系数。

当您将 **补偿器系数来源** 参数设置为 `Input port` 时，
仅支持一种配置（输入信号端口、系数输入端口和输出信号端口）。
