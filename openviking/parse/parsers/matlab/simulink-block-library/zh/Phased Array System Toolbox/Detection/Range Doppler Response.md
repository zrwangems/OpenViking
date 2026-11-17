---
type: simulink-block
title: 'Range Doppler Response'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'rangedopplerresponse'
documentation_source_path: '../radar/../phased/ref/rangedopplerresponse.html'
language: zh-CN
chinese_source: worker-translation
---

# Range Doppler Response

## 端口
```yaml
ports:
- name: X
  summary: 输入复值 *K*×*L* 矩阵 | *K*×*N*×*L* 数组
  direction: input
  data_types: single | double
- name: Coeff
  summary: 匹配滤波器系数 列向量
  direction: input
  data_types: single | double
- name: XRef
  summary: 参考信号 向量
  direction: input
  data_types: double
- name: PRF
  summary: 脉冲重复频率 正标量
  direction: input
  data_types: double
- name: Resp
  summary: 距离-多普勒响应 复数
  direction: output
- name: Range
  summary: 距离采样 向量
  direction: output
  data_types: double
- name: Dop
  summary: 多普勒或速度采样 向量
  direction: output
  data_types: double
```

### 输入

### **X** — 输入复值 *K*×*L* 矩阵 | *K*×*N*×*L* 数组

输入数据，指定为复值 *K*×*L* 矩阵或 *K*×*N*×*L* 数组，其中

- *K* 表示快时间采样数。
- *N* 表示通道数，例如波束或传感器。当 *N* 为 1 时，仅存在单个数据通道。
- *L* 表示用于匹配滤波处理的脉冲数和用于 FFT 处理的扫描数。

**数据类型：** `single` | `double`

### **Coeff** — 匹配滤波器系数 列向量

匹配滤波器系数，指定为列向量。

#### 依赖关系

要启用此端口，请将**距离处理方法**设置为 `Matched filter`。

**数据类型：** `single` | `double`

### **XRef** — 参考信号 向量

参考信号，指定为

#### 依赖关系

要启用此端口，请将**距离处理方法**设置为 `FFT`，然后选中**去调频输入信号**复选框。

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

脉冲重复频率，指定为正标量。`prf` 必须小于或等于 `SampleRate` 属性中指定的采样率除以输入信号 `x` 第一维的长度。您可以将此参数指定为单精度或双精度。

#### 依赖关系

要启用此端口，请将**脉冲重复频率来源**下拉菜单设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Resp** — 距离-多普勒响应 复数

距离-多普勒响应，返回为复值 *M*×*P* 矩阵或 *M*×*N*×*P* 数组。

### **Range** — 距离采样 向量

评估距离-多普勒响应时所对应的距离采样。输出为长度为 *M* 的列向量。

**数据类型：** `double`

### **Dop** — 多普勒或速度采样 向量

评估距离-多普勒响应时所对应的多普勒采样或速度采样。返回为长度为 *P* 的列向量。`Dop` 包含多普勒采样还是速度采样取决于**多普勒输出**参数。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Measurement mode
  summary: 测量模式 Monostatic（默认）| Bistatic
  group: ''
- name: Range processing method
  summary: 距离处理方法 Matched filter（默认）| FFT
  group: ''
- name: Propagation speed (m/s)
  summary: 信号传播速度 physconst('LightSpeed')（默认）| 正标量
  group: ''
- name: Inherit sample rate
  summary: 从上游模块继承采样率 on（默认）| off
  group: ''
- name: Sample rate (Hz)
  summary: 信号采样率 1e6（默认）| 正实值标量
  group: ''
- name: Reference range (m)
  summary: 参考距离 0（默认值）
  group: ''
- name: Source of pulse repetition frequency
  summary: 脉冲重复频率来源 Auto（默认值）| Property | Input port
  group: ''
- name: Pulse repetition frequency of the input signal (Hz)
  summary: 输入信号的脉冲重复频率 10e3（默认值）
  group: ''
- name: Source of FFT length in Doppler processing
  summary: 多普勒处理中 FFT 长度的来源 Auto（默认值）| Property
  group: ''
- name: FFT length in Doppler processing
  summary: 多普勒处理中的 FFT 长度 1024
  group: ''
- name: Doppler processing window
  summary: 多普勒处理窗 None（默认值）| Hamming | Chebyshev | Hann | Kaiser | Taylor
  group: ''
- name: Doppler sidelobe attenuation level
  summary: 多普勒旁瓣衰减电平 30（默认值）
  group: ''
- name: Doppler output
  summary: 多普勒输出 Frequency（默认值）| Range rate | Speed
  group: ''
