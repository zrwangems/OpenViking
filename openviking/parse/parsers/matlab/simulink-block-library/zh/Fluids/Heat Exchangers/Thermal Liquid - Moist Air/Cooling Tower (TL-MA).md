---
type: simulink-block
title: 'Cooling Tower (TL-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Moist Air'
documentation_page: 'coolingtowertlma'
documentation_source_path: 'ref/coolingtowertlma.html'
language: zh-CN
chinese_source: worker-translation
---

# Cooling Tower (TL-MA)

## 端口
```yaml
ports:
- name: M
  summary: 质量流量，kg/s 物理信号
  direction: input
- name: V
  summary: 体积流量，m^3/s 物理信号
  direction: input
- name: Pwr
  summary: 风机功率，W 物理信号
  direction: input
- name: P
  summary: 压力，Pa 物理信号
  direction: input
- name: T
  summary: 温度，K 物理信号
  direction: input
- name: W
  summary: 湿度度量，无量纲 物理信号
  direction: input
- name: Tw
  summary: 湿球温度，K 物理信号
  direction: input
- name: Vm
  summary: 体积流量，m^3/s 物理信号
  direction: input
- name: Tm
  summary: 温度，K 物理信号
  direction: input
- name: Q
  summary: 传热量，W 物理信号
  direction: output
- name: E
  summary: 蒸发速率，kg/s 物理信号
  direction: output
- name: L
  summary: 液位，m 物理信号
  direction: output
- name: Pwr
  summary: 风机功率，W 物理信号
  direction: output
- name: A1
  summary: 热液入口 热液
  direction: output
- name: B1
  summary: 热液出口 热液
  direction: output
- name: A2
  summary: 湿空气入口或出口 湿空气
  direction: output
- name: B2
  summary: 湿空气入口或出口 湿空气
  direction: output
```

### 输入

### **M** — 质量流量，kg/s 物理信号

进入冷却塔的湿空气的质量流量。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，并将 **Flow rate input signal specification** 设置为 `Mass flow rate`。

### **V** — 体积流量，m^3/s 物理信号

进入冷却塔的湿空气的体积流量。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，并将 **Flow rate input signal specification** 设置为 `Volumetric flow rate`。

### **Pwr** — 风机功率，W 物理信号

驱动湿空气通过冷却塔的风机功率。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，并将 **Flow rate input signal specification** 设置为 `Fan power`。

### **P** — 压力，Pa 物理信号

进入冷却塔的湿空气的压力。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`。

### **T** — 温度，K 物理信号

进入冷却塔的湿空气的干球温度。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`。

### **W** — 湿度度量，无量纲 物理信号

进入冷却塔的湿空气的相对湿度、比湿度、水蒸气摩尔分数或湿度比。使用 **Humidity input signal specification** 参数指定湿度输入信号的类型。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，并将 **Humidity input signal specification** 设置为除 `Wet-bulb temperature` 之外的任意选项。

### **Tw** — 湿球温度，K 物理信号

进入冷却塔的湿空气的湿球温度。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，并将 **Humidity input signal specification** 设置为 `Wet-bulb temperature`。

### **Vm** — 体积流量，m^3/s 物理信号

补充因蒸发和漂移而损失的水的热液体积流量。

#### 依赖

要启用此端口，请选中 **Model cold-water basin** 并清除 **Automatically replenish lost water** 复选框。

### **Tm** — 温度，K 物理信号

补充因蒸发和漂移而损失的水的热液温度。

#### 依赖

要启用此端口，请选中 **Model cold-water basin** 并清除 **Automatically replenish lost water** 复选框。
### 输出

### **Q** — 传热量，W 物理信号

湿空气与热液之间的总显热和潜热传递。

### **E** — 蒸发速率，kg/s 物理信号

热液的蒸发速率。

### **L** — 液位，m 物理信号

冷却塔水池中热液的深度。

#### 依赖

要启用此端口，请选中 **Model cold-water basin** 并清除 **Automatically replenish lost water** 复选框。

### **Pwr** — 风机功率，W 物理信号

冷却塔中湿空气流动所需的风机功率。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，将 **Flow rate input signal specification** 设置为 `Mass flow rate` 或 `Volumetric flow rate`，并选中 **Output fan power**。
### 守恒

### **A1** — 热液入口 热液

与热液侧入口关联的热液守恒端口。

### **B1** — 热液出口 热液

与热液侧出口关联的热液守恒端口。

### **A2** — 湿空气入口或出口 湿空气

与湿空气侧入口或出口关联的湿空气守恒端口。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Moist air domain port`。

### **B2** — 湿空气入口或出口 湿空气

与湿空气侧入口或出口关联的湿空气守恒端口。

#### 依赖

要启用此端口，请将 **Moist air operating conditions** 设置为 `Moist air domain port`。
## 参数
```yaml
parameters:
- name: Flow arrangement
  summary: 湿空气和热液的流动布置 Counter flow（默认）| Cross flow
  group: Thermal Liquid 1
- name: Nominal capacity specification
  summary: 指定系统尺寸的方法 Water volumetric flow rate（默认）| Water mass flow rate | Rate of cooling in cooling tower | Rate of cooling
    in evaporator
  group: Thermal Liquid 1
- name: Nominal water mass flow rate
  summary: 额定工况下的质量流量 42.7 kg/s（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal water volumetric flow rate
  summary: 额定工况下的体积流量 154 m^3/hr（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal cooling tower heat transfer
  summary: 额定工况下的传热量 1000 kW（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal evaporator heat transfer
  summary: 额定工况下的蒸发器传热量 800 kW（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal hot-water inlet temperature
  summary: 热液入口温度 35 degC（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal cold-water outlet temperature
  summary: 热液出口温度 29.44 degC（默认）| 正标量
  group: Thermal Liquid 1
- name: Model cold-water basin
  summary: 将热液侧 1 建模为水箱的选项 on（默认）| off
  group: Thermal Liquid 1
- name: Basin cross-sectional area
  summary: 水池面积 8 m^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Cross-sectional area at port A1
  summary: 热液入口流通面积 0.01 m^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Cross-sectional area at port B1
  summary: 热液出口流通面积 0.01 m^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Drift rate as fraction of water flow
  summary: 热液漂移率 0（默认）| 正标量
  group: Thermal Liquid 1
