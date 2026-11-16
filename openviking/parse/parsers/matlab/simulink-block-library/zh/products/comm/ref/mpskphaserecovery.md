---
type: simulink-block
title: 'M-PSK Phase Recovery'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Propagation and Channel Models'
documentation_page: 'mpskphaserecovery'
documentation_source_path: 'ref/mpskphaserecovery.html'
language: zh-CN
chinese_source: worker-translation
---

# M-PSK Phase Recovery

## 端口

R2025b 中未提供文档。

## 参数

**M 元数**
:   所传输 PSK 信号的信号星座中的点数。该值必须为偶数。

**观测区间**
:   假定载波相位保持恒定的符号数。观测区间参数必须是输入信号向量长度的整数倍。

    当此参数恰好等于输入信号的向量长度时，模块始终可以正常工作。当该整数倍不等于 `1` 时，在 **Simulation** 选项卡上，选择 **Model Settings**。然后，在 **Solver** > **Solver selection** 部分中，选择 **Type:** `Fixed-step`，并取消选中 **Treat each discrete rate as a separate task** 复选框。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2006a 之前推出**

### R2020a: M-PSK Phase Recovery 已移除

M-PSK Phase Recovery 已移除。请改用 Carrier Synchronizer。

## 描述

（已移除）使用 M 次幂法恢复载波相位

M-PSK Phase Recovery 模块使用 M 次幂法恢复输入信号的载波相位。这种前馈、非数据辅助、时钟辅助的方法适用于采用基带相移键控 (PSK) 调制的系统。它也适用于采用基带正交幅度调制 (QAM) 的系统，但其结果不如同类 PSK 系统准确。调制所用的符号集大小必须为偶数。

对于 PSK 信号，**M 元数** 参数表示符号集大小。对于 QAM 信号，无论符号集大小如何，**M 元数** 都应为 4，因为 4 次幂法最适合 QAM 信号。

M 次幂法假设载波相位在一系列连续符号内保持恒定，并返回该系列符号的载波相位估计值。**观测区间** 参数是假定载波相位保持恒定的符号数。此数值必须是输入信号向量长度的整数倍。

### 输入和输出信号

此模块接受 `double` 或 `single` 类型的标量或列向量输入信号。输入信号表示符号速率下的基带信号，因此必须为复数信号，并且每个符号必须包含一个采样点。

输出如下：

- 标记为 `Sig` 的输出端口给出将输入信号逆时针旋转后得到的结果，旋转角度等于载波相位估计值。因此，`Sig` 输出是输入信号的校正版本，其采样时间和向量大小与输入信号相同。
- 标记为 `Ph` 的输出端口以 degrees 为单位，输出观测区间内所有符号的载波相位估计值。`Ph` 输出为标量信号。

  **注意**

  由于模块在内部计算复数的辐角，载波相位估计值存在固有的模糊性。载波相位估计值介于 -180/M degrees 和 180/M degrees 之间，并且可能与实际载波相位相差 360/M degrees 的整数倍。

### 延迟和时延

模块的算法要求在计算单个载波相位估计值之前，先在长度为 **观测区间** 的一段时间内收集符号。因此，每个估计值都会延迟 **观测区间** 个符号，并且相对于输入信号，校正后的信号具有 **观测区间** 个符号的时延。
