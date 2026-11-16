---
type: simulink-block
title: 'Prelookup'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Calibration and Measurement Data'
documentation_page: 'prelookup'
documentation_source_path: 'ref/prelookup.html'
language: zh-CN
chinese_source: worker-translation
---

# Prelookup

## 端口

### 输入

### **Port\_1** — 输入信号，`u` 标量 | 向量 | 矩阵

Prelookup 模块接受这些数据类型的实值信号：`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`，并且特别对于信号和断点数据，接受定点数据类型。

**数据类型：** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixed point`

### 输出

### **Port\_2** — 包含输出索引和小数的总线 `Simulink.Bus` 对象

以总线形式输出索引和小数，该总线指定包含输入的区间以及输入在该区间上的归一化位置。`bus` 类型根据 **Targeted Routine Library** 设置为定点 (IFX) 还是浮点 (IFL) 代码替换而自动定义。

**数据类型：** `bus`

## 参数

### **Targeted Routine Library** — 指示用于模块代码替换的 AUTOSAR 例程库 `IFX (fixed-point)` | `IFL (floating-point)`

如果为模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则从此模块生成的代码将由选定的 AUTOSAR 例程库替换。此参数使您能够选择定点 (IFX) 或浮点 (IFL) 代码替换和验证检查。

### **Targeted Routine** — 用于代码替换的 AUTOSAR 库例程 `Ifx_DPSearch` | `Ifl_DPSearch`

此参数反映用于替换此模块所生成代码的 AUTOSAR 代码替换库 (CRL) 例程的名称。命名约定包含目标例程库、插值方法和模块类型。此参数仅供引用，不得编辑。

当 `Targeted Routine Library` 设置为 `IFX (fixed-point)` 时，该值默认为 `Ifx_DPSearch`。

当 `Targeted Routine Library` 设置为 `IFL (floating-point)` 时，该值默认为 `Ifl_DPSearch`。

### 表规格

### **Breakpoints Specification** — 选择如何输入断点数据 `Explicit values`（默认） | `Breakpoint object`

如果将此参数设置为：

- `Explicit values`，则 **Breakpoints** 参数将在对话框中可见。
- `Breakpoint object`，则 **Name** 参数将在对话框中可见。

#### 编程使用

|  |
| --- |
| **模块参数：** `BPSpecification` |
| **类型：** character vector | string |
| **值：** `"Explicit values" | "Breakpoint object"` |
| **默认值：** `"Explicit values"` |

### **Breakpoints** — 断点数据值 `[1 2 3]`（默认）

显式指定断点数据。每个断点数据集必须是严格单调递增的向量，并包含两个或更多元素。

#### 依赖关系

要启用此参数，请将 **Breakpoints Specification** 设置为 `Explicit values`。

#### 编程使用

|  |
| --- |
| **模块参数：** `BreakpointsData` |
| **类型：** character vector |
| **值：** 1-by-n 或 n-by-1 的单调递增值的向量 |
| **默认值：** `'[1 2 3]'` |

### **Name** — `Simulink.Breakpoint` 对象的名称 `Simulink.Breakpoint` 对象

指定 `Simulink.Breakpoint` 对象的名称。如果 `Simulink.Breakpoint` 对象不存在，请单击操作按钮并选择 **Create**。新断点对象的相应参数将使用模块信息填充。

#### 依赖关系

要启用此参数，请将 **Breakpoints Specification** 设置为 `Breakpoint object`。

#### 编程使用

|  |
| --- |
| **模块参数：** `BreakpointObject` |
| **类型：** character vector |
| **值：** `Simulink.Breakpoint` 对象 |
| **默认值：** `'[]'` |

### 算法

### **Index search method** — 搜索断点数据的方法 `Linear search`（默认） | `Binary search`

每种搜索方法在不同情况下具有速度优势：

- 如果 `u` 的输入值在时间步之间没有显著变化，则选择 `Linear search` 并启用 **Begin index search using previous index result** 可获得最佳性能。
- 如果 `u` 的输入值每个时间步跳过超过一个或两个表区间，则选择 `Binary search` 可获得最佳性能。

索引搜索方法选择次优可能导致严重依赖查找表的模型性能变慢。

#### 编程使用

|  |
| --- |
| **模块参数：** `IndexSearchMode` |
| **类型：** character vector | string |
| **值：**`"Linear search" | "Binary search"` |
| **默认值：** `"Linear search"` |

### **Begin index search using previous index result** — 使用上一个时间步找到的索引开始搜索 `off`（默认） | `on`

对于相对于区间大小变化缓慢的 `u` 输入值，启用此选项可以提高性能。否则，线性搜索和二分搜索方法可能耗时更长，尤其是在断点集很大时。

#### 编程使用

|  |
| --- |
| **模块参数：** `BeginIndexSearchusingPreviousIndexResult` |
| **类型：** character vector | string |
| **值：** `"off" | "on"` |
| **默认值：** `"off"` |

### **Integer rounding mode** — 定点或浮点运算的舍入模式 `Zero`（默认） | `Round`

指定在仿真期间或执行从模型生成的代码期间发生的定点或浮点查找表计算的舍入模式。

此选项不影响模块参数值的舍入。Simulink™ 会将这些值舍入到最接近的可表示整数值。

#### 依赖关系

仅当将此参数设置为 `Round` 时，此参数才可见。AUTOSAR 4.x 和用于 SIL 测试的主机库不支持整数舍入，并且默认情况下隐藏此参数。要启用 SIL 工作流，请将此设置更改为 `Zero`。

#### 编程使用

|  |
| --- |
| **模块参数：** `RndMode` |
| **类型：** character vector | string |
| **值：** `"Round" | "Zero"` |
| **默认值：** `"Zero"` |

## 所属库

AUTOSAR Blockset / Classic Platform / Library Routines / Interpolation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a：Integer rounding mode 被隐藏

**Integer rounding mode** 默认设置为 `"Zero"` 并隐藏，因为 AUTOSAR 4.x 和用于 SIL 测试的主机库仅支持 `"Zero"`。

### R2025a：AUTOSAR 代码替换库支持 Release 4.0 之后的架构

从 25a 开始，AUTOSAR 代码替换库支持 AUTOSAR 4.0 之后的 AUTOSAR 架构版本。要使用最新的 AUTOSAR 例程，请在模型配置参数对话框的 **Code Generation** > **Interface** 窗格中，将 **Code replacement libraries** 指定为 `AUTOSAR 4.x`。

## 描述

为 Curve Using Prelookup 或 Map Using Prelookup 模块计算索引和小数

Prelookup 模块计算索引和小数，以指定其输入值 `u` 与断点数据集的关系。Prelookup 模块将生成的输出索引和小数值作为总线馈送到 Curve Using Prelookup 模块以对一维表进行插值，或馈送到 Map Using Prelookup 模块以对二维表进行插值。当 Prelookup 模块与 Curve Using Prelookup 或 Map Using Prelookup 模块一起使用时，它们执行与 Curve 或 Map 模块相同的算法操作。这两个模块一起使用可提供更大的灵活性以及更高效的仿真和代码生成。

如果为 AUTOSAR 模型选择 AUTOSAR 4.x 代码替换库 (CRL)，则从此模块生成的代码将替换为在模块参数对话框中配置的 AUTOSAR 库例程。
