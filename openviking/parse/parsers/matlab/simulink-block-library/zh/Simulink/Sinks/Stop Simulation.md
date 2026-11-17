---
type: simulink-block
title: 'Stop Simulation'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'stopsimulation'
documentation_source_path: 'slref/stopsimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# Stop Simulation

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: double | Boolean
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

当输入信号非零时停止仿真。此端口接受 `double` 或 `Boolean` 数据类型的实数信号。

**数据类型：** `double` | `Boolean`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / Sinks HDL Coder / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产代码。涉及嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化较大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会逐步演变为适合生产代码。因此，适合生产代码的模块会保持适合。

当停止条件为真时，生成的代码停止执行。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，表示未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

当输入非零时停止仿真

Stop Simulation 模块在输入非零时停止仿真。仿真在终止前完成当前时间步。如果模块输入是向量，任何非零向量元素都会导致仿真停止。

在 For Iterator 子系统（For 迭代器子系统）中使用 Stop Simulation 模块时，停止操作会在一个时间步内子系统执行*所有*迭代之后发生。停止操作不会中断执行，直到下一个时间步开始。

不能使用 Stop Simulation 模块暂停仿真。要创建一个暂停仿真的模块，请参阅 Pause Simulation Using Assertion Blocks。
