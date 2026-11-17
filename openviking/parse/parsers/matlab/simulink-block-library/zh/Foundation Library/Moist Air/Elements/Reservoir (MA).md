---
type: simulink-block
title: 'Reservoir (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'reservoirma'
documentation_source_path: 'ref/reservoirma.html'
language: zh-CN
chinese_source: worker-translation
---

# Reservoir (MA)

## 端口

### 输入

### **P** — 储液器压力，Pa 物理信号

控制储液器压力的物理信号端口。

#### 依赖

要启用此端口，请选择 **Provide input signal for pressure**。

### **T** — 储液器温度，K 物理信号

控制储液器温度的物理信号端口。

#### 依赖

要启用此端口，请选择 **Provide input signal for temperature**。

### **W** — 储液器湿度，无量纲 物理信号

控制储液器湿度水平的物理信号端口。要选择控制信号所代表的量，请使用 **Reservoir humidity specification** 参数。

#### 依赖

要启用此端口，请选择 **Provide input signal for humidity** 并将 **Reservoir humidity specification** 参数设置为以下选项之一：

- `Relative humidity`
- `Specific humidity`
- `Mole fraction`
- `Humidity ratio`

### **Tw** — 储液器湿球温度，K 物理信号

控制储液器湿球温度的物理信号端口。

#### 依赖

要启用此端口，请选择 **Provide input signal for humidity** 并将 **Reservoir humidity specification** 参数设置为 `Wet-bulb temperature`。

### **G** — 储液器微量气体水平，无量纲 物理信号

控制储液器微量气体水平的物理信号端口。要选择控制信号所代表的量，请使用 **Reservoir trace gas specification** 参数。

#### 依赖

要启用此端口，请选择 **Provide input signal for trace gas**。

### **D** — 储液器水滴质量比，无量纲 物理信号

控制储液器中水滴与湿空气质量比的物理信号端口。

#### 依赖

要启用此端口，请选择 **Provide input signal for water droplets**。
### 守恒

### **A** — 储液器入口湿空气

与储液器入口相关联的湿空气守恒端口。

## 参数

### **Provide input signal for pressure** — 指定压力的方法 `off`（默认）| `on`

用于指定储液器中压力的方法。如果清除此复选框，模块将基于 **Reservoir pressure** 参数的值或大气压力对压力进行建模。如果选中此复选框，模块将基于端口 **P** 处的信号值对压力进行建模。

### **Reservoir pressure specification** — 储液器压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

储液器压力的指定方法：

- `Atmospheric pressure` — 使用连接到回路的 Moist Air Properties (MA) 模块所指定的大气压力。
- `Specified pressure` — 使用 **Reservoir pressure** 参数指定一个值。

#### 依赖

要启用此参数，请清除 **Provide input signal for pressure** 复选框。

### **Reservoir pressure** — 储液器中的压力 `0.101325 MPa`（默认）| 正标量

储液器中的压力。该压力在仿真期间保持恒定。

#### 依赖

要启用此参数，请清除 **Provide input signal for pressure** 复选框并将 **Reservoir pressure specification** 设置为 `Specified pressure`。

### **Provide input signal for temperature** — 指定储液器温度的方法 `off`（默认）| `on`

用于指定储液器中温度的方法。如果清除此复选框，模块将基于 **Reservoir temperature** 参数的值或大气温度对温度进行建模。如果选中此复选框，模块将基于端口 **T** 处的信号值对微量气体进行建模。

### **Reservoir temperature specification** — 储液器温度的指定方法 `Atmospheric temperature`（默认）| `Specified temperature`

储液器温度的指定方法：

- `Atmospheric temperature` — 使用连接到回路的大气属性（MA）模块所指定的大气温度。
- `Specified temperature` — 使用 **Reservoir temperature** 参数指定一个值。

### **Reservoir temperature** — 储液器中的温度 `293.15 K`（默认）| 正标量

储液器中的温度。该温度在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for temperature** 复选框，并将 **Reservoir temperature specification** 设置为 `Specified temperature`。

### **Provide input signal for humidity** — 指定湿度的方式 `off`（默认）| `on`

