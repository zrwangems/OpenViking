---
type: simulink-block
title: 'Check Discrete Gradient'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checkdiscretegradient'
documentation_source_path: '../simulink/slref/checkdiscretegradient.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Discrete Gradient

## 端口
```yaml
ports:
- name: Port_1
  summary: 检查梯度的输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 断言输出信号 标量
  direction: output
  data_types: double | Boolean
```

### 输入

### **Port\_1** — 检查梯度的输入信号 标量 | 向量 | 矩阵

模块检查的输入信号，用于确定连续采样之间每个元素的差值是否小于 **Maximum gradient** 参数的绝对值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 断言输出信号 标量

输出信号，如果断言成功则为 `true (1)`，如果断言失败则为 `false (0)`。如果在配置参数窗口的 **Math and Data Types** 部分中，在 **Advanced parameters** 下，选择 **Implement logic signals as Boolean data**，则输出数据类型为 `Boolean`。否则，信号的数据类型为 `double`。

#### 依赖

要启用此输出端口，请选中 **Output assertion signal** 参数复选框。

**数据类型：** `double` | `Boolean`
## 参数
```yaml
parameters:
- name: Maximum gradient
  summary: 允许差值的最大值 1 （默认） | 标量
  group: ''
  block_parameter: gradient
  type: 字符串标量或字符向量
  values: 实数标量
- name: Enable assertion
  summary: 启用或禁用检查 on （默认） | off
  group: ''
  block_parameter: enabled
  type: 字符串标量或字符向量
  values: '"on" | "off"'
- name: Simulation callback when assertion fails (optional)
  summary: 断言失败时求值的表达式 "" （默认） | MATLAB 表达式
  group: ''
  block_parameter: callback
  type: 字符串标量或字符向量
- name: Stop simulation when assertion fails
  summary: 检查失败时是否停止仿真 on （默认） | off
  group: ''
  block_parameter: stopWhenAssertionFail
  type: 字符串标量或字符向量
  values: '"on" | "off"'
- name: Output assertion signal
  summary: 创建输出信号 off （默认） | on
  group: ''
  block_parameter: export
  type: 字符串标量或字符向量
  values: '"on" | "off"'
- name: Select icon type
  summary: 选择图标类型 graphic （默认） | text
  group: ''
  block_parameter: icon
  type: 字符串标量或字符向量
  values: '"graphic" | "text"'
```

### **Maximum gradient** — 允许差值的最大值 `1` （默认） | 标量

指定输入信号允许梯度的值。

#### 程序化使用

|  |
| --- |
| **参数：** `gradient` |
| **类型：** 字符串标量或字符向量 |
| **值：** 实数标量 |
| **默认：** `"1"` |

### **Enable assertion** — 启用或禁用检查 `on` （默认） | `off`

清除此参数将禁用该模块，并使模型的行为如同该模块不存在一样。要启用或禁用所有验证模块，无论此选项的设置如何，请转到配置参数窗口，点击 **Diagnostics** > **Data Validity**，展开 **Advanced parameters** 部分，并将 **Model Verification block enabling** 设置为 `Enable all` 或 `Disable all`。

#### 程序化使用

|  |
| --- |
| **参数：** `enabled` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **Simulation callback when assertion fails (optional)** — 断言失败时求值的表达式 `""` （默认） | MATLAB 表达式

指定断言失败时要求值的 MATLAB® 表达式。由于该表达式在 MATLAB 工作区中求值，请在该工作区中定义表达式中使用的所有变量。

#### 依赖

要启用此参数，请选中 **Enable assertion**。

#### 程序化使用

|  |
| --- |
| **参数：** `callback` |
| **类型：** 字符串标量或字符向量 |
| **默认：** `""` |

### **Stop simulation when assertion fails** — 检查失败时是否停止仿真 `on` （默认） | `off`

选中此参数可在检查失败时停止仿真。清除此参数可显示警告并继续仿真。

#### 程序化使用

|  |
| --- |
| **参数：** `stopWhenAssertionFail` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"on"` |

### **Output assertion signal** — 创建输出信号 `off` （默认） | `on`

选中此参数以启用输出端口。

#### 程序化使用

|  |
| --- |
| **参数：** `export` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"on"` | `"off"` |
| **默认：** `"off"` |

### **Select icon type** — 选择图标类型 `graphic` （默认） | `text`

指定模块图标的样式。`graphic` 选项在图标上显示断言条件的图形表示。`text` 选项显示表示断言条件的数学表达式。

#### 程序化使用

|  |
| --- |
| **参数：** `icon` |
| **类型：** 字符串标量或字符向量 |
| **值：** `"graphic"` | `"text"` |
| **默认：** `"graphic"` |
## 所属库

Simulink / Model Verification HDL Coder / Model Verification

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

有关 Simulink® Coder™ 生成的代码如何处理模型验证模块的信息，请参阅 Configure Model for Debugging (Simulink Coder)。

不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

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

检查离散信号连续采样之间差值的绝对值是否小于指定值

Check Discrete Gradient 模块检查每个信号元素，并确定该元素连续值之间差值的绝对值是否小于指定值。然后模块在比较后执行断言。您可以通过调整 **Maximum gradient** 参数来指定梯度值（默认为 `1`）。如果输入信号差值小于 **Maximum gradient** 的绝对值，则断言为 `true (1)`，模块不执行任何操作。否则，模块默认停止仿真并返回错误消息。

**注意**

要运行仿真，Check Discrete Gradient 模块需要定步长离散求解器。如果选择了其他求解器，则会提示错误。
