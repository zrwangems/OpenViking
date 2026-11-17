---
type: simulink-block
title: 'Sample-Rate Match'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'sampleratematch'
documentation_source_path: 'ref/sampleratematch.html'
language: zh-CN
chinese_source: worker-translation
---

# Sample-Rate Match

## 端口

### 输入

### **In1** — 第一个输入信号 列向量 | 矩阵

第一个输入信号，指定为列向量或 *K*1×*N*chan1 矩阵。*K*1 是行数，*N*chan1 是输入信号矩阵中的通道数。

**数据类型：** `single` | `double`
**复数支持：** 是

### **In2** — 第二个输入信号 列向量 | 矩阵

第二个输入信号，指定为列向量或 *K*2×*N*chan2 矩阵。*K*2 是行数，*N*chan2 是输入信号矩阵中的通道数。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Out** — 输出信号 矩阵

输出信号，返回为 *P*×(*N*chan1+*N*chan2) 矩阵，数据类型与输入信号相同。*P* 是 `Output samples per frame` 参数值。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Input sample rate (Hz)** — 每个输入信号的采样率 [1 2]\*1e6（默认）| 2 元素向量

每个输入信号的采样率，以 Hz 为单位，指定为正值组成的 2 元素向量。

### **Output samples per frame** — 每帧输出的样本数 1000（默认）| 正整数

每帧输出的样本数，指定为正整数。

### **Output sample rate options** — 输出采样率选项 `Auto`（默认）| `Specify via property`

输出采样率选项，指定为 `Auto` 或 `Specify via property`。

- `Auto` — 输出采样率设置为 `Input sample rate (Hz)` 参数中的最高值。
- `Specify via property` — 使用 `Output sample rate (Hz)` 参数指定输出采样率值。

### **Output sample rate (Hz)** — 输出信号采样率 2e6（默认）| 正标量

输出信号采样率，以 Hz 为单位，指定为正标量。该值必须大于或等于 `Input sample rate (Hz)` 参数值。

#### 依赖关系

要启用此参数，请将 `Output sample rate options` 参数设置为 `Specify via property`。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

将两个信号上采样至公共速率

Sample-Rate Match 模块根据需要将输入信号上采样至公共输出采样率。此模块会为仿真引入延迟。使用 `srmdelay` 函数计算将引入的延迟。
