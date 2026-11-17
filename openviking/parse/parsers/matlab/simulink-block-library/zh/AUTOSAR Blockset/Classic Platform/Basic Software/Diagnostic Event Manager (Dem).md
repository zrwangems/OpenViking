---
type: simulink-block
title: 'Diagnostic Service Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software'
documentation_page: 'diagnosticservicecomponent'
documentation_source_path: 'ref/diagnosticservicecomponent.html'
language: zh-CN
chinese_source: worker-translation
---

# Diagnostic Service Component

## 端口

R2025b 中未记录。

## 参数

### **ID (RTE 选项卡)** — 用于标识服务事件、操作循环或带抑制条件的函数的 ID 1（默认值）| 标量

RTE 选项卡表格中的每一行表示从基础软件调用方模块对 Dem 或 FiM 服务的一次调用。检查事件、操作循环和带抑制条件的函数的 ID 映射。对于事件，作用于同一事件的调用使用相同的事件 ID。有关将 Dem 客户端端口映射到共享事件 ID 的示例，请参阅 Simulate AUTOSAR Basic Software Services and Run-Time Environment。

### **Increment step size** — 当 PREFAIL 事件到达时递增事件 ID 计数器的固定步长值 1（默认值）| 标量（1 到 32767）

指定当 PREFAIL 事件到达时 Dem 事件 ID 计数器递增的固定步长值。

### **Decrement step size** — 当 PREPASS 事件到达时递减事件 ID 计数器的固定步长值 1（默认值）| 标量（1 到 32767）

指定当 PREPASS 事件到达时 Dem 事件 ID 计数器递减的固定步长值。

### **Failed threshold** — 表示失败状态的 Dem 事件 ID 计数器阈值 2（默认值）| 标量（1 到 32767）

指定表示失败状态的 Dem 事件 ID 计数器阈值。达到此阈值的事件被视为已失败。

### **Passed threshold** — 表示通过状态的 Dem 事件 ID 计数器阈值 -1（默认值）| 标量（-32768 到 -1）

指定表示通过状态的 Dem 事件 ID 计数器阈值。达到此阈值的事件被视为已通过。

### **ID (FiM 选项卡)** — 抑制条件 ID 1（默认值）| 标量

在 FiM 选项卡表格中，分组在某个 FID 下的每一行表示一个抑制条件，包含一个 ID、一个或多个与该 ID 关联的组件客户端端口以及一个掩码。对于每个抑制条件，您可以修改 ID 值。有关抑制条件配置的示例，请参阅 Configure and Simulate AUTOSAR Function Inhibition Service Calls。

### **Mask** — 抑制条件掩码 LAST\_FAILED | NOT\_TESTED | TESTED | TESTED\_AND\_FAILED

在 FiM 选项卡表格中，分组在某个 FID 下的每一行表示一个抑制条件，包含一个 ID、一个或多个与该 ID 关联的组件客户端端口以及一个掩码。对于每个抑制条件，您可以修改掩码值。有关抑制条件配置的示例，请参阅 Configure and Simulate AUTOSAR Function Inhibition Service Calls。

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

为仿真配置 AUTOSAR 诊断服务和运行时环境 (RTE)

Diagnostic Service Component 模块提供了 AUTOSAR 基础软件 (BSW) 调用方模块所支持的诊断事件管理器 (Dem) 和函数抑制管理器 (FiM) 服务的参考实现。当与 Dem 和 FiM 调用方模块配合使用时，这些参考实现使您能够配置并运行 AUTOSAR Dem 和 FiM 服务调用的系统级或组合级仿真。

该模块具有预填充的参数，包括 RTE 服务 ID 参数、Dem **Counter-Based Debouncing** 参数和 FiM 抑制条件参数。检查参数设置，如有必要，根据您使用 Dem 或 FiM 服务操作的方式进行调整。

RTE 选项卡列出了组件客户端端口及其到事件、操作循环或带抑制条件的函数的 Dem 或 FiM 服务 ID 的映射。表格中的每一行表示从基础软件调用方模块对 Dem 或 FiM 服务的一次调用，您可以修改其 ID 值。

Dem 选项卡的 **Counter-Based Debouncing** 参数控制 Dem 服务参考实现所提供的基于计数器的去抖算法。在多次仿真过程中，您可以调整事件步长和阈值参数并观察其效果。

使用基于计数器的去抖参数来确定受监控事件何时通过或失败。对于每个事件 ID，软件维护一个计数器。当 PREFAIL 事件到达时，事件 ID 计数器按 **Increment step size**（默认值 1）递增。当 PREPASS 事件到达时，事件 ID 计数器按 **Decrement step size**（默认值 1）递减。要确定事件失败或通过时的事件 ID 计数器阈值，请使用模块参数 **Failed threshold**（默认值 2）和 **Passed threshold**（默认值 -1）。

在 Dem 参考实现中，步长和阈值参数全局应用于事件 ID，而不是应用于单个 ID。

FIM 选项卡列出了函数标识符 (FID) 及其关联的抑制条件和客户端端口。该选项卡提供了图形控件，用于为选定的 FID 添加或移除抑制条件。对于每个抑制条件，选择 ID 和掩码值。
