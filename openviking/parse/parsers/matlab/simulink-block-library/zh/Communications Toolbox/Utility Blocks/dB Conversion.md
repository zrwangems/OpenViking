---
type: simulink-block
title: 'dB Conversion'
family: 'math-functions'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Math Operations'
documentation_page: 'dbconversion'
documentation_source_path: '../dsp/ref/dbconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# dB Conversion

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要转换的输入信号，指定为实数标量、向量或矩阵。

当输入信号参数设置为：

- `Power` — 输入被视为功率信号，以 Watts 为单位指定。
- `Amplitude` — 输入被视为电压信号，以 Volts 为单位指定。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

转换后的输出信号，以标量、向量或矩阵形式返回。输出与输入具有相同的大小和数据类型。输出 `y` 的计算如下。

当输入信号参数设置为 `Power` 且 **转换为** 参数设置为：

- `dB` — 该模块执行此 dB 转换：

  ```
  y = 10*log10(u)
  ```
- `dBm` — 该模块执行此 dBm 转换：

  ```
  y = 10*log10(u) + 30
  ```

dBm 转换等效于将输入转换为 milliwatts 后执行 dB 运算。

输入 *u* 是以 Watts 为单位指定的实数、非负功率信号。

当 **输入信号** 参数设置为 `Amplitude` 且 **转换为** 参数设置为：

- `dB` — 该模块执行此 dB 转换：

  ```
  y = 10*log10(abs(u)^2/R)
  ```
- `dBm` — 该模块执行以下 dBm 转换：

  ```
  y = 10*log10(abs(u)^2/R) + 30
  ```

输入 *u* 是以 Volts 为单位指定的实数电压信号。

dBm 转换等效于将 `(abs(u)^2/R)` 结果转换为 milliwatts 后执行 dB 运算。缩放因子 R 以 Ohms 为单位指定。

**数据类型：** `single` | `double`

## 参数

### **转换为** — 要转换的信号 `dB`（默认）| `dBm`

输入转换到的对数缩放，`dB` 或 `dBm`。对于转换为 dB，参考功率为 1 Watt；对于转换为 dBm，参考功率为 1 mW。

幅度转换使用由 **负载电阻** 参数以 ohms 指定的缩放因子 *R*，将电压输入转换为功率单位（watts），然后再转换为 dB 或 dBm。

当输入信号参数设置为 `Power` 且 **转换为** 参数设置为：

- `dB` — 该模块执行此 dB 转换：

  ```
  y = 10*log10(u)
  ```
- `dBm` — 该模块执行此 dBm 转换：

  ```
  y = 10*log10(u) + 30
  ```

dBm 转换等效于将输入转换为 milliwatts 后执行 dB 运算。

输入 *u* 是以 Watts 为单位指定的实数、非负功率信号。

**输入信号** 设置为 `Amplitude`，且 **转换为** 参数设置为：

- `dB` — 该模块执行此 dB 转换：

  ```
  y = 10*log10(abs(u)^2/R)
  ```
- `dBm` — 该模块执行此 dBm 转换：

  ```
  y = 10*log10(abs(u)^2/R) + 30
  ```

dBm 转换等效于将 `(abs(u)^2/R)` 结果转换为 mW 后执行 dB 运算。缩放因子 *R* 以 Ohms 为单位指定。

输入 *u* 是以 Volts 为单位指定的实数电压信号。

**可调：** Yes

### **输入信号** — 信号类型 `Amplitude`（默认）| `Power`

输入信号的类型，`Power` 或 `Amplitude`。

当 **输入信号** 设置为：

- `Power` –– 输入 *u* 是实数、非负的功率信号（单位为 Watts）。
- `Amplitude` –– 输入 *u* 是实数电压信号（单位为 Volts）。

### **负载电阻 (ohms)** — 缩放因子 `1`（默认）| 正标量 | 正整数

缩放因子 *R*，以 ohms 为单位指定。该模块使用缩放因子将电压输入转换为功率单位（watts），然后再转换为 dB 或 dBm。

**可调：** Yes

#### 依赖关系

要启用此参数，请将输入信号参数设置为 `Amplitude`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** Yes

### **向输入添加 eps 以防止 "log(0) = -inf"** — 添加 eps `off`（默认）| `on`

选择此参数会将 `eps` 添加到所有输入值（功率或电压）。

**可调：** Yes

## 所属库

DSP System Toolbox / Math Functions / Math Operations Communications Toolbox / Utility Blocks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将幅度数据转换为分贝（dB 或 dBm）

dB Conversion 模块将线性缩放的功率或幅度输入转换为 dB 或 dBm。对于转换为 dB，参考功率为 1 Watt；对于转换为 dBm，参考功率为 1 mWatt。该模块的 **输入信号** 参数指定输入是功率信号还是电压信号，**转换为** 参数控制输出的缩放。选中时，**向输入添加 eps 以防止 “log(0) = -inf”** 参数会将 `eps` 值添加到所有功率和电压输入。未选中此参数时，零值输入会在输出端产生 `-``Inf`。
