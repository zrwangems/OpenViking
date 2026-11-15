---
type: simulink-block
title: 'SM ST7C'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control / Automatic Voltage Regulators — ST Type'
documentation_page: 'smst7c'
documentation_source_path: 'ref/smst7c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM ST7C

## 端口

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定点，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 端电压标量

端电压幅值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 端电流标量

端电流幅值，以标幺值表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励磁限制信号标量

来自过励磁限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自过励磁限制器的输入，请将 **备用 OEL 输入位置（V\_OEL）** 设置为 `Unused`。
- 要在求和点使用来自过励磁限制器的输入，请将 **备用 OEL 输入位置（V\_OEL）** 设置为 `Summation point at voltage reference`。
- 要在 Take-over Logic 子系统处使用来自过励磁限制器的输入，请将 **备用 OEL 输入位置（V\_OEL）** 设置为 `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统处使用来自过励磁限制器的输入，请将 **备用 OEL 输入位置（V\_OEL）** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励磁限制信号标量

来自欠励磁限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自欠励磁限制器的输入，请将 **备用 UEL 输入位置（V\_UEL）** 设置为 `Unused`。
- 要在求和点使用来自欠励磁限制器的输入，请将 **备用 UEL 输入位置（V\_UEL）** 设置为 `Summation point at voltage reference`。
- 要在 Take-over Logic 子系统处使用来自欠励磁限制器的输入，请将 **备用 UEL 输入位置（V\_UEL）** 设置为 `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统处使用来自欠励磁限制器的输入，请将 **备用 UEL 输入位置（V\_UEL）** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

在使用求和点时来自定子电流限制器的输入，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Unused`。
- 要在求和点使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Summation point at voltage reference`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 用于过励磁限制器的接管定子电流限制标量

在使用接管点时来自定子电流限制器的输入，用于防止磁场过励磁，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Unused`。
- 要在 Take-over Logic 子系统处使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Take-over at voltage reference`。
- 要在 Take-over Logic1 子系统处使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 用于欠励磁限制器的接管定子电流限制标量

在使用接管点时来自定子电流限制器的输入，用于防止磁场欠励磁，以标幺值表示，指定为标量。

#### 依赖关系

- 要忽略来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Unused`。
- 要在 Take-over Logic 子系统处使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Take-over at voltage error`。
- 要在 Take-over Logic1 子系统处使用来自定子电流限制器的输入，请将 **备用 SCL 输入位置（V\_SCL）** 设置为 `Take-over at voltage regulator output`。

**数据类型：** `single` | `double`

### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的标幺励磁电压，返回为标量。

**数据类型：** `single` | `double`

## 参数

### 常规

### **初始励磁电压，Efd0 (pu)** — 初始输出电压 `1`（默认） | real scalar

要施加到同步电机励磁电路的初始标幺电压。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认） | `0` | positive scalar

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅在掩码上提升模块参数。

### 预控制

### **负载补偿的电阻分量，R\_C (pu)** — 补偿电阻 `0`（默认） | positive scalar

电流补偿系统中使用的电阻。将此参数和 **负载补偿的电抗分量，X\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **负载补偿的电抗分量，X\_C (pu)** — 补偿电抗 `0`（默认） | positive scalar

电流补偿系统中使用的电抗。将此参数和 **负载补偿的电阻分量，R\_C (pu)** 设置为 `0` 以禁用电流补偿。

### **调节器输入滤波器时间常数，T\_R (s)** — 调节器时间常数 `0`（默认） | positive scalar

电压换能器滤波的等效时间常数。

### 控制

### **调节器输入滤波器时间常数，T\_G (s)** — 电压滤波时间常数 `1`（默认） | positive scalar

电压滤波的等效时间常数。

### **电压调节器分母（滞后）时间常数，T\_F (s)** — 电压调节器的滞后时间常数 `1`（默认） | positive scalar

电压调节器的等效滞后时间常数，以秒为单位。

### **最大电压参考值，V\_max (pu)** — 最大电压参考 `1.1`（默认） | real scalar

电压调节器的最大标幺电压参考值。

### **最小电压参考值，V\_min (pu)** — 最小电压参考 `0.9`（默认） | real scalar

电压调节器的最小标幺电压参考值。

### **电压调节器增益，K\_PA (pu)** — 电压调节器增益 `40`（默认） | positive scalar

电压调节器的标幺增益。

### **电压调节器分母（滞后）时间常数，T\_B (s)** — 电压调节器滞后时间常数 `1`（默认） | positive scalar

电压调节器的等效滞后时间常数。当附加滞后动态可忽略时，请将此参数设置为 `0`。

### **电压调节器分子（超前）时间常数，T\_C (s)** — 电压调节器超前时间常数 `1`（默认） | positive scalar

电压调节器的等效超前时间常数。当附加超前动态可忽略时，请将此参数设置为 `0`。

### **晶闸管桥触发控制等效时间常数，T\_A (s)** — 第一个超前-滞后环节的调节器滞后时间常数 `0`（默认） | positive scalar

晶闸管桥触发控制中的等效时间常数。

### **调节器最大输出，V\_Rmax (pu)** — 调节器最大输出 `5`（默认） | real scalar

