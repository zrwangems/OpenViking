---
type: simulink-block
title: 'CMOS NAND'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits / Logic'
documentation_page: 'cmosnand'
documentation_source_path: 'ref/cmosnand.html'
language: zh-CN
chinese_source: worker-translation
---

# CMOS NAND

## 端口

### 守恒端口

### **A** — 输入端口（电气）

与 CMOS NAND 输入关联的电气守恒端口。

### **B** — 输入端口（电气）

与 CMOS NAND 输入关联的电气守恒端口。

### **J** — 输出端口（电气）

与 CMOS NAND 输出关联的电气守恒端口。

## 参数

### 输入

### **Low level input voltage** — 低电平输入电压 `2` `V`（默认值）

低于该电压值时，模块将输入电压解释为逻辑 `LOW`。

### **High level input voltage** — 高电平输入电压 `3` `V`（默认值）

高于该电压值时，模块将输入电压解释为逻辑 `HIGH`。

### **Average input capacitance** — 平均输入电容 `5` `pF`（默认值）

用于近似 MOSFET 栅极输入电容的固定电容。MOSFET 电容取决于所施加的电压。当您用另一个栅极驱动此模块时，**Average input capacitance** 产生的上升时间与 MOSFET 相似。通常可以在制造商数据手册中找到该电容值。将此值设置为零可能会加快仿真速度。

### 输出

### **Output current-voltage relationship** — 输出电流-电压关系 `Linear`（默认值）| `Quadratic`

选择输出模型：

- `Linear` - 这是默认值。
- `Quadratic`

### **Low level output voltage** — 低电平输出电压 `0` `V`（默认值）

当输出逻辑电平为 `LOW` 时输出端的电压值。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Linear` 时，此参数才可见。

### **High level output voltage** — 高电平输出电压 `5` `V`（默认值）

当输出逻辑电平为 `HIGH` 时输出端的电压值。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Linear` 时，此参数才可见。

### **Output resistance** — 输出电阻 `25` `Ohm`（默认值）

