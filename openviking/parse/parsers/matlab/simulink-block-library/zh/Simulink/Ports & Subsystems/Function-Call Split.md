---
type: simulink-block
title: 'Function-Call Split'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functioncallsplit'
documentation_source_path: 'slref/functioncallsplit.html'
language: zh-CN
chinese_source: worker-translation
---

# Function-Call Split

## 端口
```yaml
ports:
- name: Function Call
  summary: 函数调用线标量
  direction: input
- name: Function Call
  summary: 函数调用信号标量
  direction: output
```

### 输入

### **Function Call** — 函数调用线标量

Function-Call Generator 模块、S-Function 模块、Hit Crossing 模块或 Stateflow® 图可以提供函数调用事件。

### 输出

### **Function Call** — 函数调用信号标量

连接到函数调用子系统或函数调用模型的函数调用线。
## 参数
```yaml
parameters:
- name: Icon shape
  summary: 选择模块图标形状 distinctive（默认）| round
  group: ''
  block_parameter: IconShape
  type: character vector
  values: '''distinctive'' | ''round'''
  default: '''distinctive'''
- name: Number of output ports
  summary: 指定输出端口数量 2（默认）| 整数
  group: ''
  block_parameter: NumOutputPorts
  type: character vector
  values: '''2'' | ''<integer>'''
  default: '''2'''
- name: Output port layout
  summary: 选择输出端口的顺序 default（默认）| reverse
  group: ''
  block_parameter: OutputPortLayout
  type: character vector
  values: '''default'' | ''reverse'''
  default: '''default'''
```

### **Icon shape** — 选择模块图标形状 `distinctive`（默认）| `round`

选择模块图标形状。

#### 设置

`distinctive`
：   矩形模块图标。

`round`
：   圆形模块图标。

#### 编程使用

|  |
| --- |
| **模块参数**：`IconShape` |
| **类型**：character vector |
| **值**：`'distinctive'` | `'round'` |
| **默认值**：`'distinctive'` |

### **Number of output ports** — 指定输出端口数量 `2`（默认）| 整数

指定函数调用信号输出端口的数量。

#### 设置

`2`
：   两个函数调用输出端口。

整数
：   整数

#### 编程使用

|  |
| --- |
| **模块参数**：`NumOutputPorts` |
| **类型**：character vector |
| **值**：`'2'` | `'<integer>'` |
| **默认值**：`'2'` |

### **Output port layout** — 选择输出端口的顺序 `default`（默认）| `reverse`

选择函数调用输出端口的顺序，即哪个端口先提供函数调用。

#### 设置

`default`
：   顶部端口先提供函数调用。

`reverse`
：   底部端口先提供函数调用。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputPortLayout` |
| **类型**：character vector |
| **值**：`'default'` | `'reverse'` |
| **默认值**：`'default'` |
## 所属库

Simulink / Ports & Subsystems

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

为拆分函数调用线提供连接点

Function-Call Split 模块允许函数调用线分支并连接到多个函数调用子系统或函数调用模型。

连接到 Function-Call Split 模块输出端口且标记有圆点的函数调用子系统或函数调用模型，先于连接到其他输出端口的子系统或模型执行。如果子系统或模型之间的数据依赖关系不支持指定的执行顺序，Function-Call Split 模块将返回错误。要消除此错误，可考虑在参与数据依赖循环的一个或多个函数调用子系统或模型的 Inport 模块上，选中 **Latch input for feedback signals of function-call subsystem outputs** 参数。选中此选项会延迟相应的函数调用，从而消除数据依赖循环。

要显示连接到给定函数调用信号各分支的函数调用子系统的执行顺序，请在 Simulink Editor 的 **Debug** 选项卡上，选择 **Information Overlays**，然后点击 **Execution Order**。Simulink 画布上会打开一个窗格，表示 **Execution Order Block List**。在该列表中，函数调用子系统的执行顺序表示为 [`n`]←[`m`] `subsystem block name`，其中：

- `n` 表示子系统的执行顺序。
- `m` 表示生成函数调用信号的模块的执行顺序。
- `subsystem block name` 表示函数调用子系统的名称。

Function-Call Split 模块支持 Signal Label Propagation。

以下模型展示了如何应用 **Latch input for feedback signals of function-call subsystem outputs** 参数，以绕过由 Function-Call Split 模块引起的数据依赖错误。通过在 `f1` 子系统的 Inport 模块中打开此参数，Function-Call Split 模块会忽略信号 b 的数据依赖关系。该模块打破了子系统 `f1` 和 `g1` 之间的数据依赖循环。该模型实现了始终先调用 f1 再调用 g1 执行的行为。对于给定的执行步，子系统 `f1` 使用在上一个执行步计算出的 `g1` 输出。
