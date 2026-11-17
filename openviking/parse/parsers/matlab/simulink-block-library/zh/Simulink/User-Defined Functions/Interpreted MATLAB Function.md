---
type: simulink-block
title: 'Interpreted MATLAB Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'interpretedmatlabfunction'
documentation_source_path: 'slref/interpretedmatlabfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Interpreted MATLAB Function

## 端口
```yaml
ports:
- name: In
  summary: Interpreted MATLAB 函数的输入 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: Out
  summary: Interpreted MATLAB 函数的输出 标量 | 向量 | 矩阵
  direction: output
  data_types: double
```

### 输入

### **In** — Interpreted MATLAB 函数的输入 标量 | 向量 | 矩阵

Interpreted MATLAB Function 模块接受一个 `double` 类型的实数或复数输入，并根据 **Output signal type** 参数的设置生成 `double` 类型的实数或复数输出。

**数据类型：** `double`
### 输出

### **Out** — Interpreted MATLAB 函数的输出 标量 | 向量 | 矩阵

Interpreted MATLAB Function 模块接受一个 `double` 类型的实数或复数输入，并根据 **Output signal type** 参数的设置生成 `double` 类型的实数或复数输出。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: MATLAB Function
  summary: 指定函数或表达式 函数（默认）
  group: ''
- name: Output dimensions
  summary: 指定模块输出信号的维度 标量 | 矩阵 | 向量 | 继承
  group: ''
- name: Output signal type
  summary: 指定模块输出信号类型 auto（默认） | real | complex
  group: ''
- name: Collapse 2-D results to 1-D
  summary: 将二维数组输出为一维数组 off（默认） | on
  group: ''
- name: Sample time
  summary: 指定模块中的采样时间 标量
  group: ''
```

### **MATLAB Function** — 指定函数或表达式 函数（默认）

指定函数或表达式。如果仅指定函数，则无需在括号中包含输入参数。

### **Output dimensions** — 指定模块输出信号的维度 标量 | 矩阵 | 向量 | 继承

指定模块输出信号的维度，例如，`2` 表示二元素向量。输出维度必须与 **MATLAB function** 字段中函数或表达式返回值的维度匹配。

指定 `-1` 以从指定函数或表达式的输出继承维度。为确定输出维度，Simulink 在仿真开始前运行一次函数或表达式。

**注意**

如果为此参数指定 `-1` 且函数具有持久变量，则这些变量可能在仿真开始前更新。如果需要使用持久变量，请考虑将此参数设置为 `-1` 以外的值。

### **Output signal type** — 指定模块输出信号类型 auto（默认） | real | complex

将模块的输出信号类型指定为 `real`、`complex` 或 `auto`。值为 `auto` 时，输出类型与输入信号类型相同。

### **Collapse 2-D results to 1-D** — 将二维数组输出为一维数组 off（默认） | on

选中此复选框可将二维数组输出为一维数组，其中包含按列主序排列的二维数组元素。

### **Sample time** — 指定模块中的采样时间 标量

**注意**

除非将此参数显式设置为 `-1` 以外的值，否则此参数在模块对话框中不可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。
## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

### R2022b：将被移除

Interpreted MATLAB Function 模块将在未来版本中移除。建议改用内置模块。如果建模需要 MATLAB 代码，请使用 MATLAB Function 模块。您也可以考虑将函数编写为 MEX 文件 S-function，并使用 S-Function 模块实现。

## 描述

（将被移除）将 MATLAB 函数或表达式应用于输入

Interpreted MATLAB Function 模块将指定的 MATLAB® 函数或表达式应用于输入。函数的输出必须与模块的输出维度匹配。仅在当前工作区中使用 Interpreted MATLAB Function 模块。

此模块的一些有效表达式为：

```
sin
atan2(u(1), u(2))
u(1)^u(2)
```

**注意**

此模块速度较慢，因为它在每个积分步中调用 MATLAB 解析器。请考虑改用内置模块，例如 Math Function 模块。或者，您可以将函数编写为 MEX 文件 S-function，然后使用 S-Function 模块访问它。
