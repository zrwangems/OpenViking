---
type: simulink-block
title: 'S-R Latch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits / Logic'
documentation_page: 'srlatch'
documentation_source_path: 'ref/srlatch.html'
language: zh-CN
chinese_source: worker-translation
---

# S-R Latch

## 端口
```yaml
ports:
- name: S
  summary: 置位引脚电气端口
  direction: conserving
- name: R
  summary: 复位引脚电气端口
  direction: conserving
- name: Q
  summary: 输出引脚电气端口
  direction: conserving
```

### 守恒端口

### **S** — 置位引脚电气端口

与 S-R 锁存器置位引脚关联的电气守恒端口。

### **R** — 复位引脚电气端口

与 S-R 锁存器复位引脚关联的电气守恒端口。

### **Q** — 输出引脚电气端口

与 S-R 锁存器输出引脚关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Low level input voltage
  summary: 低电平输入电压 2 V（默认值）
  group: 输入
- name: High level input voltage
  summary: 高电平输入电压 3 V（默认值）
  group: 输入
- name: Average input capacitance
  summary: 平均输入电容 5 pF（默认值）
  group: 输入
- name: Output current-voltage relationship
  summary: 输出电流-电压关系 Linear（默认值） | Quadratic
  group: 输出
- name: Low level output voltage
  summary: 低电平输出电压 0 V（默认值）
  group: 输出
- name: High level output voltage
  summary: 高电平输出电压 5 V（默认值）
  group: 输出
- name: Output resistance
  summary: 输出电阻 25 Ohm（默认值）
  group: 输出
- name: Supply voltage
  summary: 电源电压 5 V（默认值）
  group: 输出
- name: Measurement voltage
  summary: 测量电压 5 V（默认值）
  group: 输出
- name: Logic HIGH output resistance at zero current and at I_OH
  summary: 零电流和 I_OH 时的逻辑 HIGH 输出电阻 [25, 250] Ohm
  group: 输出
- name: Logic HIGH output current I_OH when shorted to ground
  summary: 短接到地时的逻辑 HIGH 输出电流 I_OH 63 mA（默认值）
  group: 输出
- name: Logic LOW output resistance at zero current and at I_OL
  summary: 零电流和 I_OL 时的逻辑 LOW 输出电阻 [30, 800] Ohm（默认值）
  group: 输出
- name: Logic LOW output current I_OL when shorted to Vcc
  summary: 短接到 Vcc 时的逻辑 LOW 输出电流 I_OL -45 mA（默认值）
  group: 输出
- name: Propagation delay
  summary: 传播延迟 25 ns（默认值）
  group: 输出
- name: Protection diode on resistance
  summary: 保护二极管导通电阻 5 Ohm（默认值）
  group: 输出
- name: Protection diode forward voltage
  summary: 保护二极管正向电压 0.6 V（默认值）
  group: 输出
- name: Output initial state
  summary: 输出初始状态 Low（默认值） | High
  group: 初始条件
```

### 输入

### **Low level input voltage** — 低电平输入电压 `2` `V`（默认值）

低于该电压值时，模块将输入电压解释为 `LOW`。

### **High level input voltage** — 高电平输入电压 `3` `V`（默认值）

高于该电压值时，模块将输入电压解释为 `HIGH`。

### **Average input capacitance** — 平均输入电容 `5` `pF`（默认值）

用于近似 MOSFET 栅极输入电容的固定电容值。通常可以在制造商数据手册中找到该电容值。将此值设置为零可以加快仿真速度。

### 输出

### **Output current-voltage relationship** — 输出电流-电压关系 `Linear`（默认值） | `Quadratic`

选择输出模型：

- `Linear` - 这是默认值。
- `Quadratic`

### **Low level output voltage** — 低电平输出电压 `0` `V`（默认值）

当输出逻辑电平为 `LOW` 时，输出端的电压值。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Linear`。

### **High level output voltage** — 高电平输出电压 `5` `V`（默认值）

当输出逻辑电平为 `HIGH` 时，输出端的电压值。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Linear`。

### **Output resistance** — 输出电阻 `25` `Ohm`（默认值）

用于模拟由输出电流引起的输出电压降的串联输出电阻值。可以通过将高电平输出电压除以最大低电平输出电流，从数据手册中推导出该值。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Linear`。

### **Supply voltage** — 电源电压 `5` `V`（默认值）

施加到电路中栅极的电源电压值。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Measurement voltage** — 测量电压 `5` `V`（默认值）

定义掩膜数据输出电阻和电流时所对应的栅极电源电压。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic HIGH output resistance at zero current and at I\_OH** — 零电流和 I\_OH 时的逻辑 HIGH 输出电阻 `[25, 250]` `Ohm`

