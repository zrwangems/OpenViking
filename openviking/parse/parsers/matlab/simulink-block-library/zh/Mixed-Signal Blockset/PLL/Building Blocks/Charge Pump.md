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
```yaml
ports:
- name: up
  summary: 输入端口 标量
  direction: input
  data_types: double
- name: down
  summary: 输入端口 标量
  direction: input
  data_types: double
- name: out
  summary: 输出端口 标量
  direction: output
  data_types: double
```

### 输入

### **up** — 输入端口 标量

输入端口，连接到 PLL 系统中 PFD 的 **up** 输出。

**数据类型：** `double`

### **down** — 输入端口 标量

输入端口，连接到 PLL 系统中 PFD 的 **down** 输出。

**数据类型：** `double`
### 输出

### **out** — 输出端口 标量

输出端口，连接到 PLL 系统中的 Loop Filter 模块。**out** 输出的电流与 **up** 和 **down** 输入端口之间的占空比差值成正比。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Output current (A)
  summary: 设计输出电流 1e-3（默认）| 正实数标量
  group: 配置
- name: Input threshold (V)
  summary: 输入端口的逻辑切换阈值 0.5（默认）| 实数标量
  group: 配置
- name: Enable increased buffer size
  summary: 启用增大的缓冲区大小 off（默认）| on
  group: 配置
- name: Buffer size
  summary: 仿真期间可用的输入缓冲采样数 10（默认）| 正整数标量
  group: 配置
- name: Enable current impairments
  summary: 将电流损伤添加到仿真 on（默认）| off
  group: 损伤
- name: Current imbalance (A)
  summary: 满量程正电流与负电流之间的差值 1e-7（默认）| 正实数标量
  group: 损伤
- name: Leakage current (A)
  summary: 无任何输入时的输出电流 1e-8（默认）| 非负实数标量
  group: 损伤
- name: Enable timing impairments
  summary: 向仿真添加时序损伤 on（默认）| off
  group: 损伤
- name: Output step size calculation
  summary: 确定如何计算输出步长 Default（默认）| Advanced
  group: 损伤
- name: Maximum frequency of interest (Hz)
  summary: 输出端的最大关注频率 10e9（默认）| 正实数标量
  group: 损伤
- name: Rise/fall time (s)
  summary: up 输入端口 20%-80% 上升/下降时间 5e-9（默认）| 正实数标量
  group: 损伤
- name: Up propagation delay
  summary: up 输入端口的总传播延迟 6e-9（默认）| 正实数标量
  group: 损伤
- name: Rise/fall time
  summary: down 输入端口 20%-80% 上升/下降时间 2e-9（默认）| 正实数标量
  group: 损伤
- name: Down propagation delay
  summary: down 输入端口的总传播延迟 4e-9（默认）| 正实数标量
  group: 损伤
