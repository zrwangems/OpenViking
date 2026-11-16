---
type: simulink-block
title: 'Charge Pump'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'chargepump'
documentation_source_path: 'ref/chargepump.html'
language: zh-CN
chinese_source: worker-translation
---

# Charge Pump

## 端口

### 输入

### **up** — 输入端口标量

输入端口，连接到 PLL 系统中 PFD 的 **up** 输出。

**数据类型：** `double`

### **down** — 输入端口标量

输入端口，连接到 PLL 系统中 PFD 的 **down** 输出。

**数据类型：** `double`
### 输出

### **out** — 输出端口标量

输出端口，连接到 PLL 系统中的 Loop Filter 模块。**out** 提供与 **up** 和 **down** 输入端口之间占空比差值成比例的电流。

**数据类型：** `double`

## 参数

### 配置

### **输出电流 (A)** — 设计输出电流 `1e-3`（默认）| 正实数标量

设计输出电流的满量程幅值，指定为以 amperes 为单位的正实数标量。此参数可调。

#### 程序化使用

- 使用 `get_param(gcb,'OutputCurrent')` 查看 **输出电流 (A)** 的当前值。
- 使用 `set_param(gcb,'OutputCurrent',value)` 将 **输出电流 (A)** 设置为特定值。

### **输入阈值 (V)** — 输入端口处的逻辑切换阈值 `0.5`（默认）| 实数标量

输入端口处的逻辑切换阈值，指定为以 volts 为单位的实数标量。

#### 程序化使用

- 使用 `get_param(gcb,'InputThreshold')` 查看 **输入阈值 (V)** 的当前值。
- 使用 `set_param(gcb,'InputThreshold',value)` 将 **输入阈值 (V)** 设置为特定值。

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小 off（默认）| on

选中此选项可在仿真期间启用增大的缓冲区大小。这会增大 Charge Pump 模块内部 Logic Decision 和 Slew Rate 的缓冲区大小。默认情况下，此选项处于未选中状态。

### **缓冲区大小** — 仿真期间可用的输入缓冲的样本数 `10`（默认）| 正整数标量

仿真期间可用的输入缓冲的样本数，指定为正整数标量。这用于设置 Charge Pump 模块内部 Logic Decision 和 Slew Rate 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **缓冲区大小** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当在 **配置** 选项卡中选中 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBuffer')` 查看 **缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **缓冲区大小** 设置为特定值。

### 损伤

### **启用电流损伤** — 向仿真添加电流损伤 on（默认）| off

选中此选项可向仿真添加电流损伤，例如电流不平衡和泄漏电流。默认情况下，此选项处于选中状态。

### **电流不平衡 (A)** — 满量程正电流与负电流之间的差值 `1e-7`（默认）| 正实数标量

满量程正电流与负电流之间的差值，指定为以 amperes 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用电流损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'CurrentImbalance')` 查看 **电流不平衡 (A)** 的当前值。
- 使用 `set_param(gcb,'CurrentImbalance',value)` 将 **电流不平衡 (A)** 设置为特定值。

**数据类型：** `double`

### **泄漏电流 (A)** — 没有任何输入时的输出电流 `1e-8`（默认）| 非负实数标量

当两个输入均处于逻辑零时的输出电流，指定为以 amperes 为单位的非负实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用电流损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'LeakageCurrent')` 查看 **泄漏电流 (A)** 的当前值。
- 使用 `set_param(gcb,'LeakageCurrent',value)` 将 **泄漏电流 (A)** 设置为特定值。

**数据类型：** `double`

### **启用时序损伤** — 向仿真添加时序损伤 on（默认）| off

选中此选项可向仿真添加时序损伤，例如上升/下降时间和传播延迟。默认情况下，此选项处于选中状态。

### **输出步长计算** — 确定如何计算输出步长 `Default`（默认）| `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据上升/下降时间计算输出步长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据感兴趣的最大频率计算输出步长。输出步长 (ΔT) 由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**，并为 **输出步长计算** 选择 **Advanced**。

### **感兴趣的最大频率 (Hz)** — 输出端感兴趣的最大频率 `10e9`（默认）| 正实数标量

输出端感兴趣的最大频率，指定为以 Hz 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**，并为 **输出步长计算** 选择 **Advanced**。

#### 程序化使用

- 使用 `get_param(gcb,'MaxFreqInterest')` 查看 **感兴趣的最大频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'MaxFreqInterest',value)` 将 **感兴趣的最大频率 (Hz)** 设置为特定值。

**数据类型：** `double`

#### up

### **上升/下降时间 (s)** — **up** 输入端口的 20%-80% 上升/下降时间 `5e-9`（默认）| 正实数标量

**up** 输入端口的 20%-80% 上升/下降时间，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallUp')` 查看 **up 上升/下降时间** 的当前值。
- 使用 `set_param(gcb,'RiseFallUp',value)` 将 **up 上升/下降时间** 设置为特定值。

### **Up 传播延迟** — **up** 输入端口的总传播延迟 `6e-9`（默认）| 正实数标量

**up** 输入端口的总传播延迟，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayUp')` 查看 **Up 传播延迟** 的当前值。
- 使用 `set_param(gcb,'PropDelayUp',value)` 将 **Up 传播延迟** 设置为特定值。

#### down

### **上升/下降时间** — **down** 输入端口的 20%-80% 上升/下降时间 `2e-9`（默认）| 正实数标量

**down** 输入端口的 20%-80% 上升/下降时间，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallDown')` 查看 **down 上升/下降时间** 的当前值。
- 使用 `set_param(gcb,'RiseFallDown',value)` 将 **down 上升/下降时间** 设置为特定值。

### **Down 传播延迟** — **down** 输入端口的总传播延迟 `4e-9`（默认）| 正实数标量

**down** 输入端口的总传播延迟，指定为以 seconds 为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用损伤**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayDown')` 查看 **Down 传播延迟** 的当前值。
- 使用 `set_param(gcb,'PropDelayDown',value)` 将 **Down 传播延迟** 设置为特定值。

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

输出与两个输入端口之间占空比差值成比例的电流

Charge Pump 模块生成输出电流，该电流与其 **up** 和 **down** 输入端口上信号之间的占空比差值成比例。在锁相环 (PLL) 系统中，Charge Pump 模块将 PFD 模块的两个输出所表示的相位误差转换为 Loop Filter 输入端处的单个电流。
