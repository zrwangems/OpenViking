---
type: simulink-block
title: 'Pipe (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'pipetl'
documentation_source_path: 'ref/pipetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (TL)

## 端口
```yaml
ports:
- name: EL
  summary: 端口高程差，m 物理信号
  direction: input
- name: G
  summary: 重力加速度，m/s^2 物理信号
  direction: input
- name: A
  summary: 管道开口 热液体
  direction: input
- name: B
  summary: 管道开口 热液体
  direction: input
- name: H
  summary: 管壁 热
  direction: input
```

### 输入

### **EL** — 端口高程差，m 物理信号

端口 **A** 与 **B** 之间的可变高程差，指定为物理信号。该模块将 **EL** 处的信号值限制在 *-L* 与 *L* 之间，其中 *L* 为 **Pipe length** 参数的值。

#### 依赖

要启用此端口，请将 **Elevation gain specification** 设置为 `Variable`。

### **G** — 重力加速度，m/s^2 物理信号

可变重力加速度，指定为物理信号。

#### 依赖

要启用此端口，请将 **Gravitational acceleration specification** 设置为 `Variable`。
### 守恒

### **A** — 管道开口 热液体

管道的液体入口或出口端口。

### **B** — 管道开口 热液体

管道的液体入口或出口端口。

### **H** — 管壁 热

管壁温度。
## 参数
```yaml
parameters:
- name: Enable dynamic compressibility
  summary: 是否对流体动态可压缩性建模 on（默认）| off
  group: 配置
- name: Enable fluid inertia
  summary: 是否对流体加速度建模 off（默认）| on
  group: 配置
- name: Number of segments
  summary: 管道离散化 1（默认）| 正的无量纲标量
  group: 配置
- name: Pipe total length
  summary: 管道总长度 5 m（默认）| 以长度单位为单位的正标量
  group: 配置
- name: Cross-sectional geometry
  summary: 管道几何形状 Circular（默认）| Annular | Rectangular | Elliptical | Isosceles triangular | Custom
  group: 配置
- name: Pipe diameter
  summary: 管道直径 0.1 m（默认）| 正标量
  group: 配置
- name: Pipe inner diameter
  summary: 管道内径 0.05 m（默认）| 正标量
  group: 配置
- name: Pipe outer diameter
  summary: 管道外径 0.1 m（默认）| 正标量
  group: 配置
- name: Pipe width
  summary: 矩形管道宽度 0.1 m（默认）| 正标量
  group: 配置
- name: Pipe height
  summary: 矩形管道高度 0.1 m（默认）| 正标量
  group: 配置
- name: Pipe major axis
  summary: 椭圆管道长轴 0.1 m（默认）| 正标量
  group: 配置
- name: Pipe minor axis
  summary: 椭圆管道短轴 0.05 m（默认）| 正标量
  group: 配置
- name: Pipe side length
  summary: 三角形管道边长 0.1 m（默认）| 正标量
  group: 配置
- name: Pipe vertex angle
  summary: 三角形管道顶角 30 deg（默认）| 正标量
  group: 配置
- name: Cross-sectional area
  summary: 无变形时的管道横截面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Hydraulic diameter
  summary: 非圆形管道的有效直径 0.1128 m（默认）| 以长度单位为单位的正标量
  group: 配置
- name: Elevation gain specification
  summary: 设置管道高程属性 Constant（默认）| Variable
  group: 配置
- name: Elevation gain from port A to port B
  summary: 从端口 A 到端口 B 的高程变化 0 m（默认）| 以长度单位为单位的正标量
  group: 配置
- name: Gravitational acceleration specification
  summary: 加速度规格 Constant（默认）| Variable
  group: 配置
- name: Gravitational acceleration
  summary: 管道平均高程处的重力加速度 9.81 m/s^2（默认）| 标量
  group: 配置
- name: Viscous friction parameterization
  summary: 摩擦模型 Haaland correlation（默认）| Nominal pressure drop vs. nominal mass flow rate | Tabulated data - Darcy friction
    factor vs. Reynolds number
  group: 粘性摩擦
- name: Local resistances specification
  summary: 在 Haaland 关联式中量化压力损失的方法 Aggregate equivalent length（默认）| Local loss coefficient
  group: 粘性摩擦
- name: Total local loss coefficient
  summary: 定义管道上的损失系数 0.1（默认）| 正标量
  group: 粘性摩擦
- name: Aggregate equivalent length of local resistances
  summary: 管道中的局部阻力压力损失，以长度表示 1 m（默认）| 正标量
  group: 粘性摩擦
- name: Surface roughness specification
  summary: '用于粗糙度指定的管道材料 Commercially smooth brass, lead, copper, or plastic pipe: 1.52 um（默认）| Steel and wrought iron : 46
    um | Galvanized iron or steel : 152 um | Cast iron : 259 um | Custom'
  group: 粘性摩擦
- name: Internal surface absolute roughness
  summary: 管壁绝对粗糙度 1.5e-5 m（默认）| 以长度单位为单位的正标量
  group: 粘性摩擦
- name: Laminar friction constant for Darcy friction factor
  summary: 层流的摩擦常数 64（默认）| 正标量
  group: 粘性摩擦
- name: Laminar flow upper Reynolds number limit
  summary: 低于该雷诺数时流动为层流 2e+3（默认）| 正标量
  group: 粘性摩擦
- name: Turbulent flow lower Reynolds number limit
  summary: 高于该雷诺数时流动为湍流 4e+3（默认）| 正标量
  group: 粘性摩擦
- name: Nominal mass flow rate
  summary: 管道质量流量 [0.1 1] kg/s（默认）| 以质量/时间为单位的标量或数值向量
  group: 粘性摩擦
- name: Nominal pressure drop
  summary: 管道上的压力降 [0.001 0.01] MPa（默认）| 以压力为单位的标量或数值向量
  group: 粘性摩擦
- name: Mass flow rate threshold for flow reversal
  summary: 低于该阈值时应用数值平滑 1e-6 kg/s（默认）| 以质量/时间为单位的正标量
  group: 粘性摩擦
- name: Reynolds number vector for turbulent Darcy friction factor
  summary: 用于制表 Darcy 摩擦因子的雷诺数 [ 400 1000 1.5e+3 3e+3 4e+3 6e+3 1e+4 2e+4 4e+4 6e+4 1e+5 1e+8 ]（默认）| 正数向量
  group: 粘性摩擦
- name: Darcy friction factor vector
  summary: 制表雷诺数处的 Darcy 摩擦因子 [ 0.264 0.112 0.07099999999999999 0.0417 0.0387 0.0268 0.025 0.0232 0.0226 0.022 0.0214 0.0214
    ]（默认）| 正数向量
  group: 粘性摩擦
- name: Pipe wall specification
  summary: 管壁柔性 Rigid（默认）| Flexible
  group: Pipe Wall
- name: Volumetric expansion specification
  summary: 线性膨胀相关性 Cross-sectional area vs. pressure（默认）| Cross-sectional area vs. pressure - Tabulated | Hydraulic diameter
    vs. pressure | Based on material properties
  group: Pipe Wall
- name: Static gauge pressure to cross-sectional area gain
  summary: 面积相关管道变形的系数 1e-6 m^2/MPa（默认）| 正标量
  group: Pipe Wall
- name: Static gauge pressure vector
  summary: 表压向量 [.1,1] MPa（默认）| 向量
  group: Pipe Wall
- name: Cross sectional area gain vector
  summary: 管道横截面积向量 [1e-05, 1.1e-05] m^2（默认）| 向量
  group: Pipe Wall
- name: Static gauge pressure to hydraulic diameter gain
  summary: 直径相关管道变形的系数 1e-6 m/MPa（默认）| 正标量
  group: Pipe Wall
- name: Material behavior
  summary: 指定材料行为的方法 Linear Elastic（默认）| Multilinear Elastic
  group: Pipe Wall
- name: Pipe wall thickness
  summary: 管壁宽度 0.05 m（默认）| 正标量
  group: Pipe Wall
- name: Young's modulus
  summary: 管壁材料的杨氏模量 69 GPa（默认）| 正标量
  group: Pipe Wall
- name: Poisson's ratio
  summary: 管壁材料的泊松比 0.33（默认）| 正标量
  group: Pipe Wall
- name: Stress vector
  summary: 管壁材料的应力向量 [276, 310] MPa（默认）| 向量
  group: Pipe Wall
- name: Strain vector
  summary: 管壁材料的应变向量 [.004, .02]（默认）| 向量
  group: Pipe Wall
- name: Check if stress exceeds specified allowable level
  summary: 当应力超过指定最大值时的通知 None（默认）| Warning | Error
  group: Pipe Wall
- name: Maximum allowable stress
  summary: 管壁上允许的最大应力 400 MPa（默认）| 正标量
  group: Pipe Wall
- name: Volumetric expansion time constant
  summary: 管道变形时间常数 0.01 s（默认）| 正标量
  group: Pipe Wall
- name: Pipe thermal expansion
  summary: 是否对热膨胀建模 off（默认）| on
  group: Pipe Wall
- name: Coefficient of thermal expansion
  summary: 管道热膨胀系数 24 um/(deltaK*m)（默认）| 正标量
  group: Pipe Wall
- name: Thermal expansion reference temperature
  summary: 管道热膨胀的参考温度 293.15 K（默认）| 正标量
  group: Pipe Wall
- name: Heat transfer parameterization
  summary: 捕获与管壁对流传热的方法 Gnielinski correlationNominal temperature differential vs. nominal mass flow rate（默认）| Dittus-Boelter
    correlation | Tabulated data - Colburn factor vs. Reynolds number | Tabulated data - Nusselt number vs. Reynolds number
    & Prandtl number
  group: 传热
- name: Nusselt number for laminar flow heat transfer
  summary: 层流换热计算中使用的努塞尔数 3.66（默认）
  group: 传热
- name: Nominal mass flow rate
  summary: 管道质量流量 [0.1 1] kg/s（默认）| 以质量/时间为单位的标量或数值向量
  group: 传热
- name: Nominal inflow temperature
  summary: 管道入口温度 [293.15 293.15] K（默认）| 以温度为单位的标量或数值向量
  group: 传热
- name: Nominal outflow temperature
  summary: 管道出口温度 [300 300] K（默认）| 以温度为单位的标量或数值向量
  group: 传热
- name: Nominal inflow pressure
  summary: 管道入口压力 [0.101325 0.101325] MPa（默认）| 以压力为单位的标量或数值向量
  group: 传热
- name: Nominal wall temperature
  summary: 管道壁温 [303.15 303.15] K（默认）| 以温度为单位的标量或数值向量
  group: 传热
- name: Coefficient a
  summary: Dittus-Boelter 关联式的经验常数 *a* 0.023（默认）| 正标量
  group: 传热
- name: Exponent b
  summary: Dittus-Boelter 关联式的经验常数 *b* 0.8（默认）| 正标量
  group: 传热
- name: Exponent c
  summary: Dittus-Boelter 关联式的经验常数 *c* 0.4（默认）| 正标量
  group: 传热
- name: Reynolds number vector for Colburn factor
  summary: 用于将 Colburn 因子制表的 Reynolds 数 [100 150 1000]（默认）| 正数向量
  group: 传热
- name: Colburn factor vector
  summary: 在制表的 Reynolds 数处的 Colburn 因子 [0.019 0.013 0.002]（默认）| 正数向量
  group: 传热
- name: Reynolds number vector for Nusselt number
  summary: 用于将 Nusselt 数制表的 Reynolds 数 [100 150 100]（默认）| 正数向量
  group: 传热
- name: Prandtl number vector for Nusselt number
  summary: 用于将 Nusselt 数制表的 Prandtl 数 [1 10]（默认）| 正数向量
  group: 传热
- name: Nusselt number table
  summary: 在制表的 Reynolds 数和 Prandtl 数处的 Nusselt 数 [ 3.72 4.21; 3.75 4.44; 4.21 7.15 ]（默认）| 正数矩阵
  group: 传热
- name: 初始液体温度
  summary: 仿真开始时的液体温度 293.15 K（默认）
  group: 初始条件
- name: 初始液体压力
  summary: 仿真开始时的管道压力 0.101325 MPa（默认）| 正标量
  group: 初始条件
- name: 标称液体温度
  summary: 标称工况下的温度 293.15 K（默认）| 标量
  group: 初始条件
- name: 标称液体压力
  summary: 标称工况下的压力 0.101325 MPa（默认）| 标量
  group: 初始条件
```

