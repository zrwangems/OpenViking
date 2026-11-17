---
type: simulink-block
title: 'Cable and Connectors'
family: 'connectors-references'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'cableandconnectors'
documentation_source_path: 'ref/cableandconnectors.html'
language: zh-CN
chinese_source: worker-translation
---

# Cable and Connectors

## 端口

### 守恒

### **In** — 输入连接器端子 electrical | electrical array-of-nodes

与输入连接器端子关联的 electrical 守恒端口或 electrical array-of-nodes 守恒端口。

如果清除 **Model multiple conductors in cable** 参数，则此端口是 electrical 守恒端口。

如果选中 **Model multiple conductors in cable** 参数，则此端口是 electrical array-of-nodes 守恒端口。要将此端口连接到电气网络，请使用 Array Connection 模块。有关详细信息，请参阅 Cable。

### **Out** — 输出连接器端子 electrical | electrical array-of-nodes

与输出连接器端子关联的 electrical 守恒端口或 electrical array-of-nodes 守恒端口。

如果清除 **Model multiple conductors in cable** 参数，则此端口是 electrical 守恒端口。

如果选中 **Model multiple conductors in cable** 参数，则此端口是 electrical array-of-nodes 守恒端口。要将此端口连接到电气网络，请使用 Array Connection 模块。有关详细信息，请参阅 Cable。

### **H** — 热质量 thermal

与热质量关联的热守恒端口。

#### 依赖项

要启用此端口，请选中 **Model thermal effects** 参数。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主

### **Model multiple conductors in cable** — 对电缆中的多个导体建模的选项 `Off` (默认) | `On`

对电缆中的多个导体建模的选项。

### **Number of independent conductors in cable** — 电缆中独立导体的数量 `3` (默认) | finite positive scalar

电缆中独立导体的数量。

#### 依赖项

要启用此参数，请选中 **Model multiple conductors in cable** 参数。

### **Model input connector** — 对输入连接器建模的选项 `On` (默认) | `Off`

对输入连接器建模的选项。

### **Model output connector** — 对输出连接器建模的选项 `On` (默认) | `Off`

对输出连接器建模的选项。

### 电缆

### **Conductor material** — 导体材料 `Copper` (默认) | `Annealed copper` | `Aluminum` | `Silver` | `Gold` | `Custom`

导体材料。此参数确定材料的电导率和磁导率。要为材料属性指定自己的值，请将此参数设置为 `Custom`。

### **Electrical conductivity of material** — 材料的电导率 `5.96e7` `S/m` (默认) | nonnegative scalar

材料的电导率。

#### 依赖项

要启用此参数，请将 **Conductor material** 设置为 `Custom`。

### **Length of conductor** — 导体长度 `1` `m` (默认) | positive scalar

每个导体的长度。

### **Gauge of each conductor** — AWG 系统中的导体线规 `Custom` (默认) | `AWG1` | `AWG2` | ...

每个导体的线规，以美国线规 (AWG) 系统指定。请选择从 `AWG1` 到 `AWG40` 的值。

要以长度单位指定线规，请将此参数设置为 `Custom`，并为 **Conductor diameter** 参数指定值。

### **Conductor diameter** — 以长度单位表示的每个导体线规 `0.5` `mm` (默认) | positive scalar

每个导体的线规，以长度单位指定。

#### 依赖项

要启用此参数，请将 **Gauge of each conductor** 设置为 `Custom`。

### **Model cable inductance** — 对电缆电感建模的选项 `Off` (默认) | `On`

对电缆电感建模的选项。

清除此参数以优先考虑高仿真速度。选中此参数以优先考虑准确结果。

### **Model skin effect** — 对集肤效应建模的选项 `Off` (默认) | `On`

对集肤效应建模的选项。

### **Rated frequency** — 额定频率 `50` `Hz` (默认) | nonnegative scalar

电缆的额定频率。

#### 依赖项

要启用此参数，请选中 **Model skin effect** 参数。

### **Relative magnetic permeability of material** — 材料的相对磁导率 `1` (默认) | positive scalar

材料的相对磁导率。

#### 依赖项

要启用此参数，请将 **Conductor material** 设置为 `Custom`。

### 连接器

### **Contact resistance between pins and sockets** — 引脚与插座之间的接触电阻 `1` `Ohm` (默认) | positive scalar

引脚与插座之间的接触电阻。

#### 依赖项

要启用此参数，请选中 **Model input connector** 或 **Model output connector** 参数。

