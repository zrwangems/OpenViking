---
type: simulink-block
title: 'SPMT Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'spmtswitch'
documentation_source_path: 'ref/spmtswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# SPMT Switch

## 端口

### 输入

### **vT** — 开关控制端口物理信号

用于打开和关闭开关的信号，指定为物理信号。
### 守恒

### **p** — 公共端口电气

与公共极关联的电气守恒端口。

### **n1** — 掷端口 1 电气

与第一掷关联的电气守恒端口。

### **n2** — 掷端口 2 电气

与第二掷关联的电气守恒端口。

### **n3** — 掷端口 3 电气

与第三掷关联的电气守恒端口。

### **n4** — 掷端口 4 电气

与第四掷关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of throw ports** 设置为
`4`、`5`、
`6`、`7` 或
`8`。

### **n5** — 掷端口 5 电气

与第五掷关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of throw
ports** 设置为 `5`、
`6`、`7` 或
`8`。

### **n6** — 掷端口 6 电气

与第六掷关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of throw
ports** 设置为 `6`、
`7` 或
`8`。

### **n7** — 掷端口 7 电气

与第七掷关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of throw
ports** 设置为 `7` 或
`8`。

### **n8** — 掷端口 8 电气

与第八掷关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of throw
ports** 设置为 `8`。

## 参数

### 主要

### **Number of throw ports** — Number of throw ports `4`（默认） | `3` | `5` | `6` | `7` | `8`

掷连接的数量。

### **Closed resistance** — Closed resistance `0.01` `Ohm`（默认） | 正标量

当开关闭合时，**p** 端口和掷端口之间的电阻。该值必须大于零。

### **Open conductance** — Open conductance `1e-6` `S`（默认） | 正标量

当开关断开时，**p** 端口和掷端口之间的电导。该值必须大于零。

### 故障

### **Stuck throw fault** — 添加卡掷故障的选项 `Add fault`（默认）

在 SPMT Switch 模块中添加卡掷故障的选项。

要添加故障，请点击 **Add fault**
超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认） | 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Timed`。

### **Maximum permissible common port current** — Maximum permissible common port current `inf` `A`（默认） | 正标量

允许流过公共端口的最大电流，超过此值可能触发故障。

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **Time to fail when exceeding current** — Time to fail when exceeding current `1` `s`（默认） | 正标量

公共端口电流必须持续超过最大允许电流多长时间，才会触发行为故障。

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

单刀多掷开关

SPMT Switch 模块对单刀多掷开关进行建模。您可以通过将 **Number
of throw ports** 参数设置为所需数量来指定三到八个掷连接。如果只需要一个或两个掷端口，请参阅 SPST Switch 和 SPDT Switch 模块。

开关控制端口物理信号 **vT** 指定哪个掷端口连接到极：

- 当 **vT** 在 `[-inf, 1.5]`
  范围内时，极始终连接到掷端口 1，
  **n1**。
- 当 **vT** 在一和掷端口数量之间时，
  信号值四舍五入到最接近的整数。然后极连接到
  与该整数值对应的掷端口。
- 当 **vT** 高于掷端口数量时，
  极始终连接到最后一个掷端口。

断开连接由电阻建模，其值等于 **Open conductance** 参数值的倒数。闭合连接由电阻建模，其值等于 **Closed resistance**
参数值。

### 故障

要在 SPMT Switch 模块中对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。
