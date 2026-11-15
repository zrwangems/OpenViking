---
type: simulink-block
title: 'Clarke Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'clarketransform'
documentation_source_path: 'ref/clarketransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Clarke Transform

## 端口

### 输入

### **abc** — *a*、*b* 和 *c* 相分量向量

三相系统在 *abc* 参考坐标系中的分量。

#### 依赖关系

要启用此端口，请清除 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数，或者选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Three inputs`。*（自 R2025a 起）*

**数据类型：** `single` | `double`

### **a** — *a* 相分量标量

*自 R2025a 起*

三相系统在 *abc* 参考坐标系中的 *a* 相分量。

#### 依赖关系

要启用此端口，请选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **b** — *b* 相分量标量

*自 R2025a 起*

三相系统在 *abc* 参考坐标系中的 *b* 相分量。

#### 依赖关系

要启用此端口，请选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### 输出

### **αβ0** — *α*-*β* 轴和零分量向量

静止参考坐标系中的 Alpha 轴分量 *α*、Beta 轴分量 *β* 和零分量。

#### 依赖关系

要启用此端口，请清除 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数，或者选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Three inputs`。*（自 R2025a 起）*

**数据类型：** `single` | `double`

### **α** — Alpha 轴分量标量

*自 R2025a 起*

静止参考坐标系中的 Alpha 轴分量 *α*。

#### 依赖关系

要启用此端口，请选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **β** — Beta 轴分量标量

*自 R2025a 起*

静止参考坐标系中的 Beta 轴分量 *β*。

#### 依赖关系

要启用此端口，请选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

## 参数

### **Power Invariant** — 启用功率不变性 `off`（默认）| `on`

用于保持系统在 *abc* 参考坐标系中的有功功率和无功功率的选项。

### **Use block for embedded implementation (requires Motor Control Blockset™)** — 将模块用于嵌入式实现的选项 `off`（默认）| `on`

*自 R2025a 起*

将模块用于嵌入式实现的选项。此选项需要 Motor Control Blockset 工具箱。

### **Number of inputs** — 模块输入的数量 `Two inputs`（默认）| `Three inputs`

*自 R2025a 起*

选择可指定的输入数量：

- `Two inputs` — 将模块配置为接受两个单独的输入信号 *a* 和 *b*。模块生成两个单独的输出信号 *α* 和 *β*。
- `Three inputs` — 将模块配置为接受包含 *a*、*b* 和 *c* 信号的多路复用输入。模块生成包含 *α*、*β* 和 *0* 信号的多路复用输出。

#### 依赖关系

要启用此参数，请选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：为嵌入式实现优化模块

如果您拥有 Motor Control Blockset 工具箱许可证，则可以为嵌入式实现优化 Clarke Transform 模块。要为嵌入式实现优化此模块，请选择 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数。

## 描述

实现 abc 到 αβ0 变换

Clarke Transform 模块将三相系统在 *abc* 参考坐标系中的时域分量转换为静止 *ɑβ0* 参考坐标系中的分量。该模块可以通过实现 Clarke 变换的功率不变版本，使有功功率和无功功率与系统在 *abc* 参考坐标系中的功率保持一致。对于平衡系统，零分量等于零。

如果您拥有 Motor Control Blockset™ 工具箱许可证，则可以将此模块用于嵌入式实现。使用 **Number of inputs** 参数指定两个或三个输入。当您将 **Number of inputs** 参数设置为 `Two inputs` 时，模块接受三相 (*abc*) 中的两个信号，自动计算第三个信号，并输出 *αβ* 参考坐标系中的对应分量。*（自 R2025a 起）*

图中显示：

- 在 *abc* 参考坐标系和静止 *ɑβ0* 参考坐标系中定子绕组的磁轴方向
- 静止参考坐标系中的等效 *ɑ*、*β* 和零分量
- 等效平衡 *abc* 和 *ɑβ0* 系统各分量的时间响应

### 方程

该模块按如下方式实现 Clarke 变换

[αβ0]=23[1−12−12032−32121212][abc],

其中：

- *a*、*b* 和 *c* 是三相系统在 *abc* 参考坐标系中的分量。
- *α* 和 *β* 是两轴系统在静止参考坐标系中的分量。
- *0* 是两轴系统在静止参考坐标系中的零分量。

该模块按如下方式实现 Clarke 变换的功率不变版本

[αβ0]=23[1−12−12032−32121212][abc].
