---
type: simulink-block
title: 'Inverse Clarke Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inverseclarketransform'
documentation_source_path: 'ref/inverseclarketransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Clarke Transform

## 端口

### 输入

### **αβ0** — *α*-*β* 轴和零分量向量

静止参考系中的 α 轴分量 *α*、β 轴分量 *β* 和零分量。

#### 依赖关系

要启用此端口，请清除 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数，或选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Three inputs`。*（自 R2025a 起）*

**数据类型：** `single` | `double`

### **α** — α 轴分量标量

*自 R2025a 起*

静止参考系中的 α 轴分量 *α*。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **β** — β 轴分量标量

*自 R2025a 起*

静止参考系中的 β 轴分量 *β*。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`
### 输出

### **abc** — *a*、*b* 和 *c* 相分量向量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请清除 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数，或选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Three inputs`。*（自 R2025a 起）*

**数据类型：** `single` | `double`

### **a** — *a* 相分量标量

*自 R2025a 起*

*abc* 参考系中三相系统的 *a* 相分量。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **b** — *b* 相分量标量

*自 R2025a 起*

*abc* 参考系中三相系统的 *b* 相分量。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **c** — *c* 相分量标量

*自 R2025a 起*

*abc* 参考系中三相系统的 *c* 相分量。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

## 参数

### **Power Invariant** — 启用功率不变性 `off`（默认）| `on`

用于在旋转参考系中保持系统有功功率和无功功率的选项。

### **Use block for embedded implementation (requires Motor Control Blockset™)** — 使用模块进行嵌入式实现的选项 `off`（默认）| `on`

*自 R2025a 起*

使用模块进行嵌入式实现的选项。此选项需要 Motor Control Blockset 工具箱。

### **Number of inputs** — 模块输入数量 `Two inputs`（默认）| `Three inputs`

*自 R2025a 起*

选择可以指定的输入数量：

- `Two inputs` — 将模块配置为接受两个单独的输入信号 *α* 和 *β*。模块生成三个单独的输出信号 *a*、*b* 和 *c*。
- `Three inputs` — 将模块配置为接受包含 *α*、*β* 和 *0* 信号的多路复用输入。模块生成包含 *a*、*b* 和 *c* 信号的多路复用输出。

#### 依赖关系

要启用此参数，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：为嵌入式实现优化模块

如果您拥有 Motor Control Blockset 工具箱的许可证，则可以为嵌入式实现优化 Inverse Clarke Transform 模块。要为嵌入式实现优化此模块，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数。

## 描述

实现 αβ0 到 abc 变换

Inverse Clarke Transform 模块将静止参考系中的时域 α、β 和零分量转换为 *abc* 参考系中的三相分量。该模块可以通过实现功率不变版本的逆 Clarke 变换，使有功功率和无功功率与静止参考系中系统的功率保持一致。如果零分量为零，则三相系统中的分量是平衡的。

如果您拥有 Motor Control Blockset™ 工具箱的许可证，则可以将此模块用于嵌入式实现。使用 **Number of inputs** 参数指定两个或三个输入。当您将 **Number of inputs** 参数设置为 `Two inputs` 时，模块接受三相（*abc*）中的两个信号，自动计算第三个信号，并输出 *αβ* 参考系中的对应分量。*（自 R2025a 起）*

图中显示了：

- 静止参考系中的平衡 *ɑ*、*β* 和零分量
- 静止 *ɑβ0* 参考系和 *abc* 参考系中定子绕组磁轴的方向
- 等效平衡 *ɑβ0* 和 *abc* 系统各分量的时间响应

### 方程

该模块将逆 Clarke 变换实现为

[abc]=[101−12321−12−321][αβ0]

其中：

- *α* 和 *β* 是静止参考系中的分量。
- *0* 是静止参考系中的零分量。
- *a*、*b* 和 *c* 是 *abc* 参考系中三相系统的分量。

该模块将此功率不变版本的逆 Clarke 变换实现为

[abc]=23[1012−123212−12−3212][αβ0]
