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
```yaml
ports:
- name: 1+
  summary: 一次绕组正极端子电气
  direction: conserving
- name: 1-
  summary: 一次绕组负极端子电气
  direction: conserving
- name: 2+
  summary: 二次绕组正极端子电气
  direction: conserving
- name: 2-
  summary: 二次绕组负极端子电气
  direction: conserving
```

### 守恒端口

### **1+** — 一次绕组正极端子电气

与一次绕组正极端子关联的电气守恒端口。

### **1-** — 一次绕组负极端子电气

与一次绕组负极端子关联的电气守恒端口。

### **2+** — 二次绕组正极端子电气

与二次绕组正极端子关联的电气守恒端口。

### **2-** — 二次绕组负极端子电气

与二次绕组负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Inductance L1
  summary: 一次绕组中的标称电感值 10 H（默认）| 正标量
  group: 主
- name: Inductance L2
  summary: 二次绕组中的标称电感值 0.1 H（默认）| 正标量
  group: 主
- name: Coefficient of coupling
  summary: 绕组之间的互感耦合 0.9（默认）| 范围 [-1,1] 内的标量
  group: 主
- name: Tolerance (%)
  summary: 电感容差，以百分比表示 20（默认）
  group: 主
- name: L1 tolerance application
  summary: 选择如何对一次绕组应用容差 None — use nominal value（默认）| Random tolerance | Apply maximum tolerance value | Apply minimum tolerance
    value
  group: 主
- name: L1 tolerance distribution
  summary: 选择一次绕组的分布类型 Uniform（默认）| Gaussian
  group: 主
- name: L1 number of standard deviations for quoted tolerance
  summary: 用于计算一次绕组的高斯随机数 4（默认）
  group: 主
- name: L2 tolerance application
  summary: 选择如何对二次绕组应用容差 None — use nominal value（默认）| Random tolerance | Apply maximum tolerance value | Apply minimum tolerance
    value
  group: 主
- name: L2 tolerance distribution
  summary: 选择二次绕组的分布类型 Uniform（默认）| Gaussian
  group: 主
- name: L2 number of standard deviations for quoted tolerance
  summary: 用于计算二次绕组的高斯随机数 4（默认）
  group: 主
- name: Series resistance, [R_primary R_secondary]
  summary: 一次绕组和二次绕组的等效串联电阻 [0.001, 0.001] Ohm（默认）
  group: 电阻
- name: Parallel conductance, [G_primary G_secondary]
  summary: 与一次绕组和二次绕组关联的并联泄漏路径 [1e-9,1e-9] 1/Ohm（默认）
  group: 电阻
- name: Enable operating limits
  summary: 选择 Yes 以在超出工作限制时启用报告 No（默认）| Yes
  group: 工作限制
- name: Reporting when operating limits exceeded
  summary: 选择报告方法 Warn（默认）| Error
  group: 工作限制
- name: Saturation current
  summary: 电感饱和电流 1 A（默认）
  group: 工作限制
- name: Power rating
  summary: 电感中的最大功率耗散 1 A（默认）
  group: 工作限制
- name: Mutual inductor fault
  summary: 对互感电感中的故障进行建模的选项 Add fault（默认）
  group: 故障
- name: Faulted winding
  summary: 选择用于故障建模的绕组 Primary（默认）| Secondary
  group: 故障
- name: Location of fault node (% of total turns from - terminal)
  summary: 与故障绕组的 – 端口接触的子电感中的匝数百分比 50（默认）| 范围 (0,100) 内的标量
  group: 故障
- name: Short-circuit turns
  summary: 选择故障是否导致其中一个段短路 No（默认）| To negative terminal | To positive terminal
  group: 故障
- name: Open-circuit at fault node
  summary: 选择是否在段之间应用开路故障 No（默认）| Yes
  group: 故障
- name: Ground fault
  summary: 选择故障是否导致其中一个段短路 No（默认）| Negative terminal side of fault node | Positive terminal side of fault node
  group: 故障
- name: Conductance of faulted ground path
  summary: 两个子电感之间的互感耦合 0 1/Ohm（默认）| 非负标量
  group: 故障
