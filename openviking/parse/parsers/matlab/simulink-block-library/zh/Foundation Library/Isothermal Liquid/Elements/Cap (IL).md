---
type: simulink-block
title: 'Cap (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'capil'
documentation_source_path: 'ref/capil.html'
language: zh-CN
chinese_source: worker-translation
---

# Cap (IL)

## 端口
```yaml
ports:
- name: A
  summary: 质量流量为零的等温液体
  direction: conserving
```

### 守恒端口

### **A** — 质量流量为零的等温液体

等温液体守恒端口，其质量流量等于零。
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

**在 R2025a 中引入**

## 描述

零流量的等温液体端口终端

Cap (IL) 模块表示等温液体支路的终端。没有质量流量通过该容性终端。

您可以使用此模块来端接其他模块上您想要封盖的等温液体端口。使用此模块并非必需，因为如果您将守恒端口保持未连接状态，物理网络会将该端口处的所有 Through 变量设置为 0。但是，终端模块可以提高图表的可读性。

您还可以使用此模块来设置节点的初始压力。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可以提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
