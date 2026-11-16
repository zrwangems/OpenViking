---
type: simulink-block
title: 'Mutual Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'mutualinductor'
documentation_source_path: 'ref/mutualinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Mutual Inductor

## 端口

### 守恒

### **1+** — 初级绕组正端子

与初级绕组正端子相关联的电气守恒端口。

### **1-** — 初级绕组负端子

与初级绕组负端子相关联的电气守恒端口。

### **2+** — 次级绕组正端子

与次级绕组正端子相关联的电气守恒端口。

### **2-** — 次级绕组负端子

与次级绕组负端子相关联的电气守恒端口。

## 参数

### 主要

### **Inductance L1** — 初级绕组中的标称电感值 `10` `H` (默认) | positive scalar

初级绕组中的标称电感值。

### **Inductance L2** — 次级绕组中的标称电感值 `0.1` `H` (默认) | positive scalar

次级绕组中的标称电感值。

### **Coefficient of coupling** — 绕组之间的互感耦合 0.9 (默认) | scalar in the range [-1,1]

定义初级和次级绕组之间互感的耦合系数。要反转其中一个绕组的方向，请使用负值。

不要使用非常接近 1 的量值，例如 0.999，因为这些值会引入快速仿真动态。要在同时保留正确的低频行为（隔直）的情况下将耦合系数设置为 1，请使用 Simscape Foundation library 中的 Mutual Inductor 模块，并选择 **Perfect coupling – no leakage** 参数。

### **Tolerance (%)** — 电感容差，以百分比表示 20 (默认)

如制造商数据表中定义的电感容差。数据表通常会为给定电感类型提供容差百分比。因此，此值对两个绕组相同。

### **L1 tolerance application** — 选择如何对初级绕组应用容差 `None — use nominal value` (默认) | `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择在仿真期间如何对初级绕组应用容差：

- `None — use nominal value` — 模块不应用容差，使用标称电感值。
- `Random tolerance` — 模块在容差值限制内对电感值应用随机偏移。您可以通过 **Tolerance distribution** 参数选择 Uniform 或 Gaussian 分布来计算随机数。
- `Apply maximum tolerance value` — 电感增加指定的容差百分比值。
- `Apply minimum tolerance value` — 电感减少指定的容差百分比值。

### **L1 tolerance distribution** — 选择初级绕组的分布类型 `Uniform` (默认) | `Gaussian`

选择随机容差的分布类型：

- `Uniform` — 均匀分布
- `Gaussian` — 高斯分布

#### 依赖关系

当 **L1 tolerance application** 参数设置为 `Random tolerance` 时启用。

### **L1 number of standard deviations for quoted tolerance** — 用于计算初级绕组的高斯随机数 4 (默认)

用于计算高斯随机数的标准偏差数。

#### 依赖关系

当 **L1 tolerance distribution** 参数设置为 `Gaussian` 时启用。

### **L2 tolerance application** — 选择如何对次级绕组应用容差 `None — use nominal value` (默认) | `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择在仿真期间如何对次级绕组应用容差：

- `None — use nominal value` — 模块不应用容差，使用标称电感值。
- `Random tolerance` — 模块在容差值限制内对电感值应用随机偏移。您可以通过 **Tolerance distribution** 参数选择 Uniform 或 Gaussian 分布来计算随机数。
- `Apply maximum tolerance value` — 电感增加指定的容差百分比值。
- `Apply minimum tolerance value` — 电感减少指定的容差百分比值。

### **L2 tolerance distribution** — 选择次级绕组的分布类型 `Uniform` (默认) | `Gaussian`

选择随机容差的分布类型：

- `Uniform` — 均匀分布
- `Gaussian` — 高斯分布

#### 依赖关系

当 **L2 tolerance application** 参数设置为 `Random tolerance` 时启用。

### **L2 number of standard deviations for quoted tolerance** — 用于计算次级绕组的高斯随机数 `4` (默认)

用于计算高斯随机数的标准偏差数。

#### 依赖关系

当 **L2 tolerance distribution** 参数设置为 `Gaussian` 时启用。

### 电阻

### **Series resistance, [R\_primary R\_secondary]** — 初级和次级绕组的等效串联电阻 `[0.001, 0.001]` `Ohm` (默认)