- name: Fault transition time constant
  summary: 过渡到故障状态的时间常数 1e-3 s（默认）| 正标量
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Maximum permissible voltage
  summary: 故障过渡的电压阈值 100 V（默认）| 正标量
  group: 故障
- name: Number of events to fail when exceeding voltage
  summary: 电压超过阈值时可失败的最大次数 1（默认）| 正标量
  group: 故障
- name: Maximum permissible current
  summary: 故障转换的电流阈值 1 A（默认）| 正标量
  group: 故障
- name: Time to fail when exceeding current
  summary: 电流超过阈值的最长时间 1 s（默认）| 非负标量
  group: 故障
```

### 主

### **Inductance L1** — 一次绕组中的标称电感值 `10` `H`（默认）| 正标量

一次绕组中的标称电感值。

### **Inductance L2** — 二次绕组中的标称电感值 `0.1` `H`（默认）| 正标量

二次绕组中的标称电感值。

### **Coefficient of coupling** — 绕组之间的互感耦合 0.9（默认）| 范围 [-1,1] 内的标量

定义一次绕组和二次绕组之间互感耦合的耦合系数。要反转其中一个绕组的方向，请使用负值。

不要使用非常接近 1 的数值，例如 0.999，因为这些值会引入快速的仿真动态。要在保持正确的低频行为（阻断直流）的同时将耦合系数设置为 1，请使用 Simscape Foundation 库中的 Mutual Inductor 模块，并选择 **Perfect coupling – no leakage** 参数。

### **Tolerance (%)** — 电感容差，以百分比表示 20（默认）

制造商数据手册中定义的电感容差。数据手册通常会给出给定电感类型的容差百分比。因此，该值对两个绕组相同。

### **L1 tolerance application** — 选择如何对一次绕组应用容差 `None — use nominal value`（默认）| `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择在仿真期间如何对一次绕组应用容差：

- `None — use nominal value`
  — 模块不应用容差，使用标称电感值。
- `Random tolerance` — 模块在容差
  值限制内对电感值应用随机偏移。您可以使用
  **Tolerance distribution**
  参数选择 Uniform 或 Gaussian
  分布来计算随机数。
- `Apply maximum tolerance value`
  — 电感增加指定的容差
  百分比值。
- `Apply minimum tolerance value`
  — 电感减少指定的容差
  百分比值。

### **L1 tolerance distribution** — 选择一次绕组的分布类型 `Uniform`（默认）| `Gaussian`

选择随机容差的分布类型：

- `Uniform` — 均匀
  分布
- `Gaussian` — 高斯
  分布

#### 依赖关系

当 **L1 tolerance application**
参数设置为 `Random
tolerance` 时启用。

### **L1 number of standard deviations for quoted tolerance** — 用于计算一次绕组的高斯随机数 4（默认）

用于计算高斯随机数的标准差数量。

#### 依赖关系

当 **L1 tolerance distribution**
参数设置为 `Gaussian` 时启用。

### **L2 tolerance application** — 选择如何对二次绕组应用容差 `None — use nominal value`（默认）| `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

选择在仿真期间如何对二次绕组应用容差：

- `None — use nominal value`
  — 模块不应用容差，使用标称电感值。
- `Random tolerance` — 模块在容差
  值限制内对电感值应用随机偏移。您可以使用
  **Tolerance distribution**
  参数选择 Uniform 或 Gaussian
  分布来计算随机数。
- `Apply maximum tolerance value`
  — 电感增加指定的容差
  百分比值。
- `Apply minimum tolerance value`
  — 电感减少指定的容差
  百分比值。

### **L2 tolerance distribution** — 选择二次绕组的分布类型 `Uniform`（默认）| `Gaussian`

选择随机容差的分布类型：

- `Uniform` — 均匀
  分布
- `Gaussian` — 高斯
  分布

#### 依赖关系

当 **L2 tolerance application**
参数设置为 `Random
tolerance` 时启用。

### **L2 number of standard deviations for quoted tolerance** — 用于计算二次绕组的高斯随机数 `4`（默认）