- name: 信号载波频率 (Hz)
  summary: 信号载波频率 3e8（默认）| 正标量
  group: ''
- name: FM 扫频斜率 (Hz/s)
  summary: FM 扫频斜率 1e9（默认）
  group: ''
- name: 去线性调频输入信号
  summary: 去线性调频输入信号 关（默认）| 开
  group: ''
- name: 距离处理中 FFT 长度的来源
  summary: 距离处理中 FFT 长度的来源 Auto（默认）| Property
  group: ''
- name: 距离处理中的 FFT 长度
  summary: 距离处理中的 FFT 长度 1024（默认）
  group: ''
- name: 距离处理窗
  summary: 距离处理窗 None（默认）| Hamming | Chebyshev | Hann | Kaiser | Taylor
  group: ''
- name: 在中心设置参考距离
  summary: 在中心设置参考距离 开（默认）| 关
  group: ''
- name: 距离旁瓣衰减电平
  summary: 距离旁瓣衰减电平 30（默认）
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
  default: Interpreted Execution
```

### **Measurement mode** — 测量模式 `Monostatic`（默认）| `Bistatic`

测量模式，指定为 `Monostatic` 或 `Bistatic`。当设置为 `Monostatic` 时，距离测量为单基地距离。当设置为 `Bistatic` 时，距离测量为双基地距离。

**示例：** `Bistatic`

**数据类型：** `char` | `string`

### **Range processing method** — 距离处理方法 `Matched filter`（默认）| `FFT`

将距离处理方法指定为 `Matched filter` 或 `FFT`

|  |  |
| --- | --- |
| `Matched filter` | 对输入信号应用匹配滤波器。此技术通常用于脉冲信号，其中匹配滤波器是发射信号的时间反转。选择此选项将创建 `Coeff` 输入端口。 |
| `FFT` | 通过对输入信号应用 FFT 来执行距离处理。此方法通常用于 FMCW 和线性调频脉冲信号。 |

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认）| 正标量

信号传播速度，指定为实值正标量。光速的默认值为 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用**采样率 (Hz)**参数指定采样率。

**数据类型：** `Boolean`

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除**继承采样率**复选框。

**数据类型：** `double`

### **Reference range (m)** — 参考距离 `0`（默认值）

将距离网格的参考距离指定为非负标量。

- 如果将 **Range processing method** 参数设置为 `Matched filter`，则参考距离设置为距离网格的起点。
- 如果将 **Range processing method** 属性设置为 `FFT`，则参考距离取决于 **Set reference range at center** 复选框。

  - 当选中 **Set reference range at center** 复选框时，参考距离设置为距离网格的中心。
  - 如果未选中 **Set reference range at center** 复选框，则参考距离设置为距离网格的起点。

  单位为米。

### **Source of pulse repetition frequency** — 脉冲重复频率来源 `Auto`（默认值）| `Property` | `Input port`

将脉冲重复频率的来源指定为

- `Auto` — 自动计算脉冲重复频率（PRF）。PRF 是信号的采样率除以输入端口信号 `X` 的行数。
- `Property` — 使用 `PRF` 参数指定脉冲重复频率。
- `Input port` — 使用 `PRF` 输入端口指定 PRF。

当脉冲重复频率无法由信号持续时间确定时（例如距离门控数据），请使用 `Property` 或 `Input port` 选项。

### **Pulse repetition frequency of the input signal (Hz)** — 输入信号的脉冲重复频率 `10e3`（默认值）

将输入信号的脉冲重复频率指定为正标量。`PRF` 必须小于或等于采样率除以输入信号的行数。当信号长度可变时，请改用输入信号可能的最大行数。

#### 依赖关系

要启用此参数，请将 **Source of pulse repetition frequency** 参数设置为 `Property`。

### **Source of FFT length in Doppler processing** — 多普勒处理中 FFT 长度的来源 `Auto`（默认值）| `Property`

指定模块如何确定多普勒处理中使用的 FFT 长度。此参数的值为

|  |  |
| --- | --- |
| `Auto` | FFT 长度等于输入信号的行数。 |
| `Property` | 此模块的 **FFT length in Doppler processing** 参数指定 FFT 长度。 |

### **FFT length in Doppler processing** — 多普勒处理中的 FFT 长度 `1024`

将多普勒处理中使用的 FFT 长度指定为正整数。

#### 依赖关系

仅当将 **Source of FFT length in Doppler processing** 设置为 `Property` 时，此参数才会显示。

### **Doppler processing window** — 多普勒处理窗 `None`（默认值）| `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

