---
type: simulink-block
title: 'Array of Electrical Nodes Connector'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Connectors'
documentation_page: 'arrayofelectricalnodesconnector'
documentation_source_path: 'ref/arrayofelectricalnodesconnector.html'
language: zh-CN
chinese_source: worker-translation
---

# Array of Electrical Nodes Connector

## 端口

### 守恒

### **inConnk** — 要拼接的电气节点数组 *k*，电气节点数组

要拼接的电气节点数组 *k*，其中 *k* 是范围为 [1, **输入连接数**] 的整数。此类型的端口数等于您为 **输入连接数** 参数设置的值。

### **outConn** — 拼接后的电气节点数组，电气节点数组

拼接后的电气节点数组。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条上的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### **输入连接数** — 要拼接的电气节点数组数 `one`（默认）| `two` | `three` | `four` | ...

要拼接的电气节点数组数。您可以指定 `one` 和 `fifty` 之间的任意值。

### **节点 k 中的元素数** — 连接节点 *k* 中的元素数 `1`（默认）

连接节点 *k* 中的元素数，其中 *k* 是范围为 [1, **输入连接数**] 的整数。此类参数的数量等于您为 **输入连接数** 参数设置的值。

## 所属库

Simscape / Battery / Connectors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：将被移除

Array of Electrical Nodes Connector 模块将在未来版本中移除。请改用 Array Connection 模块。

## 描述

（将被移除）将电气节点数组拼接为单个电气节点数组端口

Array of Electrical Nodes Connector 模块将不同的电气节点数组拼接为单个电气节点数组。此模块通过将所有输入节点数组拼接为单个一维数组，充当 Simscape™ 电气域的 mux。

要指定要拼接的电气节点数组数，请设置 **输入连接数** 参数。此操作会启用与 **输入连接数** 参数值相等的端口数和参数数。此模块支持来自具有不同 `ElectricalNodes` 属性的不同电池模块的 1 到 50 个不同连接。

要指定每个连接节点中的元素数，请设置 **节点 k 中的元素数** 参数，其中 *k* 是范围为 [1, **输入连接数**] 的整数。
