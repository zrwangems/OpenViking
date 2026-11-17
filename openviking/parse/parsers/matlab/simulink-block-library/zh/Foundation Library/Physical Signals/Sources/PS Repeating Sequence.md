---
type: simulink-block
title: 'PS Repeating Sequence'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'psrepeatingsequence'
documentation_source_path: 'ref/psrepeatingsequence.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Repeating Sequence

## 端口
```yaml
ports:
- name: Y
  summary: 输出物理信号，无量纲物理信号
  direction: output
```

### 输出

### **Y** — 输出物理信号，无量纲物理信号

输出物理信号。
## 参数
```yaml
parameters:
- name: Initial output
  summary: 时间为零时的输出 0（默认）
  group: ''
- name: Time offset
  summary: 初始时间偏移 0 s（默认）
  group: ''
- name: Signal type
  summary: 生成信号的类型 Discontinuous（默认）| Continuous | Discrete
  group: ''
- name: Durations
  summary: 线性段持续时间 [ 1, 1 ] s（默认）
  group: ''
- name: Start output values
  summary: 每个线性段的起始值 [ 0, 2 ]（默认）
  group: ''
- name: End output values
  summary: 每个线性段的结束值 [ 1, 1 ]（默认）
  group: ''
```

### **Initial output** — 时间为零时的输出 `0`（默认）

时间零时输出信号的值。该模块的输出保持此值，直到仿真时间达到 **Time offset** 值。

### **Time offset** — 初始时间偏移 `0 s`（默认）

初始时间偏移的值，在重复序列开始之前。在此期间，模块的输出保持在 **Initial output** 值。

### **Signal type** — 生成信号的类型 `Discontinuous`（默认）| `Continuous` | `Discrete`

选择以下信号类型之一：

- `Discontinuous` — 对于重复序列中的每个线性段，定义其持续时间、起始值和结束值。如果某段的结束值与下一段的起始值不同，则它们通过垂直线连接。这是默认方法。
- `Continuous` — 对于重复序列中的每个线性段，定义其持续时间和起始值。某段的结束值与下一段的起始值相同。
- `Discrete` — 对于重复序列中的每个线性段，定义其持续时间和起始值。某段的结束值与其起始值相同。

### **Durations** — 线性段持续时间 `[ 1, 1 ] s`（默认）

将线性段持续时间指定为 1×*`n`* 行向量，其中 *`n`* 是重复序列中线性段的数量。*`n`* 不得大于 100。默认值指定两个线性段，每个持续 1 秒。

### **Start output values** — 每个线性段的起始值 `[ 0, 2 ]`（默认）

将每个线性段的输出信号起始值指定为 1×*`n`* 行向量，其中 *`n`* 是重复序列中线性段的数量。向量的大小必须与 **Durations** 行向量的大小匹配。默认值指定两个线性段中的第一个从 0 开始，第二个从 2 开始。

### **End output values** — 每个线性段的结束值 `[ 1, 1 ]`（默认）

将每个线性段的输出信号结束值指定为 1×*`n`* 行向量，其中 *`n`* 是重复序列中线性段的数量。向量的大小必须与 **Durations** 行向量的大小匹配。

#### 依赖关系

仅当 **Signal type** 参数设置为 `Discontinuous` 时启用。对于其他信号类型，段的结束值由下一段的起始值（`Continuous`）或同一段的起始值（`Discrete`）定义。
## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

输出周期性分段线性信号

PS Repeating Sequence 模块输出一个周期性分段线性信号 *`y`*。您可以选择性地指定初始信号值和初始时间偏移。重复序列由多个相互连接的线性段组成。段数不得大于 100。您通过选择信号类型来指定如何连接这些段。对于相同的模块参数值集合，根据信号类型的不同，生成的输出信号也会不同：

- `Discontinuous` — 重复序列中的每个线性段由其持续时间、起始值和结束值定义。如果某段的结束值与下一段的起始值不同，则它们通过垂直线连接。
- `Continuous` — 重复序列中的每个线性段由其持续时间和起始值定义。某段的结束值与下一段的起始值相同。
- `Discrete` — 重复序列中的每个线性段由其持续时间和起始值定义。某段的结束值与其起始值相同。

使用此模块生成各种类型的物理信号，例如脉冲、锯齿波、阶梯波等。

### 不连续重复序列

此示例展示了模块参数值与生成的输出信号之间的映射关系。

按如下所示设置模块参数：

以下绘图展示了生成的模块输出。

信号从 0 开始，由两个线性段组成。第一段的持续时间为 1 秒，该段从 0 开始，到 4 结束。信号是不连续的，第一段的结束值与第二段的起始值不同，因此它们通过垂直线连接。第二段从 2 开始，持续 2 秒，到 0 结束，之后序列重复。