### 配置

### **Enable dynamic compressibility** — 是否对流体动态可压缩性建模 `on`（默认）| `off`

是否对由流体可压缩性引起的任何流体密度变化进行建模。当您选择 **Fluid compressibility** 时，除了由压力变化引起的密度变化外，还会计算由流入模块的质量流量引起的变化。

### **Enable fluid inertia** — 是否对流体加速度建模 `off`（默认）| `on`

是否考虑由流体质量引起的质量流量中的加速度。

#### 依赖

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Number of segments** — 管道离散化 `1`（默认）| 正的无量纲标量

管道分段数。每个分段表示一个单独的段，在该段上根据管道入口压力、流体可压缩性以及（如适用）壁面柔性计算压力。每个分段中的流体体积保持固定。

#### 依赖

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Pipe total length** — 管道总长度 `5` `m`（默认）| 以长度单位为单位的正标量

所有管道分段的总管道长度。

### **Cross-sectional geometry** — 管道几何形状 `Circular`（默认）| `Annular` | `Rectangular` | `Elliptical` | `Isosceles triangular` | `Custom`

管道横截面几何形状。根据横截面几何形状计算标称水力直径和标称横截面积。

### **Pipe diameter** — 管道直径 `0.1 m`（默认）| 正标量

圆形横截面管道的直径。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Circular`。

### **Pipe inner diameter** — 管道内径 `0.05 m`（默认）| 正标量

环形管道流动或两个同心管道之间流动的内径。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Annular`。

### **Pipe outer diameter** — 管道外径 `0.1 m`（默认）| 正标量

环形管道流动或两个同心管道之间流动的外径。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Annular`。

### **Pipe width** — 矩形管道宽度 `0.1 m`（默认）| 正标量

矩形管道的宽度。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Rectangular`。