### **Conductance between pins** — 引脚之间的电导 `1e-12` `S` (默认) | positive scalar

引脚之间的电导。

#### 依赖项

要启用此参数：

- 选中 **Model input connector** 或 **Model output connector** 参数。
- 选中 **Model multiple conductors in cable** 参数。

### 热

### **Model thermal effects** — 对热效应建模的选项 `Off` (默认) | `On`

对热效应建模的选项。选中此参数以启用 **H** 端口。

### **Resistance temperature coefficient** — 电阻温度系数 `1e-6` `1/K` (默认) | nonnegative scalar

电阻温度系数。

#### 依赖项

要启用此参数，请选中 **Model thermal effects** 参数。

### **Measurement temperature** — 测量温度 `298.15` `K` (默认) | scalar

测量温度。此值是您提供 **Resistance temperature coefficient** 参数值的温度。

#### 依赖项

要启用此参数，请选中 **Model thermal effects** 参数。

### **Thermal mass of each conductor** — 每个导体的热质量 `0.1` `J/K` (默认) | positive scalar

每个导体的热质量。

#### 依赖项

要启用此参数，请选中 **Model thermal effects** 参数。

### **Thermal mass of each connector pin** — 每个连接器引脚的热质量 `0.1` `J/K` (默认) | positive scalar

每个连接器引脚的热质量。

#### 依赖项

要启用此参数，请选中 **Model thermal effects** 参数。

### 故障

### **Inter-pin short circuit in input connector fault** — 添加输入连接器引脚间短路故障的选项 `Add fault`

向输入连接器添加引脚间短路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

#### 依赖项

要启用此参数，请选中 **Model multiple conductors in cable** 和 **Model input connector** 参数。

### **Short-circuit conductance of faulted input connector** — 故障输入连接器的短路电导 `1e9` `S` (默认) | nonnegative scalar

故障输入连接器的短路电导。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。

### **Faultable pin pairs** — 可发生故障的引脚对 `Make all pin pairs faultable` (默认) | `Specify faultable pin pairs`

使所有引脚对可发生故障或指定可发生故障的引脚对的选项。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。

### **Matrix of faultable pin pairs** — 可发生故障的引脚对 `[1,2;1,3]` (默认) | matrix

可发生故障的引脚对，指定为 `N`×`2` 矩阵，其中 `N` 是可发生故障的引脚对数量，每行通过索引定义一对引脚。例如，要启用引脚 1 和引脚 2 之间的短路故障，请将行 `1,2;` 添加到矩阵中。当短路故障触发时，引脚间电导仅对您指定的引脚对发生变化。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。
- 将 **Faultable pin pairs** 设置为 `Specify faultable pin pairs`。

### **Trigger type** — 触发类型 `Always on` (默认) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Behavioral` — 故障在仿真期间因故障参数值而注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器而注入。选中此选项，并点击 **Open fault properties** 超链接，以在 Property Inspector 中将 **Trigger type** 设置为以下值之一：
  - `Conditional` — 故障因反映与信号关联行为的条件而注入。条件会在每个时间步计算 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选中 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真余下时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。要了解详细信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解详细信息，请参阅 Manually Trigger Faults in Models。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s` (默认) | nonnegative scalar

模块进入故障状态时的仿真时间。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible temperature** — 故障转换的温度上限阈值 `inf` `degC` (默认) | scalar

行为故障转换的温度上限阈值。如果温度连续超过此值的时间长于 **Time to fail when exceeding temperature** 参数的值，则模块进入故障状态。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 选中 **Model thermal effects** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding temperature** — 超过温度时发生故障的时间 `1` `s` (默认) | positive scalar

在行为故障触发之前，温度必须连续超过最大允许温度的时间量。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 选中 **Model thermal effects** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Maximum permissible voltage** — 故障转换的电压阈值 `inf` `V` (默认) | positive scalar

故障转换的电压阈值。如果电压连续超过此值的时间长于 **Time to fail when exceeding voltage** 参数的值，则模块进入故障状态。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding voltage** — 超过电压时发生故障的时间 `1` `s` (默认) | positive scalar

在短路故障触发之前，电压必须连续超过最大允许电压的时间量。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model input connector** 参数。
- 点击 **Inter-pin short circuit in input connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Additional triggers`。

### **Inter-pin short circuit in output connector fault** — 添加输出连接器引脚间短路故障的选项 `Add fault`

向输出连接器添加引脚间短路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

#### 依赖项

要启用此参数，请选中 **Model multiple conductors in cable** 和 **Model output connector** 参数。

