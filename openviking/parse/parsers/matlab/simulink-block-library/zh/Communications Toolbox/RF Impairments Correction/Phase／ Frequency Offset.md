---
type: simulink-block
title: 'Phase/Frequency Offset'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'phasefrequencyoffset'
documentation_source_path: 'ref/phasefrequencyoffset.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase/Frequency Offset

## 端口

### 输入

### **In** — 复数信号 标量 | 向量 | 矩阵

复数信号，指定为标量、向量或矩阵。

在您启用 **Frequency offset from port** 参数之前，此端口在模块上未命名。

**数据类型：** `double` | `single`
**复数支持：** 是

### **Frq** — 频率偏移 标量 | 向量 | 矩阵

频率偏移，指定为标量、行数或列数与输入信号相同的向量，或与输入信号维度相同的矩阵。有关详细信息，请参阅 Interdependent Offset-I/O Dimensions。

#### 依赖关系

要启用此端口，请选中 **Frequency offset from port** 参数。

**数据类型：** `double` | `single`
### 输出

### **Out** — 输出信号 标量 | 向量 | 矩阵

输出信号，以标量、向量或矩阵形式返回。此输出的维度和数据类型与输入信号相同。

此端口在模块上未命名。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Phase offset (deg)** — 相位偏移 `0`（默认）| 标量 | 向量 | 矩阵

相位偏移，以度为单位，指定为标量、向量或矩阵。

如果 **Phase offset (deg)** 和 **Frequency offset (Hz)** 均为非标量，则它们的大小必须相同。

**可调：** 是

### **Frequency offset from port** — 用于添加端口以设置频率偏移的选项 `off`（默认）| on

选中此参数以添加 **Frq** 端口。

- 选中此参数时，**Frq** 端口指定频率偏移。
- 清除此参数时，**Frequency offset (Hz)** 参数指定频率偏移。

### **Frequency offset (Hz)** — 频率偏移 `0`（默认）| 标量 | 向量 | 矩阵

频率偏移，以赫兹为单位，指定为标量、行数或列数与输入信号相同的向量，或与输入信号维度相同的矩阵。有关详细信息，请参阅 Interdependent Offset-I/O Dimensions。

如果 **Phase offset (deg)** 和 **Frequency offset (Hz)** 均为非标量，则它们的大小必须相同。

**可调：** 是

#### 依赖关系

要启用此端口，请清除 **Frequency offset from port** 参数。

## 所属库

Communications Toolbox / RF Impairments Correction Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

**Frequency offset (Hz)** 和 **Phase offset (deg)** 参数在 Normal 模式、Accelerator 模式和 Rapid Accelerator 模式下可调。如果您使用 Simulink Coder™ 快速仿真 (RSIM) 目标来构建 RSIM 可执行文件，则可以在不重新编译模型的情况下调整这些参数。有关详细信息，请参阅 Tunable Parameters (Simulink)。

## 版本历史

**在 R2006a 之前引入**

## 描述

对复数基带信号应用相位和频率偏移

Phase/Frequency Offset 模块对复数信号应用相位和频率偏移。

此图标显示了启用所有端口的模块。带有可选频率偏移输入端的 Phase/Frequency Offset 模块