用于指定储液器中湿度的方式。如果清除此复选框，模块将基于 **Reservoir humidity specification** 参数的值来建模湿度。如果选中此复选框，模块将基于端口 **W** 或 **Tw** 处的信号值来建模痕量气体。

### **Reservoir humidity specification** — 储液器湿度的指定方法 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

储液器湿度的指定方法：

- `Relative humidity` ― 使用相对湿度指定湿度。
- `Specific humidity` ― 使用比湿指定湿度。
- `Mole fraction` ― 使用水蒸气摩尔分数指定湿度。
- `Humidity ratio` ― 使用湿度比指定湿度。
- `Wet-bulb temperature` ― 使用湿球温度指定湿度。

### **Reservoir relative humidity** — 储液器中的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

储液器中的相对湿度。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for humidity** 复选框，并将 **Reservoir humidity specification** 设置为 `Relative humidity`。

### **Reservoir specific humidity** — 储液器中的比湿 `0.01`（默认）| [0,1] 范围内的标量

储液器中的比湿。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for humidity** 复选框，并将 **Reservoir humidity specification** 设置为 `Specific humidity`。

### **Reservoir water vapor mole fraction** — 储液器中的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

储液器中的水蒸气摩尔分数。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for humidity** 复选框，并将 **Reservoir humidity specification** 设置为 `Mole fraction`。

### **Reservoir humidity ratio** — 储液器中的湿度比 `0.01`（默认）| [0,1] 范围内的标量

储液器中的湿度比。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for humidity** 复选框，并将 **Reservoir humidity specification** 设置为 `Humidity ratio`。

### **Reservoir wet-bulb temperature** — 储液器中的湿球温度 `287 K`（默认）| 正标量

储液器中的湿球温度。该值在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for humidity** 复选框，并将 **Reservoir humidity specification** 设置为 `Wet-bulb temperature`。

### **Provide input signal for trace gas** — 指定示踪气体的方法 `off`（默认）| `on`

用于指定储层中示踪气体的方法。如果清除此复选框，模块将基于**Reservoir trace gas mass fraction**或**Reservoir trace gas mole fraction**参数的值对示踪气体建模。如果选中此复选框，模块将基于端口**G**处信号的值对示踪气体建模。

### **Reservoir trace gas specification** — 示踪气体的指定方法 `Mass fraction`（默认）| `Mole fraction`

储层示踪气体的指定方法：

- `Mass fraction` ― 指定示踪气体质量分数。
- `Mole fraction` ― 指定示踪气体摩尔分数。

### **Reservoir trace gas mass fraction** — 储层中的示踪气体质量分数 `0.001`（默认）| [0,1] 范围内的标量

储层中的示踪气体质量分数。该值在仿真期间保持恒定。

#### 依赖

要启用此参数，请选中**Provide input signal for trace gas**并将**Reservoir trace gas specification**设置为`Mass fraction`。

### **Reservoir trace gas mole fraction** — 储层中的示踪气体摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

储层中的示踪气体摩尔分数。该值在仿真期间保持恒定。

#### 依赖

要启用此参数，请选中**Provide input signal for trace gas**并将**Reservoir trace gas specification**设置为`Mole fraction`。

### **Provide input signal for water droplets** — 指定水滴质量比的方法 `off`（默认）| `on`

用于指定储层中水滴质量比的方法。如果清除此复选框，模块将基于**Reservoir mass ration of water droplets to moist air**参数的值对水滴建模。如果选中此复选框，模块将基于端口**D**处信号的值对水滴建模。

### **Reservoir mass ration of water droplets to moist air** — 储层中的水滴质量比 `0`（默认）| 正标量

储层中水滴与湿空气的质量比。

#### 依赖

要启用此参数，请清除**Provide input signal for water droplets**复选框。

### **Relative humidity at saturation** — 发生冷凝时的相对湿度 `1`（默认）| 正标量

发生冷凝时的相对湿度。

### **Cross-sectional area at port A** — 储层入口处垂直于流路的面积 `0.01 m^2`（默认）| 正标量

储层入口的横截面积。

### **Inputs outside valid range** — 信号值超出有效范围时要执行的操作 `Warn and limit to valid values`（默认）| `Limit to valid values` | `Error`

当输入信号值超出有效范围时模块要执行的操作：

