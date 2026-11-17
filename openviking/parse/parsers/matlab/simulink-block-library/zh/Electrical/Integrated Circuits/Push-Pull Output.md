---
type: simulink-block
title: 'Push-Pull Output'
family: 'sps'
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

与模块输出关联的电气守恒端口。该端口名称在模块图标上隐藏，但可以在仿真数据日志中看到。

## 参数

### 输入缩放

### **Input signal scaling, k** — 输入信号缩放 `1` `V`（默认）

输入物理信号 X 通过 *Vg* = *k* · ( X + *c* ) 映射到栅极电压，其中 *k* 是输入信号缩放。将此参数与 **Input signal offset, c** 结合使用，可将 X 的范围映射到由电源定义的电压范围。

### **Input signal offset, c** — 输入信号偏移 `0`（默认）

输入物理信号 X 通过 *Vg* = *k* · ( X + *c* ) 映射到栅极电压，其中 *c* 是输入信号偏移。将此参数与 **Input signal scaling, k** 结合使用，可将 X 的范围映射到由电源定义的电压范围。

### 输出特性

### **Output current-voltage relationship** — 输出模型 `Linear`（默认）| `Quadratic`

选择输出模型：

- `Linear` - 输出电压随输出电流线性下降。这是默认选项。
- `Quadratic` - 输出电压对输出电流的依赖性由两个输出 MOSFET 器件的二次 I-V 特性定义。

### **Output resistance** — 输出电阻 `25` `Ohm`（默认）

定义输出 I-V 特性斜率的倒数。

#### 依赖关系

此参数仅在 **Output current-voltage relationship** 参数设置为 `Linear` 时可见。

### **Power rail voltages, [V- V+], used for measurements** — 用于测量的电源轨电压 `[0, 5]` `V`（默认）

定义用于定义掩膜数据输出电阻和电流的电源轨电压。

#### 依赖关系

此参数仅在 **Output current-voltage relationship** 参数设置为 `Quadratic` 时可见。

### **Output resistance values at zero output current and at I\_OH when Vg=V-** — 零输出电流时以及 Vg=V- 时 I\_OH 处的输出电阻值 `[25, 250]` `Ohm`（默认）

包含两个电阻值的行向量 [ R\_OH1 R\_OH2 ]。第一个值 R\_OH1 是互补对输出为高电平（Vg=V-）且无输出电流时输出电压-电流关系的梯度。第二个值 R\_OH2 是输出为高电平且输出电流为 I\_OH 时输出电压-电流关系的梯度。

#### 依赖关系

此参数仅在 **Output current-voltage relationship** 参数设置为 `Quadratic` 时可见。

### **Output current I\_OH when output is shorted to V- and Vg=V-** — 输出短接到 V- 且 Vg=V- 时的输出电流 I\_OH `63` `mA`（默认）

输出为高电平（Vg=V-）但负载将输出电压强制到负电源轨时产生的电流。

#### 依赖关系

此参数仅在 **Output current-voltage relationship** 参数设置为 `Quadratic` 时可见。

### **Output resistance values at zero output current and at I\_OL when Vg=V+** — 零输出电流时以及 Vg=V+ 时 I\_OL 处的输出电阻值 `[30, 800]` `Ohm`（默认）

包含两个电阻值的行向量 [ R\_OL1 R\_OL2 ]。第一个值 R\_OL1 是互补对输出为低电平（Vg=V+）且无输出电流时输出电压-电流关系的梯度。第二个值 R\_OL2 是输出为低电平且输出电流为 I\_OL 时输出电压-电流关系的梯度。

#### 依赖关系

此参数仅在 **Output current-voltage relationship** 参数设置为 `Quadratic` 时可见。

### **Output current I\_OL when output is shorted to V+ and Vg=V+** — 输出短接到 V+ 且 Vg=V+ 时的输出电流 I\_OL `-45` `mA`（默认）

输出为低电平（Vg=V+）但负载将输出电压强制到正电源电压时产生的电流。

#### 依赖关系

此参数仅在 **Output current-voltage relationship** 参数设置为 `Quadratic` 时可见。

