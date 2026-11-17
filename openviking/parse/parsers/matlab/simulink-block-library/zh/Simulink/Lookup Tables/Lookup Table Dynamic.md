---
type: simulink-block
title: 'Lookup Table Dynamic'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'lookuptabledynamic'
documentation_source_path: 'slref/lookuptabledynamic.html'
language: zh-CN
chinese_source: worker-translation
---

# Lookup Table Dynamic

## 端口

### 输入

### **x** — 输入向量 标量 | 向量 | 二维数组

该模块接受实数值或复数值输入。

**示例：** `2:12`

#### 依赖关系

`x` 输入向量和 `xdat` 断点数据必须具有相同的符号、偏置和分数斜率。此外，`x` 的精度和范围必须大于或等于 `xdat` 的精度和范围。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **xdat** — 断点数据 严格单调递增值的 1×n 向量

`xdat` 向量是断点数据，必须严格单调递增。转换为定点数据类型后，向量中下一个元素的值必须大于前一个元素的值。由于量化，`xdat` 在浮点数据类型下可以是严格单调的，但转换为定点数据类型后则不然。

**提示**

等间距的断点可以使 Simulink Coder 生成的代码无除法运算。有关详细信息，请参阅 Simulink 文档中的 `fixpt_evenspace_cleanup` 以及 Simulink Coder 文档中的 Identify questionable fixed-point operations (Embedded Coder)。

**示例：** `1:10`

#### 依赖关系

`xdat` 断点数据和 `x` 输入向量必须具有相同的符号、偏置和分数斜率。此外，`x` 的精度和范围必须大于或等于 `xdat` 的精度和范围。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **ydat** — 表数据 1×n 向量

`ydat` 输入是实数值或复数值表数据的 1×n 向量，即函数在断点值处的求值结果。

**示例：**
`[0 3 12 27 48 75 108 147 192 243 300]`

#### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和分数斜率。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### 输出

### **y** — 使用动态表数据对 `y = f(x)` 的近似 1×n 向量

该模块使用 `xdat` 和 `ydat` 输入向量计算函数 `y = f(x)` 的近似值。查找方法可以使用插值、外插或输入的原始值。

#### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和分数斜率。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主选项卡

### **Lookup Method** — 指定查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的 **Lookup Method** 应用于断点数据（`xdat`）和表数据（`ydat`）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 编程使用

|  |
| --- |
| **模块参数**：`LookUpMeth` |
| **类型**：character vector |
| **值**：`'Interpolation-Extrapolation' | 'Interpolation-Use End Values' | 'Use Input Nearest' | 'Use Input Below' | 'Use Input Above'` |
| **默认值**：`'Interpolation-Use End Values'` |

### 信号属性选项卡

### **Output data type** — 输出数据类型 `double`（默认）| `'Inherit: Inherit via back propagation'` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

指定输出信号 `y` 的数据类型。

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请点击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和分数斜率。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via back propagation' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | <data type expression>` |
| **默认值**：`'double'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **值**：| `'off'`（默认）| `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入方式，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **值**：| `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate to max or min when overflows occur** — 溢出操作的方法 `off`（默认）| `on`

选中此复选框时，溢出饱和到数据类型可以表示的最大值或最小值。否则，溢出将回绕。

选中此复选框时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Lookup Tables

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当 **Lookup Method** 参数设置为 `Interpolation-Extrapolation` 时，Lookup Table Dynamic 模块不生成代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

Simulink PLC Coder™ 软件不支持 Simulink Lookup Table Dynamic 模块。为方便起见，plclib/Simulink/Lookup Tables 库包含使用 Prelookup 和 Interpolation Using Prelookup 模块的动态表查找模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用动态表近似一维函数

### 此模块与其他查找表模块的区别

Lookup Table Dynamic 模块使用 `xdat` 和 `ydat` 向量计算函数 `y = f(x)` 的近似值。查找方法可以使用插值、外插或输入的原始值。

使用 Lookup Table Dynamic 模块，您可以在不停止仿真的情况下更改表数据。例如，如果您所仿真的物理系统发生变化，您可以合并新的表数据。

作为 Lookup Table Dynamic 模块的替代方案，请参阅 n-D Lookup Table。

### 断点和表数据的输入

`xdat` 向量是断点数据，必须*严格单调递增*。转换为定点数据类型后，向量中下一个元素的值必须大于前一个元素的值。由于量化，`xdat` 在浮点数据类型下可以是严格单调的，但转换为定点数据类型后则不然。

`ydat` 向量是表数据，即函数在断点值处的求值结果。

**注意**

`xdat` 和 `ydat` 的输入不能是标量（单元素数组）值。如果您为其中任一输入提供标量值，仿真时会看到错误。请为 `xdat` 和 `ydat` 输入都提供 1×n 向量。

### 查找表定义

您通过将 `xdat` 和 `ydat` 作为 1×n 向量馈送到模块来定义查找表。为减少此模块生成代码中的 ROM 使用量，您可以为 `xdat` 和 `ydat` 使用不同的数据类型。

**提示**

等间距的断点可以使 Simulink® Coder™ 生成的代码无除法运算。有关详细信息，请参阅 Simulink 文档中的 `fixpt_evenspace_cleanup` 以及 Simulink Coder 文档中的 Identify questionable fixed-point operations (Embedded Coder)。

### 模块如何生成输出

该模块使用输入值，通过您为 **Lookup Method** 选择的方法生成输出：

| Lookup Method | 模块操作 |
| --- | --- |
| `Interpolation-Extrapolation` | 对输入执行线性插值和外插。 - 如果输入与断点匹配，输出为表数据中对应的元素。 - 如果输入与断点不匹配，模块在表的两个元素之间执行线性插值以确定输出。如果输入落在断点值范围之外，模块使用前两个或后两个点进行外插。 **注意** 如果您选择此查找方法，Simulink Coder 软件无法为此模块生成代码。 |
| `Interpolation-Use End Values`（默认） | 执行线性插值，但不在断点数据的端点之外进行外插。相反，模块使用端点值。 |
| `Use Input Nearest` | 查找 `xdat` 中最接近当前输入的元素。`ydat` 中对应的元素即为输出。 |
| `Use Input Below` | 查找 `xdat` 中最接近且低于当前输入的元素。`ydat` 中对应的元素即为输出。如果 `xdat` 中没有低于当前输入的元素，模块将查找最接近的元素。 |
| `Use Input Above` | 查找 `xdat` 中最接近且高于当前输入的元素。`ydat` 中对应的元素即为输出。如果 `xdat` 中没有高于当前输入的元素，模块将查找最接近的元素。 |

**注意**

当输入 `x` 与断点值匹配时，`Use Input Nearest`、`Use Input Below` 和 `Use Input Above` 方法执行相同的操作。

某些连续求解器将仿真时间跨度细分为主时间步和次时间步。次时间步是主时间步的细分。求解器在每个主时间步产生结果，并使用次时间步的结果来提高主时间步结果的精度。对于连续求解器，Lookup Table Dynamic 模块的输出可能看起来像阶梯状，因为信号在次时间步中固定以避免不正确的结果。有关求解器对模块输出影响的详细信息，请参阅 Simulink 文档中的 Compare Solvers。
