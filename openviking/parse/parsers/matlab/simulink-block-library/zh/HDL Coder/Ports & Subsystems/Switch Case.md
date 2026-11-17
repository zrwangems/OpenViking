---
type: simulink-block
title: 'Switch Case'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'switchcase'
documentation_source_path: '../simulink/slref/switchcase.html'
language: zh-CN
chinese_source: worker-translation
---

# Switch Case

## 端口
```yaml
ports:
- name: u1 (logical operator)
  summary: 用于 case 选择的值 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | enumerated
- name: case
  summary: 用于 Switch Case Action Subsystem 模块的动作信号 标量
  direction: output
```

### 输入

### **u1 (logical operator)** — 用于 case 选择的值 标量

Switch Case 模块标记为 **u1** 的端口的输入可以是：

- 一个 Simulink 支持的内置数据类型的标量值。但是，Switch Case 模块不支持布尔或定点数据类型，并且会将数值输入截断为 32 位有符号整数。
- 任意枚举数据类型的标量值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `enumerated`
### 输出

### **case** — 用于 Switch Case Action Subsystem 模块的动作信号 标量

**Case** 和 **default** 端口的输出是连接到 Switch Case Action Subsystem 模块的动作信号。
## 参数
```yaml
parameters:
- name: Case conditions
  summary: 指定 case 值 {1}（默认）| case 列表
  group: ''
  block_parameter: CaseConditions
  type: 字符向量
  values: '''{1}'' | 带引号的 case 列表'
  default: '''{1}'''
- name: Show default case
  summary: 控制默认输出端口的显示 on（默认）| off
  group: ''
  block_parameter: ShowDefaultCase
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Enable zero-crossing detection
  summary: 控制过零检测 on（默认）| off
  group: ''
  block_parameter: ZeroCross
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
```

### **Case conditions** — 指定 case 值 `{1}`（默认）| case 列表

使用 MATLAB® 元胞表示法指定 case 值。

{1}
:   指定标记为 `case[1]` 的输出端口在输入端口值为 `1` 时输出动作信号。

带 case 赋值的端口列表
:   使用 MATLAB 元胞表示法指定多个 case 和端口。例如，输入 `{1,[7,9,4]}` 表示当输入值为 `1` 时运行输出端口 `case[1]`，当输入值为 `7`、`9` 或 `4` 时运行输出端口 `case [7 9 4]`。

    您可以使用冒号表示法指定整数 case 条件的范围。例如，输入 `{[1:5]}` 表示当输入值为 `1`、`2`、`3`、`4` 或 `5` 时运行输出端口 **case[1 2 3 4 5]**。

    根据模块大小，长 case 条件列表中的 case 会以缩短形式显示在 Switch Case 模块的表面上，并使用终止省略号 (...)。

    您可以使用枚举类型的名称来指定 case 条件，其中包含该枚举类型中每个值的 case。

#### 编程使用

|  |
| --- |
| **模块参数**：`CaseConditions` |
| **类型**：字符向量 |
| **值**：`'{1}'` | 带引号的 case 列表 |
| **默认值**：`'{1}'` |

### **Show default case** — 控制默认输出端口的显示 `on`（默认）| `off`

控制默认输出端口的显示。

on
:   将默认输出端口显示为 Switch Case 模块上的最后一个 case。这允许您指定一个默认 case，当输入值不匹配任何其他 case 值时执行该 case。

off
:   隐藏默认输出端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ShowDefaultCase` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Enable zero-crossing detection** — 控制过零检测 `on`（默认）| `off`

控制过零检测。

on
:   检测过零。

off
:   不检测过零。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |
## 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

当此模块在 For Each Subsystem 模块内使用时，不支持代码生成。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用类似于 switch 语句的逻辑选择子系统执行

带有包含 Action Port 模块的 Switch Case Action Subsystem 模块的 Switch Case 模块实现 switch 逻辑以控制子系统执行。有关使用 Switch Case 模块的示例，请参阅 Select Subsystem Execution。

模型 ex\_switch\_case\_block

Switch Case 模块有一个输入。要选择 case，请使用 **Case conditions** 参数定义输入值。case 从第一个 case 开始自上而下求值。

每个 case 都与一个输出端口关联，该端口连接到 Switch Case Action Subsystem 模块。当选择某个 case 时，关联的输出端口发送动作信号以执行子系统。

在所有其他 case 条件求值为 false 后，将选择 `default` case。提供 `default` case 是可选的，即使其他 case 条件未穷尽所有可能的输入值也是如此。

Switch Case 模块的 case 在 Switch Case Action Subsystem 模块执行后包含隐含的 break。因此，Simulink® Switch Case 模块没有标准 C `switch` 语句中的贯穿行为。