调节器的最大标幺输出。

### **调节器最小输出，V\_Rmin (pu)** — 调节器最小输出 `-4.5`（默认） | real scalar

调节器的最小标幺输出。

### **备用 OEL 输入位置（V\_OEL）** — OEL 输入位置 `Unused`（默认） | `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

过励磁限制器输入位置，指定为以下选项之一：

- `Summation point at voltage reference` — **V\_OEL** 是 Summation Point Logic 子系统的输入。
- `Take-over at voltage reference` — **V\_OEL** 是 Take-over Logic 子系统的输入。
- `Take-over at voltage regulator output` — **V\_OEL** 是 Take-over Logic 1 子系统的输入。

### **备用 UEL 输入位置（V\_UEL）** — UEL 输入位置 `Unused`（默认） | `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

欠励磁限制器输入位置，指定为以下选项之一：

- `Summation point at voltage reference` — **V\_UEL** 是 Summation Point Logic 子系统的输入。
- `Take-over at voltage reference` — **V\_UEL** 是 Take-over Logic 子系统的输入。
- `Take-over at voltage regulator output` — **V\_UEL** 是 Take-over Logic 1 子系统的输入。

### **备用 SCL 输入位置（V\_SCL）** — SCL 输入位置 `Unused`（默认） | `Summation point at voltage reference` | `Take-over at voltage reference` | `Take-over at voltage regulator output`

定子电流限制器输入位置。指定为以下选项之一：

- `Summation point` — 使用 **V\_SCLsum** 输入端口。
- 任意 `Take-over` 选项 — 使用 **V\_SCLoel** 和 **V\_SCLuel** 输入端口。

### 励磁机

### **最小励磁限制增益，K\_L (pu)** — 最小励磁限制增益 `1`（默认） | real scalar

励磁机的最小标幺增益。

### **最大励磁限制增益，K\_H (pu)** — 最大励磁限制增益 `1`（默认） | real scalar

励磁机的最大标幺增益。

### **PI 调节器反馈增益，K\_IA (pu)** — PI 调节器反馈增益 `1`（默认） | real scalar

PI 调节器的标幺反馈增益。

### **PI 调节器反馈时间常数，T\_IA (s)** — PI 调节器反馈时间常数 `3`（默认） | positive scalar

PI 调节器的反馈时间常数，以秒为单位。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 ST7C 静态励磁系统，带有自动电压调节器

SM ST7C 模块实现符合 IEEE Std 421.5-2016 [1] 的同步电机型 ST7C 静态励磁系统模型。

使用此模块对同步电机的励磁电压的控制和调节进行建模。

使用 **采样时间（-1 表示继承）** 参数在模块的连续实现和离散实现之间切换。要为连续时间配置积分器，请将 **采样时间（-1 表示继承）** 参数设置为 `0`。要为离散时间配置积分器，请将 **采样时间（-1 表示继承）** 参数设置为正标量。要从上游模块继承采样时间，请将 **采样时间（-1 表示继承）** 参数设置为 `-1`。

SM ST7C 模块包含三个主要组件：

- Current Compensator 组件根据端电流修正测得的端电压。
- Voltage Measurement Transducer 组件使用低通滤波器模拟端电压换能器的动态。
- Excitation Control Elements 组件将电压换能器输出与端电压参考值进行比较，以产生电压误差值。然后，该组件将此值通过电压调节器以产生励磁电压。

此图显示 ST7C 励磁系统模型的结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测得端电压和端电流。
- *VC1* 是电流补偿后的端电压。
- *VC* 是滤波后的电流补偿端电压。
- *VREF* 是参考端电压。
- *VS* 是电力系统稳定器电压。
- *EFD* 是励磁电压。

### Current Compensator 和 Voltage Measurement Transducer

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块将电压测量换能器实现为具有时间常数 *TR* 的 Low-Pass Filter 模块。有关精确的离散和连续实现的信息，请参阅 Low-Pass Filter 模块的文档。

### Excitation Control Elements

此图显示励磁控制元件的结构：

图中：

- Summation Point Logic 子系统对过励磁限制器 (OEL)、欠励磁限制器 (UEL) 和定子电流限制器 (SCL) 电压的求和点输入位置进行建模。有关将此模块与限制器一起使用的详细信息，请参阅励磁电流限制器。
- 有两个 Take-over Logic 子系统。这些子系统对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关将此模块与限制器一起使用的详细信息，请参阅励磁电流限制器。
- 串联的 Lead-Lag 模块引入微分功能，并将调节器转换为 PID。这通常仅用于无刷励磁系统。
- *KL* 和 *KH* 对调节发电机励磁电流的高带宽调节器内环进行建模。

### 励磁电流限制器

您可以使用不同类型的励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励磁限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励磁限制器在励磁过低时提升励磁，因为励磁过低有失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将任何这些限制器的输出连接到以下点之一：

- 求和点 — 将限制器用作自动电压调节器 (AVR) 反馈回路的一部分。
- 接管点 — 覆盖 AVR 的常规行为。

如果在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果在接管点使用定子电流限制器，请使用过励磁输入 *VSCLoel* 和欠励磁输入 *VSCLuel*。
