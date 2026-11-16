---
type: simulink-block
title: 'Dem Status Inject'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'demstatusinject'
documentation_source_path: 'ref/demstatusinject.html'
language: zh-CN
chinese_source: worker-translation
---

# Dem Status Inject

## 端口

R2025b 中未记录。

## 参数

### **EventID** — 指定事件 0（默认）| integer

指定要使用此模块覆盖的 AUTOSAR 事件。

#### 编程用法

|  |
| --- |
| **模块参数：** `EventId` |
| **类型：** integer |
| **值：** 0 | integer |
| **默认值：** `0` |

### **Fault type** — 指定故障类型 `Event Fail`（默认）| `Event Pass` | `Operation Cycle Start` | `Operation Cycle End` | `Fault Record Overwritten` | `Fault Maturation` | `Clear Diagnostic` | `Aging` | `Healing` | `Indicator Conditions Met`

指定要注入系统的诊断事件类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `FaultType` |
| **类型：** character vector |
| **值：** `'Event Fail' | 'Event Pass' | 'Operation Cycle Start' | 'Operation Cycle End' | 'Fault Record Overwritten' | 'Fault Maturation' | 'Clear Diagnostic' | 'Aging' | 'Healing' | 'Indicator Conditions Met'` |
| **默认值：** `'Event Fail'` |

### **Trigger type** — 指定注入条件 `rising`（默认）| `falling` | `either` | `function-call`

指定何时将诊断事件注入系统。

#### 编程用法

|  |
| --- |
| **模块参数：** `InjectTriggerType` |
| **类型：** character vector |
| **值：** `'rising' | 'falling' | 'either' | 'function-call'` |
| **默认值：** `'rising'` |

### **Test Failed** — 指示最近执行的测试的结果 `Clear`（默认）| `Set`

上次检查时测试失败。

此只读属性由 **Fault type** 设置。

### **Test Failed this Operation Cycle** — 指示诊断测试在当前操作周期内是否报告了失败 `Clear`（默认）| `Set`

在当前操作周期内测试失败。

此只读属性由 **Fault type** 设置。

### **Pending DTC** — 指示诊断测试在当前或上一个完成的操作周期内是否报告了失败 `Clear`（默认）| `Set`

在当前或上一个操作周期内测试失败。

此只读属性由 **Fault type** 设置。

### **Confirmed DTC** — 指示故障被检测到的次数是否足以使 DTC 应存储在长期内存中 `Clear`（默认）| `Set`

在请求时确认测试失败。

此只读属性由 **Fault type** 设置。

### **Test Not Complete Since Last Clear** — 指示自上次调用 `ClearDiagnosticInformation` 以来测试是否已运行并完成 `Clear`（默认）| `Set`

自上次清除代码以来未执行测试。

此只读属性由 **Fault type** 设置。

### **Test Failed Since Last Clear** — 指示自上次调用 `ClearDiagnosticInformation` 以来测试是否已失败 `Clear`（默认）| `Set`

自上次清除代码以来测试至少失败一次。

此只读属性由 **Fault type** 设置。

### **Test Not Complete This Operation Cycle** — 当前操作周期内未执行测试 `Clear`（默认）| `Set`

在此操作周期内测试未完成。

此只读属性由 **Fault type** 设置。

### **Warning Indicator Requested** — 指示与特定 DTC 关联的任何警告指示器的状态 `Clear`（默认）| `Set`

测试失败非常严重，以致于向服务器发出警报。

此只读属性由 **Fault type** 设置。

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

注入事件失败以测试恢复

Dem Status Inject 模块可配置为即时设置 Diagnostic Service Component 模块中仿真的 AUTOSAR 事件的诊断状态。此状态值可根据 Unified Diagnostic Services (UDS) 标准进行配置。具体而言，您可以使用此模块将瞬态故障注入系统，以测试其恢复能力。此模块模拟并响应影响其状态的其他模块，以显示系统恢复。
