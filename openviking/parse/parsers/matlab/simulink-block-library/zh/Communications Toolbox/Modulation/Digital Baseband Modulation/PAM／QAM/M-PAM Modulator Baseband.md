---
type: simulink-block
title: 'M-PAM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'mpammodulatorbaseband'
documentation_source_path: 'ref/mpammodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-PAM Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 列向量

输入信号，指定为标量或列向量。输入数据必须是二进制值或范围在 [0, (*M* – 1)] 内的整数，其中 *M* 是由 **M-ary number** 参数指定的调制阶数。此端口在模块上未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — *M*-PAM 调制基带信号 标量 | 列向量

*M*-PAM 调制基带信号，以标量或列向量形式返回。使用 **Output data type** 参数指定输出数据类型。此端口在模块上未命名。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **M-ary number** — 调制阶数 `4`（默认）| 正偶整数

调制阶数，指定为正偶整数。调制阶数 *M* 指定信号星座图中的点数。模块根据 **Normalization method** 参数的设置对信号星座图进行缩放。有关详细信息，请参阅星座图大小和缩放。

### **Input type** — 输入值类型 `Integer`（默认）| `Bit`

输入值类型，指定为 `Integer` 或 `Bit`。当您将此参数设置为 `Bit` 时，**M-ary number** 参数必须为 2*K*，其中 *K* 为某个正整数。

### **Constellation ordering** — 符号映射顺序 `Binary`（默认）| `Gray`

符号的映射顺序，指定为 `Gray` 或 `Binary`。此参数指示模块如何将二进制字映射到信号星座图的点。

- 当您将此参数设置为 `Binary` 时，模块使用二进制编码星座图。
- 当您将此参数设置为 `Gray` 时，模块使用格雷编码星座图。

### **Normalization method** — 星座图缩放方法 `Min. distance between symbols`（默认）| `Average Power` | `Peak Power`

星座图的缩放方法，指定为 `Min. distance between symbols`、`Average Power` 或 `Peak Power`。有关详细信息，请参阅星座图大小和缩放。

### **Minimum distance** — 两个最近星座点之间的距离 `2`（默认）| 正标量

两个最近星座点之间的距离，指定为正标量。

#### 依赖关系

当您将 **Normalization method** 设置为 `Min. distance between symbols` 时，此参数出现。

### **Average power, referenced to 1 ohm (watts)** — 平均功率 `1`（默认）| 正标量

星座图中符号的平均功率（以瓦特为单位），指定为正标量。功率值假定标称阻抗为 1 欧姆。

#### 依赖关系

当您将 **Normalization method** 设置为 `Average Power` 时，此参数出现。

### **Peak power, referenced to 1 ohm (watts)** — 最大功率 `1`（默认）| 正标量

星座图中符号的最大功率（以瓦特为单位），指定为正标量。功率值假定标称阻抗为 1 欧姆。

#### 依赖关系

当您将 **Normalization method** 设置为 `Peak Power` 时，此参数出现。

### **View Constellation** — 绘制参考星座图的选项 按钮

单击模块掩码上的 **View Constellation**，以可视化指定模块参数的信号星座图。在查看星座图之前，请应用参数设置。有关详细信息，请参阅查看调制器模块的星座图。

### 数据类型

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

输出数据类型，指定为 `double`、`single`、`fixdt(1,16)`、`fixdt(1,16,0)`、`Inherit: Inherit via back propagation` 或 `<data type expression>`。

- `fixdt(1,16)`、`fixdt(1,16,0)` 或 `<data type expression>` 会启用可进一步指定细节的参数。
- `Inherit: Inherit via back propagation` 将输出数据类型和定标设置为与下一个模块匹配。

有关指定数据类型的信息，请参阅数据类型助手。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / AM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 如果 ''input type'' 设置为 ''bit''，则输入为 ufix(1)。如果 ''input type'' 设置为 ''integer'' 以进行 M 进制调制，则输入为 ufix(ceil(log2(M)))。  b 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 M 进制脉冲幅度调制进行调制

M-PAM Modulator Baseband 模块使用 *M* 进制脉冲幅度调制对信号进行调制。输出是调制信号的基带表示。

**注意**

所有功率值均假定标称阻抗为 1 欧姆。
