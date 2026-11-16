---
type: simulink-block
title: 'Circuit Breaker'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'circuitbreaker'
documentation_source_path: 'ref/circuitbreaker.html'
language: zh-CN
chinese_source: worker-translation
---

# Circuit Breaker

## 端口

### 输入

### **vT** — 标量控制端口物理信号

标量物理信号控制端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `PS control port`。
### 守恒

### **1** — 端口 1 电气

电气守恒端口。

### **2** — 端口 2 电气

电气守恒端口。

### **+** — 正端口电气

正电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。

### **-** — 负端口电气

负电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Electrical control port`。

## 参数

### **Modeling option** — 指定物理控制端口还是电气控制端口 `PS control port`（默认） | `Electrical control port`

为开关门极指定物理控制端口还是电气控制端口。

### **Closed resistance** — 闭合电阻 `0.001` `Ohm`（默认）

断路器闭合时端口 **1** 和 **2** 之间的电阻。

### **Open conductance** — 断开电导 `1e-6` `1/Ohm`（默认）

断路器断开时端口 **1** 和 **2** 之间的电导。

### **Threshold** — 阈值电压 `0.5` `V`（默认）

控制端口 **vT** 的阈值电压。该模块使用阈值电压以及仿真开始时 **vT** 的值来确定断路器初始是断开还是闭合。如果将 **Breaker Behavior** 设置为 `Open when current crosses zero after vT >= Threshold`，则当电压升至阈值以上时，断路器在其电流过零时断开。如果将 **Breaker Behavior** 设置为 `Open when vT >= Threshold`，则断路器在电压升至阈值以上时立即断开。当控制端口电压降至阈值以下时，断路器闭合。

### **Breaker Behavior** — *vT* 升至阈值以上时的断路器行为 `Open when current crosses zero after vT >= Threshold`（默认） | `Open when vT >= Threshold`

当控制端口 **vT** 处的值大于或等于 **Threshold** 参数的值时的断路器行为。断路器既可以在电压升至阈值以上时立即断开，也可以在其电流也过零时断开。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

单极单掷断路器

Circuit Breaker 模块对单相断路器进行建模，该断路器使用外部信号和相电流信息来断开电路。

下表显示了外部信号 **vT** 和 **Breaker Behavior** 参数如何控制模块行为。

| 条件 | | 模块行为 | 使用的电阻参数 |
| --- | --- | --- | --- |
| **vT** < **Threshold** | | 断路器闭合。端口 **1** 连接到端口 **2**。 | **Closed Resistance** |
| **vT** ≥**Threshold** | `Open when current crosses zero after vT >= Threshold` | 当端口 **1** 中的电流过零时，相线与端口 **2** 断开。断路器断开。 | **Open Conductance** |
| `Open when vT >= Threshold` | 断路器断开。 |