- name: Automatically replenish lost water
  summary: 在热液侧 1 自动补充损失水的选项 on（默认）| off
  group: Thermal Liquid 1
- name: Temperature of make-up water
  summary: 补充水温度 15 degC（默认）| 正标量
  group: Thermal Liquid 1
- name: Initialize thermal liquid to nominal operating conditions
  summary: 初始化热液的选项 on（默认）| off
  group: Thermal Liquid 1
- name: Initial basin liquid temperature
  summary: 仿真开始时的水池温度 29.44 degC（默认）| 正标量
  group: Thermal Liquid 1
- name: Initial basin liquid level
  summary: 仿真开始时的水池液位 0.2 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Gravitational acceleration
  summary: 重力加速度常数 9.81 m/s^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Moist air operating conditions
  summary: 指定湿空气工况的方法 Provided by input signals（默认）| Moist air domain ports
  group: Moist Air 2
- name: Flow rate input signal specification
  summary: 指定实际湿空气流量的方法 Volumetric flow rate（默认）| Mass flow rate | Fan power
  group: Moist Air 2
- name: Output fan power
  summary: 输出风机功率的选项 off（默认）| on
  group: Moist Air 2
- name: Nominal fan power
  summary: 额定运行工况下的风机功率 7.5 kW（默认）| 正标量
  group: Moist Air 2
- name: Humidity input signal specification
  summary: 用于描述塔湿空气入口实际湿度水平的物理量 Wet-bulb temperature（默认）| Specific humidity | Mole fraction | Humidity ratio | Relative humidity
  group: Moist Air 2
- name: Input signals outside valid range
  summary: 处理无效信号值的方法 Warn and limit to valid values（默认）| Limit to valid values | Error
  group: Moist Air 2
- name: Specify full moist air nominal condition
  summary: 指定湿空气额定工况的选项 off（默认）| on
  group: Moist Air 2
- name: Nominal flow rate specification
  summary: 指定湿空气流量的选项 Volumetric flow rate（默认）| Mass flow rate
  group: Moist Air 2
- name: Nominal moist air mass flow rate
  summary: 额定质量流量 36 kg/s（默认）| 正标量
  group: Moist Air 2
- name: Nominal moist air volumetric flow rate
  summary: 额定体积流量 30 m^3/s（默认）| 正标量
  group: Moist Air 2
- name: Nominal moist air pressure loss
  summary: 额定工况下湿空气端口之间的压降 250 Pa（默认）| 正标量
  group: Moist Air 2
- name: Nominal inlet pressure
  summary: 湿空气侧入口处的压力 0.101325 MPa（默认）| 正标量
  group: Moist Air 2
- name: Nominal inlet temperature
  summary: 湿空气侧入口处的温度 34.28 degC（默认）| 正标量
  group: Moist Air 2
- name: Nominal humidity specification
  summary: 用于描述额定工况下湿度水平的量 Wet-bulb temperature（默认）| Specific humidity | Mole fraction | Humidity ratio | Relative humidity
  group: Moist Air 2
- name: Nominal inlet relative humidity
  summary: 入口处的相对湿度 0.5（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Nominal inlet specific humidity
  summary: 入口处的比湿度 0.0167（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Nominal inlet water vapor mole fraction
  summary: 入口处水蒸气的摩尔分数 0.0266（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Nominal inlet humidity ratio
  summary: 入口处的湿度比 0.017（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Nominal inlet wet-bulb temperature
  summary: 湿空气入口处的湿球温度 25.56 degC（默认）| 正标量
  group: Moist Air 2
- name: Nominal trace gas specification
  summary: 用于描述额定微量气体水平的量 Mass fraction（默认）| Mole fraction
  group: Moist Air 2
- name: Nominal inlet trace gas mass fraction
  summary: 入口处微量气体的质量分数 6e-4（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Nominal inlet trace gas mole fraction
  summary: 入口处微量气体的摩尔分数 4e-4（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Moist air volume
  summary: 冷却塔中湿空气的总体积 24 m^3（默认）| 正标量
  group: Moist Air 2
- name: Cross-sectional area at port A2
  summary: 湿空气入口或出口的面积 4 m^2（默认）| 正标量
  group: Moist Air 2
- name: Cross-sectional area at port B2
  summary: 湿空气入口或出口的面积 4 m^2（默认）| 正标量
  group: Moist Air 2
- name: Initialize moist air to nominal operating conditions
  summary: 初始化湿空气的选项 on（默认）| off
  group: Moist Air 2
- name: Initial moist air pressure
  summary: 仿真开始时的湿空气压力 0.101325 MPa（默认）| 正标量
  group: Moist Air 2
- name: Initial moist air temperature
  summary: 仿真开始时的湿空气温度 34.28 degC（默认）| 标量 | 二元素向量
  group: Moist Air 2
- name: Initial humidity specification
  summary: 用于描述初始湿度水平的量 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: Moist Air 2
- name: Initial moist air relative humidity
  summary: 仿真开始时的相对湿度 0.5（默认）| [0,1] 范围内的标量 | 二元素向量
  group: Moist Air 2
- name: Initial moist air specific humidity
  summary: 仿真开始时的比湿度 0.0167（默认）| [0,1] 范围内的标量 | 二元素向量
  group: Moist Air 2
- name: Initial moist air water vapor mole fraction
  summary: 仿真开始时水蒸气的摩尔分数 0.0266（默认）| [0,1] 范围内的标量 | 二元素向量
  group: Moist Air 2
- name: Initial moist air humidity ratio
  summary: 仿真开始时的湿度比 0.017（默认）| [0,1] 范围内的标量 | 二元素向量
  group: Moist Air 2
- name: Initial moist air wet-bulb temperature
  summary: 仿真开始时的湿球温度 25.56 degC（默认）| 正标量
  group: Moist Air 2
- name: Initial trace gas specification
  summary: 用于描述初始微量气体水平的量 Mass fraction（默认）| Mole fraction
  group: Moist Air 2
- name: Initial moist air trace gas mass fraction
  summary: 仿真开始时微量气体的质量分数 6e-4（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Initial moist air trace gas mole fraction
  summary: 仿真开始时微量气体的摩尔分数 4e-4（默认）| [0,1] 范围内的标量
  group: Moist Air 2
