---
type: simulink-block
title: 'Schmitt Trigger'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Integrated Circuits / Logic'
documentation_page: 'schmitttrigger'
documentation_source_path: 'ref/schmitttrigger.html'
language: zh-CN
chinese_source: worker-translation
---

# Schmitt Trigger

## 端口

### 守恒

### **A** — 电气输入端口

与 Schmitt Trigger 输入关联的电气守恒端口。

### **J** — 电气输出端口

与 Schmitt Trigger 输出关联的电气守恒端口。

## 参数

### 输入

### **Low level input voltage** — Low level input voltage `2` `V` (默认)

当输入电压低于此电压值时，模块将输入电压解释为逻辑 `LOW`。

### **High level input voltage** — High level input voltage `3` `V` (默认)

当输入电压高于此电压值时，模块将输入电压解释为逻辑 `HIGH`。

### **Average input capacitance** — Average input capacitance `5` `pF` (默认)

用于近似 MOSFET 栅极输入电容的固定电容。MOSFET 电容取决于所施加的电压。当您用另一个栅极驱动此模块时，**Average input capacitance** 会产生与 MOSFET 相似的上升时间。您通常可以在制造商数据表中找到此电容值。将此值设置为零可能会加快仿真时间。

### 输出

### **Output current-voltage relationship** — Output current-voltage relationship `Linear` (默认) | `Quadratic`

选择输出模型：

- `Linear` - 这是默认值。
- `Quadratic`

### **Low level output voltage** — Low level output voltage `0` `V` (默认)

当输出逻辑电平为 `LOW` 时，输出端的电压值。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Linear` 时，此参数才可见。

### **High level output voltage** — High level output voltage `5` `V` (默认)

当输出逻辑电平为 `HIGH` 时，输出端的电压值。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Linear` 时，此参数才可见。

### **Output resistance** — Output resistance `25` `Ohm` (默认)

用于对输出电流导致的输出电压降进行建模的串联输出电阻的值。您可以通过将高电平输出电压除以最大低电平输出电流，从数据表中推导出此值。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Linear` 时，此参数才可见。

### **Supply voltage** — Supply voltage `5` `V` (默认)

电路中施加到栅极的电源电压值。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Measurement voltage** — Measurement voltage `5` `V` (默认)

为其定义掩模数据输出电阻和电流的栅极电源电压。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic HIGH output resistance at zero current and at I\_OH** — Logic HIGH output resistance at zero current and at I\_OH `[25, 250]` `Ohm`

由两个电阻值组成的行向量 [ *R\_OH1**R\_OH2* ]。第一个值 *R\_OH1* 是当栅极为逻辑 HIGH 且没有输出电流时输出电压-电流关系的梯度。第二个值 *R\_OH2* 是当栅极为逻辑 HIGH 且输出电流为 *I\_OH* 时输出电压-电流关系的梯度。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic HIGH output current I\_OH when shorted to ground** — Logic HIGH output current I\_OH when shorted to ground `63` `mA` (默认)

当栅极处于逻辑 HIGH 状态但负载迫使输出电压为零时产生的电流。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic LOW output resistance at zero current and at I\_OL** — Logic LOW output resistance at zero current and at I\_OL `[30, 800]` `Ohm` (默认)

由两个电阻值组成的行向量 [ *R\_OL1**R\_OL2* ]。第一个值 *R\_OL1* 是当栅极为逻辑 LOW 且没有输出电流时输出电压-电流关系的梯度。第二个值 *R\_OL2* 是当栅极为逻辑 LOW 且输出电流为 *I\_OL* 时输出电压-电流关系的梯度。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic LOW output current I\_OL when shorted to Vcc** — Logic LOW output current I\_OL when shorted to Vcc `-45` `mA` (默认)

当栅极处于逻辑 LOW 状态但负载迫使输出电压为电源电压 Vcc 时产生的电流。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Propagation delay** — Propagation delay `25` `ns` (默认)

输入逻辑电平变化后，输出从 `LOW` 摆到 `HIGH` 或从 `HIGH` 摆到 `LOW` 所需的时间。

### **Protection diode on resistance** — Protection diode on resistance `5` `Ohm` (默认)

保护二极管正向偏置时电压-电流关系的梯度。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Protection diode forward voltage** — Protection diode forward voltage `0.6` `V` (默认)

使保护二极管开启的电压阈值。

#### 依赖关系

仅当您为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### 初始条件

### **Output initial state** — Output initial state `Low` (默认) | `High`

指定模块的初始输出状态是 `High` 还是 `Low`。如果 **Propagation delay** 参数大于零，并且 Solver Configuration 模块未选择 **Start simulation from steady state** 选项，则此参数同时用于线性输出状态和二次输出状态。

## 所属库

Simscape / Electrical / Integrated Circuits / Logic

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

施密特触发器的行为模型

Schmitt Trigger 模块实现施密特触发器的行为模型。

当输入升高到 **High level input voltage** (*V*IH) 值以上时，模块输出逻辑电平为 `HIGH`，并且直到输入降到值更低的 **Low level input voltage** (*V*IL) 值以下时才会变为 `LOW`。此逻辑在输入和输出之间实现了迟滞特性。

在图中，*V*OH 和 *V*OL 分别对应 **High level output voltage** 和 **Low level output voltage** 值。

下图显示了参数为 *V*IH = 2V、*V*IL = -2V、*V*OH = 3V 和 *V*OL = -3V 时该模块的示例输出。

模块按如下方式确定栅极输入的逻辑电平：

- 如果栅极电压大于阈值电压，模块将输入解释为逻辑 1。
- 否则，模块将输入解释为逻辑 0。

*threshold voltage* 是 **High level input voltage** 参数值与 **Low level input voltage** 参数值之间的中点电压值。

**注意**

为了提高仿真速度，模块不会对构成栅极的所有内部单个 MOSFET 器件进行建模。有关详细信息，请参阅假设和限制。

模块按如下方式对栅极建模：

- 栅极输入具有无限电阻和有限或零电容。
- 栅极输出提供两种模型选择：`Linear` 和 `Quadratic`。有关详细信息，请参阅选择逻辑模块的输出模型。使用 **Output current-voltage relationship** 参数指定输出模型。
- 您可以为两种输出模型指定传播延迟。对于 `Linear` 输出，模块设置栅极输出电容的值，使电阻-电容时间常数等于 **Propagation delay** 参数值。对于 `Quadratic` 输出，栅极输入需求会滞后，以近似 **Propagation delay** 参数值。

模块输出电压取决于所选的输出模型：

- 对于 `Linear` 模型，输出高电平为 **High level output voltage** 参数值，输出低电平为 **Low level output voltage** 参数值。
- 对于 `Quadratic` 模型，High 和 Low 状态的输出电压是输出电流的函数，如 Quadratic 模型输出和参数中所述。对于零负载电流，输出高电平为 Vcc（即 **Supply voltage** 参数值），输出低电平为零伏。

### 绘制输入和输出波形

您无需构建完整模型即可绘制 Schmitt Trigger 模块的输入和输出波形。使用这些图可探究参数选择对器件特性的影响。如果您根据数据表对模块进行参数化，则可以将您的图与数据表进行比较，以检查是否正确地对模块进行了参数化。如果您已有完整的工作模型但不知道使用哪个制造器件，则可以将您的图与数据表进行比较以帮助决策。

要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **电气** > **基本特性**。

**注意**

使用 **基本特性** 选项创建的图不会显示 **Propagation delay** 参数对逻辑模块输出电压的影响。