初级和次级绕组的等效串联电阻，指定为二元素向量。第一个数字对应初级绕组，第二个数字对应次级绕组。对于发生故障的绕组，模块根据各段中的匝数按比例将电阻分配给每个段。

### **Parallel conductance, [G\_primary G\_secondary]** — 与初级和次级绕组相关联的并联泄漏路径 `[1e-9,1e-9]` `1/Ohm` (默认)

与初级和次级绕组相关联的并联泄漏路径，指定为二元素向量。第一个数字对应初级绕组，第二个数字对应次级绕组。并联电导直接跨接在初级和次级绕组的 + 和 – 端子两端。

### 工作限制

### **Enable operating limits** — 选择 `Yes` 以在超出运行限制时启用报告 `No` (默认) | `Yes`

选择 `Yes` 可在超出运行限制时启用报告。**工作限制** 部分中的关联参数将变为可见，使您可以选择报告方法，并以功率和电流为单位指定运行限制。

### **Reporting when operating limits exceeded** — 选择报告方法 `Warn` (默认) | `Error`

选择超出运行限制时发生的情况：

- `Warn` — 模块发出警告。
- `Error` — 仿真停止并报错。

#### 依赖关系

当 **Enable operating limits** 参数设置为 `Yes` 时启用。

### **Saturation current** — 电感饱和电流 `1` `A` (默认)

电感饱和电流，如制造商数据表中定义。如果流入初级和次级绕组的净电流超过此值，则磁芯材料进入饱和，模块将报告违反运行限制。也就是说，模块将该限值与 |*i*1 + *i*2| 进行比较，其中当电流流入 + 节点时定义为正。

#### 依赖关系

当 **Enable operating limits** 参数设置为 `Yes` 时启用。

### **Power rating** — 电感中的最大功率耗散 `1` `A` (默认)

与互感器相关联的电阻和电导元件中的最大瞬时（总）功率耗散。如果总功率（包括初级和次级绕组）超过此数值，模块将报告违反运行限制。

#### 依赖关系

当 **Enable operating limits** 参数设置为 `Yes` 时启用。

### 故障

### **Mutual inductor fault** — 对互感器中的故障进行建模的选项 `Add fault` (默认)

用于在 Mutual Inductor 模块中对故障进行建模的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Faulted winding** — 选择用于故障建模的绕组 `Primary` (默认) | `Secondary`

选择故障发生在初级还是次级绕组中。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接，向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 分析直流电枢绕组故障。

### **Location of fault node (% of total turns from - terminal)** — 与故障绕组 – 端口接触的子电感中的匝数百分比 `50` (默认) | scalar in the range (0,100)

在实践中，故障是通过将故障绕组分段为两个串联连接的耦合子电感来实现的。电感与相应段中匝数的平方成正比，每个子电感的串联电阻与每段中的匝数成正比。并联电导跨越两个段。

此参数表示分配给与故障绕组 – 端口接触的子电感的匝数百分比。其余匝数分配给另一个子电感。默认值为 `50`，这意味着故障绕组的总电感被分成两个相等的耦合子电感。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接，向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 分析直流电枢绕组故障。

### **Short-circuit turns** — 选择故障是否导致其中一个段短路 `No` (默认) | `To negative terminal` | `To positive terminal`

选择故障是否导致其中一个子电感段短路：

- `No` — 故障不会产生短路。
- `To negative terminal` — 故障使与模块 – 端口接触的子电感短路。
- `To positive terminal` — 故障使与模块 + 端口接触的子电感短路。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接，向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 分析直流电枢绕组故障。

### **Open-circuit at fault node** — 选择是否在两个段之间施加开路故障 `No` (默认) | `Yes`

选择是否在两个子电感段之间施加开路故障。默认值为 `No`。即使存在开路故障，子电感的特性仍然相关，因为即使在故障状态下它们也磁耦合。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接，向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 分析直流电枢绕组故障。

### **Ground fault** — 选择故障是否导致其中一个段短路 `No` (默认) | `Negative terminal side of fault node` | `Positive terminal side of fault node`

选择在发生故障时，是否存在电流流向接地节点的路径：

