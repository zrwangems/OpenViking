---
type: simulink-block
title: 'Positive-Displacement Compressor (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Turbomachinery'
documentation_page: 'positivedisplacementcompressorma'
documentation_source_path: 'ref/positivedisplacementcompressorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Positive-Displacement Compressor (MA)

## 端口
```yaml
ports:
- name: A
  summary: 压缩机入口湿空气
  direction: conserving
- name: B
  summary: 压缩机出口湿空气
  direction: conserving
- name: C
  summary: 压缩机壳体机械旋转
  direction: conserving
- name: R
  summary: 压缩机轴机械旋转
  direction: conserving
```

### 守恒端口

### **A** — 压缩机入口湿空气

与压缩机入口关联的湿空气守恒端口。

### **B** — 压缩机出口湿空气

与压缩机出口关联的湿空气守恒端口。

### **C** — 压缩机壳体机械旋转

与压缩机壳体关联的机械旋转守恒端口。

### **R** — 压缩机轴机械旋转

与压缩机轴关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Displacement specification
  summary: 按体积或标称条件指定排量的选项 Volumetric displacement（默认）| Nominal mass flow rate and shaft speed
  group: 排量
- name: Displacement volume
  summary: 排量体积 130 cm^3/rev（默认）| 正标量
  group: 排量
- name: Nominal mass flow rate
  summary: 标称质量流量 0.01 kg/s（默认）| 正标量
  group: 排量
- name: Nominal shaft speed
  summary: 标称轴转速 1000 rpm（默认）| 正标量
  group: 排量
- name: Efficiency specification
  summary: 通过解析方法或使用表格参数化容积效率的选项 Analytical（默认）| Tabulated
  group: 效率
- name: Thermodynamic model
  summary: 热力学模型参数化选项 Polytropic（默认）| Isentropic
  group: 效率
- name: Polytropic exponent
  summary: 多变指数 1.2（默认）| 正标量
  group: 效率
- name: Isentropic efficiency
  summary: 等熵效率 0.65（默认）| 正标量
  group: 效率
- name: Isentropic efficiency table, eta_isen(pr,w)
  summary: 等熵效率表 [.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]（默认）|
    矩阵
  group: 效率
- name: Nominal volumetric efficiency
  summary: 标称容积效率 0.95（默认）| 正标量
  group: 效率
- name: Pressure ratio vector, pr
  summary: 压力比向量 [2, 4, 6, 8]（默认）| 向量
  group: 效率
- name: Shaft speed vector, w
  summary: 轴转速向量 [800, 1500, 2800, 3300, 4000] rpm（默认）| 向量
  group: 效率
- name: Volumetric efficiency table, eta_vol(pr,w)
  summary: 容积效率 [.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]（默认）|
    矩阵
  group: 效率
- name: Nominal pressure ratio
  summary: 标称压力比 5（默认）| 正标量
  group: 标称条件
- name: Nominal inlet pressure
  summary: 标称入口压力 0.101325 MPa（默认）| 正标量
  group: 标称条件
- name: Nominal inlet temperature
  summary: 标称入口温度 293.15 K（默认）| 正标量
  group: 标称条件
- name: Inlet humidity specification
  summary: 用于描述入口湿度水平的量 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: 标称条件
- name: Nominal inlet relative humidity
  summary: 入口相对湿度 0.5（默认）| [0,1] 范围内的标量
  group: 标称条件
- name: Nominal inlet specific humidity
  summary: 入口比湿度 0.01（默认）| [0,1] 范围内的标量
  group: 标称条件
- name: Nominal inlet water vapor mole fraction
  summary: 入口水蒸气摩尔分数 0.01（默认）| [0,1] 范围内的标量
  group: 标称条件
- name: Nominal inlet humidity ratio
  summary: 入口湿度比 0.01（默认）| [0,1] 范围内的标量
  group: 标称条件
- name: Nominal inlet wet-bulb temperature
  summary: 入口湿球温度 287 K（默认）| 正标量
  group: 标称条件
- name: Inlet trace gas specification
  summary: 用于描述入口微量气体水平的量 Mass fraction（默认）| Mole fraction
  group: 标称条件
- name: Nominal inlet trace gas mass fraction
  summary: 入口微量气体质量分数 0.001（默认）| [0,1] 范围内的标量
  group: 标称条件
