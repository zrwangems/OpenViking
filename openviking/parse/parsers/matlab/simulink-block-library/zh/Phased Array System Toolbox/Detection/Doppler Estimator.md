---
type: simulink-block
title: 'Doppler Estimator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'dopplerestimator'
documentation_source_path: 'ref/dopplerestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Doppler Estimator

## 端口
```yaml
ports:
- name: Resp
  summary: 多普勒处理后的响应数据立方体 复值 *P*×1 列向量 | 复值 *M*×*P* 矩阵 | 复值 *M*×*N*×*P* 数组
  direction: input
  data_types: double
- name: Doppler
  summary: 沿多普勒维度的多普勒网格值 实值 *P*×1 列向量
  direction: input
  data_types: double
- name: DetIdx
  summary: 检测索引 实值 *Nd*×*Q* 矩阵
  direction: input
- name: NoisePower
  summary: 检测位置处的噪声功率 正标量 | 正实值 1×*Q* 行向量
  direction: input
- name: Clusters
  summary: 簇 ID 正实值 1×*Q* 行向量
  direction: input
- name: Est
  summary: 多普勒估计 实值 *K*×1 列向量
  direction: output
- name: Var
  summary: 多普勒估计方差 正实值 *K*×1 列向量
  direction: output
```

### 输入

### **Resp** — 多普勒处理后的响应数据立方体 复值 *P*×1 列向量 | 复值 *M*×*P* 矩阵 | 复值 *M*×*N*×*P* 数组

多普勒处理后的响应数据立方体，指定为复值 *P*×1 列向量、复值 *M*×*P* 矩阵或复值 *M*×*N*×*P* 数组。*M* 表示距离采样数，*N* 是传感器阵元或波束数，*P* 是多普勒 bin 数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能发生变化。

**数据类型：** `double`
**复数支持：** 是

### **Doppler** — 沿多普勒维度的多普勒网格值 实值 *P*×1 列向量

沿多普勒维度的多普勒网格值，指定为实值 *P*×1 列向量。`Doppler` 定义了与输入到 **Resp** 端口的数据的多普勒维度相对应的多普勒值。多普勒值必须单调递增且等间距。单位为赫兹或米/秒。

**示例：** `[-0.3,-0.2,-0.1,0,0.1,0.2,0.3]`

**数据类型：** `double`

### **DetIdx** — 检测索引 实值 *Nd*×*Q* 矩阵

检测索引，指定为实值 *Nd*×*Q* 矩阵。*Q* 是检测数，*Nd* 是响应数据立方体 **Resp** 中的维度数。**DetIdx** 的每一列包含响应数据立方体中一个检测的索引。

### **NoisePower** — 检测位置处的噪声功率 正标量 | 正实值 1×*Q* 行向量

检测位置处的噪声功率，指定为正标量或正实值 1×*Q* 行向量。*Q* 是在 **DetIdx** 输入端口中指定的检测数。

#### 依赖

要启用此端口，请选择 **Output variance for parameter estimates** 参数，然后将 **Source of noise power parameter** 设置为 `Input port`。

### **Clusters** — 簇 ID 正实值 1×*Q* 行向量

簇 ID，指定为实值 1×*Q* 行向量，其中 *Q* 是在 **DetIdx** 输入端口中指定的检测数。**Clusters** 的每个元素对应于 **DetIdx** 的一个元素。

#### 依赖

要启用此输入端口，请选中 **Enable cluster ID input** 复选框。
### 输出

### **Est** — 多普勒估计 实值 *K*×1 列向量

多普勒估计，返回为实值 *K*×1 列向量。

- 当未选中 **Enable cluster ID input** 时，每个多普勒估计对应于 **DetIdx** 输入端口中的一列。此时 *K* 等于 **DetIdx** 的元素数 *Q*。
- 当选中 **Enable cluster ID input** 时，每个多普勒估计对应于 **Clusters** 输入端口中的一个簇 ID。此时 *K* 等于唯一簇 ID 的数量。

### **Var** — 多普勒估计方差 正实值 *K*×1 列向量

多普勒估计方差，返回为正实值 *K*×1 列向量，其中 *K* 是 **Est** 的维度。**Var** 的每个元素对应于 **Est** 的一个元素。估计器方差使用 Ziv-Zakai 界计算。

#### 依赖

要启用此端口，请选择 **Output variance for parameter estimates** 参数。
## 参数
```yaml
parameters:
- name: Maximum number of estimates
  summary: 要报告的最大估计数 1（默认）| 正整数
  group: ''
- name: Enable cluster ID input
  summary: 启用聚类 ID 输入 off（默认）| on
  group: ''
- name: Output variance for parameter estimates
  summary: 启用输出方差端口 off（默认）| on
  group: ''
- name: Number of pulses in Doppler processed waveform
  summary: 脉冲数 2（默认）| 正整数
  group: ''
- name: Source of noise power
  summary: 噪声功率值来源 Property（默认）| Input port
  group: ''
- name: Noise power
  summary: 噪声功率值 1.0（默认）| 正标量
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
```

### **Maximum number of estimates** — 要报告的最大估计数 `1`（默认）| 正整数

要报告的最大估计数，指定为正整数。当请求的估计数大于 **DetIdx** 中的元素数时，其余部分用 `NaN` 填充。

**数据类型：** `double`

### **Enable cluster ID input** — 启用聚类 ID 输入 `off`（默认）| `on`

启用 **Cluster** 输入端口以传入聚类关联信息。

**数据类型：** `Boolean`

### **Output variance for parameter estimates** — 启用输出方差端口 `off`（默认）| `on`

启用通过 **Var** 端口输出参数估计方差。

**数据类型：** `Boolean`

### **Number of pulses in Doppler processed waveform** — 脉冲数 `2`（默认）| 正整数

多普勒处理波形中的脉冲数，指定为正整数。

#### 依赖关系

要启用此参数，请选择 **Output variance for parameter estimates** `Output variance for parameter estimates` 参数。

**数据类型：** `double`

### **Source of noise power** — 噪声功率值来源 `Property`（默认）| `Input port`

噪声功率的来源，指定为 `Property` 或 `Input port`。如果将此参数设置为 `Property`，请使用 **Noise power** 参数设置检测位置处的噪声功率。当将此参数设置为 `Input port` 时，通过 `NoisePower` 输入端口指定噪声功率。

### **Noise power** — 噪声功率值 `1.0`（默认）| 正标量

用于检测的噪声功率，指定为正标量。相同的噪声功率值应用于所有检测。噪声功率使用线性单位。

#### 依赖关系

要启用此参数，请选择 **Output variance for parameter estimates** 复选框，并将 **Source of noise power** 参数设置为 `Property`。

**数据类型：** `double`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

多普勒估计

Doppler Estimator 模块估计从雷达响应数据中获得的目标检测的多普勒（径向速度）。
