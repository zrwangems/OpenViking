---
type: simulink-block
title: 'Clarke to Park Angle Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'clarketoparkangletransform'
documentation_source_path: 'ref/clarketoparkangletransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Clarke to Park Angle Transform

## 端口

### 输入

### **αβ0** — *α*-*β* 轴和零分量向量

静止参考系中两相系统的 alpha 轴 *α*、beta 轴 *β* 和零分量。

#### 依赖关系

要启用此端口，请清除 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数，或选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Three inputs`。*（自 R2025a 起）*

**数据类型：** `single` | `double`

### **α** — Alpha 轴分量标量

*自 R2025a 起*

静止参考系中的 alpha 轴分量 *α*。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **β** — Beta 轴分量标量

*自 R2025a 起*

静止参考系中的 beta 轴分量 *β*。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **θe** — 旋转角度标量 | 以弧度为单位

旋转参考系的角位置。此参数的值等于 *abc* 参考系中 *a* 相向量到 *dq0* 参考系初始对齐轴的极距。

#### 依赖关系

要启用此端口，请清除 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数，或选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Theta input** 设置为 `Electrical position`。*（自 R2025a 起）*

**数据类型：** `single` | `double`

### **sinθe** — 旋转角度的正弦值标量

*自 R2025a 起*

变换角度 *θe* 的正弦值。*θe* 是旋转参考系与 *α* 轴之间的夹角。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Theta input** 设置为 `Sine and Cosine electrical position`。

**数据类型：** `single` | `double`

### **cosθe** — 旋转角度的余弦值标量

*自 R2025a 起*

变换角度 *θe* 的余弦值。*θe* 是旋转参考系与 *α* 轴之间的夹角。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Theta input** 设置为 `Sine and Cosine electrical position`。

**数据类型：** `single` | `double`
### 输出

### **dq0** — *d*-*q* 轴和零分量向量

旋转参考系中系统的直轴分量、交轴分量和零分量。

#### 依赖关系

要启用此端口，请清除 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数，或选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Three inputs`。*（自 R2025a 起）*

**数据类型：** `single` | `double`

### **d** — 直轴分量标量

*自 R2025a 起*

旋转 *dq* 参考系中的直轴分量 *d*。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

### **q** — 交轴分量标量

*自 R2025a 起*

旋转 *dq* 参考系中的交轴分量 *q*。

#### 依赖关系

要启用此端口，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Number of inputs** 设置为 `Two inputs`。

**数据类型：** `single` | `double`

## 参数

### **Alpha-axis alignment** — *dq0* 参考系对齐方式 `Q-axis`（默认）| `D-axis`

将 *abc* 参考系的 *a* 相向量对齐到旋转参考系的 *d* 轴或 *q* 轴。

### **Use block for embedded implementation (requires Motor Control Blockset™)** — 使用模块进行嵌入式实现的选项 `off`（默认）| `on`

*自 R2025a 起*

使用模块进行嵌入式实现的选项。此选项需要 Motor Control Blockset™ 工具箱。

### **Number of inputs** — 模块输入数量 `Two inputs`（默认）| `Three inputs`

*自 R2025a 起*

选择可以指定的输入数量：

- `Two inputs` — 将模块配置为接受两个独立的输入信号 *α* 和 *β*。模块生成两个独立的输出信号 *d* 和 *q*。
- `Three inputs` — 将模块配置为接受包含 *α*、*β* 和 *0* 信号的多路复用输入。模块生成包含 *d*、*q* 和 *0* 信号的多路复用输出。

#### 依赖关系

要启用此参数，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数。

### **Theta input** — 位置输入类型 `Sine and Cosine electrical position`（默认）| `Electrical position`

*自 R2025a 起*

位置（theta）输入类型：

- `Sine and Cosine electrical position` — 将模块配置为直接接受 *sinθe* 和 *cosθe* 输入。
- `Electrical position` — 将模块配置为接受电位置（*θe*）输入。模块根据 *θe* 输入在内部计算 *sinθe* 和 *cosθe* 信号。

#### 依赖关系

要启用此参数，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数。

### **Theta units** — 电位置输入的单位 `Per-unit`（默认）| `Radians` | `Degrees`

*自 R2025a 起*

电位置输入 *θe* 的单位。

#### 依赖关系

要启用此参数，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Theta input** 设置为 `Electrical position`。

### **Number of data points for lookup table** — 查找表数组的大小 `1024`（默认）| 标量

*自 R2025a 起*

模块用于根据 *θe* 输入计算 *sinθe* 和 *cosθe* 信号的查找表数组的大小。可以指定 125 到 4095 之间的值。

#### 依赖关系

要启用此参数，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数并将 **Theta input** 设置为 `Electrical position`。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：针对嵌入式实现优化模块

如果拥有 Motor Control Blockset 工具箱的许可证，可以针对嵌入式实现优化 Clarke to Park Angle Transform 模块。要针对嵌入式实现优化此模块，请选中 **Use block for embedded implementation (requires Motor Control Blockset™)** 参数。

## 描述

实现 αβ0 到 dq0 变换

Clarke to Park Angle Transform 模块将静止参考系中的 alpha、beta 和零分量转换为旋转参考系中的直轴、交轴和零分量。

该模块接受以下输入：

- 静止参考系中的 *α-β* 轴分量或多路复用分量 *αβ0*。使用 **Number of inputs** 参数选择使用两个或三个输入。
- 相应变换角度的正弦和余弦值。

对于平衡三相系统，零分量等于零。

可以将模块配置为在时间 *t* = 0 时将三相系统的 *a* 相轴对齐到旋转参考系的 *q* 轴或 *d* 轴。图中显示了三相系统中定子绕组的磁轴方向、静止 *αβ0* 参考系和旋转 *dq0* 参考系，其中：

- *a* 轴和 *q* 轴初始对齐。
- *a* 轴和 *d* 轴初始对齐。

在两种情况下，角度 *θ* = *ω**t*，其中

- *θ* 是 *q* 轴对齐时 *a* 轴与 *q* 轴之间的夹角，或 *d* 轴对齐时 *a* 轴与 *d* 轴之间的夹角。
- *ω* 是 *d*-*q* 参考系的旋转速度。
- *t* 是从初始对齐开始的时间，单位为 s。

图中显示了等效平衡 *αβ0* 和 *dq0* 各分量的时间响应，针对以下情况：

- *a* 相向量对齐到 *q* 轴
- *a* 相向量对齐到 *d* 轴

### 方程

Clarke to Park Angle Transform 模块针对 *a* 相到 *q* 轴对齐实现以下变换：

[dq0]=[sin(θ)−cos(θ)0cos(θ)sin(θ)0001][αβ0]

其中：

- *α* 和 *β* 是静止参考系中两相系统的 alpha 轴和 beta 轴分量。
- *0* 是零分量。
- *d* 和 *q* 是旋转参考系中两轴系统的直轴和交轴分量。

对于 *a* 相到 *d* 轴对齐，模块使用以下方程实现变换：

[dq0]=[cos(θ)sin(θ)0−sin(θ)cos(θ)0001][αβ0]
