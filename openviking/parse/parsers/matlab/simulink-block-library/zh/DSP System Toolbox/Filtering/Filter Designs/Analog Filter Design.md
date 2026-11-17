---
type: simulink-block
title: 'Analog Filter Design'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'analogfilterdesign'
documentation_source_path: 'ref/analogfilterdesign.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Filter Design

## 端口

### 输入

### **Port\_1** — 输入信号 标量

滤波器的输入信号，指定为基于采样的、连续时间、实值标量值。

**数据类型：** `double`
### 输出

### **Port\_1** — 输出信号 标量

滤波后的信号，以实数双精度标量值返回。

**数据类型：** `double`

## 参数

### **Design method** — 滤波器设计 `Butterworth`（默认）| `Chebyshev I` | `Chebyshev II` | `Elliptic` | `Bessel`

滤波器设计方法包括：

- `Butterworth` — Butterworth 滤波器的幅值响应在通带内最大平坦，整体单调。Butterworth 设计使用工具箱函数 `butter`。
- `Chebyshev I` — Chebyshev I 滤波器的幅值响应在通带内等波纹，在阻带内单调。Chebyshev I 设计使用工具箱函数 `cheby1`。
- `Chebyshev II` — Chebyshev II 滤波器的幅值响应在通带内单调，在阻带内等波纹。Chebyshev II 设计使用工具箱函数 `cheby2`。
- `Elliptic` — 椭圆滤波器的幅值响应在通带和阻带内均为等波纹。椭圆设计使用工具箱函数 `ellip`。
- `Bessel` — Bessel 滤波器的幅值响应在通带内最大平坦，整体单调。该滤波器具有最大平坦的线性相位响应。Bessel 设计使用函数 `besself`。

**可调：** 是

### **Filter type** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

要设计的滤波器类型：

- `Lowpass`
- `Highpass`
- `Bandpass`
- `Bandstop`

**可调：** 是

### **Filter order** — 滤波器阶数 `8`（默认）| 标量值

当 `Filter type` 设置为以下值时，滤波器的阶数：

- `Lowpass`
- `Highpass`

当 **Filter type** 设置为以下值时，最终滤波器的阶数为 **Filter order** 值的*两倍*：

- `Bandpass`
- `Bandstop`

。

### **Passband edge frequency (rad/s)** — 通带边缘频率 `30`（默认）| 标量值

通带边缘频率，以 rad/s 为单位。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Butterworth`
- `Chebyshev I`
- `Elliptic`
- `Bessel`

且 `Filter type` 设置为以下值时出现：

- `Lowpass`
- `Highpass`

### **Lower passband edge frequency (rad/s)** — 通带下边缘频率 `30`（默认）| 标量值

通带下边缘频率，以 rad/s 为单位指定。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Butterworth`
- `Chebyshev I`
- `Elliptic`
- `Bessel`

且 `Filter type` 设置为以下值时出现：

- `Bandpass`
- `Bandstop`

### **Upper passband edge frequency (rad/s)** — 通带上边缘频率 `80`（默认）| 标量值

通带上边缘频率，以 rad/s 为单位指定。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Butterworth`
- `Chebyshev I`
- `Elliptic`
- `Bessel`

且 `Filter type` 设置为以下值时出现：

- `Bandpass`
- `Bandstop`

### **Stopband edge frequency (rad/s)** — 阻带边缘频率 `30`（默认）| 标量值

阻带边缘频率，以 rad/s 为单位指定。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Chebyshev II`

且 `Filter type` 设置为以下值时出现：

- `Lowpass`
- `Highpass`

### **Lower stopband edge frequency (rad/s)** — 阻带下边缘频率 `30`（默认）| 标量值

阻带下边缘频率，以 rad/s 为单位。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Chebyshev II`

且 `Filter type` 设置为以下值时出现：

- `Bandpass`
- `Bandstop`

### **Upper stopband edge frequency (rad/s)** — 阻带上边缘频率 `80`（默认）| 标量值

阻带上边缘频率，以 rad/s 为单位指定。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Chebyshev II`

且 `Filter type` 设置为以下值时出现：

- `Bandpass`
- `Bandstop`

### **Passband ripple in dB** — 通带波纹 `2`（默认）| 标量值

通带波纹，以 dB 为单位指定。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Chebyshev I`
- `Elliptic`

### **Stopband attenuation in dB** — 阻带衰减 `40`（默认）| 标量值

阻带衰减，以 dB 为单位。

**可调：** 是

#### 依赖关系

此参数仅在 `Design method` 设置为以下值时出现：

- `Chebyshev II`
- `Elliptic`

## 所属库

DSP System Toolbox / Filtering / Filter Designs

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块不建议用于生产代码生成。

请考虑使用 Model Discretizer (Simulink) 将此连续模块映射为支持代码生成的离散等效模块。要访问 Model Discretizer，请在 **Apps** 选项卡上的 **Apps** 下，在 **Control Systems** 下，点击 **Model Discretizer**。

## 版本历史

**在 R2006a 之前引入**

## 描述

设计并实现模拟滤波器

Analog Filter Design 模块以高通、低通、带通或带阻配置设计并实现 Butterworth、Chebyshev I 型、Chebyshev II 型、椭圆或 Bessel 滤波器。

您可以从对话框中的 `Design method` 和 `Filter type` 下拉列表中选择滤波器的设计和频带配置。对于每种设计方法和频带配置的组合，都会显示一组相应的辅助参数。有关更多详细信息，请参阅设计/频带组合表。

Analog Filter Design 模块使用状态空间滤波器表示，并使用 Simulink® Continuous 库中的 State-Space (Simulink) 模块来应用滤波器。所有设计方法都使用 Signal Processing Toolbox™ 函数来设计滤波器。

Analog Filter Design 模块基于 Signal Processing Toolbox 软件的滤波器设计功能构建。

**注意**

Analog Filter Design 模块不能与 Simulink 离散求解器一起使用，当您在 **Model Configuration Parameters** 对话框的 **Solver** 窗格中将 **Solver** 列表设置为 `Discrete (no continuous states)` 时，该求解器会被启用。请改为选择一种连续求解器（例如 `ode4`）。
