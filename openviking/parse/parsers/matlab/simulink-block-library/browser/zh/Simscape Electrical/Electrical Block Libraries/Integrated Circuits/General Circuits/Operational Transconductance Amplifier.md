---
type: simulink-block
title: 'Operational Transconductance Amplifier'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Integrated Circuits / General Circuits'
documentation_page: 'operationaltransconductanceamplifier'
documentation_source_path: 'ref/operationaltransconductanceamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Operational Transconductance Amplifier

## 端口

### 守恒端口

### **+** — 同相输入电端口

与运算放大器同相输入端关联的电气守恒端口。

### **-** — 负电压电端口

与运算放大器反相输入端关联的电气守恒端口。

### **C** — 控制电流电端口

与运算放大器控制电流关联的电气守恒端口。

### **OUT** — 输出电流电端口

与运算放大器输出关联的电气守恒端口。该端口名称在模块图标上隐藏，但你可以在仿真数据日志中看到它。

## 参数

### 标称测量

### **Transconductance** — 跨导 `9600` `uS`（默认）

当控制电流等于 **Reference control current** 时的跨导 *g*m。这是跨导电流 *i*gm 与 `+` 和 `-` 引脚两端电压差 *v* 之比。

### **Input resistance** — 输入电阻 `25` `kOhm`（默认）

当控制电流等于 **Reference control current** 时的输入电阻 *R*in。输入电阻是 `+` 和 `-` 引脚两端电压差 *v* 与从 `+` 引脚流向 `-` 引脚的电流之比。

### **Output resistance** — 输出电阻 `3` `MOhm`（默认）

当控制电流等于 **Reference control current** 时的输出电阻 *R*out。有关定义输出电阻的方程，请参见上文。

### **Reference control current** — 参考控制电流 `500` `uA`（默认）

给出 **Transconductance**、**Input resistance** 和 **Output resistance** 时所对应的控制电流。

### 动态

### **Dynamics** — 动态 `No lag`（默认） | `Finite bandwidth with slew rate limiting`

选择以下选项之一：

- `No lag` — 不建模输出电流与输入电压之间关系的动态。这是默认值。
- `Finite bandwidth with slew rate limiting` — 使用一阶滞后建模输出电流与输入电压之间关系的动态。如果选择此选项，**Bandwidth**、**Maximum current slew rate** 和 **Initial current** 参数将出现在 **Dynamics** 选项卡上。

### **Bandwidth** — 一阶滞后的带宽 `2` `MHz`（默认）

用于建模输出电流与输入电压之间关系动态的一阶滞后的带宽。

#### 依赖项

仅当 **Dynamics** 参数设置为 `Finite bandwidth with slew rate limiting` 时，此参数可见。

### **Maximum current slew rate** — 跨导电流的最大变化率 `2` `A/us`（默认）

当器件周围没有反馈时，跨导电流的最大变化率。注意，数据手册有时将压摆率表示为电压的最大变化率。在这种情况下，该值取决于特定测试电路。要获得 **Maximum current slew rate** 的准确值，请在 Simscape™ Electrical™ 模型中复现测试电路，并调整参数值以匹配数据手册中的值。如果测试电路为开环，并且给出了负载电阻，则可以通过将电压压摆率除以负载电阻来获得 **Maximum current slew rate** 的近似值。

#### 依赖项

仅当 **Dynamics** 参数设置为 `Finite bandwidth with slew rate limiting` 时，此参数可见。

### **Initial current** — 初始跨导电流 `0` `A`（默认）

初始跨导电流（注意，不是初始输出电流）。这是流入内部输出电阻 *R*out 和输出引脚的跨导电流。

#### 依赖项

仅当 **Dynamics** 参数设置为 `Finite bandwidth with slew rate limiting` 时，此参数可见。

### 限值

### **Minimum output voltage** — 最小输出电压 `-15` `V`（默认）

输出电压被限制为大于此参数的值。

### **Maximum output voltage** — 最大输出电压 `15` `V`（默认）

输出电压被限制为小于此参数的值。

### **Additional output resistance at voltage swing limits** — 电压摆幅限值处的附加输出电阻 `1` `Ohm`（默认）