### **Short-circuit conductance of faulted output connector** — 故障输出连接器的短路电导 `1e9` `S` (默认) | nonnegative scalar

故障输出连接器的短路电导。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model output connector** 参数。
- 点击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。

### **Faultable pin pairs** — 可发生故障的引脚对 `Make all pin pairs faultable` (默认) | `Specify faultable pin pairs`

使所有引脚对可发生故障或指定可发生故障的引脚对的选项。

#### 依赖项

要启用此参数：

- 选中 **Model multiple conductors in cable** 参数。
- 选中 **Model output connector** 参数。
- 点击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。

### **Matrix of faultable pin pairs** — Faultable pin pairs `[1,2;1,3]`（默认） | matrix

可发生故障的引脚对，指定为一个 `N`-by-`2` 矩阵，其中 `N` 是可发生故障的引脚对的数量，每一行通过引脚索引定义一对引脚。例如，要启用引脚 1 和引脚 2 之间的短路故障，请将行 `1,2;` 添加到矩阵中。当短路故障触发时，仅会为您指定的引脚对改变引脚间电导。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model output connector** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。
- 将 **Faultable pin pairs** 设置为 `Specify faultable pin pairs`

### **Trigger type** — Trigger type `Always on`（默认） | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

**Trigger type**，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Behavioral` — 故障由于仿真期间的故障参数值而注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障由于模块对话框中不可用的其他触发器而注入。选择此选项并单击 **Open fault properties** 超链接，以在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由于反映与信号关联行为的条件而注入。条件在每个时间步计算 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件第一次变为 true 时，模块进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model input connector** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认） | nonnegative scalar

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model input connector** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible temperature** — 故障转换的上温度阈值 `inf` `degC`（默认） | scalar

行为故障转换的上温度阈值。如果温度连续超过此值的时间长于 **Time to fail when exceeding temperature** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model input connector** 参数。
- 选择 **Model thermal effects** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding temperature** — 超过温度时的失效时间 `1` `s`（默认） | positive scalar

在行为故障触发之前，温度必须连续超过最大允许温度的时间量。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model input connector** 参数。
- 选择 **Model thermal effects** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Maximum permissible voltage** — 故障转换的电压阈值 `inf` `V`（默认） | positive scalar

故障转换的电压阈值。如果电压连续超过此值的时间长于 **Time to fail when exceeding voltage** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model input connector** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding voltage** — 超过电压时的失效时间 `1` `s`（默认） | positive scalar

在短路故障触发之前，电压必须连续超过最大允许电压的时间量。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model input connector** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用其他触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的其他触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请单击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 选择 **Model output connector** 参数。
- 单击 **Inter-pin short circuit in output connector fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Additional triggers`。

### **Open-circuit fault** — 添加开路故障的选项 `Add fault`

用于向电缆中的导体添加开路故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Open-circuit conductance** — 开路电导 `1e-5` `S`（默认） | positive scalar

电缆中发生故障的导体的开路电导。

#### 依赖关系

要启用此参数，请单击 **Open-circuit fault** 参数的 **Add fault** 超链接。

### **Faultable conductors** — 可故障导体 `Make all conductors faultable`（默认） | `Specify faultable conductors`

用于使所有导体可发生故障，或指定可发生故障的导体的选项。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 单击 **Open-circuit fault** 参数的 **Add fault** 超链接。

### **Indices of faultable conductors** — 可故障导体的索引 `[1,2]`（默认） | vector

可故障导体的索引。当开路故障触发时，仅具有您指定索引的导体的电导会发生变化。

#### 依赖关系

要启用此参数：

- 选择 **Model multiple conductors in cable** 参数。
- 单击 **Open-circuit fault** 参数的 **Add fault** 超链接。
- 将 **Faultable conductors** 设置为 `Specify faultable conductors`。

### **Trigger type** — Trigger type `Always on`（默认） | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

