---
type: simulink-block
title: 'Push-Pull Output'
family: 'integrated-circuits'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'pushpulloutput'
documentation_source_path: 'ref/pushpulloutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Push-Pull Output

## 端口

### 输入

### **X** — 输入端口物理信号

与 Push-Pull Output 输入关联的物理端口。
### 守恒

### **J** — 输出端口电气

与模块输出关联的电气守恒端口。端口名称在模块图标上隐藏，但您可以在仿真数据日志中看到它。

## 参数

### 输入缩放

### **Input signal scaling, k** — 输入信号缩放 `1` `V` (默认)

输入物理信号 X 通过 *Vg* = *k* · ( X + *c* ) 映射到栅极电压，其中 *k* 是输入信号缩放。将本参数与 **Input signal offset, c** 结合使用，以将 X 的范围映射到由电源定义的电压范围。

### **Input signal offset, c** — 输入信号偏移 `0` (默认)

输入物理信号 X 通过 *Vg* = *k* · ( X + *c* ) 映射到栅极电压，其中 *c* 是输入信号偏移。将本参数与 **Input signal scaling, k** 结合使用，以将 X 的范围映射到由电源定义的电压范围。

### 输出特性

### **Output current-voltage relationship** — 输出模型 `Linear` (默认) | `Quadratic`

选择输出模型：

- `Linear` - 输出电压随输出电流线性下降。这是默认选项。
- `Quadratic` - 输出电压对输出电流的依赖关系由两个输出 MOSFET 器件的二次 I-V 特性定义。

### **Output resistance** — 输出电阻 `25` `Ohm` (默认)

定义输出 I-V 特性斜率的倒数。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数设置为 `Linear` 时，此参数可见。

### **Power rail voltages, [V- V+], used for measurements** — 用于测量的电源轨电压 `[0, 5]` `V` (默认)

定义封装数据输出电阻和电流所对应的电源轨电压。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数设置为 `Quadratic` 时，此参数可见。

### **Output resistance values at zero output current and at I\_OH when Vg=V-** — 当 Vg=V- 时，在零输出电流和 I\_OH 处的输出电阻值 `[25, 250]` `Ohm` (默认)

一个包含两个电阻值的行向量 [ R\_OH1 R\_OH2 ]。第一个值 R\_OH1 是当互补对输出为 HIGH (Vg=V-) 且没有输出电流时输出电压-电流关系的梯度。第二个值 R\_OH2 是当输出为 HIGH 且输出电流为 I\_OH 时输出电压-电流关系的梯度。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数设置为 `Quadratic` 时，此参数可见。

### **Output current I\_OH when output is shorted to V- and Vg=V-** — 当输出短接到 V- 且 Vg=V- 时的输出电流 I\_OH `63` `mA` (默认)

当输出为 HIGH (Vg=V-) 但负载将输出电压强制到负电源轨时产生的电流。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数设置为 `Quadratic` 时，此参数可见。

### **Output resistance values at zero output current and at I\_OL when Vg=V+** — 当 Vg=V+ 时，在零输出电流和 I\_OL 处的输出电阻值 `[30, 800]` `Ohm` (默认)

一个包含两个电阻值的行向量 [ R\_OL1 R\_OL2 ]。第一个值 R\_OL1 是当互补对输出为 LOW (Vg=V+) 且没有输出电流时输出电压-电流关系的梯度。第二个值 R\_OL2 是当输出为 LOW 且输出电流为 I\_OL 时输出电压-电流关系的梯度。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数设置为 `Quadratic` 时，此参数可见。

### **Output current I\_OL when output is shorted to V+ and Vg=V+** — 当输出短接到 V+ 且 Vg=V+ 时的输出电流 I\_OL `-45` `mA` (默认)

当输出为 LOW (Vg=V+) 但负载将输出电压强制到正电源电压时产生的电流。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数设置为 `Quadratic` 时，此参数可见。

### **Propagation delay** — 传播延迟 `25` `ns` (默认)

