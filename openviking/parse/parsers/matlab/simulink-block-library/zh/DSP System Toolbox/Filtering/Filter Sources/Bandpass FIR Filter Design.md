---
type: simulink-block
title: 'Bandpass FIR Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'bandpassfirfilterdesign'
documentation_source_path: 'ref/bandpassfirfilterdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Bandpass FIR Filter Design

## 端口
```yaml
ports:
- name: N
  summary: 滤波器阶数 偶数正整数
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Fc
  summary: 滤波器中心频率 小于或等于 1 的正标量
  direction: input
  data_types: single | double
- name: BW
  summary: 滤波器带宽 小于或等于 1 的正标量
  direction: input
  data_types: single | double
- name: r
  summary: 旁瓣衰减（以 dB 为单位） 正标量
  direction: input
  data_types: single | double
- name: beta
  summary: Kaiser 窗参数 非负标量
  direction: input
  data_types: single | double
- name: Num
  summary: 分子系数 行向量
  direction: output
  data_types: single | double
```

### 输入

### **N** — 滤波器阶数 偶数正整数

将滤波器阶数指定为小于或等于 *Nmax* 的偶数正整数，其中 *Nmax* 是您在 **Filter maximum order (must be even)** 参数中指定的值。您可以在仿真期间更改通过此端口输入的滤波器阶数。

#### 依赖关系

要启用此端口，请选中 **Specify filter order from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Fc** — 滤波器中心频率 小于或等于 1 的正标量

以归一化频率单位将滤波器的中心频率指定为小于或等于 `1` 的正标量。您可以在仿真期间更改通过此端口输入的中心频率。

#### 依赖关系

要启用此端口，请选中 **Specify center frequency from input port** 参数。

**数据类型：** `single` | `double`

### **BW** — 滤波器带宽 小于或等于 1 的正标量

以归一化频率单位将滤波器的带宽指定为小于或等于 `1` 的正标量。您可以在仿真期间更改通过此端口输入的带宽。

#### 依赖关系

要启用此端口，请选中 **Specify bandwidth from input port** 参数。

**数据类型：** `single` | `double`

### **r** — 旁瓣衰减（以 dB 为单位） 正标量

将 Chebyshev 类型滤波器的旁瓣衰减指定为以 dB 为单位的正标量。您可以在仿真期间更改通过此端口输入的旁瓣衰减。

#### 依赖关系

要启用此端口：

- 将 **Window function** 参数设置为 `Chebyshev`。
- 选中 **Specify sidelobe attenuation from input port** 参数。

**数据类型：** `single` | `double`

### **beta** — Kaiser 窗参数 非负标量

将 Kaiser 窗参数指定为非负标量。您可以在仿真期间更改通过此端口输入的 Kaiser 窗参数。

#### 依赖关系

要启用此端口：

- 将 **Window function** 参数设置为 `Kaiser`。
- 选中 **Specify kaiser window parameter from input port** 参数。

**数据类型：** `single` | `double`
### 输出

### **Num** — 分子系数 行向量

分子系数，以长度为 *Nmax* + 1 的行向量形式返回，其中 *Nmax* 是您使用 **Filter maximum order (must be even)** 参数指定的最大滤波器阶数。

此方程表示分子系数向量 **b**。

b=[b0,b1,b2,...,bNmax]

此方程表示传递函数形式的 FIR 滤波器。

H(z)=b0+b1z−1+b2z−2+...+bNmaxz−Nmax

当实际滤波器阶数 *N* 小于最大滤波器阶数 *Nmax* 时，向量中最后的 *Nmax* − *N* 个元素为值为 0 的平凡元素。

此端口的数据类型取决于 **Output data type** 参数的值。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Smooth tuned filter parameters
  summary: 平滑可调滤波器参数 off（默认）| on
  group: ''
- name: Smoothing factor
  summary: 平滑因子 0.6（默认）| 小于 1 的非负标量
  group: ''
- name: Specify filter order from input port
  summary: 从输入端口指定滤波器阶数的标志 off（默认）| on
  group: ''
- name: Filter order (must be even)
  summary: 滤波器阶数 100（默认）| 偶数正整数
  group: ''
