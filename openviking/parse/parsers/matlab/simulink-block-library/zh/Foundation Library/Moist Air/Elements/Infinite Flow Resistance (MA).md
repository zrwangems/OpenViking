---
type: simulink-block
title: 'Infinite Flow Resistance (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'infiniteflowresistancema'
documentation_source_path: 'ref/infiniteflowresistancema.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (MA)

## 端口
```yaml
ports:
- name: A
  summary: 质量流量和能量流量均为零的湿空气
  direction: conserving
- name: B
  summary: 质量流量和能量流量均为零的湿空气
  direction: conserving
```

### 守恒端口

### **A** — 质量流量和能量流量均为零的湿空气

湿空气守恒端口，其中质量流量和能量流量均等于零。

### **B** — 质量流量和能量流量均为零的湿空气

湿空气守恒端口，其中质量流量和能量流量均等于零。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

湿空气网络中的完全隔热断口

Infinite Flow Resistance (MA) 模块表示湿空气网络中的一个断口。没有质量或能量流过该断口。然而，连接到回路的 Moist Air Properties (MA) 模块所指定的湿空气属性在断口两侧是相同的。使用此模块可设置端口 **A** 和端口 **B** 之间压力、温度、比湿度和示踪气体质量分数差的优先级和初始目标值。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables 和 Initial Conditions for Blocks with Finite Moist Air Volume。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
