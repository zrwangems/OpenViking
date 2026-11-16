---
type: simulink-block
title: 'DVBS-APSK Modulator Baseband'
family: 'satcom'
product_id: 'satcom'
product_name: 'Satellite Communications Toolbox'
documentation_release: R2025b
official_category: 'Signal Transmission'
documentation_page: 'dvbsapskmodulatorbaseband'
documentation_source_path: 'ref/dvbsapskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# DVBS-APSK Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。输入信号必须是二进制值或范围 [0, (*M* – 1)] 内的整数，其中 *M* 是 **调制阶数**。此端口在模块上未命名。

**注意**

要将输入信号作为二进制元素处理，请将 **输入类型** 参数值设置为 `Bit`。对于二进制输入，行数必须是 log2(*M*) 的整数倍。一列中每组 log2(*M*) 个比特映射到一个符号，第一个比特表示 MSB，最后一个比特表示 LSB。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — DVB-S2/S2X/SH 标准特定的 APSK 调制信号 标量 | 向量 | 矩阵

DVB-S2/S2X/SH 标准特定的 APSK 调制信号，返回为复标量、向量或矩阵。输出信号维度取决于指定的 **输入类型** 值。此端口在模块上未命名。

| **输入类型** | 输出信号维度 |
| --- | --- |
| `Integer` | 输出信号与输入信号具有相同的维度。 |
| `Bit` | 输出信号的行数等于输入信号的行数除以 log2(*M*)，其中 *M* 是 **调制阶数**。 |

使用 **输出数据类型** 指定输出数据类型。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **DVB 标准后缀** — 标准后缀 `S2`（默认） | `S2X` | `SH`

DVB 调制变体的标准后缀，指定为 `S2`、`S2X` 或 `SH`。

### **帧长度** — 帧长度 `Normal`（默认） | `Short`

帧长度，指定为 `Normal` 或 `Short`。

#### 依赖关系

此参数仅在 **DVB 标准后缀** 设置为 `S2` 或 `S2X` 时适用。

### **调制阶数** — 调制阶数 `16`（默认） | `8` | `32` | `64` | `256`

调制阶数 *M*，指定为 2 的幂。调制阶数指定输出信号星座图中的总点数。有效调制阶数列表因 **DVB 标准后缀** 和 **帧长度** 的值而异。

| **DVB 标准后缀** | **帧长度** | **调制阶数** 选项 |
| --- | --- | --- |
| `S2` | `Normal` 或 `Short` | `16` 或 `32` |
| `S2X` | `Normal` | `8`、`16`、`32`、`64` 或 `256` |
| `Short` | `16` 或 `32` |
| `SH` | 不适用 | `16` |

### **代码标识符** — 代码标识符 `2/3` | character vector

代码标识符，指定为 character vector。有效代码标识符值列表因指定的 **DVB 标准后缀**、**帧长度** 和 **调制阶数** 值而异。此表列出了 **代码标识符** 值的选项。

| **调制阶数** | **DVB 标准后缀** | **帧长度** | **代码标识符** 选项 |
| --- | --- | --- | --- |
| `8` | `S2X` | `Normal` | `100/180` 或 `104/180` |
| `16` | `S2` 或 `S2X` | `Normal` | `2/3`、`3/4`、`4/5`、`5/6`、`8/9` 或 `9/10` |
| `Short` | `2/3`、`3/4`、`4/5`、`5/6` 或 `8/9` |
| `16` | `S2X` | `Normal` | `26/45`、`3/5`、`28/45`、`23/36`、`25/36`、`13/18`、`140/180`、`154/180`、`100/180`、`96/180`、`90/180`、`18/30` 或 `20/30` |
| `Short` | `7/15`、`8/16`、`26/45`、`3/5` 或 `32/45` |
| `32` | `S2` 或 `S2X` | `Normal` | `3/4`、`4/5`、`5/6`、`8/9` 或 `9/10` |
| `Short` | `3/4`、`4/5`、`5/6` 或 `8/9` |
| `32` | `S2X` | `Normal` | `128/180`、`132/180`、`140/180` 或 `2/3` |
| `Short` | `2/3` 或 `32/45` |
| `64` | `S2X` | `Normal` | `128/180` , `132/180`、`7/9`、`4/5` 或 `5/6` |
| `128` | `S2X` | `Normal` | `135/180` 或 `140/180` |
| 256 | `S2X` | `Normal` | `116/180`、`124/180`、`128/180`、`20/30` 或 `135/180` |

有关详细信息，请参阅 DVB-S2 标准 [1] 中的表 9 和表 10，以及 DVB-S2X 标准 [2] 中的表 17a。

#### 依赖关系

此参数仅在 **DVB 标准后缀** 设置为 `S2` 或 `S2X` 时适用。

### **星座图缩放** — 星座图缩放 `Outer radius as 1`（默认） | `Unit average power`

星座图缩放，指定为 `Outer radius as 1` 或 `Unit average power`。

#### 依赖关系

此参数仅在 **DVB 标准后缀** 设置为 `S2` 或 `S2X` 时适用。

### **输入类型** — 输入类型 `Integer`（默认） | `Bit`

输入类型，指定为 `Integer` 或 `Bit`。要使用 `Integer`，输入信号必须由范围 [0, (*M* – 1)] 内的整数组成。要使用 `Bit`，输入数据必须包含二进制值，并且行数必须是 log2(*M*) 的整数倍，其中 *M* 是 **调制阶数**。

### **输出数据类型** — 输出数据类型 `double`（默认） | `single`

输出数据类型，指定为 `double` 或 `single`。

### **查看星座图** — 绘制参考星座图 `button`

要绘制参考星座图，请点击 **查看星座图** 按钮。

### **仿真方式** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为：

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。

## 所属库

Satellite Communications Toolbox / Modulation / Digital Baseband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2024b：从 Communications Toolbox 移至 Satellite Communications Toolbox

以前，`DVBS-APSK Modulator Baseband` 需要 Communications Toolbox™。

## 描述

DVB-S2/S2X/SH 标准特定的 APSK 调制

DVBS-APSK Modulator Baseband 模块使用数字视频广播 (DVB-S2/S2X/SH) 标准特定的幅相键控 (APSK) 调制对输入信号进行调制。
