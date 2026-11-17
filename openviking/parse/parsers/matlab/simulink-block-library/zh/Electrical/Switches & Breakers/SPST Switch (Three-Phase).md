---
type: simulink-block
title: 'SPST Switch (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'spstswitchthreephase'
documentation_source_path: 'ref/spstswitchthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# SPST Switch (Three-Phase)

## 端口

### 输入

### **vT** — 控制端口物理信号

物理控制端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Expanded three-phase ports | PS control
port` 或 `Composite three-phase ports |
PS control port`。
### 守恒

### **~1** — 可扩展三相端口电气

可扩展三相电气守恒端口。

### **~2** — 可扩展三相端口电气

可扩展三相电气守恒端口。

### **vT** — 控制端口电气

电气守恒控制端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Expanded three-phase ports| Electrical control
port` 或 `Composite three-phase ports|
Electrical control port`。

## 参数

### **Modeling option** — 连接和门控端口 `Composite three-phase ports | PS control port`（默认）| `Composite three-phase ports| Electrical control port` | `Expanded three-phase ports | PS control port` | `Expanded three-phase ports| Electrical control port`

选择对复合三相端口还是可扩展三相端口进行建模，以及使用物理信号控制端口还是电气控制端口。

### **Closed resistance** — 闭合电阻 `0.001` `Ohm`（默认）

当开关闭合时，端口 **~1** 和
**~2** 之间的电阻。

### **Open conductance** — 断开电导 `1e-6` `1/Ohm`（默认）

当开关断开时，端口 **~1** 和
**~2** 之间的电导。

### **Threshold** — 阈值 `0.5` `V`（默认）

控制端口 **vT** 的阈值电压。当电压高于阈值时，开关闭合。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

三相单刀单掷开关

SPST Switch (Three-Phase) 模块用于对三相单掷开关进行建模，该开关使用外部信号通过内部电阻将端口 **~1** 的每一相与端口 **~2** 的对应相连接。

下表显示了外部信号 *vT* 如何控制模块行为。

| 条件 | 模块行为 | 使用的电阻参数 |
| --- | --- | --- |
| *vT* ≤**Threshold** | 开关断开。复合三相端口 **~1** 中的每一相通过大内部电阻连接到端口 **~2** 中的对应相。 | **Open conductance** |
| *vT* >**Threshold** | 开关闭合。复合三相端口 **~1** 中的每一相通过小内部电阻连接到端口 **~2** 中的对应相。 | **Closed resistance** |
