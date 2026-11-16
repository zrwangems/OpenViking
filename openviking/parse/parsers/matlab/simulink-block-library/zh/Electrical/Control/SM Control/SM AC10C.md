---
type: simulink-block
title: 'SM AC10C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smac10c'
documentation_source_path: 'ref/smac10c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM AC10C

## 端口

### 输入

### **V\_REF** — 电压参考标量

电压调节器参考设定点，采用 per-unit 表示，
指定为标量。

**数据类型：** `single` | `double`

### **V\_S** — 来自稳定器的输入标量

来自电力系统稳定器的输入，采用 per-unit 表示，
指定为标量。

**数据类型：** `single` | `double`

### **V\_T** — 机端电压标量

机端电压幅值，采用 per-unit 表示，指定为标量。

**数据类型：** `single` | `double`

### **I\_T** — 机端电流标量

机端电流幅值，采用 per-unit 表示，指定为标量。

**数据类型：** `single` | `double`

### **V\_OEL** — 过励限制信号标量

来自过励限制器的输入，采用 per-unit 表示，
指定为标量。

#### 依赖项

- 要忽略来自过励限制器的输入，
  请将 **备用 OEL 输入位置
  (V\_OEL)** 设置为
  `Unused`。
- 要在求和点使用来自过励限制器的输入，
  请将 **备用 OEL 输入
  位置 (V\_OEL)** 设置为
  `Summation point`。