### **Pipe height** — 矩形管道高度 `0.1 m`（默认）| 正标量

矩形管道的高度。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Rectangular`。

### **Pipe major axis** — 椭圆管道长轴 `0.1 m`（默认）| 正标量

椭圆管道的长轴。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Elliptical`。

### **Pipe minor axis** — 椭圆管道短轴 `0.05 m`（默认）| 正标量

椭圆管道的短轴。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Elliptical`。

### **Pipe side length** — 三角形管道边长 `0.1 m`（默认）| 正标量

等腰三角形管道的两条相等边的长度。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Isosceles triangular`。

### **Pipe vertex angle** — 三角形管道顶角 `30 deg`（默认）| 正标量

三角形管道的顶角。该值必须小于 180 度。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Isosceles triangular`。

### **Cross-sectional area** — 无变形时的管道横截面积 `0.01` `m^2`（默认）| 正标量

无变形时管道的横截面积。

#### 依赖

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Custom`。

### **Hydraulic diameter** — 非圆形管道的有效直径 `0.1128` `m`（默认）| 以长度单位为单位的正标量

用于传热、动量平衡和管道柔性方程的有效直径。对于非圆形管道，水力直径为管道中流体的有效直径。对于圆形管道，水力直径与管道直径相同。

#### 依赖

要启用此参数，请执行以下任一操作：

- 清除 **Enable dynamic compressibility** 复选框，并将 **Cross-sectional geometry** 设置为 `Custom`。
- 选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 参数设置为 `Rigid`，并将 **Cross-sectional geometry** 设置为 `Custom`。

### **Elevation gain specification** — 设置管道高程属性 `Constant`（默认）| `Variable`

将管道高程设置为 `Constant` 或 `Variable`。选择 `Variable` 将显示物理信号端口 **EL**。

### **Elevation gain from port A to port B** — 从端口 A 到端口 B 的高程变化 `0 m`（默认）| 以长度单位为单位的正标量

恒定高程管道的高程差。

#### 依赖

要启用此参数，请将 **Elevation gain specification** 设置为 `Constant`。

### **Gravitational acceleration specification** — 加速度规格 `Constant`（默认）| `Variable`

重力加速度是恒定的还是可变的。

### **Gravitational acceleration** — 管道平均高程处的重力加速度 `9.81` `m/s^2`（默认）| 标量

管道平均高程处的重力加速度常数。

#### 依赖

要启用此参数，请将 **Gravitational acceleration specification** 设置为 `Constant`。

### 粘性摩擦

### **Viscous friction parameterization** — 摩擦模型 `Haaland correlation`（默认）| `Nominal pressure drop vs. nominal mass flow rate` | `Tabulated data - Darcy friction factor vs. Reynolds number`

由壁面摩擦引起的压力损失的参数化。提供解析公式和表格公式。

### **Local resistances specification** — 在 Haaland 关联式中量化压力损失的方法 `Aggregate equivalent length`（默认）| `Local loss coefficient`

量化由管道非均匀性引起的压力损失的方法。

#### 依赖

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`。

### **Total local loss coefficient** — 定义管道上的损失系数 `0.1`（默认）| 正标量

与每个管道非均匀性相关的损失系数。您可以输入单个损失系数或沿管道的所有损失系数之和。

#### 依赖

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`，并将 **Local resistance specifications** 设置为 `Local loss coefficient`。

### **Aggregate equivalent length of local resistances** — 管道中的局部阻力压力损失，以长度表示 `1` `m`（默认）| 正标量

等效于带有弯头、面积变化或其他不均匀性的管道所产生的水力损失的管道长度。管道的有效长度是 **Pipe length** 与 **Aggregate equivalent length of local resistances** 之和。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`，并将 **Local resistances specification** 设置为 `Aggregate equivalent length`。

### **Surface roughness specification** — 用于粗糙度指定的管道材料 `Commercially smooth brass, lead, copper, or plastic pipe: 1.52 um`（默认）| `Steel and wrought iron : 46 um` | `Galvanized iron or steel : 152 um` | `Cast iron : 259 um` | `Custom`

基于管道材料的绝对表面粗糙度。提供的值为 ASHRAE 标准粗糙度值。您也可以通过将 **Surface roughness specification** 设置为 `Custom` 来输入自己的值。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`。

### **Internal surface absolute roughness** — 管壁绝对粗糙度 `1.5e-5` `m`（默认）| 以长度单位为单位的正标量

管壁绝对粗糙度。此参数用于确定 Darcy 摩擦因子，该因子会影响管道中的压力损失。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Haaland correlation`，并将 **Surface roughness specification** 设置为 `Custom`。

### **Laminar friction constant for Darcy friction factor** — 层流的摩擦常数 `64`（默认）| 正标量

层流的摩擦常数。Darcy 摩擦因子用于表征压力损失计算中壁面摩擦的贡献。如果 **Cross-sectional geometry** 未设置为 `Custom`，则此参数在内部设置为 64。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Custom`。

### **Laminar flow upper Reynolds number limit** — 低于该雷诺数时流动为层流 `2e+3`（默认）| 正标量

低于该雷诺数时流动为层流。高于此阈值时，流动过渡为湍流，并在 **Turbulent flow lower Reynolds number limit** 设置处达到湍流状态。

### **Turbulent flow lower Reynolds number limit** — 高于该雷诺数时流动为湍流 `4e+3`（默认）| 正标量

高于该雷诺数时流动为湍流。低于此阈值时，流动逐渐过渡为层流，并在 **Laminar flow upper Reynolds number limit** 设置处达到层流状态。

### **Nominal mass flow rate** — 管道质量流量 `[0.1 1]` `kg/s`（默认）| 以质量/时间为单位的标量或数值向量

用于计算压力损失系数的管道标称质量流量，指定为标量或向量。所有标称值必须大于 0，并且其元素数量必须与 **Nominal pressure drop** 参数相同。当此参数以向量形式提供时，标量值 *K*p 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **Nominal pressure drop** — 管道上的压力降 `[0.001 0.01]` `MPa`（默认）| 以压力为单位的标量或数值向量

用于计算压力损失系数的管道标称压力降，指定为标量或向量。所有标称值必须大于 0，并且其元素数量必须与 **Nominal mass flow rate** 参数相同。当此参数以向量形式提供时，标量值 *K*p 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **Mass flow rate threshold for flow reversal** — 低于该阈值时应用数值平滑 `1e-6` `kg/s`（默认）| 以质量/时间为单位的正标量

反向流动的质量流量阈值。在质量流量阈值的正值和负值之间，围绕 0 kg/s 定义了一个过渡区域。在该过渡区域内，对流动响应应用数值平滑。阈值必须大于 0。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **Reynolds number vector for turbulent Darcy friction factor** — 用于制表 Darcy 摩擦因子的雷诺数 `[ 400 1000 1.5e+3 3e+3 4e+3 6e+3 1e+4 2e+4 4e+4 6e+4 1e+5 1e+8 ]`（默认）| 正数向量

