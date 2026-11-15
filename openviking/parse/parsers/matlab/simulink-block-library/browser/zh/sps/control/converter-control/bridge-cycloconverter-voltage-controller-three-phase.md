---
type: simulink-block
title: 'Bridge Cycloconverter Voltage Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control\u200b'
documentation_page: 'bridgecycloconvertervoltagecontrollerthreephase'
documentation_source_path: 'ref/bridgecycloconvertervoltagecontrollerthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Bridge Cycloconverter Voltage Controller (Three-Phase)

## 端口

### 输入

### **VRef** — 参考电压标量

参考线对中性点 RMS 电压，以标幺值表示。

**数据类型：** `single` | `double`

### **fRef** — 参考频率标量

参考电频率，单位为 Hz。

**数据类型：** `single` | `double`

### **vabc** — 相电压向量

电源的测量相电压，单位为 V。

**数据类型：** `single` | `double`

### **Vcyc** — 周波变换器电压向量

测量的周波变换器相电压，单位为 V。

**数据类型：** `single` | `double`

### **Icyc** — 周波变换器电流向量

测量的周波变换器相电流，单位为 A。

**数据类型：** `single` | `double`

### 输出

### **P** — 脉冲向量

用于控制三相桥式周波变换器的晶闸管脉冲向量。

**数据类型：** `single` | `double`

### **Visualization** — Visualization bus 总线

包含用于可视化的内部信号的总线。有关信号的完整列表，请参阅可视化一节。

**数据类型：** `single` | `double`

## 参数

### **Rated voltage (phase-to-phase RMS)** — 额定 RMS 电压 `6000`（默认）| 正数

用于标幺值转换计算的额定 RMS 电压，单位为 V。

### **Loop filter proportional gain** — LF 比例增益 `2`（默认）| 正数

用于估计输入信号相位的锁相环 (PLL) 的环路滤波器比例增益。该值决定 PLL 在跟踪和锁定相位角时的响应强度。增大该值可改善跟踪对相位角阶跃变化的反应时间。

### **Loop filter integral gain** — LF 积分增益 `20`（默认）| 正数

用于估计输入信号相位的锁相环 (PLL) 的环路滤波器积分增益。增大该值可提高消除相位角稳态误差的速率。该值还决定 PLL 在跟踪和锁定相位时的响应强度。

### **Filters time constant (s)** — 时间常数 `1e-2`（默认）| 正数

控制器中 Signal Conditioning 模块内低通滤波器的时间常数。这些滤波器减少周波变换器相电压和电流测量中不需要的高频噪声。

### **Controller proportional gain** — 比例增益 `1`（默认）| 正数

用于为周波变换器生成参考相电压的 PI 控制器的比例增益。增大该值可提高控制器的响应强度。

### **Controller integral gain** — 积分增益 `12`（默认）| 正数

用于为周波变换器生成参考相电压的 PI 控制器的积分增益。增大该值可提高消除相电压信号稳态误差的速率。

### **Controller anti-windup gain** — 抗积分饱和增益 `10`（默认）| 正数

用于为周波变换器生成参考相电压的 PI 控制器的抗积分饱和增益。

### **Thyristor pulse width (rad)** — 脉冲宽度 `5*pi/6`（默认）| 正数

发送到周波变换器的脉冲的角宽度。

### **Bank selector current threshold (A)** — 电流阈值 `5`（默认）| 正数

在正变换器和负变换器之间切换的电流阈值。

### **Pulse ordering** — 脉冲排序规则 `Sequential device order`（默认）| `Natural order of commutation`

用于生成脉冲排序的策略。

### **Sample time (-1 for inherited)** — 采样时间 `-1`（默认）| 正数

模块的采样时间（-1 表示继承）。如果在触发子系统内使用此模块，请将采样时间设置为 `-1`。如果在连续变步长模型中使用此模块，请显式设置采样时间。

## 所属库

Simscape / Electrical / Control / Converter Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

用于三相桥式周波变换器的 RMS 电压 PI 控制

Bridge Cycloconverter Voltage Controller (Three-Phase) 模块为三相桥式周波变换器实现基于 PI 的均方根 (RMS) 电压控制器。

要将三相信号直接从较高频率转换为较低频率，请将此模块与三相桥式周波变换器配合使用。有关此类转换的示例，请参阅 Three-Phase Bridge Cycloconverter。

### 工作原理

控制器将周波变换器的线对中性点 RMS 电压调节到给定值和给定电频率。周波变换器控制器的结构如本图所示。

图中：

- 控制器对所需输出频率 *fref* 进行积分，以产生参考电角度 *θe\_ref*。
- Signal Conditioning 模块对周波变换器的线对中性点电压 *vcyc* 和电流 *icyc* 进行滤波，以产生标幺值 RMS 电压 *vrms\_cyc* 和平滑电流信号 *icyc\_lpf*。
- PI Controller 根据所需输出 RMS 电压 *Vref* 与 *vrms\_cyc* 之间的误差，生成 *q* 轴上的参考相电压。
- Inverse Park Transform 模块将 *dq0* 坐标中的参考相电压转换为 *abc* 坐标中的相电压 *vabc\_ref*。
- Sinusoidal Power Measurement (PLL, Three-Phase) 模块估计输入电压信号 *vabc* 的相位角 *θ*。

  Modulator 和 Bank Selector 模块使用参考相电压 *vabc\_ref*、估计相位角 *θ* 和滤波后的周波变换器电流 *icyc\_lpf* 生成 36 个脉冲以驱动周波变换器。为生成触发角，控制器使用余弦波交叉法。

此图展示了信号调理逻辑。

图中：

- Park Transform 模块使用参考电角度 *θe\_ref* 将测量的周波变换器电压 *vcyc* 和电流 *icyc* 转换为 *d* 轴和 *q* 轴分量（*vd*、*vq*、*id*、*iq*）。
- Low-Pass Filter (LPF) 模块去除 *d* 轴和 *q* 轴电压和电流中的高频噪声，以产生滤波后的分量（*vd\_lpf*、*vq\_lpf*、*id\_lpf*、*iq\_lpf*）。
- 该模块通过对 *dq* 分量求平方和、除以 2，最后从 SI 转换为标幺值表示，来计算周波变换器标幺值 RMS 电压 *vrms\_cyc*。
- Inverse Park Transform 将 *dq* 滤波后的电流转换回 *abc* 轴，并将其输出为 *icyc\_lpf*。

周波变换器参考线对中性点 RMS 电压输出以标幺值表示。

### 可视化

该模块输出一个包含六个用于可视化的信号的总线：

- 输入电压信号 *vabc* 的估计相位角 *θ*
- 输出信号的所需 RMS 电压 *Vref*
- 所需输出信号的参考相电压 *vabc\_ref*
- 滤波后的线对中性点周波变换器 RMS 电压 *vrms\_cyc*
- 滤波后的周波变换器相电流 *icyc\_lpf*
- 滤波后的周波变换器相电压 *vcyc\_lpf*
