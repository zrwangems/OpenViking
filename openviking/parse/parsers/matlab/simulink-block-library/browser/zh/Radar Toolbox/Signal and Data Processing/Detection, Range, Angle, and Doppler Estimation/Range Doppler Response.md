---
type: simulink-block
title: 'Range-Doppler Response'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Range and Doppler Estimation'
documentation_page: 'rangedopplerresponse'
documentation_source_path: 'ref/rangedopplerresponse.html'
language: zh-CN
chinese_source: worker-translation
---

# Range-Doppler Response

## 端口

### 输入

### **X** — 输入复数值 *K*-by-*L* 矩阵 | *K*-by-*N*-by-*L* 数组

输入数据，指定为复数值
*K*-by-*L* 矩阵或
*K*-by-*N*-by-*L*
数组，其中

- *K* 表示快时间采样点数。
- *N* 表示通道（如波束或传感器）的数量。当 *N* 为 1 时，仅存在一个数据通道。
- *L* 表示用于匹配滤波处理的脉冲数以及用于 FFT 处理的扫频数。

**数据类型：** `single` | `double`

### **Coeff** — 匹配滤波器系数列向量

匹配滤波器系数，指定为列向量。

#### 依赖关系

要启用此端口，请将 **距离处理方法** 设置为 `Matched filter`。

**数据类型：** `single` | `double`

### **XRef** — 参考信号向量

参考信号，指定为

#### 依赖关系

要启用此端口，请将 **距离处理方法** 设置为 `FFT`，然后选中 **输入信号去调频** 复选框。

**数据类型：** `double`

### **PRF** — 脉冲重复频率，正标量

脉冲重复频率，指定为正标量。
`prf` 必须小于或等于 `SampleRate` 属性中指定的采样率除以输入信号 `x` 第一个维度的长度所得的商。可以将此参数指定为 single 或 double 精度。

#### 依赖关系

要启用此端口，请将 **脉冲重复频率的来源** 下拉菜单设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Resp** — 距离-多普勒响应，复数

距离-多普勒响应，以复数值
*M*-by-*P* 矩阵或
*M*-by-*N*-by-*P*
数组形式返回。

### **Range** — 距离采样向量

对距离-多普勒响应进行求值所用的距离采样点。输出为长度为 *M* 的列向量。

**数据类型：** `double`

### **Dop** — 多普勒或速度采样向量

对距离-多普勒响应进行求值所用的多普勒采样点或速度采样点，以长度为 *P* 的列向量形式返回。`Dop` 包含多普勒采样点还是速度采样点取决于 **多普勒输出** 参数。

**数据类型：** `double`

## 参数

### **测量模式** — 测量模式 `Monostatic`（默认） | `Bistatic`

测量模式，指定为 `Monostatic` 或 `Bistatic`。设置为 `Monostatic` 时，距离测量值为单基地距离。设置为 `Bistatic` 时，距离测量值为双基地距离。

**示例：** `Bistatic`

**数据类型：** `char` | `string`

### **距离处理方法** — 距离处理方法 `Matched filter`（默认） | `FFT`

将距离处理方法指定为 `Matched filter` 或 `FFT`

|  |  |
| --- | --- |
| `Matched filter` | 对输入信号应用匹配滤波器。该技术通常用于脉冲信号，其中匹配滤波器是发射信号的时间反转。选择此选项会创建 `Coeff` 输入端口。 |
| `FFT` | 通过对输入信号应用 FFT 来执行距离处理。这种方法通常用于 FMCW 信号和线性 FM 脉冲信号。 |

### **传播速度 (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认） | 正标量

