---
type: simulink-block
title: 'Interpreted MATLAB Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'interpretedmatlabfunction'
language: zh-CN
chinese_source: official
---

# Interpreted MATLAB Function

## 端口

### 输入

### **In** — Interpreted MATLAB function 的输入 标量 | 向量 | 矩阵

Interpreted MATLAB Function 模块接受一个 `double` 类型的实数或复数输入，并生成 `double` 类型的实数或复数输出，具体取决于**输出信号类型**参数的设置。

**数据类型:** `double`
### 输出

### **Out** — Interpreted MATLAB function 的输出 标量 | 向量 | 矩阵

Interpreted MATLAB Function 模块接受一个 `double` 类型的实数或复数输入，并生成 `double` 类型的实数或复数输出，具体取决于**输出信号类型**参数的设置。

**数据类型:** `double`

## 参数

### **MATLAB 函数** — 指定函数或表达式。 函数 (默认)

指定函数或表达式。如果仅指定函数，则不需要将输入参量用括号括起来。

### **输出维度** — 指定模块输出信号的维度 标量 | 矩阵 | 向量 | 继承

指定模块输出信号的维度，例如，`2` 表示二元素向量。输出维度必须与 **MATLAB 函数**字段中的函数或表达式所返回的值的维度相匹配。

如果指定 `-1`，将从指定的函数或表达式的输出继承维度。为确定输出维度，Simulink 会在仿真开始之前运行一次函数或表达式。

**注意**

如果为此参数指定 `-1`，并且您的函数具有持久变量，则这些变量可能会在仿真开始之前更新。如果需要使用持久变量，请考虑将此参数设置为除 `-1` 以外的值。

### **输出信号类型** — 指定模块输出信号类型 auto (默认) | 实数 | 复数

将模块的输出信号类型指定为 `real`、`complex` 或 `auto`。值 `auto` 会将输出类型设置为与输入信号的类型相同。

### **将二维结果降为一维** — 将二维数组输出为一维数组 off (默认) | on

选中此复选框会将二维数组输出为一维数组，其中包含的二维数组元素以列优先的顺序排列。

### **采样时间** — 指定模块中的采样时间 标量

**注意**

此参数在模块对话框中不可见，除非将其显式设置为 `-1` 以外的值。要了解详细信息，请参阅不建议设置采样时间的模块。

## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011a 中推出**

### R2022b: 将删除

在以后的版本中将会删除 Interpreted MATLAB Function 模块。推荐改用内置模块。如果建模需要 MATLAB 代码，请使用 MATLAB Function 模块。您还可以考虑将该函数编写为 MEX 文件 S-Function，并使用 S-Function 模块来实现它。

## 描述

（将删除）对输入应用 MATLAB 函数或表达式

Interpreted MATLAB Function 模块用于将指定的 MATLAB® 函数或表达式应用于输入。函数的输出必须与模块的输出维度相匹配。请仅在当前工作区中使用 Interpreted MATLAB Function 模块。

针对此模块的部分有效表达式包括：

```
sin
atan2(u(1), u(2))
u(1)^u(2)
```

**注意**

此模块很慢，因为它在每个积分步中都会调用 MATLAB 解析器。请考虑改用内置模块（如 Math Function 模块）。或者，您可以编写 MEX 文件 S-Function 形式的函数，然后使用 S-Function 模块访问该函数。