- `No` — 故障不会导致接地连接。
- `Negative terminal side of fault node` — 与模块 – 端口接触的一侧连接到地。
- `Positive terminal side of fault node` — 与模块 + 端口接触的一侧连接到地。

如果 **Open-circuit at fault node** 参数设置为 `Yes`，则需要指定哪一侧（负侧或正侧）连接到地。如果没有开路，这两个选项的行为类似。物理上，这对应于绕组与接地磁芯或机壳之间的绝缘击穿。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接，向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 分析直流电枢绕组故障。

### **Conductance of faulted ground path** — 两个子电感之间的互感耦合 `0` `1/Ohm` (默认) | nonnegative scalar

如果存在接地故障，此参数表示电流路径到地的电导。例如，如果到地的路径通过磁芯材料，则根据所使用的磁芯材料指定一个较小的电导值。对于高导电性磁芯材料或机壳短路，请指定更高的电导值。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接，向 Mutual Inductor 模块添加故障，并将 **Ground fault** 设置为 `Negative terminal side of fault node` 或 `Positive terminal side of fault node`。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 分析直流电枢绕组故障。

### **Fault transition time constant** — 过渡到故障状态的时间常数 `1e-3` `s` (默认) | positive scalar

与过渡到故障状态相关联的时间常数，如故障中所述。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接，向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 分析直流电枢绕组故障。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s` (默认) | nonnegative scalar

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible voltage** — 故障过渡的电压阈值 `100` `V` (默认) | positive scalar

定义故障过渡的电压阈值。如果电压值超过此阈值一定次数（由 **Number of events to fail when exceeding voltage** 参数值指定），则模块开始进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **超过电压时失效的事件数** — 电压可超过阈值的最大次数 `1`（默认值）| 正标量

由于基于电压的失效背后的物理机制取决于发生一次或多次局部放电事件，因此该参数允许您设置电感在故障转换开始之前能够承受的电压过冲次数。请注意，该模块不检查处于过压条件的时间，只检查转换次数。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **最大允许电流** — 故障转换的电流阈值 `1` `A`（默认值）| 正标量

故障转换的电流阈值。如果电流超过此值的时间长于 **超过电流时失效的时间** 参数值，则该模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **超过电流时失效的时间** — 电流超过阈值的最大时长 `1` `s`（默认值）| 非负标量

电流超过最大允许值而不触发故障的最大时长。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2023a: 使用单个参数实现故障的时间触发或行为触发

**启用时间触发**和**启用行为触发**参数已被移除，并替换为**故障触发**参数。可以将**故障触发**参数设置为 `Temporal` 或 `Behavioral`。只能启用一个触发。

如果在早期版本中创建了模型并同时启用了时间触发和行为触发，则现在仅启用时间触发。因此，如果行为触发在模型中导致故障，则仿真结果会有所不同。

如果要在特定时间触发故障，请将**故障触发**参数设置为 `Temporal`。如果要确定系统是否失效以及何时失效，请将**故障触发**参数设置为 `Behavioral`。

## 描述

具有每个绕组标称电感可选容差、工作限制和故障的互感电感模型

Mutual Inductor 模块允许您对具有每个绕组标称电感容差的互感电感（双绕组变压器）进行建模。该模型包括以下效应：

- 容差
- 工作限制
- 故障

您可以相互独立地打开和关闭这些建模选项。

在无故障状态下，以下方程描述 Mutual Inductor 模块的行为：

v1=L1diL1dt+​MdiL2dt+iL1R1

v2=L2diL2dt+​MdiL1dt+iL2R2

M=kL1L2

其中：

- *v1* 和 *v2* 分别是初级绕组和次级绕组两端的电压。
- *L1* 和 *L2* 分别是初级绕组和次级绕组的电感。
- *R1* 和 *R2* 分别是初级绕组和次级绕组的串联电阻。
- *M* 是互感。
- *k* 是耦合系数。要反转其中一个绕组的方向，请使用负值。
- *t* 是时间。

在初级和次级绕组的 + 和 – 端子之间放置一个并联电导，使得 *iL1* = *i1* – *G1**v1*，其中 *G1* 是初级绕组的并联电导，*i1* 是流入初级的端子电流。类似的定义和方程适用于 *iL2*。

不要将耦合系数的幅值设置为接近 1 的值，例如 0.999，因为这些值会引入快速仿真动态。要在保留正确的低频行为并阻断 DC 的同时将耦合系数设置为 1，请使用 Simscape Foundation 库中的 Mutual Inductor 模块，并选择 **完美耦合 – 无漏磁** 参数。

Simscape™ 和 Simscape Electrical™ 库包含多个模块，可对相同类型的变压器设备进行建模。但是，这些模块做出不同的建模假设。要为您的应用选择正确的模块，您必须理解这些假设如何随频率影响模块行为。有关详细信息，请参阅选择用于对变压器建模的模块。

### 容差

您可以分别为每个绕组应用容差。数据手册通常会为给定的电感类型提供容差百分比。因此，该值对于两个绕组相同。下表显示了该模块如何将容差应用于标称电感值，以及如何基于为绕组选择的容差应用选项 **L1 容差应用** 或 **L2 容差应用** 来计算电感。

| 选项 | 电感值 |
| --- | --- |
| `None — use nominal value` | *L* |
| `Random tolerance` | 均匀分布：*L* · (1 – *tol* + 2· *tol*· `rand`)  高斯分布：*L* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *L* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *L* · (1 – *tol* ) |

在表中：

- *L* 是初级或次级绕组的标称电感，即 **电感 L1** 或 **电感 L2** 参数值。
- *tol* 是小数容差，即 **容差 (%)** /100。
- *nSigma* 是您为 **引用容差的标准差数** 参数提供的值。
- `rand` 和 `randn` 是用于生成均匀分布和正态分布随机数的标准 MATLAB® 函数。

**注意**

如果选择 `Random tolerance` 选项且处于 "Fast Restart" 模式，则只要小数容差 *tol* 或 **引用容差的标准差数** *nSigma* 中至少有一个设置为 Run-time 并使用变量定义（即使您不修改该变量），随机容差值就会在每次仿真时更新。

### 工作限制

电感通常具有特定的饱和电流额定值，并且可能具有最大允许功耗。您可以根据这些值指定工作限制，以便在电感被驱动到其规格之外时生成警告或错误。

当超过工作限制时，该模块可以生成警告，也可以因错误而停止仿真。有关详细信息，请参阅工作限制参数部分。

### 故障

要在 Mutual Inductor 模块中对故障进行建模，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

电感参数的瞬时变化是非物理的。因此，当 Mutual Inductor 模块进入故障状态时，短路和开路电压会基于以下公式在一段时间内过渡到其故障值：

*`CurrentValue`* = *`FaultedValue`* – (*`FaultedValue`* – *`UnfaultedValue`*) · `sech`(∆t / τ)

其中：

- ∆t 是自故障条件开始以来的时间。
- τ 是 **故障过渡时间常数** 参数的值。

对于短路故障，短路路径的电导也会根据 `sech`(∆t / τ) 函数从小值（表示开路路径）变为大值。

Mutual Inductor 模块允许您选择故障发生在初级绕组还是次级绕组。该模块将故障绕组建模为故障电感。无故障绕组耦合到故障绕组。因此，实际方程总共涉及三个耦合绕组：两个用于故障绕组，一个用于无故障绕组。初级和次级绕组之间的耦合由 **耦合系数** 参数定义。

该模块可以触发故障转换的开始：

- 在特定时间。
- 在电压超过最大允许值一定次数之后。
- 当电流超过最大允许值的时间长于特定时间间隔时。

如果要在特定时间触发故障，请在 **故障检查器** 窗口中，将 **触发类型** 设置为 `Timed`。如果要确定系统是否失效以及何时失效，请在 **故障检查器** 窗口中，将 **触发类型** 设置为 `Behavioral`。

如果选择行为触发，则一旦其中一个触发条件为真，组件就会失效。

可故障电感通常要求您使用固定步长局部求解器，尤其是当您的模型过渡到包含短路的故障状态时。有关详细信息，请参阅为物理仿真做出最优求解器选择。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅通过标称值进行系统缩放。

**Primary current** 和 **Secondary current** 变量允许您为仿真开始时相应绕组中的初始电感电流指定高优先级目标。