用于 Darcy 摩擦因子表格化参数化的雷诺数向量。该向量元素与 **Darcy friction factor vector** 参数构成独立轴。向量元素必须按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — 制表雷诺数处的 Darcy 摩擦因子 `[ 0.264 0.112 0.07099999999999999 0.0417 0.0387 0.0268 0.025 0.0232 0.0226 0.022 0.0214 0.0214 ]`（默认）| 正数向量

用于 Darcy 摩擦因子表格化参数化的 Darcy 摩擦因子向量。该向量元素必须与 **Reynolds number vector for turbulent Darcy friction factor** 参数中的元素一一对应，并且必须唯一且大于或等于 0。

#### 依赖关系

要启用此参数，请将 **Viscous friction parameterization** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### Pipe Wall

### **Pipe wall specification** — 管壁柔性 `Rigid`（默认）| `Flexible`

管道的管壁柔性。此参数与管道横截面几何形状无关。`Flexible` 设置会保持初始管道形状，并对横截面积施加均匀膨胀。对于高变形下的非圆形横截面几何形状，`Flexible` 设置可能不准确。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Volumetric expansion specification** — 线性膨胀相关性 `Cross-sectional area vs. pressure`（默认）| `Cross-sectional area vs. pressure - Tabulated` | `Hydraulic diameter vs. pressure` | `Based on material properties`

线性膨胀相关性。这些设置将新的横截面积或水力直径与管道压力关联起来。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`。

### **Static gauge pressure to cross-sectional area gain** — 面积相关管道变形的系数 `1e-6 m^2/MPa`（默认）| 正标量

用于计算管道变形的系数。该模块将此参数的值乘以段压力与大气压力之间的压差。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并将 **Volumetric expansion specification** 设置为 `Cross-sectional area vs. pressure`。

### **Static gauge pressure vector** — 表压向量 `[.1,1] MPa`（默认）| 向量

包含表压的向量。该模块使用此向量进行查表以计算管道横截面积。向量条目必须严格为正且单调递增，并且该向量必须与 **Cross sectional area gain vector** 参数长度相同。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并将 **Volumetric expansion specification** 设置为 `Cross-sectional area vs. pressure - Tabulated`。

### **Cross sectional area gain vector** — 管道横截面积向量 `[1e-05, 1.1e-05] m^2`（默认）| 向量

包含管道横截面积的向量。该模块使用此向量进行查表，以计算其他压力下的管道横截面积。向量元素必须严格为正且单调递增，并且向量的长度必须与 **Static gauge pressure vector** 参数相同。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并将 **Volumetric expansion specification** 设置为 `Cross-sectional area vs. pressure - Tabulated`。

### **Static gauge pressure to hydraulic diameter gain** — 直径相关管道变形的系数 `1e-6 m/MPa`（默认）| 正标量

用于计算管道变形的系数。该模块将此参数的值乘以段压力与大气压力之间的压差。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并将 **Volumetric expansion specification** 设置为 `Hydraulic diameter vs. pressure`。

### **Material behavior** — 指定材料行为的方法 `Linear Elastic`（默认）| `Multilinear Elastic`

该模块用于计算材料行为的方法。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并将 **Volumetric expansion specification** 设置为 `Based on material properties`。

### **Pipe wall thickness** — 管壁宽度 `0.05 m`（默认）| 正标量

管壁的厚度。该模块使用此值来计算应力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并将 **Volumetric expansion specification** 设置为 `Based on material properties`。

### **Young's modulus** — 管壁材料的杨氏模量 `69 GPa`（默认）| 正标量

构成管壁的材料的杨氏模量。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，并将 **Material behavior** 设置为 `Linear Elastic`。

### **Poisson's ratio** — 管壁材料的泊松比 `0.33`（默认）| 正标量

构成管壁的材料的泊松比。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并将 **Volumetric expansion specification** 设置为 `Based on material properties`。

### **Stress vector** — 管壁材料的应力向量 `[276, 310] MPa`（默认）| 向量

包含构成管壁的材料的应力值的向量。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，并将 **Material behavior** 设置为 `Multilinear Elastic`。

### **Strain vector** — 管壁材料的应变向量 `[.004, .02]`（默认）| 向量

包含构成管壁的材料的应变值的向量。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，并将 **Material behavior** 设置为 `Multilinear Elastic`。

### **Check if stress exceeds specified allowable level** — 当应力超过指定最大值时的通知 `None`（默认）| `Warning` | `Error`

当应力超过 **Maximum allowable stress** 参数指定的最大应力时，该模块是不执行任何操作、生成警告还是生成错误。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，并将 **Material behavior** 设置为 `Multilinear Elastic`。

### **Maximum allowable stress** — 管壁上允许的最大应力 `400 MPa`（默认）| 正标量

该模块允许的管壁最大应力。使用 **Check if stress exceeds specified allowable level** 参数控制当应力超过此值时该模块的行为。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，将 **Volumetric expansion specification** 设置为 `Based on material properties`，将 **Material behavior** 设置为 `Multilinear Elastic`，并将 **Check if stress exceeds specified allowable level** 设置为 `Warning` 或 `Error`。

### **Volumetric expansion time constant** — 管道变形时间常数 `0.01 s`（默认）| 正标量

管道变形后管壁达到稳态所需的时间。此参数影响管道体积的动态变化。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`。

### **Pipe thermal expansion** — 是否对热膨胀建模 `off`（默认）| `on`

是否考虑管道因温度变化而产生的膨胀。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，并将 **Pipe wall specification** 设置为 `Flexible`。

### **Coefficient of thermal expansion** — 管道热膨胀系数 `24 um/(deltaK*m)`（默认）| 正标量

管道材料的线性热膨胀系数。此值是在恒定压力下，温度每变化一度时尺寸的分数变化。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并选择 **Pipe thermal expansion**。

### **Thermal expansion reference temperature** — 管道热膨胀的参考温度 `293.15 K`（默认）| 正标量

该模块在计算管道热膨胀时使用的参考温度。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**，将 **Pipe wall specification** 设置为 `Flexible`，并选择 **Pipe thermal expansion**。

### 传热

### **Heat transfer parameterization** — 捕获与管壁对流传热的方法 `Gnielinski correlation``Nominal temperature differential vs. nominal mass flow rate`（默认）| `Dittus-Boelter correlation` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`

计算流体与管壁之间传热系数的方法。可使用解析参数化和表格数据参数化。

### **Nusselt number for laminar flow heat transfer** — 层流换热计算中使用的努塞尔数 `3.66`（默认）

层流状态下对流传热与导热传热的比值。流体努塞尔数影响传热速率。

#### 依赖关系

要启用此参数，请将 **Cross-sectional geometry** 设置为 `Custom`，并将 **Heat transfer parameterization** 设置为以下之一：

- `Gnielinski correlation`。
- `Nominal temperature differential vs. nominal mass flow rate`。
- `Dittus-Boelter correlation`。

### **Nominal mass flow rate** — 管道质量流量 `[0.1 1]` `kg/s`（默认）| 以质量/时间为单位的标量或数值向量

用于计算传热系数的管道标称质量流量，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **Nominal inflow temperature** 参数相同。当此参数以向量形式提供时，标量值 *h*p 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **Nominal inflow temperature** — 管道入口温度 `[293.15 293.15]` `K`（默认）| 以温度为单位的标量或数值向量

