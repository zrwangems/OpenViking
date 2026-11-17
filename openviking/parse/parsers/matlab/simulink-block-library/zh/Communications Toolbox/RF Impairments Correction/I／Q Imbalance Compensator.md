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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Source of compensator coefficient**
:   将补偿器系数的来源指定为 `Estimated
    from input signal` 或 `Input port`。
    如果设置为 `Estimated from input signal`，
    补偿器根据输入信号计算系数。
    如果设置为 `Input port`，所有其他属性
    将被禁用，您必须通过输入
    端口提供系数。默认值为 `Estimated from input signal`。

**Initial compensator coefficient**
:   指定内部算法用于补偿 I/Q 不平衡的初始系数。默认值为 `0+0j`。

**Source of adaptation step size**
:   将自适应步长的来源指定为 `Property` 或 `Input
    port`。如果设置为 `Property`，
    在 **Adaptation step size** 字段中指定步长。
    如果设置为 `Input port`，您必须通过输入端口指定
    步长。默认值为 `Property`。

**Adaptation step size**
:   将自适应算法的步长指定为实数
    标量。此参数仅在 **Source of
    adaptation step size** 设置为 `Property` 时可用。
    默认值为 `0.00001`。

**系数自适应输入端口**
:   选中此复选框可创建一个输入端口，允许
    信号控制自适应过程。如果选中该复选框
    且输入信号为 `true`，则估计的
    补偿系数会被更新。如果自适应端口未
    启用或输入信号为 `false`，则补偿
    系数不会改变。默认情况下，该复选框未选中。

**估计系数输出端口**
:   选中此复选框可将估计的补偿
    系数提供给输出端口。默认情况下，该复选框未选中。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

补偿同相与正交分量之间的不平衡

I/Q Imbalance Compensator 减轻调制信号同相与正交
分量之间幅度和相位不平衡的
影响。支持的调制方案
包括 OFDM、M-PSK 和 M-QAM，其中 M > 2。

此模块最多接受三个输入端口，其中一个是
输入信号。当您将 **Source of compensator
coefficient** 参数设置为 `Estimated from input
signal` 时，两个额外的输入端口被启用。
第一个在您将 **Source of adaptation step
size** 参数设置为 `Input port` 时启用，
第二个在您选中 **Coefficient adaptation
input port** 复选框时启用。这两个选项相互独立。此外，
您可以选中 **估计系数输出端口** 复选框
以创建一个可选的输出端口，从中提供估计的补偿器
系数。

当您将 **Source of compensator coefficient** 参数
设置为 `Input port` 时，只有一种可能的配置
（输入信号端口、系数输入端口和输出
信号端口）。