- name: Initial mass ratio of water droplets to moist air
  summary: 水滴与湿空气的质量比 0（默认）| 正标量
  group: Moist Air 2
- name: Relative humidity at saturation
  summary: 发生冷凝的相对湿度阈值 1（默认）| 正标量
  group: Moist Air 2
- name: Water vapor condensation time constant
  summary: 冷凝的时间尺度 1e-3 s（默认）| 正标量
  group: Moist Air 2
- name: Water droplets evaporation time constant
  summary: 蒸发的时间尺度 1e-3 s（默认）| 正标量
  group: Moist Air 2
- name: Fraction of condensate entrained as water droplets
  summary: 水滴中冷凝物的比例 1（默认）| [0,1] 范围内的标量
  group: Moist Air 2
```

### Thermal Liquid 1

### **Flow arrangement** — 湿空气和热液的流动布置 `Counter flow`（默认）| `Cross flow`

冷却塔内流动的布置方式。热液始终在冷却塔内向下流动。如果选择 `Counter flow`，湿空气向上穿过填料材料。如果选择 `Cross flow`，湿空气水平穿过填料材料。

### **Nominal capacity specification** — 指定系统尺寸的方法 `Water volumetric flow rate`（默认）| `Water mass flow rate` | `Rate of cooling in cooling tower` | `Rate of cooling in evaporator`

指定冷却塔尺寸的方法。可以指定进入塔的水的质量流量或体积流量，也可以指定与塔连接的制冷回路中蒸发器的冷却速率或冷却塔中的冷却速率。

### **Nominal water mass flow rate** — 额定工况下的质量流量 `42.7` `kg/s`（默认）| 正标量

额定运行工况下进入塔的热液质量流量。模块使用此值来确定冷却塔的尺寸。

#### 依赖

要启用此参数，请将 **Nominal capacity specification** 设置为 `Water mass flow rate`。

### **Nominal water volumetric flow rate** — 额定工况下的体积流量 `154` `m^3/hr`（默认）| 正标量

额定运行工况下进入塔的热液体积流量。模块使用此值来确定冷却塔的尺寸。

#### 依赖

要启用此参数，请将 **Nominal capacity specification** 设置为 `Water volumetric flow rate`。

### **Nominal cooling tower heat transfer** — 额定工况下的传热量 `1000` `kW`（默认）| 正标量

额定运行工况下塔内热液与湿空气之间的传热量。模块使用此值来确定冷却塔的尺寸。

#### 依赖

要启用此参数，请将 **Nominal capacity specification** 设置为 `Rate of cooling in cooling tower`。

### **Nominal evaporator heat transfer** — 额定工况下的蒸发器传热量 `800` `kW`（默认）| 正标量

额定运行工况下与冷却塔连接的制冷回路中蒸发器的传热量。模块使用此值来确定冷却塔的尺寸。模块假设冷却塔中热液与湿空气之间的传热量为此参数值的 1.25 倍。

#### 依赖

要启用此参数，请将 **Nominal capacity specification** 设置为 `Rate of cooling in evaporator`。

### **Nominal hot-water inlet temperature** — 热液入口温度 `35` `degC`（默认）| 正标量

额定运行工况下进入热交换器的热液温度。模块使用此值来确定冷却塔的尺寸。

### **Nominal cold-water outlet temperature** — 热液出口温度 `29.44` `degC`（默认）| 正标量

额定运行工况下冷却后流出热交换器的热液温度。模块使用此值来确定冷却塔的尺寸。

### **Model cold-water basin** — 将热液侧 1 建模为水箱的选项 `on`（默认）| `off`

选中此参数可将热液侧的冷水池建模为水箱。如果清除此参数，请将 Tank (TL) 模块连接到端口 **B1** 来建模冷水池。

### **Basin cross-sectional area** — 水池面积 `8` `m^2`（默认）| 正标量

塔中容纳冷却水的水池的横截面积。

#### 依赖

要启用此参数，请选中 **Model cold-water basin**。

### **Cross-sectional area at port A1** — 热液入口流通面积 `0.01` `m^2`（默认）| 正标量

热液入口的流通面积。

### **Cross-sectional area at port B1** — 热液出口流通面积 `0.01` `m^2`（默认）| 正标量

热液出口的流通面积。

### **Drift rate as fraction of water flow** — 热液漂移率 `0`（默认）| 正标量

因漂移而损失的热液流量占比。漂移是指从冷却塔吹出而未蒸发的液滴。

### **Automatically replenish lost water** — 在热液侧 1 自动补充损失水的选项 `on`（默认）| `off`

选中此参数可使模块自动补充因蒸发或漂移而损失的水。如果清除此参数，模块将启用物理信号端口 **Vm** 和 **Tm**，供您指定补充水池的水的体积流量和温度。

#### 依赖

要启用此参数，请选中 **Model cold-water basin**。

### **Temperature of make-up water** — 补充水温度 `15` `degC`（默认）| 正标量

模块用于自动补充因蒸发和漂移从热液侧损失的水的水温。

#### 依赖

要启用此参数，请选中 **Model cold-water basin** 和 **Automatically replenish lost water**。

### **Initialize thermal liquid to nominal operating conditions** — 初始化热液的选项 `on`（默认）| `off`

将热液初始化为额定运行工况或指定值的选项。如果选中此参数，模块将热液初始化为额定运行工况。如果清除此参数，可以使用附加参数直接指定初始条件。

#### 依赖

要启用此参数，请选中 **Model cold-water basin**。

### **Initial basin liquid temperature** — 仿真开始时的水池温度 `29.44` `degC`（默认）| 正标量

仿真开始时冷水池中的热液温度。

#### 依赖

要启用此参数，请选中 **Model cold-water basin** 并清除 **Initialize thermal liquid to nominal operating conditions** 复选框。

### **Initial basin liquid level** — 仿真开始时的水池液位 `0.2` `m`（默认）| 正标量

仿真开始时冷水池的热液深度。

#### 依赖

要启用此参数，请选中 **Model cold-water basin**。

### **Gravitational acceleration** — 重力加速度常数 `9.81` `m/s^2`（默认）| 正标量

重力加速度常数。

#### 依赖

要启用此参数，请选中 **Model cold-water basin**。

### Moist Air 2

### **Moist air operating conditions** — 指定湿空气工况的方法 `Provided by input signals`（默认）| `Moist air domain ports`

模块在仿真期间用于指定湿空气工况的方法。如果选择 `Provided by input signals`，模块将启用物理信号端口，可用于指定湿空气的温度、压力和流量。如果选择 `Moist air domain ports`，模块将启用湿空气端口 **A2** 和 **B2**，您可以将模块连接到湿空气网络。

### **Flow rate input signal specification** — 指定实际湿空气流量的方法 `Volumetric flow rate`（默认）| `Mass flow rate` | `Fan power`

指定实际湿空气流量的方法。当 **Moist air operating conditions** 为 `Provided by input signals` 时，模块使用此参数指定的流量以及温度和压力来描述湿空气运行工况。

- 如果选择 `Mass flow rate`，模块将启用端口 **M**。
- 如果选择 `Volumetric flow rate`，模块将启用端口 **V**。
- 如果选择 `Fan power`，模块将启用端口 **Pwr**。

#### 依赖

要启用此参数，请将 **Moist air operating conditions** 设置为 `Provided by input signals`。

### **Output fan power** — 输出风机功率的选项 `off`（默认）| `on`

选中此参数可将流动所需的计算风机功率作为物理信号在端口 **Pwr** 输出。

#### 依赖

要启用此参数，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，并将 **Flow rate input signal specification** 设置为 `Mass flow rate` 或 `Volumetric flow rate`。

### **Nominal fan power** — 额定运行工况下的风机功率 `7.5` `kW`（默认）| 正标量

额定运行工况下的风机功率。数据手册通常提供此值。

#### 依赖

要启用此参数，请将 **Moist air operating conditions** 设置为 `Provided by input signals`，并且：

- 将 **Flow rate input signal specification** 设置为 `Fan power`。
- 将 **Flow rate input signal specification** 设置为 `Mass flow rate` 或 `Volumetric flow rate` 并选中 **Output fan power**。

### **Humidity input signal specification** — 用于描述塔湿空气入口实际湿度水平的物理量 `Wet-bulb temperature`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Relative humidity`

