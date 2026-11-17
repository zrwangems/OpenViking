---
type: simulink-block
title: 'D Flip-Flop'
family: 'simulink-extras'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'dflipflop'
documentation_source_path: 'ref/dflipflop.html'
language: zh-CN
chinese_source: worker-translation
---

# D Flip-Flop

## 端口
```yaml
ports:
- name: Invalid
  summary: 输出有效性，无单位物理信号
  direction: output
- name: D
  summary: 数据引脚电气
  direction: output
- name: Clk
  summary: 时钟引脚电气
  direction: output
- name: Q
  summary: 输出引脚电气
  direction: output
- name: '!Q'
  summary: 反相输出引脚电气
  direction: output
```

### 输出

### **Invalid** — 输出有效性，无单位物理信号

输出有效性端口。在建立时间和保持时间期间，物理信号的值为 `1`。在这些条件下，真实 D 触发器硬件的输出是不可预测的。否则，该物理信号的值为 `0`。

#### 依赖关系

要启用此端口，请选中 **Expose output validity port** 参数。
### 守恒

### **D** — 数据引脚电气

与数据引脚关联的电气守恒端口。

### **Clk** — 时钟引脚电气

与时钟引脚关联的电气守恒端口。

### **Q** — 输出引脚电气

与输出引脚关联的电气守恒端口。

### **!Q** — 反相输出引脚电气

与反相输出引脚关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Low level input voltage
  summary: 低于该输入电压时逻辑为 0 2 V（默认）| 非负标量
  group: 输入
- name: High level input voltage
  summary: 高于该输入电压时逻辑为 1 3 V（默认）| 正标量
  group: 输入
- name: Average input capacitance
  summary: MOSFET 栅极的输入电容 5 pF（默认）| 非负标量
  group: 输入
- name: Edge Trigger
  summary: 时钟触发的有效边沿 Falling（默认）| Rising
  group: 输入
- name: Output current-voltage relationship
  summary: 输出电流-电压关系的模型 Linear（默认）| Quadratic
  group: 输出
- name: Low level output voltage
  summary: 逻辑为 0 时的输出电压 0 V（默认）| 非负标量
  group: 输出
- name: High level output voltage
  summary: 逻辑为 1 时的输出电压 5 V（默认）| 正标量
  group: 输出
- name: Output resistance
  summary: 输出电阻 25 Ohm（默认）| 非负标量
  group: 输出
- name: Supply voltage
  summary: 电源电压 5 V（默认）| 正标量
  group: 输出
- name: Measurement voltage
  summary: 测量电源电压 5 V（默认）| 正标量
  group: 输出
- name: Logic HIGH output resistance at zero current and at I_OH
  summary: 输出逻辑为 1 时的电阻 [25, 250] Ohm | 正标量的二维向量
  group: 输出
- name: Logic HIGH output current I_OH when shorted to ground
  summary: 逻辑为 1 时的输出电流 63 mA（默认）| 正标量
  group: 输出
- name: Logic LOW output resistance at zero current and at I_OL
  summary: 输出逻辑为 0 时的电阻 [30, 800] Ohm（默认）| 正标量的二维向量
  group: 输出
- name: Logic LOW output current I_OL when shorted to Vcc
  summary: 逻辑为 0 时的输出电流 -45 mA（默认）| 负标量
  group: 输出
- name: Propagation delay
  summary: 输出电压改变状态的时间 25 ns（默认）| 非负标量
  group: 输出
- name: Setup time
  summary: 转换前输入必须保持稳定的时间 20 ns（默认）| 非负标量
  group: 输出
- name: Hold time
  summary: 转换后输入必须保持稳定的时间 5 ns（默认）| 非负标量
  group: 输出
- name: Protection diode on resistance
  summary: 保护二极管导通电阻 5 Ohm（默认）| 正标量
  group: 输出
- name: Protection diode forward voltage
  summary: 保护二极管正向电压 0.6 V（默认）| 正标量
  group: 输出
- name: Expose output validity port
  summary: 用于暴露输出有效性端口的选项 Off（默认）| On
  group: 输出
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 输入

### **Low level input voltage** — 低于该输入电压时逻辑为 `0` `2` `V`（默认）| 非负标量

低于该输入电压时，模块将输入逻辑解释为 `0`。

### **High level input voltage** — 高于该输入电压时逻辑为 `1` `3` `V`（默认）| 正标量

高于该输入电压时，模块将输入逻辑解释为 `1`。

### **Average input capacitance** — MOSFET 栅极的输入电容 `5` `pF`（默认）| 非负标量

用于近似 MOSFET 栅极输入电容的固定电容。MOSFET 电容取决于所施加的电压。当您用另一个栅极驱动此模块时，**Average input capacitance** 参数会产生与 MOSFET 相似的上升时间。您可以在制造商数据表中找到该电容值。为了加快仿真速度，请将此参数设置为零。

