---
type: simulink-block
title: 'Check Dynamic Range'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkdynamicrange'
documentation_source_path: 'slref/checkdynamicrange.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Dynamic Range

## 端口
```yaml
ports:
- name: max
  summary: 动态范围检查的上界 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: min
  summary: 动态范围检查的下界 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: u
  summary: 针对范围进行检查的输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: Port_1
  summary: 断言输出信号 标量
  direction: output
  data_types: double | Boolean
```

### 输入

### **max** — 动态范围检查的上界 标量 | 向量 | 矩阵

指定范围上界的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **min** — 动态范围检查的下界 标量 | 向量 | 矩阵

指定范围下界的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **u** — 针对范围进行检查的输入信号 标量 | 向量 | 矩阵

针对由 **max** 和 **min** 端口指定的范围进行检查的信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### 输出

### **Port\_1** — 断言输出信号 标量

如果断言成功则为 `true (1)`、如果断言失败则为 `false (0)` 的输出信号。如果在配置参数窗口的 **Math and Data Types** 部分中，在 **Advanced parameters** 下，您选择 **Implement logic signals as Boolean data**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖关系

要启用此端口，请选择 **Output assertion signal** 参数。

**数据类型：** `double` | `Boolean`
## 参数
```yaml
parameters:
- name: Enable assertion
  summary: 启用或禁用检查 on（默认） | off
  group: ''
  block_parameter: enabled
  type: 字符串标量或字符向量
  values: '"on" | "off"'
  default: '"on"'
- name: Simulation callback when assertion fails (optional)
  summary: 断言失败时要求值的表达式 ""（默认） | MATLAB 表达式
  group: ''
  block_parameter: callback
  type: 字符串标量或字符向量
  default: '""'
- name: Stop simulation when assertion fails
  summary: 检查失败时是否停止仿真 on（默认） | off
  group: ''
  block_parameter: stopWhenAssertionFail
  type: 字符串标量或字符向量
  values: '"on" | "off"'
  default: '"on"'
- name: Output assertion signal
  summary: 创建输出信号 off（默认） | on
  group: ''
  block_parameter: export
  type: 字符串标量或字符向量
  values: '"on" | "off"'
  default: '"off"'
- name: Select icon type
  summary: 选择图标类型 graphic（默认） | text
  group: ''
  block_parameter: icon
  type: 字符串标量或字符向量
  values: '"graphic" | "text"'
  default: '"graphic"'
```

### **Enable assertion** — 启用或禁用检查 `on`（默认） | `off`

清除此参数将禁用该模块，并使模型的行为如同该模块不存在一样。要启用或禁用所有验证模块（无论此选项的设置如何），请转到配置参数窗口，点击 **Diagnostics** > **Data Validity**，展开 **Advanced parameters** 部分，并将 **Model Verification block enabling** 设置为 `Enable all` 或 `Disable all`。

#### 编程用法

|  |
| --- |
| **参数：** `enabled` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

### **Simulation callback when assertion fails (optional)** — 断言失败时要求值的表达式 `""`（默认） | MATLAB 表达式

指定当断言失败时要求值的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中求值，请在该工作区中定义表达式中使用的所有变量。

#### 依赖关系

要启用此参数，请选择 **Enable assertion**。

#### 编程用法

|  |
| --- |
| **参数：** `callback` |
| **类型：** 字符串标量或字符向量 |
| **默认值：** `""` |

### **Stop simulation when assertion fails** — 检查失败时是否停止仿真 `on`（默认） | `off`

选择此参数可在检查失败时停止仿真。清除此参数将显示警告并继续仿真。

#### 编程用法

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认值：** `"on"` |

### **Output assertion signal** — 创建输出信号 `off`（默认） | `on`

选择此参数以启用输出端口。

#### 编程用法

|  |
| --- |
| **参数：** `export` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认值：** `"off"` |

### **Select icon type** — 选择图标类型 `graphic`（默认） | `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 编程用法

|  |
| --- |
| **参数：** `icon` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"graphic"` | `"text"` |
| **默认值：** `"graphic"` |
## 所属库

Simulink / Model Verification HDL Coder / Model Verification

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理模型验证模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `No HDL` | 不为该模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制未连接逻辑的移除。默认值为 `off`，这意味着未连接逻辑不会保留在 HDL 代码中。有关更多详细信息，请参阅 PreserveUpstreamLogic (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

检查信号是否落在随时间步变化的幅度范围内

Check Dynamic Range 模块检查信号在每个时间步是否落在某个值范围内，并在比较后执行断言。该范围的宽度可以随每个时间步变化。**u** 端口是受测试的输入信号。**min** 和 **max** 端口分别是范围的下界和上界，其中 **min** 和 **max** 均为排除边界。如果 **u** 介于 **max** 和 **min** 之间，则断言为 `true (1)`，模块不执行任何操作。否则，模块默认会停止仿真并返回错误消息。

输入信号可以是标量、向量或矩阵。所有三个输入信号必须具有相同的数据类型。模块根据信号的不同以不同方式将 **u** 的值与边界进行比较。

- 当将标量与向量或矩阵进行比较时，模块将标量信号与非标量信号的每个元素进行比较。
- 当将向量或矩阵信号与其他向量或矩阵进行比较时，模块逐元素检查输入。
- 对于具有多个向量或矩阵输入信号的模型，向量或矩阵必须具有相同的维度。