用于计算传热系数的标称流体入口温度，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **Nominal mass flow rate** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **Nominal outflow temperature** — 管道出口温度 `[300 300]` `K`（默认）| 以温度为单位的标量或数值向量

用于计算传热系数的标称流体出口温度，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **Nominal mass flow rate** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **Nominal inflow pressure** — 管道入口压力 `[0.101325 0.101325]` `MPa`（默认）| 以压力为单位的标量或数值向量

用于计算传热系数的标称流体入口压力，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **Nominal mass flow rate** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **Nominal wall temperature** — 管道壁温 `[303.15 303.15]` `K`（默认）| 以温度为单位的标量或数值向量

用于计算传热系数的管道壁温，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **Nominal mass flow rate** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此温度，请将 **Heat transfer parameterization** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **Coefficient a** — Dittus-Boelter 关联式的经验常数 *a* `0.023`（默认）| 正标量

要在 Dittus-Boelter 关联式中使用的经验常数 *a*。该关联式将湍流中的 Nusselt 数与传热系数关联起来。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Dittus-Boelter correlation`。

### **Exponent b** — Dittus-Boelter 关联式的经验常数 *b* `0.8`（默认）| 正标量

要在 Dittus-Boelter 关联式中使用的经验常数 *b*。该关联式将湍流中的 Nusselt 数与传热系数关联起来。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Dittus-Boelter correlation`。

### **Exponent c** — Dittus-Boelter 关联式的经验常数 *c* `0.4`（默认）| 正标量

要在 Dittus-Boelter 关联式中使用的经验常数 *c*。该关联式将湍流中的 Nusselt 数与传热系数关联起来。默认值反映向流体的传热。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Dittus-Boelter correlation`。

### **Reynolds number vector for Colburn factor** — 用于将 Colburn 因子制表的 Reynolds 数 `[100 150 1000]`（默认）| 正数向量

用于 Colburn 因子表格参数化的 Reynolds 数向量。该向量元素与 **Colburn factor vector** 参数构成独立轴。向量元素必须按升序列出，并且必须大于 0。此参数的元素数量必须与 **Colburn factor vector** 相同。对于反向流动，或从 **B** 到 **A** 的流动，相同数据以相反方向应用。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — 在制表的 Reynolds 数处的 Colburn 因子 `[0.019 0.013 0.002]`（默认）| 正数向量

用于 Colburn 因子表格参数化的 Colbrun 因子向量。该向量元素与 **Reynolds number vector for Colburn factor** 参数构成独立轴。此参数的元素数量必须与 **Reynolds number vector for Colburn factor** 相同。

#### 依赖关系

当 **Heat transfer parameterization** 模块参数设置为 `Tabulated data - Colburn factor vs. Reynolds number` 时，此参数处于活动状态。

### **Reynolds number vector for Nusselt number** — 用于将 Nusselt 数制表的 Reynolds 数 `[100 150 100]`（默认）| 正数向量

用于 Nusselt 数表格参数化的 Reynolds 数向量。该向量与 **Prandtl number vector for Nusselt number** 参数一起，为二维因变量 **Nusselt number table** 构成独立轴。向量元素必须按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`。

### **Prandtl number vector for Nusselt number** — 用于将 Nusselt 数制表的 Prandtl 数 `[1 10]`（默认）| 正数向量

用于 Nusselt 数表格参数化的 Prandtl 数向量。该向量与 **Reynolds number vector for Nusselt number** 参数一起，为二维因变量 **Nusselt number table** 构成独立轴。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`。

### **Nusselt number table** — 在制表的 Reynolds 数和 Prandtl 数处的 Nusselt 数 `[ 3.72 4.21; 3.75 4.44; 4.21 7.15 ]`（默认）| 正数矩阵

在指定 Reynolds 数和 Prandtl 数处的 *M*×*N* Nusselt 数矩阵。表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Reynolds number vector for Nusselt number** 参数中的向量元素数量。
- *N* 是 **Prandtl number vector for Nusselt number** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请将 **Heat transfer parameterization** 设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`。

### 初始条件

### **初始液体温度** — 仿真开始时的液体温度 `293.15` `K`（默认）

仿真开始时的液体温度。

### **初始液体压力** — 仿真开始时的管道压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的管道压力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **标称液体温度** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的液体温度。当动态可压缩性禁用时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **标称液体压力** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的液体压力。当动态可压缩性禁用时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。
## 所属库

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：对柔性管壁或可变重力加速度进行建模

将 **Pipe wall specification** 参数设置为 `Flexible` 以对柔性管壁进行建模。此参数化还考虑了温度变化引起的管壁变形。

将 **Gravitational acceleration specification** 参数设置为 `Variable` 以启用端口 **G** 并将重力加速度作为物理信号提供。

### R2023b：对长度短于高程增量的管道进行建模

当 **Elevation gain specification** 为 `Constant` 时，您现在可以对长度短于高程变化的管道进行建模。如果 **Elevation gain from port A to port B** 参数的值大于 **Pipe length** 参数的值，模块会发出警告而不是错误。

### R2023a：对管道特性进行建模

您现在可以使用 Pipe (TL) 模块的新参数来控制管道属性。使用 **Cross-sectional geometry** 参数指定管道横截面形状。使用 **Surface roughness specification** 参数使用管壁材料来确定表面粗糙度。

## 描述

在热液体组件之间输送流体的封闭管道

Pipe (TL) 模块表示通过管道的热液体流动。该模块根据端口之间的温差、管道高程以及端口 **H** 处的任何额外热传递来计算管道上的温度。

管道在端口 **A** 和 **B** 之间可以具有恒定或变化的高程。对于恒定高程差，使用 **Elevation gain from port A to port B** 参数。您可以通过将 **Elevation gain specification** 设置为 `Variable` 来指定可变高程。这会暴露物理信号端口 **EL**。

您可以选择包含流体动态可压缩性、惯性和管壁柔性的影响。当模块包含这些现象时，它会为您指定的每个管道段数计算流动属性。

### 管道几何形状

使用 **Cross-sectional geometry** 参数指定管道的形状。

**圆形**

标称水力直径 *DN* 和管道直径 *dcircle* 均等于 **Pipe diameter** 参数的值。管道横截面积为 SN=π4dcircle2。

**环形**

标称水力直径是 **Pipe outer diameter** 和 **Pipe inner diameter** 参数之差 *DN* = *douter* – *dinner*。管道横截面积为 SN=π4(douter2−dinner2)。

**矩形**

标称水力直径为

DN=2hwh+w，

其中：

- *h* 是 **Pipe height** 参数的值。
- *w* 是 **Pipe width** 参数的值。

管道横截面积为 SN=wh。

**椭圆形**

标称水力直径为

DN=2amajbmin(64-16(amaj-bminamaj+bmin)2)(amaj+bmin)(64-3(amaj-bminamaj+bmin)4)，

其中：

- *amaj* 是 **Pipe major axis** 参数的值。
- *bmin* 是 **Pipe minor axis** 参数的值。

管道横截面积为 SN=π4amajbmin。

**等腰三角形**

标称水力直径为