### **Edge Trigger** — 时钟触发的有效边沿 `Falling`（默认）| `Rising`

时钟有效边沿的触发。若仅在 **Clk** 端口的逻辑电平从 `1` 转换为 `0` 时更新输出，请将 **Edge trigger** 参数设置为 `Falling`。若仅在 **Clk** 端口的逻辑电平从 `0` 转换为 `1` 时更新输出，请将 **Edge trigger** 参数设置为 `Rising`。

### 输出

### **Output current-voltage relationship** — 输出电流-电压关系的模型 `Linear`（默认）| `Quadratic`

确定输出电流与输出电压之间关系的模型。将此参数设置为 `Linear` 可加快仿真速度，设置为 `Quadratic` 可获得更准确的结果。有关详细信息，请参阅 Selecting the Output Model for Logic Blocks。

### **Low level output voltage** — 逻辑为 `0` 时的输出电压 `0` `V`（默认）| 非负标量

输出引脚处逻辑电平为 `0` 时的输出电压。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Linear`。

### **High level output voltage** — 逻辑为 `1` 时的输出电压 `5` `V`（默认）| 正标量

输出引脚处逻辑电平为 `1` 时的输出电压。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Linear`。

### **Output resistance** — 输出电阻 `25` `Ohm`（默认）| 非负标量

模块用于对输出电流引起的输出电压降进行建模的输出电阻。您可以通过将高电平输出电压除以最大低电平输出电流，从数据表中计算出该值。