**Trigger type**，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Behavioral` — 故障由于仿真期间的故障参数值而注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障由于模块对话框中不可用的其他触发器而注入。选择此选项并单击 **Open fault properties** 超链接，以在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由于反映与信号关联行为的条件而注入。条件在每个时间步计算 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件第一次变为 true 时，模块进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请单击 **Open-circuit fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认） | nonnegative scalar

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请单击 **Open-circuit fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible current** — 故障转换的电流阈值 `inf` `A`（默认） | positive scalar

故障转换的电流阈值。如果电流连续超过此值的时间长于 **Time to fail when exceeding current** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请单击 **Open-circuit fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Maximum permissible temperature** — 故障转换的上温度阈值 `inf` `degC`（默认） | scalar

行为故障转换的上温度阈值。如果温度连续超过此值的时间长于 **Time to fail when exceeding temperature** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数：

- 选择 **Model thermal effects** 参数。
- 单击 **Open-circuit fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding current** — 超过电流时的失效时间 `1` `s`（默认） | positive scalar

在故障触发之前，电流必须连续超过最大允许电流的时间量。

#### 依赖关系

要启用此参数，请单击 **Open-circuit fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding temperature** — 超过温度时的失效时间 `1` `s`（默认） | positive scalar

在行为故障触发之前，温度必须连续超过最大允许温度的时间量。

#### 依赖关系

要启用此参数：

- 选择 **Model thermal effects** 参数。
- 单击 **Open-circuit fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用其他触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的其他触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请单击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请单击 **Open-circuit fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional triggers`。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: 对可逆条件故障建模

现在，您可以通过清除 **Trigger stays on once activated** 参数，在 Cable and Connectors 模块中对可逆条件故障建模。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入非故障状态。

在 R2025a 之前，当触发条件第一次变为 true 时，模块进入故障状态，并在仿真剩余时间内保持故障状态。

如果您在 R2025a 之前创建模型并在 Cable and Connectors 模块中启用条件故障，则为了实现向后兼容，该模块现在默认选择 **Trigger stays on once activated** 参数。

## 描述

具有可选故障建模的电缆和连接器

Cable and Connectors 模块使用电阻和电感对电缆和连接器进行建模。

对于大多数应用，您可以使用物理连接线直接连接两个或多个模块。这些连接线是理想化的，没有电阻或电感。如果您需要电气电缆或连接器的简单基于物理的模型，可以使用 Resistor 模块和 Inductor 模块的组合。如果您希望执行以下操作，请改用 Cable and Connectors 模块：

- 对单根电缆中的多个导体建模。
- 分析具有开路故障的电缆。
- 分析具有短路故障的输入或输出连接器。
- 通过定义材料和几何形状而非电阻和电感来参数化导体。
- 使用 American wire gauge (AWG) 系统指定导体的线规。

### Cable

Cable and Connectors 模块将电缆中的每根导体建模为电阻器。您还可以通过选中 **Model cable inductance** 参数来选择包含与电阻器串联的电感器。清除此参数以优先提高仿真速度。选中此参数以优先获得准确结果。

要对单根导体建模，请清除 **Model multiple conductors in cable** 参数。要对多根导体建模，请选中 **Model multiple conductors in cable** 参数，并使用 **Number of independent conductors in cable** 参数指定导体数量。

Cable and Connectors 模块有两个端口，分别表示电缆的输入端和输出端。如果对单根导体建模，这些 **In** 和 **Out** 端口是电气守恒端口。如果对多根导体建模，**In** 和 **Out** 端口是电气节点数组守恒端口。要将电气节点数组端口连接到网络的其余部分，请使用 Array Connection 模块充当 Simscape™ 电气域的多路复用器，将所有输入节点数组拼接成一个一维数组。首先，将 **In** 和 **Out** 端口连接到单独的 Array Connection 模块的 **RConn** 端口。**RConn** 端口名称在模块图标中不可见，但将指针悬停在该端口上时可以看到此名称。然后，将 Array Connection 模块的 **Domain** 参数设置为 `Electrical Domain`。最后，将 Array Connection 模块的 **Number of scalar elements** 参数设置为与 Cable and Connectors 模块的 **Number of independent conductors in cable** 参数相同的值。下图展示了如何将电缆中具有三根独立导体的 Cable and Connectors 模块连接到电气网络。

Cable and Connectors 模块与两个 Array Connection 模块串联连接

**方程**

该模块假设电缆中的导体是圆导线，并使用以下方程 [1] 计算每根导体的电阻 *R*：

R=ρLπ(r2−(r−δ)2)