- 要在 Take-over Logic 子系统中使用来自过励限制器的输入，请将 **备用
  OEL 输入位置 (V\_OEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统中使用来自过励限制器的输入，请将 **备用
  OEL 输入位置 (V\_OEL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_UEL** — 欠励限制信号标量

来自欠励限制器的输入，采用 per-unit 表示，
指定为标量。

#### 依赖项

- 要忽略来自欠励限制器的输入，
  请将 **备用 UEL 输入位置
  (V\_UEL)** 设置为
  `Unused`。
- 要在求和点使用来自欠励限制器的输入，
  请将 **备用 UEL 输入
  位置 (V\_UEL)** 设置为
  `Summation point`。
- 要在 Take-over Logic 子系统中使用来自欠励限制器的输入，请将 **备用
  UEL 输入位置 (V\_UEL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统中使用来自欠励限制器的输入，请将 **备用
  UEL 输入位置 (V\_UEL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_SCLsum** — 求和点定子电流限制信号标量

使用求和点时来自定子电流限制器的输入，
采用 per-unit 表示，指定为标量。

#### 依赖项

- 要忽略来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在求和点使用来自定子电流限制器的输入，
  请将 **备用 SCL 输入
  位置 (V\_SCL)** 设置为
  `Summation point`。

**数据类型：** `single` | `double`

### **V\_SCLoel** — 用于过励限制器的接管定子电流限制标量

使用接管点时，来自定子电流限制器的输入，用于防止磁场过励，
采用 per-unit 表示，指定为
标量。

#### 依赖项

- 要忽略来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统中使用来自定子电流限制器的输入，请将 **备用
  SCL 输入位置 (V\_SCL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统中使用来自定子电流限制器的输入，请将 **备用
  SCL 输入位置 (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **V\_SCLuel** — 用于欠励限制器的接管定子电流限制标量

使用接管点时，来自定子电流限制器的输入，用于防止磁场欠励，
采用 per-unit 表示，指定为
标量。

#### 依赖项

- 要忽略来自定子电流限制器的输入，
  请将 **备用 SCL 输入位置
  (V\_SCL)** 设置为
  `Unused`。
- 要在 Take-over Logic 子系统中使用来自定子电流限制器的输入，请将 **备用
  SCL 输入位置 (V\_SCL)** 设置为
  `Take-over at voltage
  error`。
- 要在 Take-over Logic1 子系统中使用来自定子电流限制器的输入，请将 **备用
  SCL 输入位置 (V\_SCL)** 设置为
  `Take-over at voltage regulator
  output`。

**数据类型：** `single` | `double`

### **Ifd\_pu** — 测量励磁电流标量

同步电机的测量 per-unit 励磁电流，指定
为标量。

**数据类型：** `single` | `double`

### 输出

### **Efd\_pu** — 励磁电压标量

要施加到同步电机励磁电路的 per-unit 励磁电压，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 常规

### **初始励磁电压, Efd0 (pu)** — 初始输出电压 `1`（默认）| real scalar

要施加到同步电机励磁电路的初始 per-unit 电压。

### **初始机端电压, Vt0 (pu)** — 初始机端电压 `1`（默认）| real scalar

要施加到机端的初始 per-unit 电压。

#### 依赖项

要启用此参数，请在 Exciter 部分中，将
**电源选择器 SW1** 设置为
`Position A: power source derived from terminal
voltage`。

### **初始机端电流, It0 (pu)** — 初始机端电流 `1`（默认）| real scalar

要施加到机端的初始 per-unit 电流。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。执行期间，
模块产生输出，并在适当情况下更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承离散时间操作，将此参数设置为 `-1`。
对于离散时间操作，将此参数设置为正整数。对于
连续时间操作，将此参数设置为 `0`。

如果此模块位于支持连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关
详细信息，请参阅 Promote Block Parameters on a Mask。

### 预控制

### **负载补偿的电阻分量, R\_C (pu)** — 补偿电阻 `0`（默认）| 正标量

用于电流补偿系统的电阻。将此参数
和 **负载补偿的电抗分量, X\_C
(pu)** 设置为 `0` 可禁用电流
补偿。

### **负载补偿的电抗分量, X\_C (pu)** — 补偿电抗 `0`（默认）| 正标量

用于电流补偿系统的电抗。将此参数
和 **负载补偿的电阻分量, R\_C
(pu)** 设置为 `0` 可禁用电流
补偿。

### **调节器输入滤波器时间常数, T\_R (s)** — 调节器时间常数 `0.01`（默认）| 正标量

电压传感器滤波的等效时间常数。

### 控制

### **调节器增益, K\_R (pu)** — 调节器增益 `600`（默认）| 正标量

调节器的增益。

### **电压调节器分母（滞后）时间常数 1, T\_B1 (s)** — 调节器滞后时间常数 1 `22.5`（默认）| 正标量

电压调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **电压调节器分子（超前）时间常数 1, T\_C1 (s)** — 调节器超前时间常数 1 `3`（默认）| 正标量

电压调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **电压调节器分母（滞后）时间常数 2, T\_B2 (s)** — 调节器滞后时间常数 2 `0.13`（默认）| 正标量

电压调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **电压调节器分子（超前）时间常数 2, T\_C2 (s)** — 调节器超前时间常数 2 `0.9`（默认）| 正标量

电压调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分母（滞后）时间常数 1, T\_UB1 (s)** — UEL 调节器滞后时间常数 1 `22.5`（默认）

欠励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分子（超前）时间常数 1, T\_UC1 (s)** — UEL 调节器超前时间常数 1 `3`（默认）

欠励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分母（滞后）时间常数 2, T\_UB2 (s)** — UEL 调节器滞后时间常数 2 `0.13`（默认）

欠励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **UEL 调节器分子（超前）时间常数 2, T\_UC2 (s)** — UEL 调节器超前时间常数 2 `0.9`（默认）

欠励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分母（滞后）时间常数 1, T\_OB1 (s)** — OEL 调节器滞后时间常数 1 `18`（默认）

过励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分子（超前）时间常数 1, T\_OC1 (s)** — OEL 调节器超前时间常数 1 `0.9`（默认）

过励限制器调节器的第二个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分母（滞后）时间常数 2, T\_OB2 (s)** — OEL 调节器滞后时间常数 2 `0.1`（默认）

过励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **OEL 调节器分子（超前）时间常数 2, T\_OC2 (s)** — OEL 调节器超前时间常数 2 `0.1`（默认）

过励限制器调节器的第一个 Lead-Lag (Discrete or Continuous) 模块中的等效超前时间常数。当附加超前动态可忽略时，将此参数设置为 `0`。

### **最大调节器输出, V\_Rmax (pu)** — 最大调节器输出 `40`（默认）| real scalar

最大 per-unit 调节器输出。

### **最小调节器输出, V\_Rmin (pu)** — 最小调节器输出 `-35`（默认）| real scalar

最小 per-unit 调节器输出。

### **最大 PSS 调节器输出, V\_RSmax (pu)** — 最大 PSS 调节器输出 `20`（默认）| real scalar

电力系统稳定器调节器的最大 per-unit 输出。

### **最小 PSS 调节器输出, V\_RSmin (pu)** — 最小 PSS 调节器输出 `-20`（默认）| real scalar

电力系统稳定器调节器的最小 per-unit 输出。

### **励磁机磁场电流调节器测量时间常数, T\_EXC (s)** — 励磁机磁场电流调节器的测量时间常数 `0`（默认）| 正标量

励磁机磁场电流调节器的测量时间常数，以秒为单位。

### **励磁机磁场电流调节器反馈增益, K\_EXC (pu)** — 励磁机磁场电流调节器的反馈增益 `1`（默认）| 正标量

励磁机磁场电流调节器的 per-unit 反馈增益。

### **励磁机磁场电流调节器比例增益, K\_CR (pu)** — 励磁机磁场电流调节器的比例增益 `0`（默认）| 正标量

励磁机磁场电流调节器的 per-unit 比例增益。

### **励磁机磁场电流调节器反馈选择器 SW\_EXC** — 励磁机磁场电流调节器反馈选择器 `Position A: feedback from generator field voltage (E_FD)`（默认）| `Position B: feedback from exciter field current (V_FE)`

用于选择励磁机磁场电流调节器电路中反馈变量的选项。

### **励磁机磁场电流调节器分子（超前）时间常数, T\_F1 (s)** — 励磁机磁场电流调节器中的超前时间常数 `0.1`（默认）| 正标量

励磁机磁场电流调节器中的等效超前时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **励磁机磁场电流调节器分母（滞后）时间常数, T\_F2 (s)** — 励磁机磁场电流调节器中的滞后时间常数 `0.1`（默认）| 正标量

励磁机磁场电流调节器中的等效滞后时间常数。当附加滞后动态可忽略时，将此参数设置为 `0`。

### **励磁机磁场电流限制器反馈增益, K\_VFE (pu)** — 励磁机磁场电流限制器增益 `1`（默认）| 正标量

励磁系统磁场电流限制器的 per-unit 反馈增益。

### **励磁机磁场电流限制器比例增益, K\_LIM (pu)** — 励磁机磁场电流比例增益 `0`（默认）| 正标量

励磁系统磁场电流限制器的 per-unit 比例增益。

如果将此参数设置为大于 `0` 的值，则 SW\_LIM Switch 模块位于位置 "A"，并且励磁机磁场电流限制器处于活动状态。

如果将此参数和 **励磁机磁场电流调节器比例增益, K\_CR (pu)** 参数均设置为 `0`，则 SW\_SS Switch 模块位于位置 "A"，并且 Current control 子系统不活动。

### **励磁机磁场电流限制器参考值, V\_FELIM (pu)** — 励磁系统磁场电流限制器的参考值 `20`（默认）| real scalar

励磁系统磁场电流限制器的 per-unit 参考值。

### **备用 PSS 输入位置 (V\_S)** — PSS 输入位置 `Voltage error or after take-over limits`（默认）| `Voltage error calculation` | `Output of AVR (after take-over limits)`

电力系统稳定器输入的位置。

### **备用 OEL 输入位置 (V\_OEL)** — OEL 输入位置 `Take-over at voltage error`（默认）| `Summation point at voltage error` | `Unused` | `Take-over at voltage regulator output`

过励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage error` — **V\_OEL** 是 **Summation Point Logic** 子系统的输入。
- `Take-over at voltage error` — **V\_OEL** 是 **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator output` — **V\_OEL** 是 **Take-over Logic 1** 子系统的输入。

### **备用 UEL 输入位置 (V\_UEL)** — UEL 输入位置 `Take-over at voltage error`（默认）| `Summation point at voltage error` | `Unused` | `Take-over at voltage regulator output`

欠励限制器输入的位置，指定为以下选项之一：

- `Summation point at voltage error` — **V\_UEL** 是 **Summation Point Logic** 子系统的输入。
- `Take-over at voltage error` — **V\_UEL** 是 **Take-over Logic** 子系统的输入。
- `Take-over at voltage regulator output` — **V\_UEL** 是 **Take-over Logic 1** 子系统的输入。

### **备用 SCL 输入位置 (V\_SCL)** — SCL 输入位置 `Take-over at voltage error` (默认) | `Summation point at voltage error` | `Unused` | `Take-over at voltage regulator output`

定子电流限制器输入的位置，指定为以下选项之一：

- `Summation point` — 使用
  **V\_SCLsum** 输入端口。
- `Take-over` 选项中的任意一项 —
  使用 **V\_OELscl** 和
  **V\_UELscl** 输入端口。

### 励磁机

### **励磁机磁场比例常数，K\_E (pu)** — 励磁机磁场增益 `1` (默认) | positive scalar

励磁机磁场的比例常数。

### **励磁机磁场时间常数，T\_E (s)** — 励磁机磁场时间常数 `1.3` (默认) | positive scalar

励磁机磁场的时间常数。

### **与换相电抗成比例的整流器负载因子，K\_C (pu)** — 整流器负载因子 `0.13` (默认) | positive scalar

整流器负载因子。该值与换相电抗成比例。

### **去磁因子，励磁机交流发电机电抗的函数，K\_D (pu)** — 去磁因子 `1.15` (默认) | positive scalar

与励磁机交流发电机电抗相关的去磁因子。

### **饱和因子 S\_E(E\_1) 对应的励磁机输出电压，E\_1 (pu)** — 第一饱和输出电压 `10` (默认) | positive scalar

第一饱和因子对应的励磁机输出电压。

### **励磁机输出电压 E\_1 处的励磁机饱和因子，S\_E(E\_1) (1)** — 第一饱和查找电压 `0.214` (默认) | positive scalar

第一励磁机的饱和因子。

### **饱和因子 S\_E(E\_2) 对应的励磁机输出电压，E\_2 (pu)** — 第二饱和输出电压 `7.5` (默认) | positive scalar

第二饱和因子对应的励磁机输出电压。

### **励磁机输出电压 E\_2 处的励磁机饱和因子，S\_E(E\_2) (1)** — 第二饱和查找电压 `0.044` (默认) | positive scalar

第二励磁机的饱和因子。

### **最大励磁机磁场电流，V\_FEmax (pu)** — 励磁机上限 `44` (默认) | real scalar

最大标幺磁场电流限值参考值。

### **最小励磁机电压输出限值，V\_Emin (pu)** — 励磁机下限 `0` (默认) | real scalar

最小标幺励磁机电压输出。

### **电压回路增益系数，K\_P (pu)** — 电压回路增益系数 `1` (默认) | real scalar

标幺电压回路增益系数。

#### 依赖项

要启用此参数，请将 **电源选择器 SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **电压回路相角 (degrees)** — 电压回路相角 `0` (默认) | real scalar

电压回路相角，单位为 degrees。

#### 依赖项

要启用此参数，请将 **电源选择器 SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **电压回路（电流）增益系数，K\_I (pu)** — 电压回路电流增益系数 `0` (默认) | real scalar

标幺电压回路电流增益系数。

#### 依赖项

要启用此参数，请将 **电源选择器 SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **与电压源相关的电抗，X\_L (pu)** — 与电压源相关的电抗 `0` (默认) | real scalar

与电压源相关的标幺电抗。

#### 依赖项

要启用此参数，请将 **电源选择器 SW1** 设置为 `Position A: power source derived from terminal voltage`。

### **与换相电抗成比例的整流器负载因子，K\_C1 (pu)** — 与换相电抗成比例的整流器负载因子 `0` (默认) | real scalar

整流器的标幺负载因子。该值与换相电抗成比例。

### **电源选择器 SW1** — 电源选择器 `Position B: power source independent of the terminal conditions` (默认) | `Position A: power source derived from terminal voltage`

电源选择器 SW1 的位置。

### **最大可用励磁机电压，V\_B1max (pu)** — 最大可用励磁机磁场电压 `1.5` (默认) | real scalar

励磁机的最大标幺可用磁场电压。

### **与换相电抗成比例的整流器负载因子，K\_C2 (pu)** — 与换相电抗成比例的整流器负载因子 `0` (默认) | real scalar

整流器的标幺负载因子。该值与换相电抗成比例，由通过单独串联二极管桥的发电机机端电流导出。

### **附加电压回路（电流）增益系数，K\_I2 (pu)** — 附加回路电流增益系数 `0` (默认) | real scalar

由通过单独串联二极管桥的发电机机端电流导出的标幺附加回路电流增益系数。将此参数设置为 `0` 可完全禁用单独的附加电源。

### **最大可用励磁机电压，V\_B2max (pu)** — 最大可用励磁机电压 `0` (默认) | real scalar

励磁机的最大标幺可用磁场电压，由通过单独串联二极管桥的发电机机端电流导出。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

离散时间或连续时间同步电机 AC10C 励磁系统，包括自动电压调节器和励磁机

SM AC10C 模块实现符合 IEEE Std 421.5-2016 [1] 的同步电机 AC10C 型励磁系统模型。

使用此模块对作为发电机运行并使用交流旋转励磁机的同步电机的励磁电压的控制和调节进行建模。

通过使用 **采样时间（-1 表示继承）** 参数在模块的连续实现和离散实现之间切换。要将积分器配置为连续时间，请将 **采样时间（-1 表示继承）** 参数设置为 `0`。要将积分器配置为离散时间，请将 **采样时间（-1 表示继承）** 参数设置为 positive scalar。要从上游模块继承采样时间，请将 **采样时间（-1 表示继承）** 参数设置为 `-1`。

SM AC10C 模块包含五个主要组件：

- 电流补偿器组件根据机端电流修改测得的端电压。
- 电压测量变送器组件使用低通滤波器模拟端电压变送器的动态特性。
- 励磁控制元件组件将电压变送器输出与端电压参考值进行比较，以产生电压误差。然后该电压误差通过电压调节器，以产生励磁机磁场电压。
- 交流旋转励磁机组件对交流旋转励磁机进行建模，该励磁机产生施加到受控同步电机的励磁电压。该模块还将励磁机磁场电流（*VFE*）反馈到励磁系统。
- 电源组件对受控整流器的电源与端电压之间的依赖性进行建模。

下图显示了 AC10C 励磁系统模型的结构：

图中：

- *VT* 和 *IT* 分别是同步电机的测得端电压和机端电流。
- *VC1* 是电流补偿后的端电压。
- *VC* 是滤波后的电流补偿端电压。
- *VREF* 是参考端电压。
- *VS* 是电力系统稳定器电压。
- *SW1* 是为受控整流器指定的电源开关。
- *VB* 是励磁机磁场电压。
- *EFE* 和 *VFE* 分别是励磁机磁场电压和电流。
- *EFD* 和 *IFD* 分别是励磁电压和电流。

### 电流补偿器和电压测量变送器

该模块使用以下方程对电流补偿器进行建模：

VC1=VT+ITRC2+XC2,

其中：

- *RC* 是负载补偿电阻。
- *XC* 是负载补偿电抗。

该模块将电压测量变送器实现为具有时间常数 *TR* 的 Low-Pass Filter 模块。有关确切的离散和连续实现信息，请参阅 Low-Pass Filter 模块的文档。

### 励磁控制元件

下图显示了励磁控制元件的结构：

图中：

- Summation Point Logic 子系统对过励限制器 (OEL)、欠励限制器 (UEL) 和定子电流限制器 (SCL) 的求和点输入位置进行建模。有关将此模块与限制器一起使用的更多信息，请参阅励磁电流限制器。
- 有两个 Take-over Logic 子系统。它们对 OEL、UEL 和 SCL 电压的接管点输入位置进行建模。有关将此模块与限制器一起使用的更多信息，请参阅励磁电流限制器。
- Lead-Lag (Discrete or Continuous) 模块的并联配置在限制器激活时提供独立控制设置。该模型为 AVR 以及欠励和过励限制器提供一个公共增益因子 *KR* 和两个 Lead-Lag (Discrete or Continuous) 模块。当 *VUEL* 和/或 *VOEL* 信号连接到各自的备用位置时，SW\_UEL 和 SW\_OEL Switch 模块激活相应的控制路径。当您将 **备用 UEL 输入位置 (V\_UEL)** 和 **备用 OEL 输入位置 (V\_OEL)** 参数设置为 `Take-over at voltage error` 时，SW\_UEL 和 SW\_OEL Switch 模块位于位置 B。
- 每个控制路径中的两个 Lead-Lag 模块对与电压调节器以及欠励和过励限制器相关的附加动态进行建模。每个相应路径中的第一个 Lead-Lag 模块表示瞬态增益降低，其中 *TC2*（或 *TUC2* 和 *TOC2*）是超前时间常数，*TB2*（或 *TUB2* 和 *TOB2*）是滞后时间常数。第二个 Lead-Lag 模块允许表示瞬态增益增加，其中 *TC1*（或 *TUC1* 和 *TOC1*）是超前时间常数，*TB1*（或 *TUB1* 和 *TOB1*）是滞后时间常数。有关离散和连续实现的信息，请参阅 Lead-Lag 模块的文档。
- 控制信号 *VR1* 要么直接控制功率级，要么用作级联励磁机磁场电流控制环路的参考。有关 Current control subsystem 的更多信息，请参阅电流控制子系统。

### 电流控制子系统

当 SW\_SS Switch 模块位于位置 “A” 时，即当您将 **励磁机磁场电流调节器比例增益，K\_CR (pu)** 和 **励磁机磁场电流限制器比例增益，K\_LIM (pu)** 参数设置为 `0` 时，SM AC10C 模块会旁路 Current control subsystem。当 SW\_SS Switch 模块位于位置 “B” 时，Current control subsystem 处于活动状态。Current control subsystem 还提供限制器，以避免励磁机过载，并将励磁机电流限制为 **励磁机磁场电流限制器参考值，V\_FELIM (pu)** 参数的值。

当 SW\_LIM Switch 模块位于位置 “B” 时，即当 **励磁机磁场电流限制器比例增益，K\_LIM (pu)** 参数大于零时，励磁机磁场电流限制器处于活动状态。当 SW\_LIM Switch 模块位于位置 “A” 时，限制器被旁路。SW\_EXC Switch 模块允许您选择反馈变量。

### 励磁电流限制器

您可以使用不同类型的励磁电流限制器在不安全运行条件下修改电压调节器的输出：

- 使用过励限制器防止因励磁电流需求过大而导致励磁绕组过热。
- 使用欠励限制器在励磁过低时提升励磁，否则会有失步风险。
- 使用定子电流限制器防止因电流过大而导致定子绕组过热。

将任一这些限制器的输出连接到以下点之一：

- 求和点 — 将限制器用作自动电压调节器 (AVR) 反馈环路的一部分。
- 接管点 — 覆盖 AVR 的通常行为。

如果在求和点使用定子电流限制器，请使用输入 *VSCLsum*。如果在接管点使用定子电流限制器，请使用过励输入 *VOELscl* 和欠励输入 *VUELscl*。

### 交流旋转励磁机

下图显示了交流旋转励磁机的结构：

图中：

- 励磁机磁场电流 *VFE* 是三个信号之和：

  - 非线性函数 *Vx* 对励磁机输出电压的饱和进行建模。
  - 比例项 *KE* 对励磁机输出电压与励磁机磁场电流之间的线性关系进行建模。
  - 该子系统使用反馈环路中的去磁常数 *KD* 对负载电流对励磁机输出电压的去磁效应进行建模。
- Integrator with variable limits 子系统对 *EFE* 和 *VFE* 之间的差值进行积分，以生成励磁机交流发电机输出电压 *VE*。*TE* 是此过程的时间常数。
- 非线性函数 *FEX* 对由整流器调节引起的励磁机输出电压降进行建模。该函数取决于常数 *KC*，而 *KC* 本身是换相电抗的函数。
- 参数 *VEmin* 和 *VFEmax* 对旋转励磁机的下限和上限进行建模。

### 电源

您可以通过设置 **电源选择器 SW1** 参数值，为受控整流器使用不同的电源表示。要从端电压导出受控整流器的电源，请将 **电源选择器 SW1** 参数设置为 `Position A: power source derived from terminal voltage`。要指定电源独立于端电压，请将 **电源选择器 SW1** 参数设置为 `Position B: power source independent from the terminal conditions`。