用于模拟由输出电流引起的输出电压降的串联输出电阻值。您可以通过将高电平输出电压除以最大低电平输出电流，从数据手册中推导出该值。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Linear` 时，此参数才可见。

### **Supply voltage** — 电源电压 `5` `V`（默认值）

施加到电路中栅极的电源电压值。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Measurement voltage** — 测量电压 `5` `V`（默认值）

定义掩膜数据输出电阻和电流时所对应的栅极电源电压。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic HIGH output resistance at zero current and at I\_OH** — 零电流和 I\_OH 时的逻辑 HIGH 输出电阻 `[25, 250]` `Ohm`

由两个电阻值组成的行向量 [ *R\_OH1**R\_OH2* ]。第一个值 *R\_OH1* 是栅极为逻辑 HIGH 且无输出电流时输出电压-电流关系的梯度。第二个值 *R\_OH2* 是栅极为逻辑 HIGH 且输出电流为 *I\_OH* 时输出电压-电流关系的梯度。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic HIGH output current I\_OH when shorted to ground** — 短接到地时的逻辑 HIGH 输出电流 I\_OH `63` `mA`（默认值）

当栅极处于逻辑 HIGH 状态但负载迫使输出电压为零时产生的电流。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic LOW output resistance at zero current and at I\_OL** — 零电流和 I\_OL 时的逻辑 LOW 输出电阻 `[30, 800]` `Ohm`（默认值）

由两个电阻值组成的行向量 [ *R\_OL1**R\_OL2* ]。第一个值 *R\_OL1* 是栅极为逻辑 LOW 且无输出电流时输出电压-电流关系的梯度。第二个值 *R\_OL2* 是栅极为逻辑 LOW 且输出电流为 *I\_OL* 时输出电压-电流关系的梯度。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Logic LOW output current I\_OL when shorted to Vcc** — 短接到 Vcc 时的逻辑 LOW 输出电流 I\_OL `-45` `mA`（默认值）

当栅极处于逻辑 LOW 状态但负载迫使输出电压达到电源电压 Vcc 时产生的电流。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Propagation delay** — 传播延迟 `25` `ns`（默认值）

输入逻辑电平变化后，输出从 `LOW` 摆动到 `HIGH` 或从 `HIGH` 摆动到 `LOW` 所需的时间。

### **Protection diode on resistance** — 保护二极管导通电阻 `5` `Ohm`（默认值）

保护二极管正向偏置时电压-电流关系的梯度。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### **Protection diode forward voltage** — 保护二极管正向电压 `0.6` `V`（默认值）

保护二极管导通时所对应的电压。

#### 依赖关系

仅当为 **Output current-voltage relationship** 参数选择 `Quadratic` 时，此参数才可见。

### 初始条件

### **Output initial state** — 输出初始状态 `Low`（默认值）| `High`

指定模块的初始输出状态为 `High` 还是 `Low`。此参数同时用于线性和二次输出状态，前提是 **Propagation delay** 参数大于零，且 Solver Configuration 模块未选择 **Start simulation from steady state** 选项。

## 所属库

Simscape / Electrical / Integrated Circuits / Logic

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

## 描述

CMOS NAND 门的行为模型

CMOS NAND 模块以行为方式表示 CMOS NAND 逻辑门：

- 如果两个门输入的逻辑电平均为 0，则模块输出逻辑电平为 `HIGH`。
- 否则，模块输出逻辑电平为 `LOW`。

模块按如下方式确定门输入的逻辑电平：

- 如果栅极电压大于阈值电压，则模块将输入解释为逻辑 1。
- 否则，模块将输入解释为逻辑 0。

*阈值电压* 是 **High level input voltage** 参数值与 **Low level input voltage** 参数值之间中点处的电压值。

**注意**

为提高仿真速度，模块不会对构成门的所有内部单个 MOSFET 器件进行建模。有关详细信息，请参阅假设和限制。

模块按如下方式对门进行建模：

- 门输入具有无限电阻和有限或零电容。
- 门输出提供两种模型选择：`Linear` 和 `Quadratic`。有关详细信息，请参阅为逻辑模块选择输出模型。使用 **Output current-voltage relationship** 参数指定输出模型。
- 您可以为两种输出模型指定传播延迟。对于 `Linear` 输出，模块设置门输出电容的值，使电阻-电容时间常数等于 **Propagation delay** 参数值。对于 `Quadratic` 输出，门输入需求被滞后以近似 **Propagation delay** 参数值。

模块的初始条件取决于所选的输出模型：

- 对于 `Linear` 模型，高初始条件对应于 **High level output voltage** 参数值 `V_OH`，低初始条件对应于 **Low level output voltage** 参数值 `V_OL`。
- 对于 `Quadratic` 模型，高初始条件是一个接近 **Supply voltage** 参数值 `Vcc` 的值，低初始条件接近 `0`。

模块的输出电压取决于所选的输出模型：

- 对于 `Linear` 模型，输出高电平为 **High level output voltage** 参数值，输出低电平为 **Low level output voltage** 参数值。
- 对于 `Quadratic` 模型，High 和 Low 状态的输出电压是输出电流的函数，如二次模型输出和参数中所述。对于零负载电流，输出高电平为 Vcc（**Supply voltage** 参数值），输出低电平为零伏。

### 绘制输入和输出波形

您无需构建完整模型即可绘制 CMOS NAND 模块的输入和输出波形。使用这些图可以探究参数选择对器件特性的影响。如果您根据数据手册对模块进行参数化，可以将图与数据手册进行比较，以检查模块参数化是否正确。如果您有一个完整的工作模型但不知道使用哪个制造器件，可以将图与数据手册进行比较以帮助您做出决定。

要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。

**注意**

使用 **Basic characteristics** 选项创建的图不会显示 **Propagation delay** 参数对逻辑模块输出电压的影响。
