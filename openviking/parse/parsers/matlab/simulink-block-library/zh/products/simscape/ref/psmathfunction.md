---
type: simulink-block
title: 'PS Math Function'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Functions'
documentation_page: 'psmathfunction'
documentation_source_path: 'ref/psmathfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Math Function

## 端口

### 输入

### **I** — 输入物理信号，*u*，无类型物理信号

操作数物理信号 *u* 的输入端口。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### 输出

### **O** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过单击模块对话框的**描述**选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

### **Function choice** — 要对操作数信号执行的函数 `sin(u)`（默认）| `cos(u)` | `exp(u)` | `log(u)` | `10.^u` | `log10(u)` | `u.^2` | `sqrt(u)` | `1./u` | `tanh(u)` | `u.^v`

选择要执行的函数。模块输出是该函数对输入信号的值和单位进行运算的结果。

### **v** — 幂 `1`（默认）| 标量、向量或矩阵

对于 `u.^v` 选项，输出信号的值是输入信号 *`u`* 的值的 **v** 次幂。如果 **v** 是向量或矩阵，则其大小必须与输入信号 *`u`* 的大小匹配，或者 *`u`* 必须是标量。

输出信号的单位是该函数对输入信号单位进行运算的结果。因此，除非输入信号无单位，否则更改 **v** 的值会更改输出信号的单位。

#### 依赖项

要启用此参数，请将 **Function choice** 设置为 `u.^v`。

## 所属库

Simscape / Foundation Library / Physical Signals / Functions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含未进行单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅《升级包含旧版物理信号模块的模型》。

## 描述

对输入物理信号应用数学函数

PS Math Function 模块将数学函数应用于输入物理信号 *u* 的值和单位。模块输出是该函数对输入进行运算的结果。您可以从 **Function choice** 参数列表中选择以下函数之一。

| 函数 | 描述 | 数学表达式 |
| --- | --- | --- |
| `sin(u)` | 正弦 | sin(*u*) |
| `cos(u)` | 余弦 | cos(*u*) |
| `exp(u)` | 指数 | e*u* |
| `log(u)` | 自然对数 | ln(*u*) |
| `10.^u` | 以 10 为底的幂 | 10*u* |
| `log10(u)` | 常用（以 10 为底）对数 | log(*u*) |
| `u.^2` | 二次幂 | *u*2 |
| `sqrt(u)` | 平方根 | *u*0.5 |
| `1./u` | 倒数 | 1/*u* |
| `tanh(u)` | 双曲正切 | tanh(*u*) |
| `u.^v` | 幂 | *u**v* |

当输入超出所用特定函数的预期域时，PS Math Function 模块会发出仿真时错误。例如，如果设置为 `sqrt(u)`，则当 PS Math Function 模块在仿真期间收到负输入时，会发出错误。

**注意**

对于 `u.^2`、`sqrt(u)`、`1./u` 和 `u.^v`，输出信号的单位是该函数对输入信号单位进行运算的结果。因此，对于 `u.^v`，除非输入信号无单位，否则更改 **v** 的值会更改输出信号的单位。对于列表中的所有其他函数，输入信号必须无单位。