用于计算高斯随机数的标准差数量。

#### 依赖关系

当 **L2 tolerance distribution**
参数设置为 `Gaussian` 时启用。

### 电阻

### **Series resistance, [R\_primary R\_secondary]** — 一次绕组和二次绕组的等效串联电阻 `[0.001, 0.001]` `Ohm`（默认）

一次绕组和二次绕组的等效串联电阻，指定为二元向量。第一个数字对应一次绕组，第二个数字对应二次绕组。对于故障绕组，模块按照该段中的匝数比例将电阻分配给每个段。

### **Parallel conductance, [G\_primary G\_secondary]** — 与一次绕组和二次绕组关联的并联泄漏路径 `[1e-9,1e-9]` `1/Ohm`（默认）

与一次绕组和二次绕组关联的并联泄漏路径，指定为二元向量。第一个数字对应一次绕组，第二个数字对应二次绕组。并联电导直接跨接在一次绕组和二次绕组的 + 和 – 端子两端。

### 工作限制

### **Enable operating limits** — 选择 `Yes` 以在超出工作限制时启用报告 `No`（默认）| `Yes`

选择 `Yes` 以在超出工作限制时启用报告。**Operating Limits** 部分中的关联参数将变为可见，以便您选择报告方法并以功率和电流的形式指定工作限制。

### **Reporting when operating limits exceeded** — 选择报告方法 `Warn`（默认）| `Error`

选择超出工作限制时发生的情况：

- `Warn` — 模块发出
  警告。
- `Error` — 仿真停止
  并报错。

#### 依赖关系

当 **Enable operating limits**
参数设置为 `Yes` 时启用。

### **Saturation current** — 电感饱和电流 `1` `A`（默认）

制造商数据手册中定义的电感饱和电流。如果流入一次绕组和二次绕组的净电流超过此值，磁芯材料进入饱和，模块报告工作限制违规。也就是说，模块将限制与 |*i*1 +
*i*2| 进行比较，其中电流在流入 + 节点时定义为正值。

#### 依赖关系

当 **Enable operating limits**
参数设置为 `Yes` 时启用。

### **Power rating** — 电感中的最大功率耗散 `1` `A`（默认）

与互感电感关联的电阻和电导元件中的最大瞬时（总）功率耗散。如果总功率（包括一次绕组和二次绕组）超过此数值，模块报告工作限制违规。

#### 依赖关系

当 **Enable operating limits**
参数设置为 `Yes` 时启用。

### 故障

### **Mutual inductor fault** — 对互感电感中的故障进行建模的选项 `Add fault`（默认）

对 Mutual Inductor 模块中的故障进行建模的选项。

要添加故障，请点击 **Add fault**
超链接。

### **Faulted winding** — 选择用于故障建模的绕组 `Primary`（默认）| `Secondary`

选择故障发生在一 次绕组还是二次绕组中。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Location of fault node (% of total turns from - terminal)** — 与故障绕组的 – 端口接触的子电感中的匝数百分比 `50`（默认）| 范围 (0,100) 内的标量

在实践中，故障是通过将故障绕组分割为两个串联连接的耦合子电感来实现的。电感与相应段中匝数的平方成正比，每个子电感的串联电阻与每段中的匝数成正比。并联电导跨越两个段。

此参数表示分配给与故障绕组的 – 端口接触的子电感的匝数百分比。其余匝数分配给另一个子电感。默认值为 `50`，这意味着故障绕组的总电感被分为两个相等的耦合子电感。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Short-circuit turns** — 选择故障是否导致其中一个段短路 `No`（默认）| `To negative terminal` | `To positive terminal`

选择故障是否导致其中一个子电感段短路：

- `No` — 故障不会
  产生短路。
- `To negative terminal` —
  故障使与模块 – 端口接触的子电感短路。
- `To positive terminal` —
  故障使与模块 + 端口接触的子电感短路。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Open-circuit at fault node** — 选择是否在段之间应用开路故障 `No`（默认）| `Yes`

