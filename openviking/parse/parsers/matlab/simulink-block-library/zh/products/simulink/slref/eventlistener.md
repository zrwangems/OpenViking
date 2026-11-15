---
type: simulink-block
title: 'Event Listener'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Event Functions'
documentation_page: 'eventlistener'
documentation_source_path: 'slref/eventlistener.html'
language: zh-CN
chinese_source: official
---

# Event Listener

## 端口

R2025b 官方文档未提供。

## 参数

### **事件类型** — 选择子系统的事件类型 **初始化** (默认) | **重新初始化** | **重置** | **终止**

选择子系统执行初始化、重新初始化、重置或终止算法的事件类型。

**初始化**
:   选择通过初始化事件触发 Initialize Function 模块的执行。

**重新初始化**
:   选择通过重新初始化事件触发 Reinitialize Function 模块的执行。

**重置**
:   选择通过重置事件触发 Reset Function 模块的执行。

**终止**
:   选择通过终止事件触发 Terminate Function 模块的执行。

#### 编程用法

|  |
| --- |
| **模块参数**：`EventType` |
| **类型：**字符向量 |
| **值**：`'Initialize'` | `'Reinitialize'` | `'Reset'` | `'Terminate'` |
| **默认值：**`'Initialize'` |

### **事件名称** — 指定事件名称 `reinit` | `reset` | 事件名称

为 Reinitialize Function 或 Reset Function 模块指定事件名称。Simulink® 在 Reinitialize Function 或 Reset Function 模块的表面上显示名称。该事件名称也是包含 Reinitialize Function 模块的 Model 或 Subsystem 模块上的重新初始化事件端口的名称，或者包含 Reset Function 模块的 Model 模块上的重置事件端口的名称。

`reinit`
:   当**事件类型**设置为**重新初始化**时的默认事件名称。

`reset`
:   当**事件类型**设置为**重置**时的默认事件名称。

输入**事件名称**时，自动完成列表会提供一些建议。该列表不完整。

**事件名称**必须是有效的 MATLAB® 变量名。

#### 依赖关系

要启用此参数，请将**事件类型**参数设置为**重新初始化**或**重置**。

#### 编程用法

|  |
| --- |
| **模块参数**：`EventName` |
| **类型：**字符向量 |
| **值：**`'reinit'` | `'reset'` | `'<event name>'` |
| **默认值：**`'reinit'` 或 `'reset'` |

### **启用变体条件** — 控制激活变体控制（条件） off (默认) | on

控制激活使用**变体控制**参数定义的变体控制（条件）。

off
:   停用子系统的变体控制。

on
:   激活子系统的变体控制。

当您选择**启用变体条件**时，会有一个标记指示更改：

#### 编程用法

|  |
| --- |
| **模块参数**：`Variant` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

**注意**

- Model 或 Subsystem 模块的重新初始化事件端口可以是有条件的，并传播在引用模型或子系统中相应的 Reinitialize Function 模块上定义的网络变体条件。
- Model 模块的重置事件端口可以是有条件的，并传播在引用模型中相应的 Reset Function 模块上定义的网络变体条件。
- 初始化和终止事件端口始终是无条件的，因为它们控制引用模型的模型默认和模块特定的初始化和终止事件。如果在引用模型中定义 Initialize Function 模块，它对应于显式初始化事件。

### **变体控制项** — 指定变体控制项（条件）表达式 `Variant` (默认) | 逻辑表达式

指定变体控制（条件）表达式，当表达式计算结果为 `true` 时，执行变体 Initialize Function、Reinitialize Function、Reset Function 或 Terminate Function 模块。

`Variant`
:   逻辑（布尔）表达式的默认名称。

逻辑表达式
:   逻辑（布尔）表达式或表示布尔表达式的 `Simulink.VariantExpression` 对象。

    如果要为模型生成代码，请将表达式中的变量定义为 `Simulink.Parameter` 对象。

#### 依赖关系

要启用此参数，请选择**启用变体条件**参数。

#### 编程用法

|  |
| --- |
| **模块参数**：`VariantControl` |
| **类型：**字符向量 |
| **值：**`'Variant'` | `'<logical expression>'` |
| **默认值：**`'Variant'` |

### **生成预处理器条件句** — 如果变体选择项包含在 C 预处理器条件语句中，则选择 off (默认) | on

如果变体选择项包含在 C 预处理器条件语句中，则选择。

off
:   不要将变体选择项包括在 C 预处理器条件语句中。

on
:   为 ERT 目标生成代码时，将变体选择项包括在 C 预处理器条件语句 (`#if`) 中。

#### 依赖关系

要启用此参数，请选择**启用变体条件**参数。

当您选择**生成预处理器条件**时，会出现一个标记来指示更改：

#### 编程用法

|  |
| --- |
| **模块参数**：`GeneratePreprocessorConditionals` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

### R2025a: 支持封装工作区和模型工作区中的变体控制项变量

您可以在封装和模型工作区中定义变体控制变量来控制 Initialize Function、Reset Function、Reinitialize Function 和 Terminate Function 模块中的活动变体，前提是**生成预处理器条件**参数为 `off`。

## 描述

初始化函数、重新初始化函数、重置函数和 Terminate Function 模块的事件端口

Event Listener 模块作为 Initialize Function、Reinitialize Function、Reset Function 和 Terminate Function 模块的事件端口。