- name: Filter maximum order (must be even)
  summary: 滤波器最大阶数 100（默认）| 偶数正整数
  group: ''
- name: Specify center frequency from input port
  summary: 从输入端口指定中心频率的标志 off（默认）| on
  group: ''
- name: Center frequency
  summary: 中心频率 0.5（默认）| 小于或等于 1 的正标量
  group: ''
- name: Specify bandwidth from input port
  summary: 从输入端口指定带宽的标志 off（默认）| on
  group: ''
- name: Bandwidth
  summary: 滤波器带宽 0.1（默认）| 小于或等于 1 的正标量
  group: ''
- name: Window function
  summary: 窗函数 Hann（默认）| Hamming | Blackman | Blackman-Harris | Chebyshev | Kaiser
  group: ''
- name: Specify sidelobe attenuation from input port
  summary: 从输入端口指定旁瓣衰减的标志 off（默认）| on
  group: ''
- name: Sidelobe attenuation (dB)
  summary: 旁瓣衰减（以 dB 为单位） 60（默认）| 正标量
  group: ''
- name: Specify kaiser window parameter from input port
  summary: 从输入端口指定 Kaiser 窗参数的标志 off（默认）| on
  group: ''
- name: Kaiser window parameter
  summary: Kaiser 窗参数 0.5（默认）| 非负标量
  group: ''
- name: Sample time (−1 for inherited)
  summary: 采样时间（以秒为单位） -1（默认）| 正标量 | Inf
  group: ''
- name: Output data type
  summary: 滤波器系数的数据类型 double（默认）| single
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Smooth tuned filter parameters** — 平滑可调滤波器参数 `off`（默认）| `on`

*自 R2024a 起*

当您选中此复选框时，模块通过使用参数的中间值反复设计滤波器来逐步更新可调滤波器参数（如滤波器阶数、中心频率、带宽、旁瓣衰减和 Kaiser 窗参数），直到参数达到所需值。此过程称为参数平滑。有关详细信息，请参阅 Parameter Smoothing。

当您清除此复选框时，模块会立即使用新的参数值重新设计滤波器。

### **Smoothing factor** — 平滑因子 0.6（默认）| 小于 1 的非负标量

*自 R2024a 起*

将平滑因子 *α* 指定为小于 1 的非负标量。当 *α* = 0 时，不发生平滑。随着 *α* 趋近于 1，平滑操作次数以及随之而来的滤波器重新设计次数会增加。

**可调：** 是

#### 依赖关系

要启用此参数，请选中 **Smooth tuned filter parameters** 参数。

### **Specify filter order from input port** — 从输入端口指定滤波器阶数的标志 `off`（默认）| `on`

选中此参数以从输入端口 **N** 指定滤波器阶数。当您清除此参数时，可以在模块对话框中通过 **Filter order (must be even)** 参数指定滤波器阶数。

### **Filter order (must be even)** — 滤波器阶数 `100`（默认）| 偶数正整数

将滤波器阶数指定为小于或等于 **Filter maximum order (must be even)** 参数值的偶数正整数。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify filter order from input port** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Filter maximum order (must be even)** — 滤波器最大阶数 `100`（默认）| 偶数正整数

将滤波器的最大阶数指定为偶数正整数。您在 **Filter order (must be even)** 参数中指定的值必须小于或等于您在 **Filter maximum order (must be even)** 参数中指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Specify center frequency from input port** — 从输入端口指定中心频率的标志 `off`（默认）| `on`

选中此参数以从输入端口 **Fc** 指定中心频率。当您清除此参数时，可以在模块对话框中通过 **Center frequency** 参数指定中心频率。

### **Center frequency** — 中心频率 `0.5`（默认）| 小于或等于 1 的正标量

以归一化频率单位将滤波器的中心频率指定为小于或等于 `1` 的正标量。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify center frequency from input port** 参数。

**数据类型：** `single` | `double`

### **Specify bandwidth from input port** — 从输入端口指定带宽的标志 `off`（默认）| `on`

选中此参数以从输入端口 **BW** 指定带宽。当您清除此参数时，可以在模块对话框中通过 **Bandwidth** 参数指定带宽。