选择是否在两个子电感段之间应用开路故障。默认值为 `No`。即使存在开路故障，子电感的特性仍然相关，因为即使在故障状态下它们仍然磁耦合。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Ground fault** — 选择故障是否导致其中一个段短路 `No`（默认）| `Negative terminal side of fault node` | `Positive terminal side of fault node`

选择在故障情况下是否存在电流流向接地节点的路径：

- `No` — 故障不会
  导致与地的连接。
- `Negative terminal side of fault
  node` — 与模块 – 端口接触的一侧连接到地。
- `Positive terminal side of fault
  node` — 与模块 + 端口接触的一侧连接到地。

如果 **Open-circuit at fault node** 参数设置为 `Yes`，您需要指定哪一侧（负或正）连接到地。如果没有开路，两个选项的行为类似。物理上，这对应于绕组与接地磁芯或机壳之间的绝缘击穿。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Conductance of faulted ground path** — 两个子电感之间的互感耦合 `0` `1/Ohm`（默认）| 非负标量

如果存在接地故障，此参数表示到地的电流路径的电导。例如，如果到地的路径通过磁芯材料，则根据所使用的磁芯材料指定较小的电导值。对于高导电性磁芯材料或机壳短路，请指定较高的电导值。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接向 Mutual Inductor 模块添加故障，并将 **Ground fault** 设置为 `Negative
terminal side of fault node` 或
`Positive terminal side of fault
node`。。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Fault transition time constant** — 过渡到故障状态的时间常数 `1e-3` `s`（默认）| 正标量

与过渡到故障状态关联的时间常数，如故障中所述。

#### 依赖关系