用于指定进入冷却塔的湿空气实际湿度水平的物理量。如果选择 `Relative humidity`、`Specific humidity`、`Mole fraction` 或 `Humidity ratio`，湿度水平为端口 **W** 处的信号。如果选择 `Wet-bulb temperature`，湿度水平为端口 **Tw** 处的信号。

#### 依赖

要启用此参数，请将 **Moist air operating conditions** 设置为 `Provided by input signals`。

### **Input signals outside valid range** — 处理无效信号值的方法 `Warn and limit to valid values`（默认）| `Limit to valid values` | `Error`

选择当表示湿空气属性的物理输入信号超出有效范围时模块的行为：

- `Limit to valid values` — 模块将信号限制为有效值，不发出警告。
- `Warn and limit to valid values` — 模块将信号限制为有效值并发出警告。
- `Error` — 模块发出错误，仿真结束。

#### 依赖

要启用此参数，请将 **Moist air operating conditions** 设置为 `Provided by input signals`。

### **Specify full moist air nominal condition** — 指定湿空气额定工况的选项 `off`（默认）| `on`

选中此参数可提供额定入口压力、额定入口温度、额定入口湿度水平和额定入口痕量气体水平。

如果清除此参数，只需指定额定入口湿球温度，模块将计算或假设其他额定工况。如果制造商数据手册仅提供额定湿球温度，请使用此选项。

### **Nominal flow rate specification** — 指定湿空气流量的选项 `Volumetric flow rate`（默认）| `Mass flow rate`

将额定工况下的湿空气流量指定为质量流量还是体积流量。

#### 依赖

要启用此参数，请选中 **Specify full moist air nominal condition**。

### **Nominal moist air mass flow rate** — 额定质量流量 `36` `kg/s`（默认）| 正标量

额定运行工况下的湿空气质量流量。

#### 依赖

要启用此参数，请选中 **Specify full moist air nominal condition** 并将 **Nominal flow rate specification** 设置为 `Mass flow rate`。

### **Nominal moist air volumetric flow rate** — 额定体积流量 `30` `m^3/s`（默认）| 正标量

额定运行工况下的湿空气体积流量。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**，并将 **Nominal flow rate specification** 设置为 `Volumetric flow rate`。

### **Nominal moist air pressure loss** — 额定工况下湿空气端口之间的压降 `250` `Pa`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的压降。

如果冷却塔数据表中不包含此值，您可以根据额定风扇功率 *Φfannom* 进行估算。额定压力损失为

ΔpMAnom=ΦfannomηfanqMAnom，

其中 *qMAnom* 是 **Nominal moist air volumetric flow rate** 参数的值，*ηfan* 是风扇效率，您可以对其进行估算。合理值约为 `0.3`。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，并选择 **Specify full moist air nominal condition**。

### **Nominal inlet pressure** — 湿空气侧入口处的压力 `0.101325` `MPa`（默认）| 正标量

额定工况下冷却塔湿空气侧入口处的压力。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**。

### **Nominal inlet temperature** — 湿空气侧入口处的温度 `34.28` `degC`（默认）| 正标量

额定工况下冷却塔湿空气侧入口处的温度。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**。

### **Nominal humidity specification** — 用于描述额定工况下湿度水平的量 `Wet-bulb temperature`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Relative humidity`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述额定工况下的湿空气湿度水平。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**。

### **Nominal inlet relative humidity** — 入口处的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

额定工况下冷却塔湿空气侧入口处的相对湿度。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**，并将 **Nominal humidity specification** 设置为 `Relative humidity`。

### **Nominal inlet specific humidity** — 入口处的比湿度 `0.0167`（默认）| [0,1] 范围内的标量

比湿度，定义为湿空气混合物中水蒸气的质量分数，在额定工况下冷却塔湿空气侧入口处的值。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**，并将 **Nominal humidity specification** 设置为 `Specific humidity`。

### **Nominal inlet water vapor mole fraction** — 入口处水蒸气的摩尔分数 `0.0266`（默认）| [0,1] 范围内的标量

额定工况下冷却塔湿空气侧入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**，并将 **Nominal humidity specification** 设置为 `Mole fraction`。

### **Nominal inlet humidity ratio** — 入口处的湿度比 `0.017`（默认）| [0,1] 范围内的标量

