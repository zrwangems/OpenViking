---
type: simulink-block
title: 'Circuit Breaker (Three Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Switches and Breakers / Switches and Breakers'
documentation_page: 'circuitbreakerthreephase'
documentation_source_path: 'ref/circuitbreakerthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Circuit Breaker (Three Phase)

## 端口

### 输入

### **vT** — 标量控制端口物理信号

标量物理信号控制端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Expanded three-phase ports | PS control port` 或 `Composite three-phase ports | PS control port`。

### 守恒

### **~1** — 可扩展三相电气端口

可扩展三相电气守恒端口。

### **~2** — 可扩展三相电气端口

可扩展三相电气守恒端口。

### **+** — 正电气端口

正电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Expanded three-phase ports| Electrical control port` 或 `Composite three-phase ports| Electrical control port`。

### **-** — 负电气端口

负电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Expanded three-phase ports| Electrical control port` 或 `Composite three-phase ports| Electrical control port`。

## 参数

### **Modeling option** — 连接和门控端口 `Composite three-phase ports | PS control port`（默认）| `Composite three-phase ports| Electrical control port` | `Expanded three-phase ports | PS control port` | `Expanded three-phase ports| Electrical control port`

是否对复合或扩展三相端口以及物理信号或电气控制端口进行建模。

### **Closed resistance** — 闭合电阻 `0.001` `Ohm`（默认）

断路器闭合时端口 **~1** 和 **~2** 之间的电阻。

### **Open conductance** — 断开电导 `1e-6` `1/Ohm`（默认）

断路器断开时端口 **~1** 和 **~2** 之间的电导。

### **Threshold** — 阈值电压 `0.5` `V`（默认）

控制端口 **vT** 的阈值电压。该模块使用阈值电压和仿真开始时 **vT** 的值来确定断路器初始是断开还是闭合。如果将 **Breaker Behavior** 设置为 `Open when current crosses zero after vT >= Threshold`，则当电压升到阈值以上时，断路器在每相电流过零时断开该相。如果将 **Breaker Behavior** 设置为 `Open when vT >= Threshold`，则当电压升到阈值以上时，断路器立即断开每相。当控制端口电压降到阈值以下时，断路器闭合。

### **Breaker Behavior** — 当 *vT* 升到阈值以上时的断路器行为 `Open when current crosses zero after vT >= Threshold`（默认）| `Open when vT >= Threshold`

当控制端口 **vT** 的值大于或等于 **Threshold** 参数的值时的断路器行为。断路器既可以在电压升到阈值以上时立即断开，也可以在其电流也过零时断开。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

由外部信号控制的三相断路器

Circuit Breaker (Three-Phase) 模块对使用外部信号和相电流信息来断开电路的三相断路器进行建模。

下表显示了外部信号 **vT** 和 **Breaker Behavior** 参数如何控制模块行为。

| 条件 |  | 模块行为 | 使用的电阻参数 |
| --- | --- | --- | --- |
| **vT** < **Threshold** |  | 断路器闭合。复合三相端口 **~1** 中的每一相连接到端口 **~2** 中的对应相。 | **Closed Resistance** |
| **vT** ≥**Threshold** | `Open when current crosses zero after vT >= Threshold` | 当复合端口 **~1** 中任一相的电流过零时，该相与端口 **~2** 中的对应相断开。断路器断开。 | **Open Conductance** |
| `Open when vT >= Threshold` | 断路器断开。 |