要启用此参数，请通过点击 **Mutual inductor fault** 参数中的 **Add fault** 超链接向 Mutual Inductor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add
fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Timed`。

### **Maximum permissible voltage** — 故障过渡的电压阈值 `100` `V`（默认）| 正标量

定义故障过渡的电压阈值。如果电压值超过此阈值一定次数（由 **Number of events to fail when exceeding voltage** 参数值指定），则模块开始进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **Number of events to fail when exceeding voltage** — 电压超过阈值时可失败的最大次数 `1`（默认）| 正标量

由于电压型失效的物理机制取决于发生一次或多次局部放电事件，此参数允许您设置电感在故障转换开始之前能够承受的电压过冲次数。请注意，该模块不检查处于过压状态的时间，只检查转换次数。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Maximum permissible current** — 故障转换的电流阈值 `1` `A`（默认）| 正标量

故障转换的电流阈值。如果电流超过此值的时间长于 **Time to fail when exceeding current** 参数值，则该模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding current** — 电流超过阈值的最长时间 `1` `s`（默认）| 非负标量

电流可以超过最大允许值而不触发故障的最长时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。
## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2023a：使用单个参数实现故障的时间触发器或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并由 **Fault trigger** 参数替代。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。您只能启用一个触发器。

如果您在较早版本中创建了模型并同时启用了时间触发器和行为触发器，现在仅启用时间触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果会有所不同。

如果您想在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果您想确定系统是否失效以及何时失效，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

具有标称电感、每个绕组的可选容差、工作限制和故障的互感模型

Mutual Inductor 模块允许您对互感（双绕组变压器）进行建模，并为每个绕组设置标称电感容差。该模型包含以下效应：

- 容差
- 工作限制
- 故障

您可以相互独立地打开和关闭这些建模选项。

在未故障状态下，以下方程描述 Mutual Inductor 模块的行为：

v1=L1diL1dt+​MdiL2dt+iL1R1

v2=L2diL2dt+​MdiL1dt+iL2R2

M=kL1L2

其中：

- *v1* 和 *v2* 分别是初级和次级绕组两端的电压。
- *L1* 和 *L2* 分别是初级和次级绕组的电感。
- *R1* 和 *R2* 分别是初级和次级绕组的串联电阻。
- *M* 是互感。
- *k* 是耦合系数。要反转其中一个绕组的方向，请使用负值。
- *t* 是时间。

在初级和次级绕组的 + 和 – 端子之间放置一个并联电导，使得 *iL1* = *i1* – *G1**v1*，其中 *G1* 是初级绕组的并联电导，*i1* 是流入初级的端子电流。类似的定义和方程适用于 *iL2*。

不要将耦合系数的幅值设置为接近 1 的值，例如 0.999，因为这些值会引入快速仿真动态。要将耦合系数设置为 1，同时保持正确的低频行为并阻断 DC，请使用 Simscape Foundation 库中的 Mutual Inductor 模块，并选择 **Perfect coupling – no leakage** 参数。

Simscape™ 和 Simscape Electrical™ 库包含多个可以对同一类型变压器设备进行建模的模块。但是，这些模块做出不同的建模假设。要为您的应用选择正确的模块，您必须了解这些假设如何影响模块行为随频率的变化。有关详细信息，请参阅 Choose Blocks to Model Transformers。

### 容差

您可以为每个绕组分别应用容差。数据手册通常给出给定电感类型的容差百分比。因此，该值对两个绕组相同。下表显示了该模块如何将容差应用于标称电感值，并根据为绕组选择的容差应用选项 **L1 tolerance application** 或 **L2 tolerance application** 计算电感。

| 选项 | 电感值 |
| --- | --- |
| `None — use nominal value` | *L* |
| `Random tolerance` | 均匀分布：*L* · (1 – *tol* + 2· *tol*· `rand`)  高斯分布：*L* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *L* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *L* · (1 – *tol* ) |

表中：

- *L* 是初级或次级绕组的标称电感，即 **Inductance L1** 或 **Inductance L2** 参数值。
- *tol* 是分数容差，即 **Tolerance (%)** /100。
- *nSigma* 是您为 **Number of standard deviations for quoted tolerance** 参数提供的值。
- `rand` 和 `randn` 是用于生成均匀分布和正态分布随机数的标准 MATLAB® 函数。

**注意**

如果您选择 `Random tolerance` 选项并且处于“Fast Restart”模式，则只要分数容差 *tol* 或 **Number of standard deviations for quoted tolerance** *nSigma* 中至少有一个设置为 Run-time 并使用变量定义（即使您不修改该变量），随机容差值就会在每次仿真时更新。

### 工作限制

电感通常以特定饱和电流为额定值，并且可能还以最大允许功率耗散为额定值。您可以根据这些值指定工作限制，以便在电感被驱动超出其规格时生成警告或错误。

当超过工作限制时，该模块可以生成警告或通过错误停止仿真。有关详细信息，请参阅 Operating Limits parameters 部分。

### 故障

要对 Mutual Inductor 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

电感参数的瞬时变化是非物理的。因此，当 Mutual Inductor 模块进入故障状态时，短路和开路电压会在一段时间内根据以下公式过渡到其故障值：

*`CurrentValue`* =
*`FaultedValue`* –
(*`FaultedValue`* –
*`UnfaultedValue`*) · `sech`(∆t
/ τ)

其中：

- ∆t 是自故障条件开始以来的时间。
- τ 是 **Fault transition time constant** 参数的值。

对于短路故障，短路路径的电导也根据 `sech`(∆t / τ) 函数从小值（表示开路路径）变化到大值。

Mutual Inductor 模块允许您选择故障发生在初级还是次级绕组中。该模块将故障绕组建模为故障电感。未故障绕组耦合到故障绕组。因此，实际方程总共涉及三个耦合绕组：两个用于故障绕组，一个用于未故障绕组。初级和次级绕组之间的耦合由 **Coefficient of coupling** 参数定义。

该模块可以触发故障转换的开始：

- 在特定时间。
- 在电压超过最大允许值一定次数之后。
- 当电流超过最大允许值的时间长于特定时间间隔时。

如果您想在特定时间触发故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Timed`。如果您想确定系统是否失效以及何时失效，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Behavioral`。

如果您选择行为触发器，则一旦其中一个触发条件为真，组件就会失效。

可故障电感通常要求您使用定步长局部求解器，特别是当您的模型转换到包含短路的故障状态时。有关详细信息，请参阅 Making Optimal Solver Choices for Physical Simulation。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期幅值。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

**Primary current** 和 **Secondary current** 变量允许您为仿真开始时相应绕组中的初始电感电流指定高优先级目标。