- name: Nominal inlet trace gas mole fraction
  summary: 仿真开始时微量气体摩尔分数 0.001（默认）| [0,1] 范围内的标量
  group: 标称条件
- name: Nominal inlet mass ratio of water droplets to moist air
  summary: 水滴与湿空气之比 0（默认）| 正标量
  group: 标称条件
- name: Relative humidity at saturation
  summary: 发生冷凝的相对湿度阈值 1（默认）| 正标量
  group: 标称条件
- name: Mechanical efficiency
  summary: 压缩机机械效率 0.9（默认）| 正标量
  group: 参数
- name: Model water droplets evaporation
  summary: 模拟水滴蒸发的选项 off（默认）| on
  group: 参数
- name: Relative humidity at saturation
  summary: 发生冷凝的相对湿度阈值 1（默认）| 正标量
  group: 参数
- name: Inlet area at port A
  summary: 入口面积 0.01 m^2（默认）| 正标量
  group: 参数
- name: 端口 B 的出口面积
  summary: 出口面积 0.01 m^2（默认）| 正标量
  group: 参数
```

### 排量

### **Displacement specification** — 按体积或标称条件指定排量的选项 `Volumetric displacement`（默认）| `Nominal mass flow rate and shaft speed`

是否按每循环体积或标称条件值指定流体排量。

### **Displacement volume** — 排量体积 `130` `cm^3/rev`（默认）| 正标量

每循环排出的流体体积。该模块将一个循环定义为一个压缩冲程和一个膨胀冲程，它们在一个曲轴旋转期间发生。该体积是最大气缸体积与余隙体积之差（*Va* — *Vc*）。通常，排量体积是压缩机在一个轴旋转期间扫过的体积。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Volumetric displacement`。

### **Nominal mass flow rate** — 标称质量流量 `0.01` `kg/s`（默认）| 正标量

模块用于计算排量体积的标称质量流量。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`。

### **Nominal shaft speed** — 标称轴转速 `1000` `rpm`（默认）| 正标量

模块用于计算排量体积的标称轴转速。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`。

### 效率

下表显示了 **Thermodynamic model** 和 **Efficiency specification** 参数的选项如何影响相关效率参数的可用性。

| **Thermodynamic model** | | | |
| --- | --- | --- | --- |
| `Polytropic` | | `Isentropic` | |
| **Efficiency specification** | | **Efficiency specification** | |
| `Analytical` | `Tabulated` | `Analytical` | `Tabulated` |
| **Polytropic exponent** | **Polytropic exponent** | **Isentropic efficiency** | **Isentropic efficiency table, eta\_isen(pr,w)** |
| **Nominal volumetric efficiency** | **Pressure ratio vector, pr** | **Nominal volumetric efficiency** | **Pressure ratio vector, pr** |
| **Shaft speed vector, w** | **Shaft speed vector, w** |
| **Volumetric efficiency table, eta\_vol(pr,w)** | **Volumetric efficiency table, eta\_vol(pr,w)** |

### **Efficiency specification** — 通过解析方法或使用表格参数化容积效率的选项 `Analytical`（默认）| `Tabulated`

是否通过解析方程或表格数据参数化排量容积效率。

### **Thermodynamic model** — 热力学模型参数化选项 `Polytropic`（默认）| `Isentropic`

使用多变或等熵热力学模型。

### **Polytropic exponent** — 多变指数 `1.2`（默认）| 正标量

模块在实现多变压力-体积关系时使用的指数。

#### 依赖关系

要启用此参数，请将 **Thermodynamic model** 设置为 `Polytropic`。

### **Isentropic efficiency** — 等熵效率 `0.65`（默认）| 正标量

模块在实现解析等熵压力-体积关系时使用的恒定效率。

#### 依赖关系

要启用此参数，请将 **Thermodynamic model** 设置为 `Isentropic`，并将 **Efficiency specification** 设置为 `Analytical`。

### **Isentropic efficiency table, eta\_isen(pr,w)** — 等熵效率表 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]`（默认）| 矩阵

模块在实现表格化等熵压力-体积关系时使用的效率。

#### 依赖关系

要启用此参数，请将 **Thermodynamic model** 设置为 `Isentropic`，并将 **Efficiency specification** 设置为 `Tabulated`。