湿度比，定义为水蒸气与干空气和微量气体的质量比，在额定工况下冷却塔湿空气侧入口处的值。

#### 依赖关系

要启用此参数，请选择 **Specify full moist air nominal condition**，并将 **Nominal humidity specification** 设置为 `Humidity ratio`。

### **Nominal inlet wet-bulb temperature** — 湿空气入口处的湿球温度 `25.56` `degC`（默认）| 正标量

额定工况下湿空气入口处的湿球温度。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 清除 **Specify full moist air nominal condition** 复选框。
- 选择 **Specify full moist air nominal condition**，并将 **Nominal humidity specification** 设置为 `Wet-bulb temperature`。

### **Nominal trace gas specification** — 用于描述额定微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

模块用于描述额定工况下微量气体水平的量。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，并选择 **Specify full moist air nominal condition**。

### **Nominal inlet trace gas mass fraction** — 入口处微量气体的质量分数 `6e-4`（默认）| [0,1] 范围内的标量

额定工况下冷却塔湿空气侧入口处湿空气混合物中微量气体的质量分数。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，选择 **Specify full moist air nominal condition**，并将 **Nominal trace gas specification** 设置为 `Mass fraction`。

### **Nominal inlet trace gas mole fraction** — 入口处微量气体的摩尔分数 `4e-4`（默认）| [0,1] 范围内的标量

额定工况下冷却塔湿空气侧入口处湿空气混合物中微量气体的摩尔分数。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，选择 **Specify full moist air nominal condition**，并将 **Nominal trace gas specification** 设置为 `Mole fraction`。

### **Moist air volume** — 冷却塔中湿空气的总体积 `24` `m^3`（默认）| 正标量

冷却塔中湿空气的总体积。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`。

### **Cross-sectional area at port A2** — 湿空气入口或出口的面积 `4` `m^2`（默认）| 正标量

湿空气入口或出口的流通面积。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`。

### **Cross-sectional area at port B2** — 湿空气入口或出口的面积 `4` `m^2`（默认）| 正标量

湿空气入口或出口的流通面积。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`。

### **Initialize moist air to nominal operating conditions** — 初始化湿空气的选项 `on`（默认）| `off`

选择此参数可将湿空气初始化为额定工况。如果清除此参数，则可以直接指定初始条件。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`。

### **Initial moist air pressure** — 仿真开始时的湿空气压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时湿空气的压力。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，并清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial moist air temperature** — 仿真开始时的湿空气温度 `34.28` `degC`（默认）| 标量 | 二元素向量

仿真开始时湿空气的温度。如果该值为标量，则初始温度均匀。如果该值为二元素向量，则初始温度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，并清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial humidity specification** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述初始湿空气湿度水平。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，并清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial moist air relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气的相对湿度。如果该值为标量，则初始相对湿度均匀。如果该值为二元素向量，则初始相对湿度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial moist air specific humidity** — 仿真开始时的比湿度 `0.0167`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气的比湿度，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则初始比湿度均匀。如果该值为二元素向量，则初始比湿度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial moist air water vapor mole fraction** — 仿真开始时水蒸气的摩尔分数 `0.0266`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气混合物中水蒸气的摩尔分数。如果该值为标量，则初始摩尔分数均匀。如果该值为二元素向量，则初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial moist air humidity ratio** — 仿真开始时的湿度比 `0.017`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气的湿度比，定义为水蒸气与干空气和微量气体的质量比。如果该值为标量，则初始湿度比均匀。如果该值为二元素向量，则初始湿度比在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial moist air wet-bulb temperature** — 仿真开始时的湿球温度 `25.56` `degC`（默认）| 正标量

仿真开始时湿空气混合物的湿球温度。如果该值为标量，则初始摩尔分数均匀。如果该值为二元素向量，则初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 用于描述初始微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数来描述仿真开始时的微量气体水平。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，并清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial moist air trace gas mass fraction** — 仿真开始时微量气体的质量分数 `6e-4`（默认）| [0,1] 范围内的标量

仿真开始时湿空气混合物中微量气体的质量分数。如果该值为标量，则初始质量分数均匀。如果该值为二元素向量，则初始质量分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial moist air trace gas mole fraction** — 仿真开始时微量气体的摩尔分数 `4e-4`（默认）| [0,1] 范围内的标量

仿真开始时湿空气混合物中微量气体的摩尔分数。如果该值为标量，则初始摩尔分数均匀。如果该值为二元素向量，则初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气的质量比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`，并清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Relative humidity at saturation** — 发生冷凝的相对湿度阈值 `1`（默认）| 正标量

塔内发生冷凝的相对湿度阈值。

### **Water vapor condensation time constant** — 冷凝的时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分恢复到饱和状态的特征时间尺度。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`。

### **Water droplets evaporation time constant** — 蒸发的时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的比例 `1`（默认）| [0,1] 范围内的标量

湿空气中以水滴形式夹带的冷凝物比例。

#### 依赖关系

要启用此参数，请将 **Moist air operating conditions** 设置为 `Moist air domain ports`。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Moist Air

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2024b：模拟悬浮在湿空气流中的水滴

湿空气域中的模块现在可以模拟悬浮在湿空气流中的水滴。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

热液体与湿空气网络之间的冷却塔

Cooling Tower (TL-MA) 模块模拟湿空气与热液体网络之间的冷却塔。该模块基于热质传递的等效效能-NTU 方法，对从热液体侧到湿空气侧的显热传递和潜热传递进行建模。热液体侧代表塔中的水，而湿空气侧代表环境空气。该模块基于性能而非基于几何结构，这意味着模块根据您指定的额定工况来确定冷却塔的尺寸。

### 冷却塔几何结构

大型 HVAC 系统使用冷却塔将水中的热量排放到环境中，适用于热量过大而常规水-空气换热器不实用的应用场景。在冷却塔中，热水和空气直接接触，这使得部分水蒸发到空气中，并通过蒸发冷却效应冷却剩余的水。

冷却塔的工作原理是将热水从塔顶散布和喷洒到大面积区域，以促使其蒸发到空气中。通常，在喷嘴下方有具有大表面积的填料，使水能够形成薄膜并铺展开来。填料增加了水与空气之间的接触面积，从而实现更多蒸发。由于没有热源，将液态水转化为水蒸气所需的潜热来自水本身。因此，未蒸发的水被冷却。冷水聚集在冷却塔底部的集水池中，可以返回 HVAC 系统。