- `Limit to valid values` ― 模块将输入信号限制为最小或最大有效值，但不发出警告。
- `Warn and limit to valid values` ― 模块发出警告并将输入信号限制为最小或最大有效值。
- `Error` ― 仿真停止并报错。

#### 依赖

要启用此参数，请至少选中以下参数之一：

- **为压力提供输入信号**
- **为温度提供输入信号**
- **为湿度提供输入信号**
- **为微量气体提供输入信号**
- **为水滴提供输入信号**

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b: 对受控储液器建模

Controlled Reservoir (MA) 和 Reservoir (MA) 模块已合并为 Reservoir (MA) 模块。选中 **Provide input signal for pressure**、**Provide input signal for temperature**、**Provide input signal for humidity**、**Provide input signal for trace gas** 和 **Provide input signal for water droplets** 复选框，以通过输入信号控制储液器条件。否则，您可以使用模块参数控制储液器条件。

如果您在自定义复合组件中使用了 Controlled Reservoir (MA)，则必须更新复合组件代码：

- 旧语法：`source = foundation.moist_air.elements.controlled_reservoir;`
- 新语法：`source = foundation.moist_air.elements.reservoir;`

### R2024b: 对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选中 **Enable entrained water droplets**。

### R2023a: 使用湿球温度指定湿度

该模块现在提供了一个选项，可使用湿球温度指定湿度。湿球温度是一种测量湿度的方法，需要将湿布包裹在温度计上，以便测量包含蒸发导致能量损失在内的温度。传统干湿球湿度计以湿球温度的形式输出数据。

## 描述

恒压、恒温、恒定湿度和微量气体水平下湿空气网络的边界条件

Reservoir (MA) 模块设置湿空气网络中的边界条件。假设储液罐内湿空气的体积为无限大。因此，假设流动为准稳态。湿空气以储液罐的压力、温度、比湿度和微量气体质量分数离开储液罐。湿空气以储液罐的压力进入储液罐，但温度、比湿度和微量气体质量分数由上游湿空气网络决定。

您可以通过模块参数值或物理信号指定储液罐压力、温度、湿度量、微量气体量和液滴量。如果在 Moist Air Properties (MA) 模块中，**Trace gas model** 为 `None`，或 **Enable entrained water droplets** 复选框已清除，则模块分别忽略与微量气体或液滴相关的参数和物理信号。

您可以将湿度指定为以下之一：

- 相对湿度，*φ*w
- 比湿度，*x*w
- 水蒸气摩尔分数，*y*w
- 湿度比，*r*w
- 湿球温度，*T*w

您可以将微量气体指定为以下之一：

- 微量气体质量分数，*x*g
- 微量气体摩尔分数，*y*g

这些湿度和微量气体量之间的关系如下：

φw=ywppwsyw=xwRwRrw=xw1−xwyg=xgRgRxa+xw+xg=1R=xaRa+xwRw+xgRg

其中：

- *p* 是压力。
- *R* 是比气体常数。

下标 `a`、`w` 和 `g` 分别表示干空气、水蒸气和微量气体的属性。下标 `ws` 表示饱和状态下的水蒸气。

模块隐式计算湿球温度：

xw=(1−xg(T))(ha(Tw)−ha(T))+xg(hg(Tw)−hg(T))+xws(Tw)1−xws(Tw)Δhfg(Tw)(ha(Tw)−ha(T))(hw(Tw)−hw(T))+11−xws(Tw)Δhfg(Tw)

其中：

- *T* 是温度。
- *T*w 是湿球温度。
- *x*w(*T*) 是比湿度。
- *x*g(*T*) 是微量气体质量分数。
- *x*ws(*T*w) 是湿球温度下的饱和比湿度。
- *h*a(*T*) 是干空气的比焓。
- *h*a(*T*w) 是湿球温度下干空气的比焓。
- *h*g(*T*) 是微量气体的比焓。
- *h*g(*T*w) 是湿球温度下微量气体的比焓。
- *h*w(*T*) 是水蒸气的比焓。
- *h*w(*T*w) 是湿球温度下水蒸气的比焓。
- *Δh*fg(*T*w) 是湿球温度下水蒸气的比汽化焓。