### **Nominal volumetric efficiency** — 标称容积效率 `0.95`（默认）| 正标量

用于计算余隙体积分数的标称容积效率。标称容积效率是压缩机在标称条件下运行时的容积效率。

#### 依赖关系

要启用此参数，请将 **Efficiency specification** 设置为 `Analytical`。

### **Pressure ratio vector, pr** — 压力比向量 `[2, 4, 6, 8]`（默认）| 向量

与压缩机容积效率对应的压力比向量。每个元素对应 **Volumetric efficiency table, eta\_vol(pr,w)** 参数的一行。此参数必须是大小为 `N` 的向量，其中 `N` 是 **Volumetric efficiency table, eta\_vol(pr,w)** 参数的长度。

#### 依赖关系

要启用此参数，请将 **Efficiency specification** 设置为 `Tabulated`。

### **Shaft speed vector, w** — 轴转速向量 `[800, 1500, 2800, 3300, 4000]` `rpm`（默认）| 向量

与压缩机容积效率对应的轴转速向量。每个元素对应 **Volumetric efficiency table, eta\_vol(pr,w)** 参数的一列。此参数必须是大小为 `M` 的向量，其中 `M` 是 **Volumetric efficiency table, eta\_vol(pr,w)** 参数的宽度。

#### 依赖关系

要启用此参数，请将 **Efficiency specification** 设置为 `Tabulated`。

### **Volumetric efficiency table, eta\_vol(pr,w)** — 容积效率 `[.95, .9, .85, .8, .75; .925, .875, .825, .775, .725; .875, .825, .775, .725, .675; .75, .7, .65, .6, .55]`（默认）| 矩阵

给定轴转速和压力比下的容积效率。此参数必须是大小为 `N` × `M` 的矩阵，其中 `N` 是 **Pressure ratio vector, pr** 参数的长度，`M` 是 **Shaft speed vector, w** 参数的长度。

#### 依赖关系

要启用此参数，请将 **Efficiency specification** 设置为 `Tabulated`。

### 标称条件

下表显示了 **Displacement specification**、**Thermodynamic model** 和 **Efficiency specification** 参数的选项如何影响相关标称条件参数的可用性。

下表显示了当您将 **Displacement specification** 参数设置为 `Volumetric displacement` 时的相关参数：

| 当 **Displacement specification** 参数为 `Volumetric displacement` 时 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Efficiency specification** | | | | | | | |
| `Analytical` | | | | `Tabulated` | | | |
| **Thermodynamic model** | | | | **Thermodynamic model** | | | |
| `Polytropic` | | `Isentropic` | | `Polytropic` | | `Isentropic` | |
| **Nominal pressure ratio** | | **Nominal pressure ratio** | |  | | **Nominal pressure ratio** | |
| **Nominal inlet pressure** | | **Nominal inlet pressure** | |
| **Nominal inlet temperature** | | **Nominal inlet temperature** | |
| Nominal inlet humidity, water droplet, and trace gas parameters | | Nominal inlet humidity, water droplet, and trace gas parameters | |

当您将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed` 时，**Nominal Conditions** 中的参数不依赖于 **Efficiency specification** 或 **Thermodynamic model** 参数。

### **Nominal pressure ratio** — 标称压力比 `5`（默认）| 正标量

模块用于计算余隙体积分数的标称压力比。

#### 依赖关系

要启用此参数，请选择除 **Displacement specification** 为 `Volumetric displacement`、**Thermodynamic model** 为 `Polytropic` 且 **Efficiency specification** 为 `Tabulated` 之外的任何参数化方式。

### **Nominal inlet pressure** — 标称入口压力 `0.101325` `MPa`（默认）| 正标量

模块用于计算排量体积的标称入口压力。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`，或将 **Displacement specification** 设置为 `Volumetric displacement` 并将 **Thermodynamic model** 设置为 `Isentropic`。

### **Nominal inlet temperature** — 标称入口温度 `293.15` `K`（默认）| 正标量

模块用于计算排量体积的标称入口温度。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`，或将 **Displacement specification** 设置为 `Volumetric displacement` 并将 **Thermodynamic model** 设置为 `Isentropic`。

### **Inlet humidity specification** — 用于描述入口湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、水蒸气摩尔分数或湿度比来描述入口湿空气湿度水平。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`，或将 **Displacement specification** 设置为 `Volumetric displacement` 并将 **Thermodynamic model** 设置为 `Isentropic`。

