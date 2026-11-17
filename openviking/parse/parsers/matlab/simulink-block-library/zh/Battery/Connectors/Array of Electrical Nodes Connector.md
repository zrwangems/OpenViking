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
```yaml
ports:
- name: inConnk
  summary: 要连接为电气节点数组的电气节点数组 *k*
  direction: unspecified
- name: outConn
  summary: 连接后的电气节点数组 电气节点数组
  direction: unspecified
```

### 守恒

### **inConnk** — 要连接为电气节点数组的电气节点数组 *k*

要连接的电气节点数组 *k*，其中 *k* 是范围 [1, **Number of Input Connections**] 内的整数。此类型端口的数量等于 **Number of Input Connections** 参数设置的值。

### **outConn** — 连接后的电气节点数组 电气节点数组

连接后的电气节点数组。
## 参数
```yaml
parameters:
- name: Number of Input Connections
  summary: 要连接的电气节点数组的数量 one（默认）| two | three | four | ...
  group: ''
- name: Number of Elements in Node k
  summary: 连接节点 *k* 中的元素数量 1（默认）
  group: ''
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Number of Input Connections** — 要连接的电气节点数组的数量 `one`（默认）| `two` | `three` | `four` | ...

要连接的电气节点数组的数量。您可以指定 `one` 到 `fifty` 之间的任意值。

### **Number of Elements in Node k** — 连接节点 *k* 中的元素数量 `1`（默认）

连接节点 *k* 中的元素数量，其中 *k* 是范围 [1, **Number of Input Connections**] 内的整数。此类型参数的数量等于 **Number of Input Connections** 参数设置的值。
## 所属库

Simscape / Battery / Connectors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：将被移除

Array of Electrical Nodes Connector 模块将在未来版本中移除。请改用 Array Connection 模块。

## 描述

（将被移除）将电气节点数组连接为单个电气节点数组端口

Array of Electrical Nodes Connector 模块将不同的电气节点数组连接为单个电气节点数组。此模块充当 Simscape™ 电气域的 mux，将所有输入节点数组连接为单个一维数组。

要指定要连接的电气节点数组的数量，请设置 **Number of Input Connections** 参数。此操作会启用与 **Number of Input Connections** 参数值相等的端口和参数数量。此模块支持来自具有不同 `ElectricalNodes` 属性的不同电池模块的一到 50 个不同连接。

要指定每个连接节点中的元素数量，请设置 **Number of Elements in Node k** 参数，其中 *k* 是范围 [1, **Number of Input Connections**] 内的整数。
