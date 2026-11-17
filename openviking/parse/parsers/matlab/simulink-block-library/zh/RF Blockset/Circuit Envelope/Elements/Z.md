---
type: simulink-block
title: 'Impedance'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'impedance'
documentation_source_path: 'ref/impedance.html'
language: zh-CN
chinese_source: worker-translation
---

# Impedance

## 端口

R2025b 中未记录。

## 参数

### **Impedance type** — 频率相关性 `Frequency independent`（默认）| `Frequency dependent`

阻抗的频率相关性，指定为 `Frequency independent` 或 `Frequency dependent`。

选择 `Frequency independent` 可对所有频率应用相同的阻抗。选择 `Frequency dependent` 可将阻抗作为分段线性函数应用。

**数据类型：** `double`

### **Complex impedance (Ohm)** — 阻抗值 `50`（默认）| 标量复数 | 复数向量

阻抗值，指定为以欧姆为单位的标量复数，或每个元素以欧姆为单位的复数向量。

当 **Impedance type** 设置为 `Frequency independent` 时，阻抗是应用于所有仿真频率的标量复数。当 **Impedance type** 设置为 `Frequency dependent` 时，阻抗是复数向量 [*Z*1, *Z*2, *Z*3, …]。该向量对所有仿真频率进行线性插值。

**数据类型：** `double`

### **Frequency** — 频率相关阻抗的频率值 `1e9`（默认）| 非负标量数值 | 非负向量数值

频率相关阻抗的频率值，指定为以 Hz 为单位的非负标量数值，或每个元素以 Hz 为单位的非负向量数值。

当 **Impedance type** 设置为 `Frequency dependent` 时，您可以指定非负频率向量 [*f*1, *f*2, *f*3, …]。数据对 *f*i、*Z*i 定义分段线性函数 *Z*(*f*)，该函数对仿真频率进行线性插值。对于范围之外的值，采用常数外推。

**数据类型：** `double`

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2021b：Impedance 模块图标已更新

从 R2021b 开始，Impedance 模块图标已更新。当您打开在 R2021b 之前创建的包含 Impedance 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对复阻抗进行建模

Impedance 模块对每个仿真频率 *f*k 实现关系 *v*k(*t*) = *Z*(*f*k)\**i*k(*t*)，其中：

- *Z*(*f*k) 表示指定仿真频率下的复值阻抗。
- *v*k(*t*) 表示时间 *t* 时元件端子两端的电压。
- *i*k(*t*) 表示时间 *t* 时流过元件的电流。

电路包络电流和电压信号在每个频率 *fk* 处包含同相分量 *Ik* 和正交分量 *Qk*。

频率相关阻抗通常无法实现为物理网络，例如 RLC 链。但是，您可以使用 Impedance 模块对非物理行为进行建模，例如频率无关的负电容或负电感。您还可以使用此模块指定滤波器网络中的谐振频率偏移。
