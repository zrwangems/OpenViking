---
type: simulink-block
title: 'Doppler Estimator'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'dopplerestimator'
documentation_source_path: '../phased/ref/dopplerestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Doppler Estimator

## 端口

### 输入

### **Resp** — Doppler 处理后的响应数据立方体 复值 *P*×1 列向量 | 复值 *M*×*P* 矩阵 | 复值 *M*×*N*×*P* 数组

Doppler 处理后的响应数据立方体，指定为复值 *P*×1 列向量、复值 *M*×*P* 矩阵或复值 *M*×*N*×*P* 数组。*M* 表示距离样本数，*N* 是传感器阵元或波束数，*P* 是 Doppler bin 数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下可能发生大小变化。

**数据类型：** `double`
**复数支持：** Yes

### **Doppler** — 沿 Doppler 维度的 Doppler 网格值 实值 *P*×1 列向量

沿 Doppler 维度的 Doppler 网格值，指定为实值 *P*×1 列向量。`Doppler` 定义与输入到 **Resp** 端口的数据的 Doppler 维度相对应的 Doppler 值。Doppler 值必须单调递增且等间隔。单位为 hertz 或 meters/sec。

**示例：** `[-0.3,-0.2,-0.1,0,0.1,0.2,0.3]`

**数据类型：** `double`

### **DetIdx** — 检测索引 实值 *Nd*×*Q* 矩阵

检测索引，指定为实值 *Nd*×*Q* 矩阵。*Q* 是检测数，*Nd* 是响应数据立方体 **Resp** 中的维数。**DetIdx** 的每一列包含响应数据立方体中某次检测的索引。

### **NoisePower** — 检测位置处的噪声功率 正标量 | 正值的实值 1×*Q* 行向量

检测位置处的噪声功率，指定为正标量或正值的实值 1×*Q* 行向量。*Q* 是在 **DetIdx** 输入端口中指定的检测数。

#### 依赖关系

要启用此端口，请选择 **参数估计的输出方差** 参数，然后将 **噪声功率来源参数** 设置为 `Input port`。

### **Clusters** — 簇 ID 实值 1×*Q* 正值行向量

簇 ID，指定为实值 1×*Q* 行向量，其中 *Q* 是在 **DetIdx** 输入端口中指定的检测数。**Clusters** 的每个元素对应于 **DetIdx** 的一个元素。

#### 依赖关系

要启用此输入端口，请选择 **启用簇 ID 输入** 复选框。

### 输出

### **Est** — Doppler 估计 实值 *K*×1 列向量

Doppler 估计，返回为实值 *K*×1 列向量。

- 当未选择 **启用簇 ID 输入** 时，每个 Doppler 估计对应于 **DetIdx** 输入端口中的一列。此时 *K* 等于 **DetIdx** 的元素数 *Q*。
- 当选择 **启用簇 ID 输入** 时，每个 Doppler 估计对应于 **Clusters** 输入端口中的一个簇 ID。此时 *K* 等于唯一簇 ID 的数量。

### **Var** — Doppler 估计方差 正实值 *K*×1 列向量

Doppler 估计方差，返回为正实值 *K*×1 列向量，其中 *K* 是 **Est** 的维度。**Var** 的每个元素对应于 **Est** 的一个元素。估计器方差使用 Ziv-Zakai bound 计算。

#### 依赖关系

要启用此端口，请选择 **参数估计的输出方差** 参数。

## 参数

### **最大估计数** — 要报告的最大估计数 `1`（默认） | 正整数

要报告的最大估计数，指定为正整数。当请求的估计数大于 **DetIdx** 中的元素数时，其余部分用 `NaN` 填充。

**数据类型：** `double`

### **启用簇 ID 输入** — 启用簇 ID 输入 `off`（默认） | `on`

启用 **Cluster** 输入端口以传入簇关联信息。

**数据类型：** `Boolean`

### **参数估计的输出方差** — 启用输出方差端口 `off`（默认） | `on`

启用通过 **Var** 端口输出参数估计方差。

**数据类型：** `Boolean`

### **多普勒处理波形中的脉冲数** — 脉冲数 `2`（默认） | 正整数

多普勒处理波形中的脉冲数，指定为正整数。

#### 依赖关系

要启用此参数，请选择 **参数估计的输出方差** `Output variance for parameter estimates` 参数。

**数据类型：** `double`

### **噪声功率来源** — 噪声功率值来源 `Property`（默认） | `Input port`

噪声功率的来源，指定为 `Property` 或 `Input port`。如果将本参数设置为 `Property`，则使用 **噪声功率** 参数设置检测位置处的噪声功率。当将该参数设置为 `Input port` 时，通过 `NoisePower` 输入端口指定噪声功率。

### **噪声功率** — 噪声功率值 `1.0`（默认） | 正标量

用于检测的噪声功率，指定为正标量。相同的噪声功率值应用于所有检测。噪声功率采用线性单位。

#### 依赖关系

要启用此参数，请选择 **参数估计的输出方差** 复选框，并将 **噪声功率来源** 参数设置为 `Property`。

**数据类型：** `double`

### **仿真使用** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

解释执行在开发和调整模型时很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真使用** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 |  |  |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化用法

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

多普勒估计

Doppler Estimator 模块估计从雷达响应数据获得的目标检测的多普勒（径向速度）。