DN=lsidesin(θ)1+sin(θ2)，

其中：

- *lside* 是 **Pipe side length** 参数的值。
- *θ* 是 **Pipe vertex angle** 参数的值。

管道横截面积为 SN=lside22sin(θ)。

**自定义**

当 **Cross-sectional geometry** 参数为 `Custom` 时，您可以使用 **Cross-sectional area** 参数指定管道横截面积。标称水力直径为 **Hydraulic diameter** 参数的值。

### 管道柔性

您可以为所有横截面几何形状建模柔性壁。当您将**管道壁规格**设置为`Flexible`时，模块假定沿所有方向均匀膨胀并保持定义的横截面形状。对于非圆形横截面积在相对于大气压的高压下，此设置可能不会产生物理结果。当您建模柔性壁时，可以使用**体积膨胀规格**参数来指定管道横截面积的体积膨胀。

当**体积膨胀规格**参数为`Cross-sectional area vs. pressure`时，体积变化为

V˙=L(A−Sτ),

其中：

- A=SN+Kps(p−patm)。
- *L* 是**管道长度**参数。
- *SN* 是为每种形状定义的标称管道横截面积。
- *S* 是当前管道横截面积。
- *p* 是管道内部压力。
- *patm* 是大气压力。
- *K*ps 是**静态表压到横截面积增益**参数。

  为计算 *Kps*，假设薄壁、开口圆柱形管道均匀弹性变形，使用

  Kps=ΔDΔp=πDN34tE,

  其中 *t* 是管道壁厚，*E* 是杨氏模量。
- *τ* 是**体积膨胀时间常数**。

当**体积膨胀规格**参数为`Cross-sectional area vs. pressure - Tabulated`时，模块使用与`Cross-sectional area vs. pressure`设置相同的 V˙ 方程。模块通过查表函数计算 *A*

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear)，

其中 *pps* 是**静态表压向量**参数，*Aps* 是**横截面积增益向量**参数。

当**体积膨胀规格**参数为`Hydraulic diameter vs. pressure`时，体积变化为

V˙=π2DL(Dstatic−Dτ),

其中：

- Dstatic=DN+Kpd(p−patm)。
- *DN* 是为每种形状定义的标称水力直径。
- *D* 是当前管道水力直径。
- *Kpd* 是**静态表压到水力直径增益**参数。为计算 *Kps*，假设薄壁、开口圆柱形管道均匀弹性变形，使用

  Kpd=ΔDΔp=DN22tE。

当**体积膨胀规格**参数为`Based on material properties`时，模块使用与`Hydraulic diameter vs. pressure`设置相同的 V˙ 方程，但根据**材料行为**参数的值计算 *Dstatic*

Dstatic=DN(1+ϵhoop)。

此参数化假设为圆柱形薄壁压力容器，其中 σradial=0。

当**材料行为**参数为`Linear elastic`时，

ϵhoop=1E[σhoop−vσlongitudinal],

其中：

- *E* 是**杨氏模量**参数的值。
- *v* 是**泊松比**参数的值。
- σhoop=pD2t，其中 *t* 是**管道壁厚**参数的值。
- σlongitudinal=pD4t。

当**材料行为**参数为`Multilinear elastic`时，模块计算 von Mises 应力 *σv*，其简化为 σv=34pD2t，以确定等效应变。环向应变为

ϵhoop=ϵhoopelastic+ϵhoopplastic

ϵhoopelastic=1E[σhoop−vσlongitudinal]ϵhoopi,jplastic=32(1Es−1E)Si,j

其中：

- 模块从**应力向量**和**应变向量**参数的第一个元素计算杨氏模量 *E*。
- ES=σtotalϵtotal，其中 *σtotal* 和 *εtotal* 分别是等效总应力和等效总应变。模块根据 von Mises 应力和应力-应变曲线计算等效总应变。
- Si,j=σi,j−[σhoop+σlongitudinal+σradial3]δi,j，其中 *σi,j* 是 Cauchy 应力张量的元素。

如果您不建模柔性壁，则 *SN* = *S* 且 *DN* = *D*。

**管道壁热膨胀**

如果您选择**管道热膨胀**，模块使用以下假设建模管道壁的热膨胀：

- 管道材料是各向同性的。
- 管道的 Biot 数小于 0.1，并且管道可以用集总热容建模。
- 温度变化和管道变形足够小，使得面积膨胀的一阶近似是准确的。

当**材料行为**参数为`Cross-sectional area vs. pressure`、`Cross-sectional area vs. pressure - Tabulated`或`Hydraulic diameter vs. pressure`，并且您选择**管道热膨胀**时，模块在计算面积或直径时添加热膨胀项。

当**材料行为**为`Cross-sectional area vs. pressure`时，

A=SN+Kps(p−patm)+SN2αΔT，

其中：

- *ɑ* 是**热膨胀系数**参数的值。
- ΔT=TI−Tref。
- *TI* 是模块内部节点的流体温度。
- *Tref* 是**热膨胀参考温度**参数的值。

当**材料行为**为`Cross-sectional area vs. pressure - Tabulated`时，

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear)+SN2αΔT。

当**材料行为**为`Hydraulic diameter vs. pressure`时，

Dstatic=DN+Kpd(p−patm)+DNαΔT。

当**材料行为**参数为`Multilinear elastic`并且您选择**管道热膨胀**时，模块计算 *Dstatic* 为

Dstatic=DN(1+ϵhoop+ϵthermal),

其中 ϵthermal=αΔT。

### Heat Transfer at the Pipe Wall

您可以通过多种方式包含与管壁之间的热传递。有两种分析模型：`Gnielinski correlation`，它使用预定义系数将努塞尔数建模为雷诺数和普朗特数的函数；以及 `Dittus-Boelter correlation - Nusselt = a*Re^b*Pr^c`，它使用用户定义的系数将努塞尔数建模为雷诺数和普朗特数的函数。

