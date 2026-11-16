---
type: simulink-block
title: 'Range Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'rangeestimator'
documentation_source_path: 'ref/rangeestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Range Estimator

## 端口

### 输入

### **Resp** — 经过距离处理的响应数据立方体 复值 *P*×1 列向量 | 复值 *M*×*P* 矩阵 | 复值 *M*×*N*×*P* 矩阵

经过距离处理的响应数据立方体，指定为复值 *P*×1 列向量、复值 *M*×*P* 矩阵或复值 *M*×*N*×*P* 数组。*M* 表示距离采样数，*N* 是传感器阵元数或波束数，*P* 是多普勒单元数。

输入矩阵第一个维度的大小可以变化，以模拟信号长度的变化。例如，对于具有可变脉冲重复频率的脉冲波形，可能会发生这种大小变化。

**数据类型：** `double`
**复数支持：** 是

### **Range** — 沿距离维度的距离网格值 实值 *M*×1 列向量

数据立方体输入 **Resp** 中沿距离维度的距离网格值，指定为实值 *M*×1 列向量。距离值必须单调递增且等间距。单位为 meters。

**示例：** `[-0.3,-0.2,-0.1,0,0.1,0.2,0.3]`

**数据类型：** `double`

### **DetIdx** — 检测索引 实值 *Nd*×*Q* 矩阵

检测索引，指定为实值 *Nd*×*Q* 矩阵。*Q* 是检测数量，*Nd* 是响应数据立方体 **Resp** 的维度数。**DetIdx** 的每一列都包含响应数据立方体中一个检测的索引。

### **NoisePower** — 检测位置的噪声功率 正标量 | 由正值组成的实值 1×*Q* 行向量

检测位置的噪声功率，指定为正标量或由正值组成的实值 1×*Q* 行向量。*Q* 是在 **DetIdx** 输入端口中指定的检测数量。

#### 依赖关系

要启用此端口，请选中 **输出参数估计的方差** 参数，然后将 **噪声功率源** 设置为 `Input port`。

### **Clusters** — 聚类 ID 由正值组成的实值 1×*Q* 行向量

聚类 ID，指定为实值 1×*Q* 行向量，其中 *Q* 是在 **DetIdx** 输入端口中指定的检测数量。**Clusters** 的每个元素对应 **DetIdx** 的一个元素。

#### 依赖关系

要启用此输入端口，请选中 **启用聚类 ID 输入** 复选框。
### 输出

### **Est** — 距离估计值 实值 *K*×1 列向量

距离估计值，指定为实值 *K*×1 列向量。

- 未选中 **启用聚类 ID 输入** 时，每个距离估计值对应 **DetIdx** 输入端口的其中一列。此时，*K* 等于 **DetIdx** 的列维度 *Q*。
- 选中 **启用聚类 ID 输入** 时，每个距离估计值对应 **Clusters** 输入端口中的一个聚类 ID。此时，*K* 等于唯一聚类 ID 的数量。

### **Var** — 距离估计方差 正实值 *K*×1 列向量

距离估计方差，返回为正实值 *K*×1 列向量，其中 *K* 是 **Est** 的维度。**Var** 的每个元素对应 **Est** 的一个元素。估计器方差使用 Ziv-Zakai 界计算。

#### 依赖关系

要启用此输出端口，请选中 **输出参数估计的方差** 参数。

## 参数

### **最大估计数** — 要报告的最大估计数 `1` (默认) | 正整数

要报告的最大估计数，指定为正整数。当请求的估计数大于 **DetIdx** 中的元素数时，其余部分用 `NaN` 填充。

**数据类型：** `double`

### **启用聚类 ID 输入** — 启用聚类 ID 输入 `off` (默认) | `on`

启用 **Cluster** 输入端口，以传入聚类关联信息。

**数据类型：** `Boolean`

### **输出参数估计的方差** — 启用输出方差端口 `off` (默认) | `on`

启用通过 **Var** 端口输出参数估计方差。

**数据类型：** `Boolean`

### **均方根距离分辨率** — 距离分辨率 `2` (默认) | 正标量

检测的均方根距离分辨率，指定为正标量。此参数必须与 **Range** 输入端口具有相同的单位。

#### 依赖关系

要启用此参数，请选中 `Output variance for parameter estimates` 参数。

**数据类型：** `double`

### **噪声功率源** — 噪声功率值的来源 `Property` (默认) | `Input port`

噪声功率的来源，指定为 `Property` 或 `Input port`。如果将此参数设置为 `Property`，请使用 **噪声功率** 参数设置检测位置的噪声功率。当此参数设置为 `Input port` 时，通过 `NoisePower` 输入端口指定噪声功率。

### **噪声功率** — 噪声功率值 `1.0` (默认) | 正标量

检测的噪声功率，指定为正标量。相同的噪声功率值应用于所有检测。噪声功率采用线性单位。

#### 依赖关系

要启用此参数，请选中 **输出参数估计的方差** 复选框，并将 **噪声功率源** 参数设置为 `Property`。

**数据类型：** `double`

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译后的代码运行，请选择 `Code Generation`。编译后的代码需要编译时间，但通常运行速度更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。与解释执行相比，长时间仿真使用生成的代码运行速度更快。您无需重新编译即可重复运行，但如果更改任何模块参数，模块会在执行前自动重新编译。

下表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，通过 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
| `Code Generation` | 编译该模块。 | 编译模型中的所有模块。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2017a 中引入**

## 描述

距离估计

Range Estimator 模块根据雷达响应数据估计所检测目标的距离。
