---
type: simulink-block
title: 'Delta-Connected Variable Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / RLC Assemblies'
documentation_page: 'deltaconnectedvariableload'
documentation_source_path: 'ref/deltaconnectedvariableload.html'
language: zh-CN
chinese_source: worker-translation
---

# Delta-Connected Variable Load

## 端口

### 输入

### **P** — 有功功率物理信号

与有功功率关联的物理信号输入端口。
### 守恒

### **~** — 三相端口电气

可扩展三相
电气守恒端口。

## 参数

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各个相。

### **Rated voltage** — 额定线电压 `24e3` `V`（默认）| 正标量

用于电阻方程的额定线电压有效值。

### **Minimum real power** — 最小有功功率 `1e3` `W`（默认）| 正标量

三相负载在额定电压供电时消耗的最小有功功率。该值必须大于 0。

## 所属库

Simscape / Electrical / Passive / RLC Assemblies

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

采用三角形配置接线的三相可变负载

Delta-Connected Variable Load 模块对采用三角形配置接线的三相可变负载进行建模。负载的每一支路包含一个电阻。该模块计算在您指定的额定电压下抽取物理信号输入 **P** 的有功功率所需的电阻。因此，该模块可以表示有功负载。

为确保电阻始终大于零，您需要指定负载消耗的最小有功功率。最小有功功率必须大于零。

### 方程

电阻定义为

R=3VRated2P，

其中：

- *R* 是每相串联电阻。
- *VRated* 是额定线电压的有效值。
- *P* 是所需的三相有功功率。如果 **P** 输入端口的值小于 **Minimum real power** 参数的值，则该模块使用最小有功功率来计算电阻。