### **Propagation delay** — 传播延迟 `25` `ns`（默认）

输入 X 发生阶跃变化后，输出达到其最终值 63.2% 所需的时间。对于 `Quadratic` 输出，它通过滞后栅极输入需求来实现。

### **Protection diode on resistance** — 保护二极管导通电阻 `5` `Ohm`（默认）

保护二极管正向偏置时电压-电流关系的梯度。

### **Protection diode forward voltage** — 保护二极管正向电压 `0.6` `V`（默认）

保护二极管导通的电压阈值。

### 电源电压

### **Negative power rail voltage, V-** — 负电源轨电压 `0` `V`（默认）

施加到 N 沟道 MOSFET 源极引脚的负电源电压。

### **Positive power rail voltage, V+** — 正电源轨电压 `5` `V`（默认）

施加到 P 沟道 MOSFET 源极引脚的正电源电压。

### 初始条件

### **Initial output voltage** — 初始输出电压 `0` `V`（默认）

此参数用于设置输出电容器上的电压，使输出电压初始化为该参数值。

#### 依赖关系

此参数仅在 **Output Characteristics** 选项卡上的 **Output current-voltage relationship** 参数设置为 `Linear` 时可见。

### **Initial input signal** — 初始输入信号 `0` `V`（默认）

此参数用于初始化传播延迟一阶滞后，使得在零时刻没有瞬态。

#### 依赖关系

此参数仅在 **Output Characteristics** 选项卡上的 **Output current-voltage relationship** 参数设置为 `Quadratic` 时可见。

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

Push-Pull Output 模块以行为级方式表示 CMOS 互补输出级。为了提高仿真速度，该模块不会对构成栅极的所有内部单个 MOSFET 器件进行建模。当使用 Simscape™ Foundation 库中的物理信号模块定义集成电路模型行为时，可以使用此模块创建具有代表性的输出电流-电压关系。

可以在两种输出电流-电压关系之间进行选择：

- `Linear` — 该模块将输出表示为电压源加串联电阻和并联电容，如下图所示。为 **Output resistance** 参数指定的值分配给串联电阻，电容值通过将 RC 时间常数与 **Propagation delay** 参数值匹配来确定。

  受控电压源模块的输入被限制在电源轨之间，并且还通过从电源电压中减去来进行反相。反相使其表现为互补输出级，高栅源电压导致低输出。
- `Quadratic` — 输出级由构成互补对的两个 MOSFET 建模。MOSFET 参数由指定为掩膜参数的输出电阻值和短路电流导出。栅极输入需求被滞后以近似 **Propagation delay** 参数值。

`Linear` 和 `Quadratic` 输出模型都会对物理输入 X 添加偏移并进行缩放，使栅极电压由下式给出：

|  |  |
| --- | --- |
| *Vg* = *k* · ( X + *c* ) | **(1)** |

其中

- *k* 是输入信号缩放。
- *c* 是输入信号偏移。

偏移和缩放可用于例如将 X 的逻辑值（即范围 `[0,1]`）匹配到输出引脚处的 [V-, V+]。例如，如果 V+ = 10V 且 V- = 0，则要将信号逻辑值匹配到此电压范围，设置 *c* = `-1` 和 *k* = `-10`。

对于 `Linear` 和 `Quadratic` 输出模型，保护二极管 D1 和 D2 用于限制输出电压范围。这些二极管是 Simscape Foundation 库中的 Diode 模块，即由其正向电压和导通电阻定义的分段线性二极管。如果 D1 两端的电压超过正向电压，则二极管开始导通，并且在导通电阻较低的情况下，它有效地防止输出超过 V+ 加上二极管正向压降。如果输出电压降得过低，也会产生等效行为。

输出模型与逻辑模块所使用的模型非常相似。有关使用 `Quadratic` 输出模型时典型输出 V-I 特性的图，请参阅 Selecting the Output Model for Logic Blocks。

**注意**

此模块由 Simscape Physical Signals 库中的模块（如 PS Add、PS Gain 等）构建而成。目前，Physical Signals 库中的模块不支持单位传播和检查。有关详细信息，请参阅 How to Work with Physical Units。