```

### 配置

### **Output current (A)** — 设计输出电流 `1e-3`（默认）| 正实数标量

设计输出电流的满量程幅值，指定为以安培为单位的正实数标量。此参数可调。

#### 程序化使用

- 使用 `get_param(gcb,'OutputCurrent')` 查看 **Output current (A)** 的当前值。
- 使用 `set_param(gcb,'OutputCurrent',value)` 将 **Output current (A)** 设置为特定值。

### **Input threshold (V)** — 输入端口的逻辑切换阈值 `0.5`（默认）| 实数标量

输入端口的逻辑切换阈值，指定为以伏特为单位的实数标量。

#### 程序化使用

- 使用 `get_param(gcb,'InputThreshold')` 查看 **Input threshold (V)** 的当前值。
- 使用 `set_param(gcb,'InputThreshold',value)` 将 **Input threshold (V)** 设置为特定值。

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 Charge Pump 模块内部 Logic Decision 和 Slew Rate 的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `10`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。此参数设置 Charge Pump 模块内部 Logic Decision 和 Slew Rate 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。将 **Buffer size** 设置为足够大的值，使输入缓冲区包含所有所需的输入采样。

#### 依赖关系

此参数仅在 **Configuration** 选项卡中选中 **Enable increased buffer size** 选项时可用。

#### 程序化使用

- 使用 `get_param(gcb,'NBuffer')` 查看 **Buffer size** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **Buffer size** 设置为特定值。

### 损伤

### **Enable current impairments** — 将电流损伤添加到仿真 on（默认）| off

选择此项可将电流损伤（如电流不平衡和泄漏电流）添加到仿真中。默认情况下，此选项已选中。

### **Current imbalance (A)** — 满量程正电流与负电流之间的差值 `1e-7`（默认）| 正实数标量

满量程正电流与负电流之间的差值，指定为以安培为单位的正实数标量。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选中 **Enable current impairments**。

#### 程序化使用

- 使用 `get_param(gcb,'CurrentImbalance')` 查看 **Current imbalance (A)** 的当前值。
- 使用 `set_param(gcb,'CurrentImbalance',value)` 将 **Current imbalance (A)** 设置为特定值。

**数据类型：** `double`

### **Leakage current (A)** — 无任何输入时的输出电流 `1e-8`（默认）| 非负实数标量

当两个输入均为逻辑零时的输出电流，指定为以安培为单位的非负实数标量。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选中 **Enable current impairments**。

#### 程序化使用

- 使用 `get_param(gcb,'LeakageCurrent')`
  查看 **Leakage current
  (A)** 的当前值。
- 使用
  `set_param(gcb,'LeakageCurrent',value)`
  将 **Leakage current (A)** 设置为
  特定值。

**数据类型：** `double`

### **Enable timing impairments** — 向仿真添加时序损伤 on（默认）| off

选择以向仿真添加时序损伤，例如上升/下降时间和
传播延迟。默认情况下，此选项为
选中状态。

### **Output step size calculation** — 确定如何计算输出步长 `Default`（默认）| `Advanced`

确定如何计算输出步长：

- 选择 `Default` 以根据上升/下降时间计算输出步
  长。输出步长 (ΔT) 由 ΔT=(Rise/fall time)26 · 0.22 给出。
- 选择 `Advanced` 以根据最大关注频率计算输出
  步长。输出步长 (ΔT)
  由 ΔT=Rise/fall time6 · Maximum frequency of interest 给出。

#### 依赖关系

要启用此参数，请在 **Impairments**
选项卡中选择 **Enable timing
impairments**。

### **Maximum frequency of interest (Hz)** — 输出端的最大关注频率 `10e9`（默认）| 正实数标量

输出端的最大关注频率，指定为正
实数标量，单位为 Hz。

#### 依赖关系

要启用此参数，请在 **Impairments**
选项卡中选择 **Enable timing
impairments**，并为 **Output
step size calculation** 选择 **Advanced**。

#### 程序化使用

- 使用 `get_param(gcb,'MaxFreqInterest')`
  查看 **Maximum frequency of
  interest (Hz)** 的当前值。
- 使用
  `set_param(gcb,'MaxFreqInterest',value)`
  将 **Maximum frequency of interest
  (Hz)** 设置为特定值。

**数据类型：** `double`

#### up

### **Rise/fall time (s)** — up 输入端口 20%-80% 上升/下降时间 `5e-9`（默认）| 正实数标量

**up** 输入端口的 20%-80% 上升/下降时间，
指定为正实数标量，单位为秒。

#### 依赖关系

要启用此参数，请在 **Impairments**
选项卡中选择 **Enable timing
Impairments**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallUp')` 查看
  **up Rise/fall
  time** 的当前值。
- 使用 `set_param(gcb,'RiseFallUp',value)`
  将 **up Rise/fall time** 设置为特定
  值。

### **Up propagation delay** — up 输入端口的总传播延迟 `6e-9`（默认）| 正实数标量

**up** 输入端口的总传播延迟，
指定为正实数标量，单位为秒。

#### 依赖关系

要启用此参数，请在 **Impairments**
选项卡中选择 **Enable
Impairments**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayUp')` 查看
  **Up propagation
  delay** 的当前值。
- 使用
  `set_param(gcb,'PropDelayUp',value)` 将
  **Up propagation delay** 设置为特定
  值。

#### down

### **Rise/fall time** — down 输入端口 20%-80% 上升/下降时间 `2e-9`（默认）| 正实数标量

**down** 输入端口的 20%-80% 上升/下降时间，
指定为正实数标量，单位为秒。

#### 依赖关系

要启用此参数，请在 **Impairments**
选项卡中选择 **Enable
Impairments**。

#### 程序化使用

- 使用 `get_param(gcb,'RiseFallDown')` 查看
  **down Rise/fall
  time** 的当前值。
- 使用
  `set_param(gcb,'RiseFallDown',value)` 将
  **down Rise/fall time** 设置为特定
  值。

### **Down propagation delay** — down 输入端口的总传播延迟 `4e-9`（默认）| 正实数标量

**down** 输入端口的总传播延迟，
指定为正实数标量，单位为秒。

#### 依赖关系

要启用此参数，请在 **Impairments**
选项卡中选择 **Enable
Impairments**。

#### 程序化使用

- 使用 `get_param(gcb,'PropDelayDown')` 查看
  **Down propagation
  delay** 的当前值。
- 使用
  `set_param(gcb,'PropDelayDown',value)` 将
  **Down propagation delay** 设置为
  特定值。
## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

输出与两个输入端口之间占空比差值成比例的电流

Charge Pump 模块产生一个输出电流，该电流与其 **up** 和 **down** 输入端口处信号的占空比差值成比例。在锁相环（PLL）系统中，Charge Pump 模块将 PFD 模块的两个输出所表示的相位误差转换为 Loop Filter 输入端的单一电流。