`Nominal temperature differential vs. nominal mass flow rate`、`Tabulated data - Colburn factor vs. Reynolds number` 和 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number` 是基于用户提供数据的查找表参数化。

流体与管壁之间的热传递通过对流 *QConv* 和传导 *QCond* 发生，其中净热流率 *QH* 为 *QH*=*QConv*+*QCond*。

传导引起的热传递为：

QCond=kISHD(TH−TI),

其中：

- *D* 是标称水力直径 *DN*（如果管壁为刚性），并且是管道稳态直径 *DS*（如果管壁为柔性）。
- *kI* 是热液体的热导率，针对每个管道段在内部定义。
- *SH* 是管壁的表面积。
- *TH* 是管壁温度。
- *TI* 是模块内部节点处的流体温度。

对流引起的热传递为：

QConv=cp,Avg|m˙Avg|(TH−TIn)[1−exp(−hSHcp,Avg|m˙Avg|)],

其中：

- *c*p, Avg 是平均流体比热，模块使用查找表计算该值。
- m˙Avg 是通过管道的平均质量流量。
- *TIn* 是流体入口端口温度。
- *h* 是管道传热系数。

传热系数 *h* 为：

h=NukAvgD,

除非使用 `Nominal temperature differential vs. nominal mass flow rate` 进行参数化，此时 *kAvg* 是整个管道上热液体的平均热导率，*Nu* 是管道中的平均努塞尔数。

**分析参数化**

当 **Heat transfer parameterization** 设置为 `Gnielinski correlation` 且流动为湍流时，平均努塞尔数计算为：

Nu=f8(Re−1000)Pr1+12.7( f8)1/2(Pr2/3−1),

其中：

- *f* 是根据 Haaland 关联式得到的平均 Darcy 摩擦因子：

  f={−1.8log10[6.9Re+(ϵR3.7D)1.11]}-2,

  其中 *ε*R 是管道 **Internal surface absolute roughness**。
- *Re* 是雷诺数。
- *Pr* 是普朗特数。

当流动为层流时，来自 [1] 的数据决定努塞尔数如何取决于 **Cross-sectional geometry** 参数：

- 当 **Cross-sectional geometry** 为 `Circular` 时，努塞尔数为 3.66。
- 当 **Cross-sectional geometry** 为 `Annular` 时，模块使用具有线性插值和最近外推的查找表从表格数据计算努塞尔数。

  | DinnerDouter | Nusselt number |
  | --- | --- |
  | 1/20 | 17.46 |
  | 1/10 | 11.56 |
  | 1/4 | 7.37 |
  | 1/2 | 5.74 |
  | 1 | 4.86 |

  模块使用修正因子 F = 0.86(DouterDinner)0.16 调整计算得到的努塞尔数。
- 当 **Cross-sectional geometry** 为 `Rectangular` 时，模块使用具有线性插值和最近外推的查找表从表格数据计算努塞尔数。

  | min(h,w)max(h,w) | Nusselt number |
  | --- | --- |
  | 0 | 7.54 |
  | 1/8 | 5.60 |
  | 1/6 | 5.14 |
  | 1/4 | 4.44 |
  | 1/3 | 3.96 |
  | 1/2 | 3.39 |
  | 1 | 2.98 |
- 当 **Cross-sectional geometry** 为 `Elliptical` 时，模块使用具有线性插值和最近外推的查找表从表格数据计算努塞尔数。

  | bminamaj | Nusselt number |
  | --- | --- |
  | 1/16 | 3.65 |
  | 1/8 | 3.72 |
  | 1/4 | 3.79 |
  | 1/2 | 3.74 |
  | 1 | 3.66 |
- 当 **Cross-sectional geometry** 为 `Isosceles triangular` 时，模块使用具有线性插值和最近外推的查找表从表格数据计算努塞尔数。

  | θ | Nusselt number |
  | --- | --- |
  | 10π/180 | 1.61 |
  | 30π/180 | 2.26 |
  | 60π/180 | 2.47 |
  | 90π/180 | 2.34 |
  | 120π/180 | 2.00 |
- 当 **Cross-sectional geometry** 为 `Custom` 时，努塞尔数是 **Nusselt number for laminar flow heat transfer** 参数的值。

当 **Heat transfer parameterization** 设置为 `Dittus-Boelter correlation` 且流动为湍流时，平均努塞尔数计算为：

Nu=aRebPrc,

其中：

- *a* 是 **Coefficient a** 参数的值。
- *b* 是 **Exponent b** 参数的值。
- *c* 是 **Exponent c** 参数的值。

模块默认的 Dittus-Boelter 关联式为：

Nu=0.023Re0.8Pr0.4.

当流动为层流时，努塞尔数取决于 **Cross-sectional geometry** 参数。

**通过表格数据参数化**

当 **Heat transfer parameterization** 参数设置为 `Tabulated data - Colburn factor vs. Reynolds number` 时，平均努塞尔数计算为：

Nu=JM(Re)RePr1/3.

其中 *J*M 是 Colburn-Chilton 因子。

当 **Heat transfer parameterization** 参数设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number` 时，努塞尔数从平均努塞尔数作为平均雷诺数和平均普朗特数的函数的三维数组中插值得到：

Nu=Nu(Re,Pr).

当 **Heat transfer parameterization** 参数设置为 `Nominal temperature difference vs. nominal mass flow rate` 且流动为湍流时，传热系数计算为：

h=hNDN1.8m˙N0.8m˙Avg0.8D1.8,

其中：

- m˙N 是 **Nominal mass flow rate** 参数的值。
- m˙Avg 是平均质量流量：

  m˙Avg=m˙A−m˙B2.
- *h*N 是标称传热系数，其计算为：

  hN=m˙Ncp,NSH,Nln(TH,N−TIn, NTH,N−TOut,N),

  其中：

  - *SH,N* 是标称壁表面积。
  - *TH,N* 是 **Nominal wall temperature** 参数的值。
  - *TIn,N* 是 **Nominal inflow temperature** 参数的值。
  - *TOut,N* 是 **Nominal outflow temperature** 参数的值。

该关系基于努塞尔数与雷诺数成正比的假设：

hDk∝(m˙DSμ)0.8.

如果管壁为刚性，则传热系数的表达式变为：

h=hNm˙N0.8m˙Avg0.8.

### Pipe Effects

该模块允许您包含动态可压缩性和流体惯性效应。开启这些效应中的每一个都可以提高模型保真度，但代价是方程复杂性增加以及潜在的仿真成本增加：

- 当您禁用动态可压缩性时，假设液体在管道体积中停留的时间可以忽略不计。因此，管道中不存在质量积聚，质量流入等于质量流出。这是最简单的选项。当管道中的液体质量占系统总液体质量的比例可以忽略不计时，该选项是合适的。
- 当您启用动态可压缩性时，质量流入和质量流出的不平衡会导致液体在管道中积聚或减少。因此，管道体积中的压力可以动态上升和下降，这为系统提供了一定的顺应性，并调节快速压力变化。这是默认选项。
- 如果启用了动态可压缩性，您还可以开启流体惯性。除了由于摩擦产生的阻力之外，该效应还会导致额外的流动阻力。该额外阻力与质量流量的变化率成正比。考虑流体惯性会减慢流量的快速变化，但也可能导致流量超调并振荡。该选项适用于非常长的管道。开启流体惯性并将多个管段串联连接，以对压力波沿管道的传播进行建模，例如水锤现象。

### Pressure Loss Due to Friction

**Haaland Correlation**

解析 Haaland 关联式通过*总等效长度*或*局部损失系数*来模拟由于壁面摩擦造成的损失；前者将由于不均匀性造成的阻力视为导致等效损失的附加直管长度，后者直接对管道不均匀性应用损失系数。

当 **Local resistances specification** 参数设置为 `Aggregate equivalent length`，且管道中的流量低于 **Laminar flow upper Reynolds number limit** 时，所有管段上的压力损失为：

Δpf,A=υλ2D2SL+Ladd2m˙A,

Δpf,B=υλ2D2SL+Ladd2m˙B,

其中：

- *ν* 是流体运动黏度。
- *λ* 是 **Laminar friction constant for Darcy friction factor** 参数的值；当 **Cross-sectional geometry** 参数为 `Custom` 时，您可以定义该值，否则该值等于 64。
- *D* 是管道水力直径。
- *L*add 是 **Aggregate equivalent length of local resistances** 参数的值。
- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