使用以下选项之一指定用于多普勒处理的窗

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

如果将此参数设置为 `Taylor`，则生成的 Taylor 窗在主瓣附近有四个近似恒定的旁瓣。

### **Doppler sidelobe attenuation level** — 多普勒旁瓣衰减电平 `30`（默认值）

将旁瓣衰减电平指定为正标量，单位为分贝。

#### 依赖关系

仅当 **Doppler processing window** 设置为 `Kaiser`、`Chebyshev` 或 `Taylor` 时，此参数才会显示。

### **Doppler output** — 多普勒输出 `Frequency`（默认值）| `Range rate` | `Speed`

多普勒域输出，在 **Dop** 输出端口返回。输出类型可以是 `Frequency`、`Range rate` 或 `Speed`。

|  |  |
| --- | --- |
| `Frequency` | **Dop** 是多普勒频移。单位为 Hz。 |
| `Range rate` | **Dop** 是对应的径向距离变化率，当目标接近雷达时为负。单位为米每秒。 |
| `Speed` | **Dop** 是径向速度，当目标接近雷达时为正。单位为米每秒。 |

#### 依赖关系

要将此参数设置为 `"Speed"`，请将 `Mode` 参数设置为 `"Monostatic"`。

### **信号载波频率 (Hz)** — 信号载波频率 `3e8`（默认）| 正标量

信号载波频率，指定为正标量。单位为 Hz。

**数据类型：** `double`

### **FM 扫频斜率 (Hz/s)** — FM 扫频斜率 `1e9`（默认）

指定线性 FM 扫频的斜率，单位为赫兹每秒，以标量形式指定。

#### 依赖关系

此参数仅在将 **距离处理方法** 设置为 `FFT` 时出现。

### **去线性调频输入信号** — 去线性调频输入信号 关（默认）| 开

选中此复选框可使模块对输入信号执行去线性调频操作。清除此复选框表示输入信号已完成去线性调频，无需执行去线性调频操作。

#### 依赖关系

此复选框仅在将 **距离处理方法** 设置为 `FFT` 时出现。

### **距离处理中 FFT 长度的来源** — 距离处理中 FFT 长度的来源 `Auto`（默认）| `Property`

指定模块如何确定距离处理中的 FFT 长度。此参数的值为

|  |  |
| --- | --- |
| `Auto` | FFT 长度等于输入信号的行数。 |
| `Property` | FFT 长度由 **距离处理中的 FFT 长度** 指定。 |

#### 依赖关系

此参数仅在将 **距离处理方法** 设置为 `FFT` 时出现。

### **距离处理中的 FFT 长度** — 距离处理中的 FFT 长度 `1024`（默认）

将距离域中的 FFT 长度指定为正整数。

#### 依赖关系

此参数仅在将 **距离处理方法** 设置为 `FFT` 且 **距离处理中 FFT 长度的来源** 设置为 `Property` 时出现。

### **距离处理窗** — 距离处理窗 `None`（默认）| `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

使用以下之一指定用于距离处理的窗

|  |
| --- |
| `None` |
| `Hamming` |
| `Chebyshev` |
| `Hann` |
| `Kaiser` |
| `Taylor` |

如果将此参数设置为 `Taylor`，生成的 Taylor 窗在主瓣附近有四个近似恒定的旁瓣。

#### 依赖关系

此参数仅在将 **距离处理方法** 设置为 `FFT` 时出现。

### **在中心设置参考距离** — 在中心设置参考距离 开（默认）| 关

在距离网格中心设置参考距离，指定为 `on` 或 `off`。选中此复选框可将参考距离设置在距离网格的中心。否则，参考距离设置为距离网格的起始位置。

### **距离旁瓣衰减电平** — 距离旁瓣衰减电平 `30`（默认）

将旁瓣衰减电平指定为正标量，单位为分贝。

#### 依赖关系

此参数仅在将 **距离处理方法** 设置为 `FFT` 且 **距离处理窗** 设置为 `Kaiser`、`Chebyshev` 或 `Taylor` 时出现。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间进行编译，但通常运行
更快。

当您开发和调整模型时，解释执行非常有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比在
解释执行中运行更快。您可以重复执行而无需重新编译，但如果您
更改任何模块参数，则模块会在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式
会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：enum |
| **值**：`Interpreted Execution`, `Code Generation` |
| **默认值**：`Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

距离-多普勒响应

Range-Doppler Response 模块计算输入信号的距离-多普勒图。输出响应是一个矩阵，其行表示距离门，其列表示多普勒 bin。