### **Bandwidth** — 滤波器带宽 `0.1`（默认）| 小于或等于 1 的正标量

以归一化频率单位将滤波器的带宽指定为小于或等于 `1` 的正标量。

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Specify bandwidth from input port** 参数。

**数据类型：** `single` | `double`

### **Window function** — 窗函数 `Hann`（默认）| `Hamming` | `Blackman` | `Blackman-Harris` | `Chebyshev` | `Kaiser`

指定用于设计滤波器的窗函数：

- `Hann`
- `Hamming`
- `Blackman`
- `Blackman-Harris`
- `Chebyshev`
- `Kaiser`

### **Specify sidelobe attenuation from input port** — 从输入端口指定旁瓣衰减的标志 `off`（默认）| `on`

选中此参数以从输入端口 **r** 指定旁瓣衰减。当您清除此参数时，可以在模块对话框中通过 **Sidelobe attenuation (dB)** 参数指定旁瓣衰减。

#### 依赖关系

要启用此参数，请将 **Window function** 参数设置为 `Chebyshev`。

### **Sidelobe attenuation (dB)** — 旁瓣衰减（以 dB 为单位） `60`（默认）| 正标量

将 Chebyshev 类型 FIR 滤波器的旁瓣衰减指定为以 dB 为单位的正标量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Window function** 参数设置为 `Chebyshev`。
- 清除 **Specify sidelobe attenuation from input port** 参数。

**数据类型：** `single` | `double`

### **Specify kaiser window parameter from input port** — 从输入端口指定 Kaiser 窗参数的标志 `off`（默认）| `on`

选中此参数以从输入端口 **beta** 指定 Kaiser 窗参数。当您清除此参数时，可以在模块对话框中通过 **Kaiser window parameter** 指定 Kaiser 窗参数。

#### 依赖关系

要启用此参数，请将 **Window function** 参数设置为 `Kaiser`。

### **Kaiser window parameter** — Kaiser 窗参数 `0.5`（默认）| 非负标量

将 Kaiser 窗参数指定为非负标量。

**可调：** 是

#### 依赖关系

要启用此参数：

- 将 **Window function** 参数设置为 `Kaiser`。
- 清除 **Specify kaiser window parameter from input port** 参数。

**数据类型：** `single` | `double`

### **Sample time (−1 for inherited)** — 采样时间（以秒为单位） `-1`（默认）| 正标量 | `Inf`

将采样时间指定为 `-1`（继承）、`Inf`（常量采样时间）或正标量。此参数决定模块在仿真期间何时产生输出并更新其内部状态。有关更多详细信息，请参阅 What Is Sample Time? (Simulink)。

**数据类型：** `single` | `double`

### **Output data type** — 滤波器系数的数据类型 `double`（默认）| `single`

指定模块通过 **Num** 端口输出的滤波器系数的数据类型。您可以将数据类型设置为 `double` 或 `single`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，C 代码会在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Filtering / Filter Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当您从此模块生成代码时，可以在生成的代码中调整滤波器设计规格。

## 版本历史

**在 R2023b 中引入**

### R2024a：**Simulate using** 参数默认值变更

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，模块默认使用 MATLAB 解释器进行仿真。

### R2024a：Tunable Bandpass FIR Filter 模块已重命名

Tunable Bandpass FIR Filter 已重命名为 Bandpass FIR Filter Design 模块。

### R2024a：支持平滑可调滤波器参数

当可调滤波器参数（如滤波器阶数、中心频率、带宽、旁瓣衰减和 Kaiser 窗参数）在仿真期间发生变化时，模块可以平滑这些参数，直到参数达到所需值。有关详细信息，请参阅 Parameter Smoothing。

## 描述

设计具有可调滤波器规格的带通 FIR 滤波器

使用 Bandpass FIR Filter Design 模块，通过 Hann、Hamming、Blackman、Blackman-Harris、Chebyshev 和 Kaiser 加窗方法设计带通 FIR 滤波器。您可以在仿真期间调整滤波器阶数、中心频率、带宽和旁瓣衰减。当这些参数的值发生变化时，模块会重新设计滤波器并以向量形式输出分子系数。