您可以使用 **Flow arrangement** 参数指定冷却塔采用横流还是逆流。该模块仅对直流式冷却塔进行建模，这意味着水与空气直接接触。该模块也仅对机械通风冷却塔进行建模，即由风扇驱动空气通过冷却塔。

下图展示了逆流、直接接触、诱导式机械通风冷却塔的示意图。

逆流直接接触、诱导式机械通风冷却塔示意图

下图展示了具有两个空气入口的直接接触、诱导式机械通风冷却塔的示意图。

双空气入口横流直接接触、诱导式机械通风冷却塔

### 传热与蒸发速率

组合的热量与水蒸气质量传递为

Qcombined=ϵQcombined,max=ϵCmin(h¯sTLin−h¯MAin),

其中：

- *Qcombined,max* 是理论上的最大组合热量与水蒸气质量传递，Qcombined,max=Cmin(h¯sTLin−h¯MAin)。
- h¯*sTLin* 是在热液体侧入口温度下评估的饱和湿空气焓值。
- h¯*MAin* 是入口处湿空气的混合物焓值。
- *Cmin* 是湿空气与热液体之间较小的热容率。

当 **Flow arrangement** 为 `Counter flow` 时，效能因子 *ε* 为

ϵ=1−exp[−(1−CR)NTU]1−CRexp[−(1−CR)NTU],

其中 *CR* 是热容比，*NTU* 是传热单元数。

当 **Flow arrangement** 为 `Cross flow` 时，模块假设一种流体为混合的，另一种为非混合的。如果 *C* 值较低的流体为非混合的，

ϵ=1−exp(−CR[1−exp(−NTU)])CR.

通常，湿空气具有较低的 *C* 值。如果 *C* 值较低的流体为混合的，

ϵ=1−exp[−1−exp(−CR∗NTU)CR].

热容比为

CR=CminCmax=min{CTL,CMA}max{CTL,CMA}.

*CMA* 和 *CTL* 分别是湿空气和热液体的热容率，

CTL=m˙TLcpTLc¯sTLCMA=m˙agMA

其中：

- *ṁTL* 是热液体质量流量。
- *cpTL* 是热液体定压比热。
- *ṁagMA* 是干空气和微量气体的质量流量。

传热单元数 *NTU* 为

NTU=UMAACminc¯pMA,

其中：

- *A* 是传热表面积。
- *UMA* 是湿空气侧的传热导率。
- c¯*pMA* 是湿空气定压比热。

组合的热量与水蒸气质量传递 *Qcombined* 考虑了显热传递、潜热以及由于液体损失导致的能量支出，

Qcombined=Q+Δhfgeffm˙e+hleffm˙e,

其中：

- *Q* 是冷却塔中热液体与湿空气之间的显热传递。模块通过 Q=Qcombined−hweffm˙e 计算该值。该项表示由于热液体与湿空气之间的温差而产生的冷却部分。
- *Δhfgeff* 是水蒸气的比汽化焓。当乘以 *ṁe* 时，该项给出冷却塔中热液体与湿空气之间的潜热传递。该项表示由于液态水转化为水蒸气时提取的能量而产生的冷却部分。
- *hleff* 是液态水的比焓。当乘以 *ṁe* 时，该项给出由于部分液体被移除而从热液体流动的能量平衡中扣除的能量。

冷却塔中的蒸发速率为

m˙e=Cmin(Wseff−WMAin)[1−exp(−NTU)],

其中：

- *Wseff* 是有效饱和湿度比。
- *WMAin* 是湿空气入口处的湿度比。

有效饱和湿度比为

Wseff=Ra+G(Rg−Ra)Rw(pφwspws(Teff)−1),

其中：

- *Ra* 是干空气的比气体常数。
- *G* 是微量气体比。
- *Rg* 是微量气体的比气体常数。
- *RW* 是水蒸气的比气体常数。
- *p* 是压力。
- *φws* 是 **Relative humidity at saturation** 参数的值。
- *pws(Teff)* 是在有效液膜表面温度下评估的水蒸气饱和压力。

有效液膜表面温度为

Teff=TTLin−h¯sTLin−h¯seffc¯sTL,

其中：

- *TTLin* 是入口处热液体的温度。
- c¯*sTL* 是在热液体温度下沿饱和曲线评估的饱和湿空气比热。
- h¯*seff* 是沿液膜表面的饱和混合物焓

  h¯seff=h¯MAin+ϵ(h¯sTLin−h¯MAin)1−exp(−NTU).

湿空气侧的传热导率 *UMAA* 为

UMAA=max{(m˙MAμMA)bPrMAck(DrefSref)ba,NulamkMA}Gfill,

其中：

- *UMA* 是传热系数。
- *ṁMA* 是湿空气质量流量。
- *μMA* 是湿空气动力粘度。
- *a* 是 Nusselt 数关联式中比例项的系数。
- *b* 是 Nusselt 数关联式中 Reynolds 数指数的系数。
- *c* 是 Nusselt 数关联式中 Prandtl 数指数的系数。
- *PrMA* 是湿空气 Prandtl 数。
- *kMA* 是湿空气的导热系数。
- *Dref* 是任意直径。模块使用该值与 *Sref* 一起进行长度无量纲化。
- *Sref* 是对应于 *Dref* 的流通面积。
- *Nulam* 为 3.66，即圆管内层流流动的理论 Nusselt 数。
- *Gfill* 是冷却塔填料的几何比例因子。模块在额定工况下计算该值。

### 冷却塔选型

模块根据额定工况下的额定性能来确定冷却塔的尺寸。在热液体侧，**Nominal capacity specification** 参数指定模块如何确定额定数据：

- `Water mass flow rate` 或 `Water volumetric flow rate` — 模块根据额定流量以及额定入口和出口温度推断额定容量。
- `Rate of cooling in cooling tower` 或 `Rate of cooling in evaporator` — 模块根据额定容量推断额定流量。

在湿空气侧，额定数据取决于 **Specify full moist air nominal conditions** 参数。

