---
type: simulink-block
title: 'Manual Switch'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'manualswitch'
documentation_source_path: 'slref/manualswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Manual Switch

## 端口
```yaml
ports:
- name: Port_1
  summary: 第一个输入信号 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_2
  summary: 第二个输入信号 标量 | 向量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量

Manual Switch 模块的两个输入中的第一个。该模块将选定的输入传播到输出。要选择输入信号，请通过双击模块来切换开关。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Port\_2** — 第二个输入信号 标量 | 向量

Manual Switch 模块的两个输入中的第二个。该模块将选定的输入传播到输出。要选择输入信号，请通过双击模块来切换开关。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

从第一个或第二个输入信号传播的输出信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Allow the two inputs to differ in size (Results in variable-size output signal)
  summary: 允许不同大小的输入 off（默认）| on
  group: ''
  block_parameter: varsize
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
```

要查看模块参数，请右键单击模块并选择 `Block Parameters
(ManualSwitch)`。

### **Allow the two inputs to differ in size (Results in variable-size output signal)** — 允许不同大小的输入 `off`（默认）| `on`

选中此复选框可允许具有不同大小的输入，并将选定的输入信号大小传播到输出信号。如果清除该复选框，该模块会将标量输入扩展为与非标量输入具有相同的维度。请参阅标量扩展的输入和参数。

#### 编程使用

|  |
| --- |
| **Parameter:** `varsize` |
| **类型**：character vector |
| **Value:** `'on'` | `'off'` |
| **默认值**：`'off'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅不建议使用采样时间的模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |
## 所属库

Simulink / Signal Routing

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

在两个输入之间切换

Manual Switch 模块是一个切换开关，它选择其两个输入之一传递到输出。要在输入之间切换，请双击模块。您可以通过在开始仿真之前设置开关，或在仿真执行时更改开关来控制信号流。Manual Switch 模块在保存模型时会保留其当前状态。

要以编程方式切换开关，请将 `set_param` 的 `sw` 属性设置为 `'0'` 或 `'1'`。例如，要将第二个输入连接到输出：

```
set_param(gcb,'sw','0')
```

要将第一个输入连接到输出：

```
set_param(gcb,'sw','1')
```

**注意**

双击 Manual Switch 模块不会打开模块对话框。相反，它会切换输入选择。