如果将 **Propagation delay** 参数设置为零，则必须将 **Output resistance** 参数设置为正值。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Linear`。

### **Supply voltage** — 电源电压 `5` `V`（默认）| 正标量

您为电路中的栅极提供的电压。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Measurement voltage** — 测量电源电压 `5` `V`（默认）| 正标量

您据以给出输出电阻和电流的栅极电源电压。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic HIGH output resistance at zero current and at I\_OH** — 输出逻辑为 `1` 时的电阻 `[25, 250]` `Ohm` | 正标量的二维向量

输出逻辑电平为 `1` 时的电阻。将此参数指定为包含两个电阻值的行向量 [*R\_OH1*, *R\_OH2*]。第一个值 *R\_OH1* 是没有输出电流时输出电压-电流关系的梯度。第二个值 *R\_OH2* 是输出短接到地时输出电压-电流关系的梯度。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic HIGH output current I\_OH when shorted to ground** — 逻辑为 `1` 时的输出电流 `63` `mA`（默认）| 正标量

输出逻辑电平为 `1` 但负载迫使输出电压为零时的输出电流。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic LOW output resistance at zero current and at I\_OL** — 输出逻辑为 `0` 时的电阻 `[30, 800]` `Ohm`（默认）| 正标量的二维向量

输出逻辑电平为 `0` 时的电阻。将此参数指定为包含两个电阻值的行向量 [*R\_OL1*, *R\_OL2*]。第一个值 *R\_OL1* 是没有输出电流时输出电压-电流关系的梯度。第二个值 *R\_OL2* 是负载迫使输出电压达到 **Supply voltage** 参数值时输出电压-电流关系的梯度。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Logic LOW output current I\_OL when shorted to Vcc** — 逻辑为 `0` 时的输出电流 `-45` `mA`（默认）| 负标量

输出逻辑电平为 `0` 但负载迫使输出电压达到 **Supply voltage** 参数值时的输出电流。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Propagation delay** — 输出电压改变状态的时间 `25` `ns`（默认）| 非负标量

在输入逻辑电平改变后，输出电压从 `low` 变为 `high` 或从 `high` 变为 `low` 状态所需的时间。

如果将 **Propagation delay** 参数设置为零，则必须将 **Output resistance** 参数设置为正值。

### **Setup time** — 转换前输入必须保持稳定的时间 `20` `ns`（默认）| 非负标量

在时钟有效边沿上的转换之前，输入数据必须保持稳定的最短时间，以便触发器的锁存器正确锁存。

### **Hold time** — 转换后输入必须保持稳定的时间 `5` `ns`（默认）| 非负标量

在时钟有效边沿上的转换之后，输入数据必须保持稳定的最短时间，以便触发器的锁存器正确锁存。

### **Protection diode on resistance** — 保护二极管导通电阻 `5` `Ohm`（默认）| 正标量

保护二极管正向偏置时其电压-电流关系的梯度。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Protection diode forward voltage** — 保护二极管正向电压 `0.6` `V`（默认）| 正标量

保护二极管导通时的电压。

#### 依赖关系

要启用此参数，请将 **Output current-voltage relationship** 设置为 `Quadratic`。

### **Expose output validity port** — 用于暴露输出有效性端口的选项 `Off`（默认）| `On`

用于暴露 **Invalid** 端口的选项。
## 所属库

Simscape / Electrical / Integrated Circuits / Logic

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

D 触发器的行为模型

D Flip-Flop 模块实现时钟 D 触发器的行为模型。该模块存储一位值，即 `0`（`low`）或 `1`（`high`）。

该模块有两个输入端口：数据引脚 **D** 和时钟引脚 **Clk**。该模块将 **D** 处的数据传输到输出引脚 **Q**。仅当时钟信号在时钟的有效边沿发生转换时，输出才会更新。否则，该模块将输出保持在其先前状态。

您可以在时钟的下降沿或上升沿更新输出。若仅在时钟从 `high` 转换为 `low` 时更新输出，请将 **Edge trigger** 参数设置为 `Falling`。若仅在时钟从 `low` 转换为 `high` 时更新输出，请将 **Edge trigger** 参数设置为 `Rising`。此真值表总结了输入和输出处的逻辑电平。下标 `n` 表示当前时钟周期的值，`n-1` 表示前一时钟周期的值。反相输出引脚 **!Q** 处的逻辑电平是 **Q** 处逻辑电平的反相。

| Edge trigger 参数值 | Clkn-1 | Clkn | Qn |
| --- | --- | --- | --- |
| `Falling` | `0` | `0` | Qn-1 |
| `Falling` | `0` | `1` | Qn-1 |
| `Falling` | `1` | `0` | Dn |
| `Falling` | `1` | `1` | Qn-1 |
| `Rising` | `0` | `0` | Qn-1 |
| `Rising` | `0` | `1` | Dn |
| `Rising` | `1` | `0` | Qn-1 |
| `Rising` | `1` | `1` | Qn-1 |

要在仿真开始时指定 **Q** 处的逻辑电平，请在 **Initial Targets** 部分中，将 **Output logic** 参数的值设置为 `0` 或 `1`。有关初始目标的详细信息，请参阅 Set Priority and Initial Target for Block Variables。

栅极输入具有无限电阻和有限或零电容。

如果栅极电压大于阈值电压，则模块将输入处的逻辑电平视为 `1`。否则，模块将输入处的逻辑电平视为 `0`。模块将阈值电压计算为 **Low level input voltage** 和 **High level input voltage** 参数值的平均值。

栅极输出取决于 **Output current-voltage relationship** 参数。将此参数设置为 `Linear` 可加快仿真速度，设置为 `Quadratic` 可获得更准确的结果。对于大多数模型，请使用 `Linear` 选项。您可以使用 `Quadratic` 选项来验证使用更简单的线性模型获得的结果。有关详细信息，请参阅 Selecting the Output Model for Logic Blocks。

如果将 **Output current-voltage relationship** 参数设置为 `Linear`：

- 如果 **Q** 端口处的逻辑电平为 `0`，则输出电压等于 **Low level output voltage** 参数值。
- 如果 **Q** 端口处的逻辑电平为 `1`，则输出电压等于 **High level output voltage** 参数值。
- 栅极输出电容的电阻-电容时间常数等于 **Propagation delay** 参数值。

如果将 **Output current-voltage relationship** 参数设置为 `Quadratic`：

- 输出电压是输出电流的函数。对于零负载电流：

  - 如果 **Q** 端口处的逻辑电平为 `0`，则输出电压为零。
  - 如果 **Q** 端口处的逻辑电平为 `1`，则输出电压等于 **Supply voltage** 参数值。
- 栅极输入需求滞后，以近似 **Propagation delay** 参数值。

有关详细信息，请参阅 Quadratic Model Output and Parameters。

### 绘制输入和输出波形

您无需构建完整模型即可绘制 D Flip-Flop 模块的输入和输出波形。使用这些图可探究您的参数选择对器件特性的影响。如果您根据数据表对模块进行参数化，则可以将您的图与数据表进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整的工作模型但不知道使用哪个制造零件，则可以将您的图与数据表进行比较，以帮助您做出决定。

要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。

**注意**

使用 **Basic characteristics** 选项创建的图不会显示 **Propagation delay** 参数对逻辑模块输出电压的影响。

### 假设和限制

- 为提高仿真速度，该模块不会对栅极中的所有内部金属氧化物半导体场效应晶体管 (MOSFET) 器件单独建模。因此，该模块无法准确地对栅极对输入噪声和接近阈值电压的输入电压的响应进行建模。
- 如果您要对具有围绕一组逻辑门的反馈路径的电路进行建模，则必须在一个或多个栅极上将 **Propagation delay** 参数设置为非零值。
