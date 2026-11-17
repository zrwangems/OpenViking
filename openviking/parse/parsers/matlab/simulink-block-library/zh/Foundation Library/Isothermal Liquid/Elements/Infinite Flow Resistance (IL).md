---
type: simulink-block
title: 'Infinite Flow Resistance (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'infiniteflowresistanceil'
documentation_source_path: 'ref/infiniteflowresistanceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (IL)

## 端口
```yaml
ports:
- name: A
  summary: 流量为零的等温液体
  direction: unspecified
- name: B
  summary: 流量为零的等温液体
  direction: unspecified
```

### 守恒

### **A** — 流量为零的等温液体

无流体流动的等温液体守恒端口。

### **B** — 流量为零的等温液体

无流体流动的等温液体守恒端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

用于设置两个节点之间初始压力差的等温液体元件

Infinite Flow Resistance (IL) 模块表示等温液体网络中的一个断点。没有液体流过该断点。但是，由连接到回路的 Isothermal Liquid Properties (IL) 模块指定的液体属性在断点两侧是相同的。使用此模块可将优先级和初始目标值设置为端口 **A** 和端口 **B** 之间的压力差。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
