---
type: simulink-block
title: 'Derivative'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Linearization'
documentation_page: 'derivative'
documentation_source_path: '../simulink/slref/derivative.html'
language: zh-CN
chinese_source: worker-translation
---

# Derivative

## 端口
```yaml
ports:
- name: Port_1
  summary: 用于逼近连续导数的信号 标量 | 向量
  direction: input
  data_types: double
- name: Port_1
  summary: 输入信号对时间的连续导数的逼近 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 用于逼近连续导数的信号 标量 | 向量

输入信号必须为实数，且可以具有标量或向量采样值。仅对具有连续采样时间的信号使用 Derivative 模块来逼近连续导数。

**数据类型：** `double`
### 输出

### **Port\_1** — 输入信号对时间的连续导数的逼近 标量 | 向量

Derivative 模块逼近输入信号对时间的连续导数，并将结果作为连续信号提供。输出信号的维度和复杂度与输入信号的维度和复杂度匹配，输入信号必须为实数。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Coefficient c in the transfer function approximation s/(c\*s + 1) used for linearization
  summary: 用于逼近模块线性化的传递函数中极点的时间常数 inf（默认）| 有限正标量数值
  group: ''
  block_parameter: CoefficientInTFapproximation
  values: inf (default) | finite positive scalar number
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Coefficient c in the transfer function approximation s/(c\*s + 1) used for linearization** — 用于逼近模块线性化的传递函数中极点的时间常数 `inf`（默认）| 有限正标量数值

连续导数的精确线性化很困难，因为动态方程 y=u˙ 不存在状态空间表示。软件通过向系统添加一个极点来逼近 Derivative 模块的线性化，从而创建形式为 s/(c∗s+1) 的传递函数。该极点还充当低通滤波器，其截止频率由该参数值决定，从而降低噪声的影响。

作为最佳实践，请将该参数值指定为 1fb，其中 fb 是添加极点后产生的低通滤波器的截止频率（以弧度/秒为单位）。选择大于或等于系统奈奎斯特速率或频率的截止频率。默认参数值 `inf` 对应于截止频率 `0`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CoefficientInTFapproximation` |
| **值**：| `inf` (default) | finite positive scalar number |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("MyModel/Derivative","CoefficientInTFapproximation","0.001")` 将模型 `MyModel` 中名为 `Derivative` 的 Derivative 模块配置为在用于模块近似线性化的传递函数中使用系数 `0.001`。该系数值产生的截止频率为 `1000` 弧度/秒。
## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

考虑使用 Model Discretizer 将连续模块映射为支持代码生成的离散等效模块。要访问 Model Discretizer，请在 **Apps** 选项卡上的 **Control Systems** 下，点击 **Model Discretizer**。

## 版本历史

**在 R2006a 之前推出**

### R2023b：新警告标识输入信号具有离散或固定小步长采样时间的 Derivative 模块

当 Derivative 模块的输入不具有连续采样时间时，该模块可能产生不正确或意外的结果。软件在编译时为每个输入信号具有离散或固定小步长采样时间的模块发出警告。

要解决该警告，您可以：

- 修改模型，使输入信号具有连续采样时间。
- 通过使用积分模块（如 Integrator 模块）进行积分而不是微分来求解系统。
- 使用其他模块实现导数，例如 Transfer Fcn 模块或 Discrete Derivative 模块。

## 描述

计算连续输入信号对时间的近似连续导数

Derivative 模块逼近连续输入信号 *u* 对仿真时间 *t* 的连续导数。当您需要为具有连续采样时间的可微信号计算导数时，请使用 Derivative 模块。

不当使用 Derivative 模块可能导致仿真结果不准确。在可能的情况下，请考虑以下 Derivative 模块的替代方案：

- 重新排列系统方程以求解积分而不是导数。然后，基于新方程构建模型，使软件使用诸如 Integrator 模块之类的模块进行积分而不是微分。

  有关示例，请参阅 Best-Form Mathematical Models。
- 当 Transfer Fcn 模块也对 Derivative 模块的输入或输出信号起作用时，通过在传递函数中添加一个零点来实现该信号的导数。
- 要计算离散系统中离散信号的有限差分或差商，请使用 Discrete Derivative 模块。

当您必须使用 Derivative 模块时，请仅对具有连续采样时间的可微输入信号使用该模块。

- 当连接到此端口的信号具有离散或固定小步长采样时间时，软件会发出警告。*（自 R2023b 起）*
- 虽然当输入信号具有常量采样时间时软件不会发出警告，但调整信号值会在输入信号中引入不连续性。对这些不连续性进行微分会在输出信号中产生尖峰。
- 要计算离散系统中离散信号的有限差分或差商，请使用 Discrete Derivative 模块。

### 确保连续导数逼近的准确性

当您使用 Derivative 模块时，必须确保模块输出信号的准确性满足您的要求。即使在适当的环境中使用，Derivative 模块输出信号的准确性也取决于步长，并且可能取决于系统其余部分的动态特性。

使用 **Max step size** 参数来防止变步长求解器采取过大而无法满足您准确性要求的步长。要为最大步长选择合适的值，您可能需要运行多次仿真。

在变步长仿真中，求解器通过监视整个模型中连续状态计算的误差来确定每个主时间步长的大小。当连续状态计算值的误差超过指定的容差水平时，求解器会减小步长，直到误差落在容差范围内。

Derivative 模块没有任何连续状态，因此求解器无法调整步长来确保 Derivative 模块的计算满足容差要求。如果当输入信号值快速变化时求解器采取较大的时间步长，该模块可能产生意外的输出值。