当雷诺数大于 **Turbulent flow lower Reynolds number limit** 时，管道中的压力损失为：

Δpf,A=f2ρIDS2L+Ladd2m˙A|m˙A|,

Δpf,B=f2ρIDS2L+Ladd2m˙B|m˙B|,

其中：

- *f* 是 Darcy 摩擦因子。它由经验 Haaland 方程近似，并基于 **Surface roughness specification**、*ε* 和管道水力直径：

  f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

  黄铜、铅、铜、塑料、钢、熟铁以及镀锌钢或铁的管道粗糙度作为 ASHRAE 标准值提供。您也可以使用 `Custom` 设置提供自己的 **Internal surface absolute roughness**。
- *ρ*I 是内部流体密度。

当 **Local resistances specification** 参数设置为 `Local loss coefficient`，且管道中的流量低于 **Laminar flow upper Reynolds number limit** 时，所有管段上的压力损失为：

Δpf,A=υλ2D2SL2m˙A.

Δpf,B=υλ2D2SL2m˙B.

当雷诺数大于 **Turbulent flow lower Reynolds number limit** 时，管道中的压力损失为：

Δpf,A=(fL2D+Closs,total)12ρIS2m˙A|m˙A|,

Δpf,B=(fL2D+Closs,total)12ρIS2m˙B|m˙B|,

其中 *C*loss,total 是损失系数，可在 **Total local loss coefficient** 参数中定义为单个系数或沿管道的所有损失系数之和。

**Nominal Pressure Drop vs. Nominal Mass Flow Rate**

Nominal Pressure Drop vs. Nominal Mass Flow Rate 参数化使用刚性或柔性壁面的损失系数来表征损失。当流体不可压缩时，由于壁面摩擦造成的整个管道上的压力损失为：

Δpf,A=Kpm˙Am˙A2+m˙th2,

其中 *K*p 为：

Kp=ΔpNm˙N2,

其中：

- *Δp*N 是 **Nominal pressure drop**，可以定义为标量或向量。
- m˙N 是 **Nominal mass flow rate**，可以定义为标量或向量。

当您将 **Nominal pressure drop** 和 **Nominal mass flow rate** 参数作为向量提供时，标量值 *Kp* 由向量元素的最小二乘拟合确定。

**Tabulated Data – Darcy Friction Factor vs. Reynolds Number**

由于黏性摩擦造成的压力损失也可以根据用户提供的 **Darcy friction factor vector** 和 **Reynolds number vector for turbulent Darcy friction factor** 参数表格数据确定。数据点之间采用线性插值。

### Momentum Balance

管道上的压差由管道端口处的压力、管道壁面的摩擦以及由于任何高程变化引起的静水变化导致：

pA−pB=Δpf+ρIgΔz,

其中：

- *pA* 是端口 **A** 处的压力。
- *pB* 是端口 **B** 处的压力。
- *Δpf* 是由于黏性摩擦造成的压差，*Δpf,A+Δpf,B*。
- *g* 是 **Gravitational acceleration** 参数的值或端口 **G** 处的信号。
- *Δz* 是端口 **A** 和端口 **B** 之间的高程差。
- *ρI* 是内部流体密度，在每个管段处测量。如果未对流体动态可压缩性建模，则为：

  pI=pA+pB2.

当未对流体惯性建模时，端口 **A** 与内部节点 I 之间的动量平衡为：

pA−pI=Δpf,A+ρIgΔz2.

当未对流体惯性建模时，端口 **B** 与内部节点 I 之间的动量平衡为：

pB−pI=Δpf,B−ρIgΔz2.

当对流体惯性建模时，端口 **A** 与内部节点 I 之间的动量平衡为：

pA−pI=Δpf,A+ρIgΔz2+m¨ASL2,

其中：

- m¨A 是端口 **A** 处的流体惯性。
- *L* 是 **Pipe length** 参数的值。
- *S* 是 **Nominal cross-sectional area** 参数的值。

当对流体惯性建模时，端口 **B** 与内部节点 I 之间的动量平衡为：

pB−pI=Δpf,B−ρIgΔz2+m¨BSL2,

其中

m¨B 是端口 **B** 处的流体惯性。

### Pipe Discretization

您可以将管道划分为多个管段。如果管道具有多个管段，则会为每个管段计算质量流量、能量流量和动量平衡方程。具有多个管段可以让您在对流体动态可压缩性建模时跟踪诸如流体密度之类的变量变化。

如果您希望捕获应用中的特定现象，例如水锤，请选择能够充分解析瞬态过程的管段数量。以下来自 Nyquist 采样定理的公式提供了将管道离散为最少 *N* 个管段的经验规则：

N=2Lfc,

其中：

- *L* 是 **Pipe length**。
- *f* 是瞬态频率。
- *c* 是声速。

对于某些应用，您可能需要串联连接 Pipe (TL) 模块。例如，您可能需要多个管段来定义沿管道长度的热边界条件。在这种情况下，通过为每个管段使用一个 Pipe (TL) 模块来对管段建模，并使用热端口设置热边界条件。

### 质量平衡

对于刚性管道和不可压缩流体，管道质量守恒方程为：

m˙A+m˙B=0，

其中：

- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

对于柔性管道和不可压缩流体，管道质量守恒方程为：

m˙A+m˙B=ρIV˙，

其中：

- *ρI* 是内部节点 I 处的热液体密度。每个管道段都有一个内部节点。
- V˙ 是管道体积的变形速率。

对于柔性管道和可压缩流体，管道内的质量可以随压力和温度变化。热液体的体积模量和热膨胀系数解释了这种依赖性，管道质量守恒方程为：

m˙A+m˙B=ρIV˙+ρIV(p˙IβI+αIT˙I)，

其中：

- *pI* 是内部节点 I 处的热液体压力。
- T˙I 是内部节点 I 处热液体温度的变化率。
- *βI* 是热液体体积模量。
- *αI* 是液体热膨胀系数。

### 能量平衡

管道在内部节点 I 处的能量积累速率定义为：

E.=ϕA+ϕB+QH−m˙AvggΔz，

其中：

- *ϕA* 是端口 **A** 处的能量流量。
- *ϕB* 是端口 **B** 处的能量流量。
- *QH* 是通过管壁的热传递。

如果流体不可压缩，能量积累速率的表达式为

E˙=ρ0cpIVdTIdt，

其中：

- *cpI* 是模块内部节点处的流体比热。
- *V* 是管道体积。
- *ρ0* 是恒定流体密度。模块根据 **Nominal liquid temperature** 和 **Nominal liquid pressure** 参数计算该值。

如果流体可压缩，能量积累速率的表达式为

E˙=∂(ρIuI)∂p|TdpIdtV+∂(ρIuI)∂T|pdTIdtV，

其中：

∂(ρIuI)∂p|T=(ρIhIβI−TIαI)V∂(ρIuI)∂T|p=(cpI−hIαI)V

并且 *hI* 是模块内部节点处的比焓。

如果流体可压缩且管壁柔性，能量积累速率的表达式为

E˙=∂(ρIuI)∂p|TdpIdtV+∂(ρIuI)∂T|pdTIdtV+ρIhIdVdt。
