---
type: simulink-block
title: 'Array of Thermal Nodes Connector'
family: 'thermal'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Thermal'
documentation_page: 'arrayofthermalnodesconnector'
documentation_source_path: 'ref/arrayofthermalnodesconnector.html'
language: zh-CN
chinese_source: worker-translation
---

# Array of Thermal Nodes Connector

## 端口

### 守恒

### **inConnk** — 要拼接为 thermal array-of-nodes 的热节点数组 *k*

要拼接的热节点数组 *k*，其中 *k* 是范围 [1,
**Number of Input Connections**] 内的整数。此类端口的数量等于将
**Number of Input Connections** 参数设置的值。

### **outConn** — 拼接后的热节点数组，thermal array-of-nodes

拼接后的热节点数组。

## 参数

### **Number of Input Connections** — 要拼接的热节点数组的数量 `one`（默认） | `two` | `three` | `four` | ...

要拼接的热节点数组的数量。可以指定 `one` 和
`fifty` 之间的任意值。

### **Concatenate dimension** — 沿其拼接输入数组的输出维度 `2`（默认） | positive scalar

*自 R2024b 起*

指定沿其拼接输入数组的输出维度：

- `1` — 垂直拼接输入。垂直数组拼接将输入数组在输出数组中彼此堆叠。
- `2` — 水平拼接输入。水平数组拼接将输入数组在输出数组中并排放置。
- `3` 或更大 — 对输入执行多维拼接。

输入数组必须具有兼容的大小才能拼接。垂直拼接要求输入数组具有相同的列数。
水平拼接要求输入数组具有相同的行数。多维拼接要求输入数组的所有维度大小相同，
但沿其拼接的维度除外。

### **Size of complementary dimensions** — 除拼接维度外所有输入数组的维度大小 `2`（默认） | positive scalar

*自 R2024b 起*

除拼接维度外，所有输入数组的维度大小。

例如，如果模块沿第二个维度拼接一个大小为 `[3,4,5]` 的热节点数组和另一个大小为
`[3,1,5]` 的热节点数组，则必须将此参数设置为 `[3,5]`，因为第二个维度是
拼接维度。

### **Size of concatenate dimension for Node k** — 连接节点 *k* 中的元素数量 `1`（默认）

连接节点 *k* 中的元素数量，其中
*k* 是范围 [1, **Number of
Input Connections**] 内的整数。此类参数的数量
等于将 **Number of Input
Connections** 参数设置的值。

## 所属库

Simscape / Battery / Thermal

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a: 将删除

Array of Thermal Nodes Connector 模块将在未来版本中删除。
请改用 Array
Connection 模块。

### R2024b: 水平或多维拼接数组

现在可以执行热节点数组的水平拼接和多维拼接。

要水平拼接输入，请将 **Concatenate
dimension** 参数设置为 `2`。要执行
多维拼接，请将 **Concatenate dimension**
参数设置为 `3` 或更大。拼接要求输入
数组的所有维度大小相同，但沿其拼接的维度除外。

## 描述

（将删除）将热节点数组拼接为单个热节点数组端口

Array of Thermal Nodes Connector 模块将
不同的热节点数组拼接为单个热节点数组。此模块
充当 Simscape™ 热域的 mux，将所有输入节点数组拼接为单个
指定维度的数组。

要指定要拼接的热节点数组的数量，请设置
**Number of Input Connections** 参数。此操作会启用
与 **Number of Input
Connections** 参数值相等的端口和参数数量。此模块支持从 1 到 50 个
来自具有不同 `ThermalNodes` 属性的不同电池模块的不同连接。

要指定每个连接节点中的元素数量，请设置 **Size of
concatenate dimension for Node k** 参数，其中 *k* 是
范围 [1, **Number of Input Connections**] 内的整数。
