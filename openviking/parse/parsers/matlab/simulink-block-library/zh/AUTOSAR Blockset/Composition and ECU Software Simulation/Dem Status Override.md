---
type: simulink-block
title: 'Dem Status Override'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Composition and ECU Software Simulation'
documentation_page: 'demstatusoverride'
documentation_source_path: 'ref/demstatusoverride.html'
language: zh-CN
chinese_source: worker-translation
---

# Dem Status Override

## 端口

R2025b 中未记录。

## 参数

### **EventID** — 指定事件 0（默认）| integer

指定要通过此模块覆盖的 AUTOSAR 事件。

#### 编程使用

|  |
| --- |
| **模块参数：** `EventId` |
| **类型：** integer |
| **值：** 0 | integer |
| **默认值：** `0` |

### **Test Failed** — 指示最近执行的测试的结果 `Clear`（默认）| `Set`

上次检查时测试失败。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

### **Test Failed this Operation Cycle** — 指示诊断测试在当前操作循环期间是否报告了失败 `Clear`（默认）| `Set`

在当前操作循环期间测试失败。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

### **Pending DTC** — 指示诊断测试在当前或上次完成的操作循环期间是否报告了失败 `Clear`（默认）| `Set`

在当前或上一个操作循环期间测试失败。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

### **Confirmed DTC** — 指示是否检测到故障足够多次，以证明该 DTC 应存储在长期存储器中 `Clear`（默认）| `Set`

在请求时确认测试失败。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

### **Test Not Completed Since Last Clear** — 指示自上次调用 `ClearDiagnosticInformation` 以来测试是否已运行并完成 `Clear`（默认）| `Set`

自上次代码清除以来未执行测试。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

### **Test Failed Since Last Clear** — 指示自上次调用 `ClearDiagnosticInformation` 以来测试是否已失败 `Clear`（默认）| `Set`

自上次代码清除以来测试至少失败过一次。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

### **Test Not Completed This Operation Cycle** — 当前操作循环期间未执行测试 `Clear`（默认）| `Set`

在此操作循环期间测试未完成。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

### **Warning Indicator Requested** — 指示与特定 DTC 关联的任何警告指示器的状态 `Clear`（默认）| `Set`

测试失败严重到足以向服务器发出警报。

要设置此属性，请选择 `Dialog` 以手动配置状态，或选择 `Input port` 以根据所连接输入的行为动态配置状态。

## 所属库

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

覆盖事件以仿真并验证行为

Dem Status Override 模块可配置为设置 Diagnostic Service Component 模块中仿真的 AUTOSAR 事件的诊断状态。此状态值可根据统一诊断服务 (UDS) 标准进行配置。具体而言，无论模型中其他事件的行为如何，您都可以使用此模块为特定事件设置 `GetEventStatus` 调用的返回值。在仿真期间尝试修改事件状态的其他模块将被忽略。此模块为测试特定行为提供了一个可预测的入口点，您可以将此作为一种低成本方法，快速获得组件模型的覆盖。