为限制输出电压摆幅，当输出电压超过限值时，在输出与电源轨之间施加一个附加输出电阻。该电阻值应相对于输出电阻和电路负载电阻较低。

### **Minimum control current for simulation** — 仿真用最小控制电流 `0.001` `uA`（默认）

在控制电流引脚 `C` 处测得的控制电流被限制为大于此参数的值。这可防止在基于控制电流值计算输入和输出电阻值时出现潜在的除零。

## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

运算跨导放大器的行为表示

Operational Transconductance Amplifier 模块提供运算跨导放大器的行为表示。跨导放大器将输入电压转换为输出电流。应用包括可变频率振荡器、可变增益放大器和电流控制滤波器。这些应用利用了跨导增益是流入控制电流引脚的电流的函数这一事实。

为了支持更快的仿真，行为表示不对详细的晶体管实现进行建模。因此，该模型仅在器件工作于线性区时有效，即器件的输入电阻、输出电阻和跨导增益均线性依赖于控制电流，并且与输入信号幅度无关。动态基于你为模块参数 **Bandwidth** 指定的值，通过一阶滞后近似。

### 控制电流

控制电流引脚 `C` 被保持在您为 **Minimum output voltage** 指定的电压。在实践中，**Minimum output voltage** 等于负电源电压加上晶体管集电极-发射极电压降。例如，如果 +-15V 电源电压下的 **Minimum output voltage** 为 -14.5，那么要实现 500μA 的控制电流，连接在 +15V 电源轨与控制电流引脚之间的电阻值必须为 (15 - (-14.5)) / 500e-6 = 59kOhm。

### 跨导

输入电压 *v* 与跨导电流 *i*gm 之间的关系为：

v=v+−v−igm=gm⋅vgm=gm0⋅icic0

其中：

- *v*+ 是模块 `+` 引脚处的电压。
- *v*– 是模块 `-` 引脚处的电压。
- *g*m 是跨导。
- *i*c 是流入控制电流引脚 `C` 的控制电流。
- *i*c0 是参考控制电流，即数据手册中给出跨导时所对应的控制电流。
- *g*m0 是在参考控制电流 *i*c0 下测得的跨导。

因此，增大控制电流会增大跨导。

### 输出电阻与确定输出电流

输出电阻 *R*out 由下式定义：

igm+io=voRoutRout=Rout0⋅ic0ic

其中：

- *i*gm 是跨导电流。
- *i*o 是输出电流，如果流入跨导放大器输出引脚，则定义为正。
- *i*c 是流入控制电流引脚 `C` 的控制电流。
- *i*c0 是参考控制电流，即数据手册中给出输出电阻时所对应的控制电流。
- *R*out0 是在参考控制电流 *i*c0 下测得的输出电阻。

因此，增大控制电流会降低输出电阻。

### 输入电阻

`+` 和 `-` 引脚两端输入电压 *v* 与流过的电流 *i* 之间的关系为：

vi=RinRin=Rin0⋅ic0ic

其中：

- *i*c 是流入控制电流引脚 `C` 的控制电流。
- *R*in 是当前控制电流值 *i*c 下的输入电阻。
- *i*c0 是参考控制电流，即数据手册中给出输入电阻时所对应的控制电流。
- *R*in0 是在参考控制电流 *i*c0 下测得的输入电阻。

因此，增大控制电流会降低输入电阻。

### 限值

由于基于电流镜的运算跨导放大器的物理构造，跨导电流 *i*gm 不能超过控制电流。因此，*i*gm 的值受下式限制：

|  |  |
| --- | --- |
| –*i*c ≤ *i*gm ≤ *i*c | **(1)** |

输出电压还受电源电压限制：

|  |  |
| --- | --- |
| *V*min ≤ *v*o ≤ *V*max | **(2)** |

其中 *V*min 是 **Minimum output voltage**，*V*max 是 **Maximum output voltage**。当超过电压限值时，通过向输出添加一个低电阻来实现输出电压限幅。该电阻的值由 **Additional output resistance at voltage swing limits** 参数设置。

跨导电流还受到压摆率限制，数据手册中通常会给出压摆率限制值：

−μ≤digmdt≤μ

其中 *μ* 是 **Maximum current slew rate**。