如果清除 **Specify full moist air nominal conditions** 复选框，您指定的唯一额定工况是 **Nominal inlet wet-bulb temperature** 参数的值。如果您的制造商数据表仅提供额定湿球温度，请使用此选项。模块计算其他额定工况：

- 模块根据 **Nominal inlet wet-bulb temperature** 参数的值计算额定入口温度，使相对湿度为 50%。
- 模块根据额定水流量计算额定流量，使额定工况下的热容比为 `1`。

模块假设额定入口压力为大气压，且没有额定微量气体。

如果选择 **Specify full moist air nominal conditions**，则必须指定额定入口压力、额定入口温度、额定入口湿度水平和额定入口微量气体水平。

模块使用额定工况求解冷却塔填料的几何比例因子 *Gfill*。该值描述冷却塔的尺寸。模块对湿空气侧的传热导率 *UMAA* 的表达式求逆，并根据额定工况下的传热导率计算 *Gfill*。然后模块在仿真期间使用 *Gfill* 计算实际工况下湿空气侧的传热导率。模块不对热液膜中的对流传热进行建模。

额定工况下的 *Gfill* 为

Gfill=(UMAA)nom(m˙MAnomμMAnom)bPrMAnomckMAnom(DrefSref)ba,

其中下标 *nom* 表示在指定额定工况下的变量值。

模块通过以下公式求解 *(UMAA)nom*

(UMAA)nom=Cminnomc¯pMA,nomNTUnom.

模块通过反演适用的效能方程来计算 *NTUnom*。

当 **Flow arrangement** 为 `Counter flow` 时，

NTUnom=11−CRnomln(1−ϵnomCRnom1−ϵnom),

其中 *CRnom* 是热容比，ϵnom=QcombinednomQcombined,maxnom，其中 *Qcombined*、*Qcombined,max* 和 *CRnom* 在额定工况下评估。

当 **Flow arrangement** 为 `Cross flow` 且 *C* 值较低的流体为混合的

NTUnom=−ln[1+CRnomln(1−ϵnom)]CRnom.

如果 *C* 值较低的流体为非混合的，

NTUnom=−ln[1+ln(1−ϵnomCRnom)CRnom].

### 热液体方程

热液体在端口 **A1** 进入冷却塔时的压力为

pTLA1=pMA,

其中 *pMA* 是冷却塔内部的湿空气压力。由于模块假设蒸发导致的水损失很小，热液体质量流量等于端口 **A1** 的流入速率，m˙TL=m˙TLA1。

热液体的稳态质量平衡方程为

m˙TLA1−m˙e−λm˙TLA1=m˙TLfill,out,

其中：

- *λ* 是 **Drift rate as fraction of water flow** 参数的值。漂移考虑了从冷却塔吹出而未蒸发的液滴。
- *ṁTLfill,out* 是填料出口点处热液体的质量流量。

热液体的稳态能量平衡方程为

ΦTLA1−Qcombined−λΦTLA1=ΦTLfill,out,

其中：

- *ΦTLA1* 是端口 **A1** 处的能量流率。
- *ΦTLfill,out* 是流出填料的能量流率。

如果选择 **Model cold-water basin**，模块对内部水箱进行建模，水箱出口位于水箱底部。由于水箱中的水必须补充，热液体质量和能量守恒方程有两个额外的源项 *ṁTLmakeup* 和 *ΦTLmakeup*。

当选择 **Automatically replenish lost water** 时，

m˙TLmakeup=m˙e+λm˙TLA1ΦTLmakeup=m˙TLmakeuphTLmakeup

其中 *hTLmakeup* 是由 **Temperature of make-up water** 参数指定的热液体比焓。

如果清除 **Automatically replenish lost water** 复选框，您可以通过端口 **Vm** 和 **Tm** 分别指定水箱补充水的体积流量和温度。端口 **L** 输出集水池中的液位。补充水项为

m˙TLmakeup=ρTL(pMA,Tmu)VmuΦTLmakeup=m˙TLmakeuphTL(pMA,Tmu)

其中：

- *pMA* 是冷却塔中的湿空气压力。
- *Tmu* 是补充水的温度，即端口 **Tm** 处信号的值。
- *ρTL(pMA,Tmu)* 是在湿空气压力和补充水温度下评估的热液体密度。
- *hTL(pMA,Tmu)* 是在湿空气压力和补充水温度下评估的热液体比焓。

如果选择 **Model cold-water basin**，模块对内部水箱进行建模。*ṁTLfill,out* 和 *ΦTLA1* 定义内部水箱的输入流量。端口 **B1** 是内部水箱的出口。

如果清除 **Model cold-water basin** 复选框，

m˙TLB1=−m˙TLfill,outΦTLB1=−ΦTLfill,out

端口 **B1** 充当任何下游组件的流量源。将 Tank (TL) 模块连接到端口 **B1** 以对冷水池进行建模。Tank (TL) 模块的 **Inlet height** 参数必须大于水箱中的液位。

### 湿空气方程

模块湿空气侧的行为取决于 **Moist air operating conditions** 参数。

**物理信号**

当您将 **Moist air operating conditions** 设置为 `Provided by input signals` 时，模块会启用物理信号端口，您可以使用这些端口来指定湿空气属性：

- 端口 **P** 是湿空气入口压力的输入信号。湿空气压力 *pMA* 等于该信号的值。
- 端口 **T** 是湿空气干球温度的输入信号。
- 流量输入端口取决于 **Flow rate input signal specification** 参数：

  | **Flow rate input signal specification** 的值 | 启用的端口 | 端口含义 |
  | --- | --- | --- |
  | `Mass flow rate` | **M** | 湿空气混合物质量流量 |
  | `Volumetric flow rate` | **V** | 湿空气混合物体积流量 |
  | `Fan power` | **Pwr** | 湿空气风机功率 |