在输入 X 发生阶跃变化后，输出达到其最终值 63.2% 所需的时间。对于 `Quadratic` 输出，它通过滞后的栅极输入需求实现。

### **Protection diode on resistance** — 保护二极管导通电阻 `5` `Ohm` (默认)

保护二极管正向偏置时电压-电流关系的梯度。

### **Protection diode forward voltage** — 保护二极管正向电压 `0.6` `V` (默认)

高于该电压时保护二极管导通。

### 电源电压

### **Negative power rail voltage, V-** — 负电源轨电压 `0` `V` (默认)

施加到 N 沟道 MOSFET 源极引脚上的负电源电压。

### **Positive power rail voltage, V+** — 正电源轨电压 `5` `V` (默认)

施加到 P 沟道 MOSFET 源极引脚上的正电源电压。

### 初始条件

### **Initial output voltage** — 初始输出电压 `0` `V` (默认)

此参数用于设置输出电容器上的电压，以便将输出电压初始化为该参数的值。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数在 **输出特性** 选项卡上设置为 `Linear` 时，此参数可见。

### **Initial input signal** — 初始输入信号 `0` `V` (默认)

此参数用于初始化传播延迟一阶滞后，使得在零时刻没有瞬态。

#### 依赖关系

仅当 **Output current-voltage relationship** 参数在 **输出特性** 选项卡上设置为 `Quadratic` 时，此参数可见。

## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

CMOS 互补输出级的行为级表示

Push-Pull Output 模块以行为级方式表示 CMOS 互补输出级。为了提高仿真速度，该模块不会对构成该门的所有内部单个 MOSFET 器件进行建模。当使用 Simscape™ Foundation 库中的 Physical Signal 模块定义集成电路模型行为时，您可以使用该模块创建具有代表性的输出电流-电压关系。

您可以在两种输出电流-电压关系之间进行选择：

- `Linear` — 该模块将输出表示为电压源加上串联电阻和并联电容，如下图所示。您为 **Output resistance** 参数指定的值将赋给串联电阻，电容值通过将 RC 时间常数与 **Propagation delay** 参数值匹配来确定。

  Controlled Voltage Source 模块的输入被限制在电源轨之间，并且还通过从电源电压中相减而被反相。该反相使其表现得像互补输出级，其中高栅源电压会导致低输出。
- `Quadratic` — 输出级由构成互补对的两个 MOSFET 建模。MOSFET 参数由您指定为封装参数的输出电阻值和短路电流推导得到。栅极输入需求被滞后，以近似 **Propagation delay** 参数值。

`Linear` 和 `Quadratic` 输出模型都会添加偏移并缩放物理输入 X，因此栅极电压由下式给出：

|  |  |
| --- | --- |
| *Vg* = *k* · ( X + *c* ) | **(1)** |

其中

- *k* 是输入信号缩放。
- *c* 是输入信号偏移。

偏移和缩放可用于例如将 X 的逻辑值（即范围 `[0,1]`）与输出引脚处的 [V-, V+] 匹配。例如，如果 V+ = 10V 且 V- = 0，则为了将信号逻辑值与该电压范围匹配，设置 *c* = `-1` 且 *k* = `-10`。

对于 `Linear` 和 `Quadratic` 输出模型，保护二极管 D1 和 D2 用于限制输出电压范围。这些二极管是 Simscape Foundation 库中的 Diode 模块，即由正向电压和导通电阻定义的分段线性二极管。如果 D1 两端的电压上升到正向电压以上，则二极管开始导通，并且在导通电阻足够低的情况下，它有效防止输出上升到 V+ 加上二极管正向电压降以上。如果输出电压下降得太低，也会产生等效行为。

输出模型与用于逻辑模块的模型非常相似。有关使用 `Quadratic` 输出模型时典型输出 V-I 特性的图，请参阅“为逻辑模块选择输出模型”。

**注意**

此模块由 Simscape Physical Signals 库中的模块构建（例如 PS Add、PS Gain 等）。目前，Physical Signals 库中的模块不支持单位传播和检查。有关详细信息，请参阅“如何使用物理单位”。