δ={1πμσf       if r≥1πμσfr                  if r≤1πμσf

其中：

- *ρ* 是每根导体的电阻率。
- *L* 是 **Length of conductor** 参数的值。
- *r* 是导体的半径。
- *δ* 是趋肤深度。
- *μ* 是导体的磁导率。
- *σ* 是导体的电导率。
- *f* 是额定频率。

对于直流电流，不存在趋肤效应。电流均匀分布在导体横截面上，因此 *δ* = *r*。对于高频交流电流，在完全趋肤效应下，电流仅在导体表面流动，因此 *δ* = 0。

如果清除 **Model skin effect** 参数，则 *f* = 0。如果选中 **Model skin effect** 参数，则 *f* 等于 **Rated frequency** 参数的值。

如果选中 **Model cable inductance** 参数，则该模块使用以下方程 [2] 计算每根导体的电感 *LDC*：

LDC=μ02πL(ln(2Lr)−Y)

Y=11+rπ4μσf

其中：

- *μ*0 是自由空间的磁导率。
- *Y* 是电流分布常数。

电流分布常数的值介于 0 和 1 之间。对于直流，*Y* = 1。对于高频交流，*Y* 趋近于 0。

### 连接器

该模块使用电阻器对连接器建模。连接器中的引脚数等于电缆中独立导体的数量。下图展示了三引脚输入连接器的等效电路。标记为 `Ri` 的电阻器对每个引脚与对应插座之间的接触电阻建模。标记为 `Gij` 的电阻器对每个引脚对 `(i,j)` 之间的引脚间电导建模。

连接器由每个引脚与插座之间以及每对引脚之间的电阻器表示

使用 **Contact resistance between pin and sockets** 参数指定电阻器 `Ri` 的电阻。使用 **Conductance between pins** 参数指定电阻器 `Gij` 的电导。

您并不总是需要对电缆两端的连接器建模。例如：

- 如果您对直接焊接到印刷电路板 (PCB) 的电缆建模，则不要对电缆该端的连接器建模，以获得更高精度。
- 如果您对具有近乎理想连接器的电缆建模，或者对电缆中的开路故障建模，则连接器中引脚间的电导以及引脚与插座之间的接触电阻对仿真结果的影响可忽略不计。

您可以使用 **Model input connector** 和 **Model output connector** 参数选择是否对每个连接器建模。为了提高仿真速度，如果不需要，请不要对连接器建模。

### 故障

要对 Cable and Connectors 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

Cable and Connectors 模块将电气故障建模为电缆或连接器电导的瞬时变化。您可以对电缆中的开路故障或连接器中的短路故障建模。

当电缆发生开路故障时，导体的电导变为 **Open-circuit conductance** 参数的值。如果您对同一电缆中的多根导体建模，可以选择为所有导体触发故障，或指定要发生故障的导体。

- 要为所有导体触发开路故障，请将 **Faultable conductors** 设置为 `Make all conductors faultable`。
- 要为特定导体触发开路故障，请将 **Faultable conductors** 设置为 `Specify faultable conductors`，并使用 **Indices of faultable conductors** 参数指定要发生故障的导体。

当输入或输出连接器短路时，引脚对的引脚间电导分别变为 **Short-circuit conductance of faulted input connector** 或 **Short-circuit conductance of faulted output connector** 参数的值。

- 要为所有引脚对触发短路故障，请将 **Faultable pin pairs** 设置为 `Make all pin pairs faultable`。
- 要为特定引脚对触发短路故障，请将 **Faultable conductors** 设置为 `Specify faultable conductors`，并使用 **Matrix of faultable pin pairs** 参数指定要发生故障的导体。此矩阵的每一行通过索引定义一对引脚。例如，要启用引脚 1 和引脚 2 之间的短路故障，请将行 `1,2;` 添加到矩阵中。

**故障触发器**

您可以使用 **Trigger type** 参数指定故障发生的方式和时间。

如果将 **Trigger type** 设置为 `Behavioral`，当温度持续超过 **Maximum permissible temperature** 的值，且持续时间长于 **Time to fail when exceeding temperature** 参数的值时，Cable and Connectors 模块会触发故障事件。该模块还会触发：

- 当电流持续超过 **Maximum permissible current** 参数的值，且持续时间长于 **Time to fail when exceeding current** 参数的值时，触发电缆中的开路故障。
- 当电压持续超过 **Maximum permissible voltage** 参数的值，且持续时间长于 **Time to fail when exceeding voltage** 参数的值时，触发连接器中的短路故障。

如果将 **Trigger type** 设置为 `Conditional`，您可以选择 Cable and Connectors 模块中的故障是否可逆 *(自 R2025a 起)*。要对不可逆故障建模，请单击 **Open fault properties** 以打开属性检查器，并选中 **Trigger stays on once activated** 参数。当触发条件第一次变为 true 时，该模块进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，该模块进入故障状态；当触发条件为 false 时，该模块进入无故障状态。

有关向模块添加故障和指定故障触发器的详细信息，请参阅 Simscape 故障简介。
