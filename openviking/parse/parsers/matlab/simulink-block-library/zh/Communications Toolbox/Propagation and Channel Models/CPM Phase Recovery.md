---
type: simulink-block
title: 'CPM Phase Recovery'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Propagation and Channel Models'
documentation_page: 'cpmphaserecovery'
documentation_source_path: 'ref/cpmphaserecovery.html'
language: zh-CN
chinese_source: worker-translation
---

# CPM Phase Recovery

## 端口

在 R2025b 中未提供文档。

## 参数

**P**
:   CPM 的调制指数表示为真分数 (h = K / P) 时的分母。

**观测间隔**
:   假定载波相位保持不变的符号数。观测间隔参数必须是输入信号向量长度的整数倍。

    当此参数恰好等于输入信号的向量长度时，模块始终可以正常工作。当该整数倍不等于 `1` 时，在 **仿真** 选项卡上，选择 **模型设置**。然后在 **求解器** > **求解器选择** 部分中，选择 **类型:** `Fixed-step`，并清除 **将每个离散速率视为单独的任务** 复选框。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2006a 之前推出**

### R2020a: 已移除 CPM Phase Recovery

CPM Phase Recovery 已被移除。请改用 Carrier Synchronizer。

## 描述

（已移除）使用 2P-Power 方法恢复载波相位

CPM Phase Recovery 模块使用 2P-Power 方法恢复输入信号的载波相位。这种前馈、非数据辅助、时钟辅助的方法适用于使用以下基带调制类型的系统：连续相位调制 (CPM)、最小频移键控 (MSK)、连续相位频移键控 (CPFSK) 和高斯最小频移键控 (GMSK)。此模块适合与 Baseband Continuous Phase Modulation 库中的模块结合使用。

如果将 CPM 的调制指数表示为真分数 h = K / P，则 P 就是名称“2P-Power”中所指的数值。观测间隔参数必须是输入信号向量长度的整数倍。

2P-Power 方法假设载波相位在一系列连续符号内保持不变，并返回该符号序列的载波相位估计值。**观测间隔** 参数是假定载波相位保持不变的符号数。此数值必须是输入信号向量长度的整数倍。

### 输入和输出信号

此模块接受 `double` 或 `single` 类型的标量或列向量输入信号。输入信号表示符号速率下的基带信号，因此它必须是复值信号，并且每个符号必须包含一个采样点。

输出如下：

- 标记为 `Sig` 的输出端口给出将输入信号逆时针旋转后的结果，其中旋转量等于载波相位估计值。因此，`Sig` 输出是输入信号的校正版本，并且与输入信号具有相同的采样时间和向量大小。
- 标记为 `Ph` 的输出端口输出观测间隔内所有符号的载波相位估计值，以 degrees 为单位。`Ph` 输出为标量信号。

  **注意**

  由于模块在内部计算复数的辐角，载波相位估计值存在固有的模糊性。载波相位估计值介于 -90/P 和 90/P degrees 之间，并且可能与实际载波相位相差 180/P degrees 的整数倍。

### 延迟和时延

模块的算法要求其在计算单个载波相位估计值之前，先在长度为 **观测间隔** 的一段时间内收集符号。因此，每个估计值都会延迟 **观测间隔** 个符号，并且相对于输入信号，校正后的信号具有 **观测间隔** 个符号的时延。