### **Nominal inlet relative humidity** — 入口相对湿度 `0.5`（默认）| [0,1] 范围内的标量

标称运行条件下入口处的湿空气相对湿度。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Displacement specification** 为 `Nominal mass flow rate and shaft speed`，且 **Inlet humidity specification** 为 `Relative humidity`。
- **Displacement specification** 为 `Volumetric displacement`，**Thermodynamic model** 为 `Isentropic`，且 **Inlet humidity specification** 为 `Relative humidity`。

### **Nominal inlet specific humidity** — 入口比湿度 `0.01`（默认）| [0,1] 范围内的标量

标称运行条件下入口处的湿空气比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Displacement specification** 为 `Nominal mass flow rate and shaft speed`，且 **Inlet humidity specification** 为 `Specific humidity`。
- **Displacement specification** 为 `Volumetric displacement`，**Thermodynamic model** 为 `Isentropic`，且 **Inlet humidity specification** 为 `Specific humidity`。

### **Nominal inlet water vapor mole fraction** — 入口水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

标称运行条件下入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Displacement specification** 为 `Nominal mass flow rate and shaft speed`，且 **Inlet humidity specification** 为 `Mole fraction`。
- **Displacement specification** 为 `Volumetric displacement`，**Thermodynamic model** 为 `Isentropic`，且 **Inlet humidity specification** 为 `Mole fraction`。

### **Nominal inlet humidity ratio** — 入口湿度比 `0.01`（默认）| [0,1] 范围内的标量

标称运行条件下入口处的湿空气湿度比，定义为水蒸气与干空气和微量气体的质量比。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Displacement specification** 为 `Nominal mass flow rate and shaft speed`，且 **Inlet humidity specification** 为 `Humidity ratio`。
- **Displacement specification** 为 `Volumetric displacement`，**Thermodynamic model** 为 `Isentropic`，且 **Inlet humidity specification** 为 `Humidity ratio`。

### **Nominal inlet wet-bulb temperature** — 入口湿球温度 `287` `K`（默认）| 正标量

标称运行条件下入口处湿空气混合物的湿球温度。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Displacement specification** 为 `Nominal mass flow rate and shaft speed`，且 **Inlet humidity specification** 为 `Wet-bulb temperature`。
- **Displacement specification** 为 `Volumetric displacement`，**Thermodynamic model** 为 `Isentropic`，且 **Inlet humidity specification** 为 `Wet-bulb temperature`。

### **Inlet trace gas specification** — 用于描述入口微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数来描述入口处的微量气体水平。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`，或将 **Displacement specification** 设置为 `Volumetric displacement` 并将 **Thermodynamic model** 设置为 `Isentropic`。

### **Nominal inlet trace gas mass fraction** — 入口微量气体质量分数 `0.001`（默认）| [0,1] 范围内的标量

标称运行条件下入口处湿空气混合物中微量气体的质量分数。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Displacement specification** 为 `Nominal mass flow rate and shaft speed`，且 **Inlet trace gas specification** 为 `Mass fraction`。
- **Displacement specification** 为 `Volumetric displacement`，**Thermodynamic model** 为 `Isentropic`，且 **Inlet trace gas specification** 为 `Mass fraction`。

### **Nominal inlet trace gas mole fraction** — 仿真开始时微量气体摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

标称运行条件下入口处湿空气混合物中微量气体的摩尔分数。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Displacement specification** 为 `Nominal mass flow rate and shaft speed`，且 **Inlet trace gas specification** 为 `Mole fraction`。
- **Displacement specification** 为 `Volumetric displacement`，**Thermodynamic model** 为 `Isentropic`，且 **Inlet trace gas specification** 为 `Mole fraction`。

### **Nominal inlet mass ratio of water droplets to moist air** — 水滴与湿空气之比 `0`（默认）| 正标量