由两个电阻值组成的行向量 [ *R\_OH1**R\_OH2* ]。第一个值 *R\_OH1* 是栅极为逻辑 HIGH 且无输出电流时输出电压-电流关系的斜率。第二个值 *R\_OH2* 是栅极为逻辑 HIGH 且输出电流为 *I\_OH* 时输出电压-电流关系的斜率。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic HIGH output current I\_OH when shorted to ground** — 短接到地时的逻辑 HIGH 输出电流 I\_OH `63` `mA`（默认值）

当栅极处于逻辑 HIGH 状态但负载将输出电压强制为零时产生的电流。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic LOW output resistance at zero current and at I\_OL** — 零电流和 I\_OL 时的逻辑 LOW 输出电阻 `[30, 800]` `Ohm`（默认值）

由两个电阻值组成的行向量 [ *R\_OL1**R\_OL2* ]。第一个值 *R\_OL1* 是栅极为逻辑 LOW 且无输出电流时输出电压-电流关系的斜率。第二个值 *R\_OL2* 是栅极为逻辑 LOW 且输出电流为 *I\_OL* 时输出电压-电流关系的斜率。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic LOW output current I\_OL when shorted to Vcc** — 短接到 Vcc 时的逻辑 LOW 输出电流 I\_OL `-45` `mA`（默认值）

当栅极处于逻辑 LOW 状态但负载将输出电压强制为电源电压 Vcc 时产生的电流。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Propagation delay** — 传播延迟 `25` `ns`（默认值）

输入逻辑电平变化后，输出从 `LOW` 摆动到 `HIGH` 或从 `HIGH` 摆动到 `LOW` 所需的时间。

### **Protection diode on resistance** — 保护二极管导通电阻 `5` `Ohm`（默认值）

保护二极管正向偏置时电压-电流关系的斜率。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Protection diode forward voltage** — 保护二极管正向电压 `0.6` `V`（默认值）

保护二极管导通的电压阈值。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### 初始条件

### **Output initial state** — 输出初始状态 `Low`（默认值） | `High`

指定模块的初始输出状态为 `High` 还是 `Low`。只要 **Propagation delay** 参数大于零且 Solver Configuration 模块未选择 **Start simulation from steady state** 选项，此参数就适用于线性和二次输出状态。
## 所属库

Simscape / Electrical / Integrated Circuits / Logic

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

## 描述

S-R 锁存器的行为模型

S-R Latch 模块是置位-复位锁存器的抽象行为模型。它不对内部单个 MOSFET 器件进行建模（详见假设和限制）。因此，该模块在仿真期间运行速度快，同时保持正确的 I/O 行为。

如果栅极电压大于阈值电压 VTH，则输入被视为 `1`（`HIGH`）。否则，输入为零（`LOW`）。栅极阈值电压 VTH 位于 **Low level input voltage**（VIL）和 **High level input voltage**（VIH）参数之间的一半处。

根据栅极输入的逻辑电平和 S-R 锁存器真值表，模块输出逻辑电平为 HIGH 或 LOW。

| S | R | Q n |
| --- | --- | --- |
| 0 | 0 | Q n-1 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

该模块对栅极建模如下：

- 栅极输入具有无限电阻和有限或零电容。
- 栅极输出提供两种模型选择：`Linear` 和 `Quadratic`。有关详细信息，请参阅 Selecting the Output Model for Logic Blocks。使用 **Output current-voltage relationship** 参数指定输出模型。
- 可以为两种输出模型指定传播延迟。对于 `Linear` 输出，模块设置栅极输出电容的值，使得电阻-电容时间常数等于 **Propagation delay** 参数值。对于 `Quadratic` 输出，栅极输入需求被延迟以近似 **Propagation delay** 参数值。

模块初始条件取决于所选的输出模型：

- 对于 `Linear` 模型，高初始条件对应于 **High level output voltage** 参数值 `V_OH`，低初始条件对应于 **Low level output voltage** 参数值 `V_OL`。
- 对于 `Quadratic` 模型，高初始条件为接近 **Supply voltage** 参数值 `Vcc` 的值，低初始条件接近 `0`。

模块输出电压取决于所选的输出模型：

- 对于 `Linear` 模型，输出高电平为 **High level output voltage** 参数值，输出低电平为 **Low level output voltage** 参数值。
- 对于 `Quadratic` 模型，High 和 Low 状态的输出电压是输出电流的函数，如 Quadratic Model Output and Parameters 中所述。对于零负载电流，输出高电平为 Vcc（**Supply voltage** 参数值），输出低电平为零伏。

### 绘制输入和输出波形

无需构建完整模型即可绘制 S-R Latch 模块的输入和输出波形。使用这些图来探索参数选择对器件特性的影响。如果从数据手册中参数化模块，可以将图与数据手册进行比较，以检查是否正确参数化了模块。如果已有完整的工作模型但不知道使用哪个制造器件，可以将图与数据手册进行比较以帮助决策。

要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。

**注意**

使用 **Basic characteristics** 选项创建的图不显示 **Propagation delay** 参数对逻辑模块输出电压的影响。
