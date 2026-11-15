---
type: simulink-block
title: 'Manual Switch'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualswitch'
language: zh-CN
chinese_source: official
---

# Manual Switch

## 端口

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量

Manual Switch 模块的两个输入中的第一个。此模块将选定的输入传播到输出。要选择输入信号，请通过双击模块切换开关。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_2** — 第二个输入信号 标量 | 向量

Manual Switch 模块的两个输入中的第二个。此模块将选定的输入传播到输出。要选择输入信号，请通过双击模块切换开关。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号是从第一个或第二个输入信号传播的。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

要查看模块参数，请右键点击模块并选择**模块参数(ManualSwitch)**。

### **允许两个输入具有不同大小(产生可变大小的输出信号)** — 允许不同大小的输入 `off` (默认) | `on`

选中此复选框可允许不同大小的输入并将所选输入信号的大小传播给输出信号。如果清除该框，模块会扩展标量输入，使其具有与非标量输入相同的维度。请参阅输入信号和参数的标量扩展。

#### 编程用法

|  |
| --- |
| **参数：**`varsize` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

在两个输入之间切换

Manual Switch 模块是一个拨动开关，可从两个输入中选择一个来传递给输出。要在输入之间进行切换，请双击此模块。您可以在仿真开始之前设置开关，或者在执行仿真的过程中更改开关，从而控制信号流。当您保存模型时，Manual Switch 模块将保留其当前状态。

要以编程方式切换开关，请将 `set_param` `sw` 属性设置为 `'0'` 或 `'1'`。例如，要将第二个输入连接到输出：

```
set_param(gcb,'sw','0')
```

要将第一个输入连接到输出：

```
set_param(gcb,'sw','1')
```

**注意**

双击 Manual Switch 模块不会打开模块对话框，而是会切换输入选项。
