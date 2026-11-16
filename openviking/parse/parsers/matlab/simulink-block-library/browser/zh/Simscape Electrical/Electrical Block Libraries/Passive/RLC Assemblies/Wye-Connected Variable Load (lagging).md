---
type: simulink-block
title: 'Wye-Connected Variable Load (lagging)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / RLC Assemblies'
documentation_page: 'wyeconnectedvariableloadlagging'
documentation_source_path: 'ref/wyeconnectedvariableloadlagging.html'
language: zh-CN
chinese_source: worker-translation
---

# Wye-Connected Variable Load (lagging)

## 端口

### 输入

### **P** — 有功功率物理信号

与有功功率相关联的物理信号输入端口。

### **Q** — 无功功率物理信号

与无功功率相关联的物理信号输入端口。

### 守恒

### **~** — 三相端口电气

可扩展三相
电气守恒端口。

### **n** — 中性相电气

与中性相相关联的电气守恒端口。

## 参数

### **Modeling option** — 是否对复合或展开的三相端口进行建模 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是否对复合或展开的三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图相对应的模型。

展开三相端口使用三个独立的电气守恒端口表示三相系统的各个相。

### 主要

### **Rated voltage** — 额定线电压 `24e3` `V`（默认）

用于电阻方程的 RMS 额定线电压。

### **Rated electrical frequency** — 标称交流电气频率 `60` `Hz`（默认）

用于电感方程的标称交流电气频率。

### **Minimum real power** — 最小有功功率 `1e3` `W`（默认） | positive scalar

三相负载在额定电压下供电时耗散的最小有功功率。该值必须大于 0。

### **Minimum reactive power** — 最小无功功率 `1e3` `V*A`（默认） | positive scalar

三相负载在额定电压下供电时耗散的最小无功功率。该值必须大于 0。

### 寄生

### **Parasitic parallel conductance** — 寄生并联电导 `1e-6` `1/Ohm`（默认）

模块并联添加到串联 RL 的电导。

## 所属库

Simscape / Electrical / Passive / RLC Assemblies

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

采用星形配置接线的三相可变滞后负载

Wye-Connected Variable Load (lagging) 模块模拟采用星形配置接线的三相可变滞后负载。负载的每个分支包含一个串联连接的电阻器 (R) 和一个电感器 (L)。该模块计算在您指定的额定电压和额定频率下，汲取物理信号输入 P 和 Q 的有功功率和无功功率所需的电阻和电感。因此，该模块可以表示有功和滞后无功负载。

为确保电阻和电感始终大于零，您需要指定负载消耗的最小有功功率和无功功率。最小有功功率和无功功率必须大于零。

### 电气定义方程

每相串联电阻和电感定义为

R=PVRated2P2+Q2

以及

L=QVRated22πFRated(P2+Q2),

其中：

- *R* 是每相串联电阻。
- *L* 是每相串联电感。
- *VRated* 是 RMS，额定
  线电压。
- *FRated* 是标称交流
  电气频率。
- *P* 是所需的三相有功功率。
- *Q* 是所需的三相滞后无功功率。

电感定义为磁通量 φ 与稳态电流之比：

L(i)=ϕ(i)i.

因此，电感器的电流-电压关系为：

v=dLdti+Ldidt.

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
