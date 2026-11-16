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
chinese_source: official
---

# Lookup Table Dynamic

## 端口

### 输入

### **x** — 输入向量 标量 | 向量 | 二维数组

模块接受实数值或复数值输入。

**示例:** `2:12`

#### 依赖关系

`x` 输入向量和 `xdat` 断点数据必须具有相同的符号、偏置和小数斜率。此外，`x` 的精度和范围必须大于或等于 `xdat` 的精度和范围。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **xdat** — 断点数据 由严格单调递增值组成的 1×n 向量

`xdat` 向量是断点数据，它必须严格单调递增。在转换为定点数据类型后，该向量中的下一个元素的值必须大于上一个元素的值。由于量化的原因，`xdat` 对于浮点数据类型可以严格单调，但在转换为定点数据类型之后，则不能严格单调。

**提示**

均匀分布的断点可使 Simulink Coder 生成的代码无分割。有关详细信息，请参阅 Simulink 文档中的 `fixpt_evenspace_cleanup` 和 Simulink Coder 文档中的Identify questionable fixed-point operations (Embedded Coder)。

**示例:** `1:10`

#### 依赖关系

`xdat` 断点数据和 `x` 输入向量必须具有相同的符号、偏置和小数斜率。此外，`x` 的精度和范围必须大于或等于 `xdat` 的精度和范围。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **ydat** — 表数据 1×n 向量

`ydat` 输入是实数值或复数值表数据的 1×n 向量，它是函数在断点值处的计算结果。

**示例:**  `[0 3 12 27 48 75 108 147 192 243 300]`

#### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和小数斜率。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### 输出

### **y** — 使用动态表数据计算 `y = f(x)` 的逼近值 1×n 向量

该模块使用 `xdat` 和 `ydat` 输入向量来计算函数 `y = f(x)` 的逼近值。查找方法可以使用内插、外插或原始输入值。

#### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和小数斜率。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### “常设”选项卡

### **查找方法** — 指定查找方法 **插值 - 使用最终值** (默认) | **内插-外插** | **取最邻近的输入值** | **向下取输入值** | **向上取输入值**

该模块通过将您选择的**查找方法**应用于断点数据 (`xdat`) 和表数据 (`ydat`) 的输入向量来计算输出。有关详细信息，请参阅模块如何生成输出。

#### 编程用法

|  |
| --- |
| **模块参数**：`LookUpMeth` |
| **类型：**字符向量 |
| **值：**`'Interpolation-Extrapolation' | 'Interpolation-Use End Values' | 'Use Input Nearest' | 'Use Input Below' | 'Use Input Above'` |
| **默认值：**`'Interpolation-Use End Values'` |

### “信号属性”选项卡

### **输出数据类型** — 输出数据类型 **double** (默认) | **'继承:通过反向传播继承'** | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **boolean** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

指定输出信号 `y` 的数据类型。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

#### 依赖关系

`ydat` 表数据和 `y` 输出向量必须具有相同的符号、偏置和小数斜率。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'Inherit: Inherit via back propagation' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | <data type expression>` |
| **默认值：**`'double'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB® 舍入函数输入表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **发生溢出时饱和处理为最大值或最小值** — 溢出操作的方法 `off` (默认) | `on`

当您选中此复选框时，溢出将饱和处理为数据类型可表示的最大值或最小值。否则，溢出将绕回。

如果选中此复选框，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

## 所属库

Simulink / Lookup Tables

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

当**查找方法**参数设置为**内插-外插**时，Lookup Table Dynamic 模块不生成代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

Simulink PLC Coder™ 软件不支持 Simulink Lookup Table Dynamic 模块。为方便起见，plclib/Simulink/Lookup Tables 库包含使用 Prelookup 和 Interpolation Using Prelookup 模块的动态表查找模块的实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用动态表逼近一维函数

### 此模块与其他 Lookup Table 模块的不同之处

Lookup Table Dynamic 模块使用 `xdat` 和 `ydat` 向量计算函数 `y = f(x)` 的逼近值。查找方法可以使用内插、外插或原始输入值。

使用 Lookup Table Dynamic 模块，您可以更改表数据而无需停止仿真。例如，如果您正在仿真的物理系统发生变化，您可以加入新的表数据。

有关替代 Lookup Table Dynamic 模块的信息，请参阅 n-D Lookup Table。

### 断点和表数据的输入

`xdat` 向量是断点数据，它必须*严格单调递增*。在转换为定点数据类型后，该向量中的下一个元素的值必须大于上一个元素的值。由于量化的原因，`xdat` 对于浮点数据类型可以严格单调，但在转换为定点数据类型之后，则不能严格单调。

`ydat` 向量是表数据，是函数在断点值处的计算结果。

**注意**

`xdat` 和 `ydat` 的输入不能是标量（一元数组）值。如果您为其中任一输入提供了标量值，您会在仿真时看到错误消息。为 `xdat` 和 `ydat` 输入都提供 1×n 向量。

### 查找表定义

您通过将 `xdat` 和 `ydat` 作为 1×n 向量馈送给模块来定义查找表。要减少为此模块生成的代码中使用的 ROM，您可以为 `xdat` 和 `ydat` 使用不同的数据类型。

**提示**

均匀分布的断点可使 Simulink® Coder™ 生成的代码无分割。有关详细信息，请参阅 Simulink 文档中的 `fixpt_evenspace_cleanup` 和 Simulink Coder 文档中的Identify questionable fixed-point operations (Embedded Coder)。

### 模块如何生成输出

此模块采用您为**查找方法**选择的方法使用输入值生成输出：

| 查找方法 | 模块操作 |
| --- | --- |
| **内插-外插** | 对输入执行线性内插和外插。  - 如果输入与断点匹配，则输出表数据中的对应元素。 - 如果输入与断点不匹配，模块将通过在表的两个元素之间执行线性内插来确定输出。如果输入不在断点值的范围内，模块将使用前两个或最后两个点进行外插。  **注意**  如果您选择此查找方法，Simulink Coder 软件将无法为此模块生成代码。 |
| **插值 - 使用最终值**（默认值） | 执行线性内插，但不会在断点数据的端点外进行外插，而是会转而使用端点值。 |
| **取最邻近的输入值** | 查找 `xdat` 中最接近当前输入的元素。输出 `ydat` 中的对应元素。 |
| **向下取输入值** | 查找 `xdat` 中最接近并且低于当前输入的元素。输出 `ydat` 中的对应元素。如果 `xdat` 中没有任何元素低于当前输入，模块将查找最邻近的元素。 |
| **向上取输入值** | 查找 `xdat` 中最接近并且高于当前输入的元素。输出 `ydat` 中的对应元素。如果 `xdat` 中没有任何元素高于当前输入，模块将查找最邻近的元素。 |

**注意**

当输入 `x` 与断点值匹配时，`Use Input Nearest`、`Use Input Below` 和 `Use Input Above` 方法执行相同的操作。

有些连续求解器将仿真时间细分为主时间步和子时间步。子时间步是对主时间步的细分。求解器在每个主时间步生成结果，并使用子时间步的结果提高主时间步结果的准确性。对于连续求解器，Lookup Table Dynamic 模块的输出可能像一个楼梯，因为信号在子时间步是固定的，以免生成不正确的结果。有关求解器如何影响模块输出的详细信息，请参阅 Simulink 文档中的比较求解器。
