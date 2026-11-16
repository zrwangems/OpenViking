---
type: simulink-block
title: 'Array of Electrical Nodes'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'arrayofelectricalnodes'
documentation_source_path: 'ref/arrayofelectricalnodes.html'
language: zh-CN
chinese_source: official
---

# Array of Electrical Nodes

## 端口

### 守恒

### **inConnk** — 要串联的电气节点 *k* 数组 电气节点数组

您想要串联的电气节点 *k* 数组，其中 *k* 是 [1, **输入连接数**] 范围内的整数。此类型端口的数量等于您为**输入连接数**参数设置的值。

### **outConn** — 串联的电气节点数组 电气节点数组

串联的电气节点数组。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上的**准备**图库中，选择**属性检查器**。

### **输入连接数** — 要串联的电气节点数组的数量 **one** (默认) | **two** | **three** | **four** | ...

您想要串联的电气节点数组的数量。您可以指定 **one** 到 **fifty** 之间的任意值。

### **节点 k 中的元素数** — 连接节点 *k* 中的元素数 `1` (默认)

连接节点 *k* 中的元素数，其中 *k* 是 [1, **输入连接数**] 范围内的整数。此类型参数的数量等于您为**输入连接数**参数设置的值。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2024b 中推出**

### R2025a: 即将删除

Array of Electrical Nodes 模块将在以后的版本中删除。请改用 Array Connection 模块。

## 描述

（即将删除）将电气节点数组串联成单个电气节点数组端口

Array of Electrical Nodes 模块将不同的电气节点数组串联成单个电气节点数组。该模块通过将所有输入节点数组串联成单个一维数组来充当 Simscape™ 电气域的复路。

要指定您想要串联的电气节点数组的数量，请设置**输入连接数**参数。此操作启用的端口和参数的数量等于**输入连接数**参数的值。该模块支持 1 到 50 个来自不同电池模块的不同连接，这些电池模块具有不同的 `ElectricalNodes` 属性。

要指定每个连接节点中的元素数，请设置**节点 k 中的元素数**参数，其中 *k* 是 [1, **输入连接数**] 范围内的整数。