- 湿度水平输入端口取决于 **Humidity input signal specification** 参数：

  | **Humidity input signal specification** 的值 | 启用的端口 | 端口含义 |
  | --- | --- | --- |
  | `Relative humidity` | **W** | 湿空气入口相对湿度 |
  | `Specific humidity` | **W** | 湿空气入口比湿度 |
  | `Mole fraction` | **W** | 湿空气入口水蒸气摩尔分数 |
  | `Humidity ratio` | **W** | 湿空气入口湿度比 |
  | `Wet-bulb temperature` | **Tw** | 湿空气入口湿球温度 |

  当 **Flow rate input signal specification** 为 `Mass flow rate` 或 `Volumetric flow rate` 时，模块使用端口 **M** 或 **V** 处的信号来计算进入冷却塔的湿空气混合物质量流量 *ṁMAin*。干空气和微量气体流量为

  m˙agMA=m˙MAin1+WMAin。

  模块根据端口 **P**、**T** 以及 **W** 或 **Tw** 处的输入信号计算湿度比 *WMAin*。

  当 **Flow rate input signal specification** 为 `Fan power` 时，风机功率 *Φfan* 与体积流量 *q* 的立方以及风机两端压力增益 *Δp* 成正比。

  湿空气混合物体积流量为

  qMA=(PwrΦfannom)1/3qMAnom，

  其中：
- *Pwr* 是端口 **Pwr** 处信号的值。
- *Φfannom* 是 **Nominal fan power** 参数的值。
- *qMAnom* 是标称体积流量。如果您选择 **Specify full moist air nominal condition**，则 *qMAnom* 是 **Nominal moist air volumetric flow rate** 参数的值。如果您清除 **Specify full moist air nominal condition**，则模块根据标称水流量计算 *qMAnom*，使容量比为 1。

当 **Moist air operating conditions** 为 `Provided by input signals` 时，模块不对微量气体建模。

**湿空气域端口**

当您将 **Moist air operating conditions** 设置为 `Moist air domain ports` 时，模块会启用湿空气端口 **A2** 和 **B2**，您可以将它们连接到湿空气网络。由于在此模块中湿空气流的方向无关紧要，端口 **A2** 或 **B2** 都可以是入口。干空气和微量气体流量为

m˙agMA=m˙MAin1+WMAin，

其中：

- *ṁMAin* 是端口 **A2** 或 **B2** 处的湿空气混合物质量流量。
- *WMAin* 是端口 **A2** 或 **B2** 处的湿空气混合物湿度比。

湿空气混合物质量守恒方程为

dMMAdt=m˙MAA2+m˙MAB2+m˙e，

其中：

- *ṁMAA2* 和 *ṁMAB2* 是端口 **A2** 和 **B2** 处的质量流量。
- *MMA* 是湿空气体积的总混合物质量。

水蒸气质量守恒方程为

MMAdxwMAdt+xwMA(m˙MAA2+m˙MAB2+m˙e)=m˙wMAA2+m˙wMAB2+m˙e，

其中 *xwMA* 是湿空气体积的比湿度，*ṁwMAA2* 和 *ṁwMAB2* 是端口 **A2** 和 **B2** 处的水蒸气质量流量。

微量气体质量守恒方程为

MMAdxgMAdt+xgMA(m˙MAA2+m˙MAB2+m˙e)=m˙gMAA2+m˙gMAB2，

其中 *xgMA* 是湿空气体积的微量气体质量分数，*ṁgMAA2* 和 *ṁgMAB2* 是端口 **A2** 和 **B2** 处的微量气体质量流量。

水滴质量守恒方程为

MMAdrdMAdt+rdMA(m˙MAA2+m˙MAB2+m˙e)=m˙dMAA2+m˙dMAB2，

其中：

- *rdMA* 是水滴与湿空气的质量比。
- *ṁdMAA2* 和 *ṁdMAB2* 是端口 **A2** 和 **B2** 处的水滴质量流量。

湿空气混合物能量守恒方程为

MMAduMAdt+uMA(m˙MAA2+m˙MAB2+m˙e)=ΦMAA2+ΦMAB2+Qcombined，

其中 *uMA* 是湿空气体积的混合物比内能，*ΦMAA2* 和 *ΦMAB2* 是端口 **A2** 和 **B2** 处的湿空气混合物能量流量。

冷却塔中湿空气的压力损失为

ΔpMA=(qMAqMAnom)2ΔpMAnom，

其中：

- *ΔpMAnom* 是 **Nominal moist air pressure loss** 参数的值。
- *qMAnom* 是 **Nominal moist air volumetric flow rate** 参数的值。
- *qMA* 是通过冷却塔的湿空气体积流量。

### 在模型中使用冷却塔

使用 Cooling Tower (TL-MA) 时，请遵循以下准则：

- 如果您清除 **Model cold-water basin** 复选框，则必须将冷却塔端口 **B1** 连接到 Tank (TL) 模块。
- 在对启动或停机等瞬态情况进行建模时，将冷却塔端口 **A1** 连接到 Partially Filled Pipe (TL) 模块的端口 **A**，以避免液体从端口 **A1** 流出的可能非物理情况。在启动和停机期间，端口 **A1** 可能暴露于环境中，这意味着不存在液体。部分填充管道通过允许液位沿管道下降来处理此场景，必要时端口 **A1** 会暴露。
- 一些冷却塔可能使用压力源将水从喷嘴中压出，并将水散布到更广的区域，这会导致入口处出现压降。要对通过喷嘴的压降建模，请将用于对压力损失建模的模块（例如 Orifice (TL)、Local Resistance (TL) 或 Flow Resistance (TL) 模块）连接到冷却塔的端口 **A1**。
- Cooling Tower (TL-MA) 模块对直接接触式冷却塔建模。要对间接接触式冷却塔建模，请将 Cooling Tower (TL-MA) 模块的热液体侧连接到 Heat Exchanger (TL-TL) 模块的一侧。在此配置中，换热器模块的另一侧表示流入和流出冷却塔的热液体，并且该模块对来自冷却塔内部盘管的热传递建模。
- 如果您将 **Moist air operating conditions** 设置为 `Moist air domain ports`，则可以对机械强制通风或诱导通风冷却塔建模。要对强制通风冷却塔建模，请将 Fan (MA) 模块连接到塔的湿空气入口侧。要对诱导通风冷却塔建模，请将 Fan (MA) 模块连接到湿空气出口侧。如果您将 **Moist air operating conditions** 设置为 `Provided by input signals`，则模块不区分强制通风和诱导通风冷却塔。

### 假设和限制

- 该模块仅对机械通风冷却塔建模，这意味着风机使湿空气通过塔。
- 该模块仅对直接接触式冷却塔建模，这意味着热液体与湿空气直接接触。
