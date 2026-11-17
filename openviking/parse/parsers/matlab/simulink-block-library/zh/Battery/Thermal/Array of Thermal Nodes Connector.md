---
type: simulink-block
title: 'Array of Thermal Nodes Connector'
family: 'simscape-battery'
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
```yaml
ports:
- name: inConnk
  summary: 要串联到 thermal array-of-nodes 的 thermal nodes 数组 *k*
  direction: conserving
- name: outConn
  summary: 串联后的 thermal nodes 数组 thermal array-of-nodes
  direction: conserving
```

### 守恒端口

### **inConnk** — 要串联到 thermal array-of-nodes 的 thermal nodes 数组 *k*

要串联的 thermal nodes 数组 *k*，其中 *k* 是范围 [1, **Number of Input Connections**] 内的整数。此类型端口的数量等于 **Number of Input Connections** 参数设置的值。

### **outConn** — 串联后的 thermal nodes 数组 thermal array-of-nodes

串联后的 thermal nodes 数组。
## 参数
```yaml
parameters:
- name: Number of Input Connections
  summary: 要串联的 thermal nodes 数组的数量 one（默认）| two | three | four | ...
  group: ''
- name: Concatenate dimension
  summary: 沿其串联输入数组的输出维度 2（默认）| 正标量
  group: ''
- name: Size of complementary dimensions
  summary: 所有输入数组中除串联维度外的维度大小 2（默认）| 正标量
  group: ''
- name: Size of concatenate dimension for Node k
  summary: 连接节点 *k* 中的元素数量 1（默认）
  group: ''
```

### **Number of Input Connections** — 要串联的 thermal nodes 数组的数量 `one`（默认）| `two` | `three` | `four` | ...

要串联的 thermal nodes 数组的数量。可以指定 `one` 到 `fifty` 之间的任意值。

### **Concatenate dimension** — 沿其串联输入数组的输出维度 `2`（默认）| 正标量

*自 R2024b 起*

指定沿其串联输入数组的输出维度：

- `1` — 垂直串联输入。垂直数组串联将输入数组在输出数组中彼此堆叠。
- `2` — 水平串联输入。水平数组串联将输入数组在输出数组中并排放置。
- `3` 或更大 — 对输入执行多维串联。

输入数组必须具有兼容的大小才能进行串联。垂直串联要求输入数组具有相同的列数。水平串联要求输入数组具有相同的行数。多维串联要求输入数组的所有维度大小相同，但沿其串联的维度除外。

### **Size of complementary dimensions** — 所有输入数组中除串联维度外的维度大小 `2`（默认）| 正标量

*自 R2024b 起*

所有输入数组中除串联维度外的维度大小。

例如，如果该模块沿第二个维度串联一个大小为 `[3,4,5]` 的 thermal nodes 数组和另一个大小为 `[3,1,5]` 的 thermal nodes 数组，则必须将此参数设置为 `[3,5]`，因为第二个维度是串联维度。

### **Size of concatenate dimension for Node k** — 连接节点 *k* 中的元素数量 `1`（默认）

连接节点 *k* 中的元素数量，其中 *k* 是范围 [1, **Number of Input Connections**] 内的整数。此类型参数的数量等于 **Number of Input Connections** 参数设置的值。
## 所属库

Simscape / Battery / Thermal

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a：将被移除

Array of Thermal Nodes Connector 模块将在未来版本中移除。请改用 Array Connection 模块。

### R2024b：水平或多维串联数组

现在可以执行 thermal nodes 数组的水平串联和多维串联。

要水平串联输入，请将 **Concatenate dimension** 参数设置为 `2`。要执行多维串联，请将 **Concatenate dimension** 参数设置为 `3` 或更大。串联要求输入数组的所有维度大小相同，但沿其串联的维度除外。

## 描述

（将被移除）将 thermal nodes 数组串联为单个 thermal nodes 数组端口

Array of Thermal Nodes Connector 模块将不同的 thermal nodes 数组串联为单个 thermal nodes 数组。该模块充当 Simscape™ thermal 域的 mux，将所有输入节点数组串联为指定维度的单个数组。

要指定要串联的 thermal nodes 数组的数量，请设置 **Number of Input Connections** 参数。此操作会启用与 **Number of Input Connections** 参数值相等数量的端口和参数。该模块支持来自具有不同 `ThermalNodes` 属性的不同电池模块的一到 50 个不同连接。

要指定每个连接节点中的元素数量，请设置 **Size of concatenate dimension for Node k** 参数，其中 *k* 是范围 [1, **Number of Input Connections**] 内的整数。
