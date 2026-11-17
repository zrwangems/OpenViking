---
type: simulink-block
title: 'dB Conversion'
family: 'dsp'
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
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

要转换的输入信号，指定为实数标量、向量或矩阵。

当 Input signal 参数设置为：

- `Power` — 输入被视为功率信号，以瓦特为单位指定。
- `Amplitude` — 输入被视为电压信号，以伏特为单位指定。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

转换后的输出信号，以标量、向量或矩阵形式返回。输出的大小和数据类型与输入相同。输出 `y` 的计算方式如下。

当 Input signal 参数设置为 `Power` 且 **Convert to** 参数设置为：

- `dB` — 模块执行以下 dB 转换：

  ```
  y = 10*log10(u)
  ```
- `dBm` — 模块执行以下 dBm 转换：

  ```
  y = 10*log10(u) + 30
  ```

dBm 转换等效于将输入转换为毫瓦后执行 dB 运算。

输入 *u* 是实数、非负的功率信号，以瓦特为单位指定。

当 **Input signal** 参数设置为 `Amplitude` 且 **Convert to** 参数设置为：

- `dB` — 模块执行以下 dB 转换：

  ```
  y = 10*log10(abs(u)^2/R)
  ```
- `dBm` — 模块执行以下 dBm 转换：

  ```
  y = 10*log10(abs(u)^2/R) + 30
  ```

输入 *u* 是实数电压信号，以伏特为单位指定。

dBm 转换等效于将 `(abs(u)^2/R)` 结果转换为毫瓦后执行 dB 运算。比例因子 R 以欧姆为单位指定。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Convert to
  summary: 要转换的信号 dB（默认）| dBm
  group: ''
- name: Input signal
  summary: 信号类型 Amplitude（默认）| Power
  group: ''
- name: Load resistance (ohms)
  summary: 比例因子 1（默认）| 正标量 | 正整数
  group: ''
- name: Add eps to input to protect against "log(0) = -inf"
  summary: 添加 eps off（默认）| on
  group: ''
```

### **Convert to** — 要转换的信号 `dB`（默认）| `dBm`

输入转换到的对数缩放，`dB` 或 `dBm`。转换为 dB 时参考功率为 1 瓦特，转换为 dBm 时参考功率为 1 mW。

幅度转换使用 **Load resistance** 参数以欧姆指定的比例因子 *R*，在转换为 dB 或 dBm 之前将电压输入转换为功率单位（瓦特）。

当 Input signal 参数设置为 `Power` 且 **Convert to** 参数设置为：

- `dB` — 模块执行以下 dB 转换：

  ```
  y = 10*log10(u)
  ```
- `dBm` — 模块执行以下 dBm 转换：

  ```
  y = 10*log10(u) + 30
  ```

dBm 转换等效于将输入转换为毫瓦后执行 dB 运算。

输入 *u* 是实数、非负的功率信号，以瓦特为单位指定。

**Input signal** 设置为 `Amplitude` 且 **Convert to** 参数设置为：

- `dB` — 模块执行以下 dB 转换：

  ```
  y = 10*log10(abs(u)^2/R)
  ```
- `dBm` — 模块执行以下 dBm 转换：

  ```
  y = 10*log10(abs(u)^2/R) + 30
  ```

dBm 转换等效于将 `(abs(u)^2/R)` 结果转换为 mW 后执行 dB 运算。比例因子 *R* 以欧姆为单位指定。

输入 *u* 是实数电压信号，以伏特为单位指定。

**可调：** 是

### **Input signal** — 信号类型 `Amplitude`（默认）| `Power`

输入信号的类型，`Power` 或 `Amplitude`。

当 **Input signal** 设置为：

- `Power` –– 输入 *u* 是实数、非负的功率信号（单位为瓦特）。
- `Amplitude` –– 输入 *u* 是实数电压信号（单位为伏特）。

### **Load resistance (ohms)** — 比例因子 `1`（默认）| 正标量 | 正整数

比例因子 *R*，以欧姆为单位指定。模块使用该比例因子在转换为 dB 或 dBm 之前将电压输入转换为功率单位（瓦特）。

**可调：** 是

#### 依赖关系

要启用此参数，请将 Input signal 参数设置为 `Amplitude`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

### **Add eps to input to protect against "log(0) = -inf"** — 添加 eps `off`（默认）| `on`

选择此参数可将 `eps` 添加到所有输入值（功率或电压）。

**可调：** 是
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

dB Conversion 模块将线性缩放的功率或幅度输入转换为 dB 或 dBm。转换为 dB 时参考功率为 1 瓦特，转换为 dBm 时参考功率为 1 mWatt。模块的 **Input signal** 参数指定输入是功率信号还是电压信号，**Convert to** 参数控制输出的缩放。选中时，**Add eps to input to protect against “log(0) = -inf”** 参数会将 `eps` 值添加到所有功率和电压输入。未选中此参数时，零值输入会在输出端产生 `-``Inf`。
