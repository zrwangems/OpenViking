---
type: simulink-block
title: 'Derivative'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / Continuous'
documentation_page: 'derivative'
documentation_source_path: 'slref/derivative.html'
language: zh-CN
chinese_source: official
---

# Derivative

## 端口

### 输入

### **Port\_1** — 要逼近连续导数的信号 标量 | 向量

输入信号必须为实数，并且可以具有标量或向量采样值。使用 Derivative 模块仅对具有连续采样时间的信号逼近连续导数。

**数据类型:** `double`
### 输出

### **Port\_1** — 输入信号关于时间的连续导数逼近 标量 | 向量

Derivative 模块逼近输入信号关于时间的连续导数，并将结果作为连续信号提供。输出信号的维度和复/实性与输入信号的维度和复/实性匹配，输入信号必须为实数。

**数据类型:** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

### **使用传递函数 s/(c\*s + 1) 进行线性化逼近时的系数 c** — 逼近模块线性化的传递函数中极点的时间常数 `inf` (默认) | 有限正标量数值

连续导数的精确线性化难以实现，因为动态方程 y=u˙ 不存在状态空间表示。软件通过在方程组中增加极点以创建 s/(c∗s+1). 形式的传递函数，来逼近 Derivative 模块的线性化。极点还充当低通滤波器（其截止频率由此参数值确定），从而降低噪声的影响。

最佳做法是将此参数值指定为 1fb，其中 fb 是添加极点后得到的低通滤波器的截止频率，单位为弧度/秒。选择一个大于或等于系统奈奎斯特速率或频率的截止频率。默认参数值 `inf` 对应于截止频率 `0`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `CoefficientInTFapproximation` |
| **值:** | `inf` (默认) | finite positive scalar number |
| **数据类型:** | `char` | `string` |

**示例:** `set_param("MyModel/Derivative","CoefficientInTFapproximation","0.001")` configures the Derivative block named `Derivative` in the model `MyModel` to use the coefficient `0.001` in the transfer function used for approximate linearization of the block. This coefficient value results in a cutoff frequency of `1000` radians per second.

## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

考虑使用模型离散化器将连续模块映射到支持代码生成的离散等效模块。要访问模型离散化器，请在 **App** 选项卡中的**控制系统**下，点击**模型离散化器**。

## 版本历史

**在 R2006a 之前推出**

### R2023b: 新警告能够标识输入信号为离散采样时间或子步中不变采样时间的 Derivative 模块

当 Derivative 模块的输入不具备连续采样时间时，该模块可能会产生不正确或意外的结果。软件在编译时会针对每个输入信号为离散采样时间或子步中不变采样时间的模块发出警告。

要解决该警告，您可以：

- 修改模型，使输入信号具有连续采样时间。
- 改用积分模块（例如 Integrator 模块）通过积分而不是微分来求解系统。
- 使用另一个模块（例如 Transfer Fcn 模块或 Discrete Derivative 模块）实现导数。

## 描述

计算连续输入信号关于时间的逼近连续导数

Derivative 模块可逼近连续输入信号 *u* 关于仿真时间 *t* 的连续导数。当需要计算具有连续采样时间的可微分信号的导数时，可以使用 Derivative 模块。

Derivative 模块如果使用不当会导致仿真结果不准确。如果可能，请考虑以下几种方案来替代 Derivative 模块：

- 重新排列系统方程以求解积分而不是导数。然后，根据新方程构建模型，以便软件使用 Integrator 等模块求积分，而不是求微分。

  有关示例，请参阅最佳形式的数学模型。
- 当 Transfer Fcn 模块也作用于 Derivative 模块的输入或输出信号时，改为通过在传递函数中添加零来实现信号的导数。
- 要计算离散系统中离散信号的有限差分或差商，请使用 Discrete Derivative 模块。

当您必须使用 Derivative 模块时，请仅对其使用具有连续采样时间的可微分输入信号。

- 当连接到此端口的信号具有离散的或子步中不变的采样时间时，软件会发出警告。 *(自 R2023b 起)*
- 当输入信号具有常数采样时间时，软件不会发出警告，但调节信号值会导致输入信号不连续。对这些不连续点求微分会在输出信号中产生尖峰。
- 要计算离散系统中离散信号的有限差分或差商，请使用 Discrete Derivative 模块。

### 确保连续导数逼近的准确度

使用 Derivative 模块时，必须确保模块输出信号的准确性满足您的要求。即使在适当的环境下使用，Derivative 模块输出信号的准确性也取决于步长，还可能取决于系统其余部分的动态特性。

使用**最大步长**参数来防止变步长求解器采用的步长过大而无法满足您的准确性要求。要为最大步长选择合适的值，您可能需要运行几次仿真。

在变步长仿真中，求解器通过监控整个模型中连续状态计算的误差来确定每个主时间步的大小。当连续状态的计算值中的误差超出指定的容差级别时，求解器会减小步长，直到误差在容差范围内。

Derivative 模块没有任何连续状态，因此求解器无法调整步长以确保 Derivative 模块计算满足容差要求。如果求解器在输入信号值快速变化时采用较大的时间步，模块可能会产生意外的输出值。