标称运行条件下入口处水滴与湿空气的质量比。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`，或将 **Displacement specification** 设置为 `Volumetric displacement` 并将 **Thermodynamic model** 设置为 `Isentropic`。

### **Relative humidity at saturation** — 发生冷凝的相对湿度阈值 `1`（默认）| 正标量

压缩机中发生冷凝的相对湿度阈值。

#### 依赖关系

要启用此参数，请将 **Displacement specification** 设置为 `Nominal mass flow rate and shaft speed`，或将 **Displacement specification** 设置为 `Volumetric displacement` 并将 **Thermodynamic model** 设置为 `Isentropic`。

### 参数

### **Mechanical efficiency** — 压缩机机械效率 `0.9`（默认）| 正标量

流体功率与机械轴功率之比。

### **Model water droplets evaporation** — 模拟水滴蒸发的选项 `off`（默认）| `on`

模拟压缩机中因温度变化引起的水滴蒸发的选项。

### **Relative humidity at saturation** — 发生冷凝的相对湿度阈值 `1`（默认）| 正标量

压缩机中发生冷凝的相对湿度阈值。

### **Inlet area at port A** — 入口面积 `0.01` `m^2`（默认）| 正标量

与端口 **A** 关联的入口面积。

### **端口 B 的出口面积** — 出口面积 `0.01` `m^2`（默认）| 正标量

与端口 **B** 关联的出口面积。
## 所属库

Simscape / Fluids / Moist Air / Turbomachinery

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a: 模拟水滴蒸发

通过使用 **Model water droplets evaporation** 参数，模拟由温度变化引起的水滴蒸发。

### R2024b: 模拟悬浮在湿空气流中的水滴

湿空气域中的模块现在可以模拟悬浮在湿空气流中的水滴。要模拟水滴，请在连接到湿空气网络的 Moist Air Properties
(MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的容积式压缩机

Positive-Displacement Compressor (MA) 模块表示湿空气网络中的容积式压缩机，例如往复活塞式、旋转螺杆式、旋转叶片式或涡旋式。端口 **R** 和端口 **C**
分别是与压缩机轴和壳体关联的机械旋转守恒端口。当端口 **R** 相对于端口
**C** 存在正旋转时，湿空气从端口 **A** 流向端口
**B**。该模块对于反向流动可能不准确。

该图显示了活塞压缩机在 P-V 图上的各个步骤，其具有以下状态：

- *a* — 压缩机气缸在入口压力下充满。
- *b* — 压缩机内部压力超过出口压力，从而导致流体排出。
- *c* — 压缩机到达活塞行程顶部，气缸内仅剩余隙容积。
- *d* — 气缸内压力降至入口压力以下，从而导致流体吸入。

显示活塞压缩机过程的图，其中点 A 处于低压、高容积，点 B 处于高压、高容积，端口 C 处于高压、低容积，点 d 处于低压、低容积。

### 质量流量

该模块按如下方式计算质量流量

m˙=ηVωVdispvs,

其中：

- *ṁ* 是质量流量。
- *ω* 是端口 **R** 相对于端口 **C** 的角速度。
- *vs* 是入口处的比容。该模块根据标称入口条件计算此值。
- *Vdisp* 是该模块使用的排量。

### 排量

当您将 **Displacement specification** 设置为 `Volumetric
displacement` 时，该模块使用 **Displacement volume**
参数作为 *Vdisp* 的值。

当您将 **Displacement specification** 设置为 `Nominal
mass flow rate and shaft speed` 时，该模块按如下方式计算排量

Vdisp=m˙nominalvs,nominalωnominalηVnominal,

其中：

- *ṁnominal* 是
  **Nominal mass flow rate** 参数的值。
- *ωnominal* 是
  **Nominal shaft speed** 参数的值。
- *ηVnominal* 是
  **Nominal volumetric efficiency** 参数的值，此时
  **Efficiency specification** 参数为
  `Analytical`。当 **Volumetric
  efficiency** 参数为 `Tabulated` 时，该模块使用 `tablelookup` 函数将 *ηVnominal*
  插值为轴转速和压力比的函数。

### 容积效率

您可以使用解析值或查找表来参数化容积效率。

**解析容积效率**

当您将 **Efficiency specification** 设置为
`Analytical` 时，该模块使用解析值计算容积效率。当 **Thermodynamic model** 参数为
`Polytropic` 时，容积效率为

ηV=1+C−C(poutpin)1n,

其中 *pin* 和
*pout* 分别是入口压力和出口压力，*n* 是 **Polytropic
exponent** 参数的值。该模块按如下方式计算余隙容积分数
*C*

C=1−ηVnominalpratio1/n−1,

其中
*ηVnominal* 是
**Nominal volumetric efficiency** 参数的值，
*pratio* 是 **Nominal
pressure ratio** 参数的值。

当 **Thermodynamic model** 参数为
`Isentropic` 时，容积效率为

ηV=1+C−C(vinvout),

其中 *vin* 和
*vout* 分别是入口和出口比容。该模块按如下方式计算余隙容积分数
*C*

C=1-ηVnominalvrnominal-1

其中 vrnominal=vinnominal/voutnominal 是标称比容比。该模块根据标称入口条件和等熵效率计算此值。

**表格化容积效率**

当您将 **Efficiency specification** 设置为
`Tabulated` 时，该模块通过将 **Volumetric efficiency table,
eta\_vol(pr,w)** 参数的值插值为轴转速和压力比的函数来计算容积效率。

### 质量守恒

当您清除 **Model water droplets evaporation** 参数时，该模块按如下方式守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中：

- m˙*B* 是端口 **B** 处的混合物质量流量。
- m˙*wA* 和 m˙*wB* 分别是端口 **A** 和 **B** 处的水蒸气质量流量。
- m˙*gA* 和 m˙*gB* 分别是端口 **A** 和 **B** 处的示踪气体质量流量。
- m˙*dA* 和 m˙*dB* 分别是端口 **A** 和 **B** 处的水滴质量流量。

如果您选择 **Model water droplets evaporation**，则质量平衡方程为

m˙A+m˙B+m˙devap=0m˙wA+m˙wB−m˙devap=0m˙gA+m˙gB=0m˙dA+m˙dB−m˙devap=0

蒸发水滴的质量流量 m˙*devap* 为

m˙devap=max{m˙A,0}rdevap.

*rdevap* 是可以蒸发的水滴质量比，

rdevap=min{rdA,xwcapacity},

其取决于 *rdA*，即端口 **A** 处水滴与湿空气的质量比。

湿空气容纳更多水蒸气的能力为

xwcapacity=max{xwsB−xwA,0},

其中 *xwsB* 是饱和比湿度，*xwA* 是比湿度。

### 能量守恒

该模块按如下方式守恒能量

ϕA+ϕB+m˙AΔht=0,

其中 *Δht* 是比总焓的变化，*ṁAΔht* 是流体功率，其等于机械功率 *torque\*ω*。

当 **Thermodynamic model** 参数为
`Polytropic` 时，流体功率为

W˙c=ωnn−1ηVpinVdisp[(pinpout)n−1n−1],

其中该模块使用多方关系 pvn=constant 来关联 *pin*、*pout*、*vin* 和 *vout*。

当 **Thermodynamic model** 参数为
`Isentropic` 时，流体功率为

W˙C=m˙AΔht.

该模块根据等熵效率 *ηisen* 计算 *Δht*。当
**Efficiency specification** 参数为
`Analytical` 时，*ηisen* 等于 **Isentropic efficiency** 参数的值。当
**Efficiency specification** 参数为
`Tabulated` 时，该模块通过将
**Isentropic efficiency table, eta\_isen(pr,w)** 参数的值插值为压力比和轴转速的函数来计算
*ηisen*。

### 可视化容积效率

要可视化模块容积效率，请右键单击该模块并选择 **Fluids** > **Plot Volumetric Efficiency**。

每次修改模块设置时，请在图窗中单击 **Reload Data**。

当您将 **Efficiency specification** 设置为
`Analytical` 并将 **Thermodynamic model** 设置为
`Polytropic` 时，该模块绘制压缩机容积效率与压力比的关系。

容积效率

当您将 **Efficiency specification** 设置为
`Analytical` 并将 **Thermodynamic model** 设置为
`Isentropic` 时，该模块绘制压缩机容积效率与压力比在 *Tout nom*（标称出口温度）下的关系。

容积效率

当您将 **Efficiency specification** 设置为
`Tabulated` 时，该模块针对 **Shaft speed vector,
w** 参数中的每个元素绘制压缩机容积效率与压力比的关系。

容积效率

### 假设和限制

- 该模块对于从端口 **B** 流向端口 **A** 的流动可能不准确。
- 该模块假设流动为准稳态。压缩机不积累质量。