信号传播速度，指定为实数正标量。光速的默认值是
`physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **继承采样率** — 从上游模块继承采样率 on（默认） | off

选中此参数可从上游模块继承采样率。否则，请使用 **采样率 (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **采样率 (Hz)** — 信号的采样率 `1e6`（默认） | 正实数标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **继承采样率** 复选框。

**数据类型：** `double`

### **参考距离 (m)** — 参考距离 `0`（默认）

将距离网格的参考距离指定为非负标量。

- 如果将 **距离处理方法** 参数设置为 `Matched filter`，则参考距离设置为距离网格的起点。
- 如果将 **距离处理方法** 属性设置为 `FFT`，则参考距离取决于 **在中心设置参考距离** 复选框。

  - 选中 **在中心设置参考距离** 复选框时，参考距离设置为距离网格的中心。
  - 如果未选中 **在中心设置参考距离** 复选框，则参考距离设置为距离网格的起点。

  单位为米。

### **脉冲重复频率的来源** — 脉冲重复频率的来源 `Auto`（默认） | `Property` | `Input port`

将脉冲重复频率的来源指定为

- `Auto` — 自动计算脉冲重复频率 (PRF)。PRF 为信号采样率除以输入端口信号 `X` 的行数。
- `Property` — 使用 `PRF` 参数指定脉冲重复频率。
- `Input port` — 使用 `PRF` 输入端口指定 PRF。

当无法根据信号持续时间确定脉冲重复频率时（例如距离选通数据的情况），请使用 `Property` 或 `Input port` 选项。

### **输入信号的脉冲重复频率 (Hz)** — 输入信号的脉冲重复频率 `10e3`（默认）

将输入信号的脉冲重复频率指定为正标量。`PRF` 必须小于或等于采样率除以输入信号的行数所得的商。当信号长度可变时，请改用输入信号可能具有的最大行数。

#### 依赖关系

要启用此参数，请将 **脉冲重复频率的来源** 参数设置为 `Property`。

### **多普勒处理中 FFT 长度的来源** — 多普勒处理中 FFT 长度的来源 `Auto`（默认） | `Property`

指定模块如何确定多普勒处理中使用的 FFT 长度。此参数的值为

|  |  |
| --- | --- |
| `Auto` | FFT 长度等于输入信号的行数。 |
| `Property` | 由此模块的 **多普勒处理中的 FFT 长度** 参数指定 FFT 长度。 |

### **多普勒处理中的 FFT 长度** — 多普勒处理中的 FFT 长度 `1024`

将多普勒处理中使用的 FFT 长度指定为正整数。

#### 依赖关系

仅当将 **多普勒处理中 FFT 长度的来源** 设置为 `Property` 时，才会显示此参数。

### **多普勒处理窗口** — 多普勒处理窗口 `None`（默认） | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

将多普勒处理所用的窗口指定为以下值之一

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

如果将此参数设置为 `Taylor`，则生成的 Taylor 窗在主瓣旁有四个近似恒定的旁瓣。

### **多普勒旁瓣衰减电平** — 多普勒旁瓣衰减电平 `30`（默认）

将旁瓣衰减电平指定为正标量，单位为分贝。

#### 依赖关系

仅当 **多普勒处理窗口** 设置为 `Kaiser`、`Chebyshev` 或 `Taylor` 时，才会显示此参数。

### **多普勒输出** — 多普勒输出 `Frequency`（默认） | `Range rate` | `Speed`

多普勒域输出，通过 **Dop** 输出端口返回。输出类型可以为 `Frequency`、`Range rate` 或 `Speed`。

|  |  |
| --- | --- |
| `Frequency` | **Dop** 为多普勒频移。单位为 Hz。 |
| `Range rate` | **Dop** 为相应的径向距离变化率，当目标接近雷达时，该值为负。单位为米每秒。 |
| `Speed` | **Dop** 为径向速度，当目标接近雷达时，该值为正。单位为米每秒。 |

#### 依赖关系

要将此参数设置为 `"Speed"`，请将 `Mode` 参数设置为 `"Monostatic"`。

### **信号载波频率 (Hz)** — 信号载波频率 `3e8`（默认） | 正标量

信号载波频率，指定为正标量。单位为 Hz。

**数据类型：** `double`

### **FM 扫频斜率 (Hz/s)** — FM 扫频斜率 `1e9`（默认）

将线性 FM 扫频的斜率指定为标量，单位为赫兹每秒。

#### 依赖关系

仅当将 **距离处理方法** 设置为 `FFT` 时，才会显示此参数。

### **输入信号去调频** — 输入信号去调频 off（默认） | on

选中此复选框可使模块对输入信号执行去调频操作。清除此复选框表示输入信号已经去调频，无需执行去调频操作。

#### 依赖关系

仅当将 **距离处理方法** 设置为 `FFT` 时，才会显示此复选框。

### **距离处理中 FFT 长度的来源** — 距离处理中 FFT 长度的来源 `Auto`（默认） | `Property`

指定模块如何确定距离处理中的 FFT 长度。此参数的值为

|  |  |
| --- | --- |
| `Auto` | FFT 长度等于输入信号的行数。 |
| `Property` | FFT 长度由 **距离处理中的 FFT 长度** 指定。 |

#### 依赖关系

仅当将 **距离处理方法** 设置为 `FFT` 时，才会显示此参数。

### **距离处理中的 FFT 长度** — 距离处理中的 FFT 长度 `1024`（默认）

将距离域中的 FFT 长度指定为正整数。

#### 依赖关系

仅当将 **距离处理方法** 设置为 `FFT` 并将 **距离处理中 FFT 长度的来源** 设置为 `Property` 时，才会显示此参数。

### **距离处理窗口** — 距离处理窗口 `None`（默认） | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

将距离处理所用的窗口指定为以下值之一

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

如果将此参数设置为 `Taylor`，则生成的 Taylor 窗在主瓣旁有四个近似恒定的旁瓣。

#### 依赖关系

仅当将 **距离处理方法** 设置为 `FFT` 时，才会显示此参数。

### **在中心设置参考距离** — 在中心设置参考距离 on（默认） | off

在距离网格的中心设置参考距离，指定为 `on` 或 `off`。选中此复选框后，可以将参考距离设置在距离网格的中心。否则，参考距离设置为距离网格的起点。

### **距离旁瓣衰减电平** — 距离旁瓣衰减电平 `30`（默认）

将旁瓣衰减电平指定为正标量，单位为分贝。

#### 依赖关系

仅当将 **距离处理方法** 设置为 `FFT` 并将 **距离处理窗口** 设置为 `Kaiser`、`Chebyshev` 或 `Taylor` 时，才会显示此参数。

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块以编译代码的形式运行，请选择 `Code Generation`。编译代码需要编译时间，但通常运行速度更快。

在开发和调优模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。与解释执行相比，长时间仿真使用生成的代码运行速度更快。无需重新编译即可重复执行，但如果更改任何模块参数，模块会在执行前自动重新编译。

下表显示了 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
| `Code Generation` | 模块将被编译。 | 模型中的所有模块都将被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中推出**

## 描述

距离-多普勒响应

Range-Doppler Response 模块计算输入信号的距离-多普勒图。输出响应是一个矩阵，其行表示距离门，列表示多普勒单元。
