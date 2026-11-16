---
type: simulink-block
title: 'Pipe (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Pipes and Fittings'
documentation_page: 'pipetl'
documentation_source_path: 'ref/pipetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (TL)

## 端口

### 输入

### **EL** — 端口高程差，m 物理信号

端口 **A** 与 **B** 之间的可变高程差，指定为物理信号。该模块将 **EL** 处的信号值限制在 *-L* 与 *L* 之间，其中 *L* 是 **管道长度** 参数的值。

#### 依赖关系

要启用此端口，请将 **高程增益指定** 设置为 `Variable`。

### **G** — 重力加速度，m/s^2 物理信号

可变重力加速度，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **重力加速度指定** 设置为 `Variable`。

### 守恒

### **A** — 管道开口热液体

管道的液体入口或出口端口。

### **B** — 管道开口热液体

管道的液体入口或出口端口。

### **H** — 管壁热

管壁温度。

## 参数

### 配置

### **启用动态可压缩性** — 是否对流体动态可压缩性建模 `on` (默认) | `off`

是否对由流体可压缩性引起的任何流体密度变化进行建模。当您选择 **流体可压缩性** 时，除了因压力变化引起的密度变化外，还会计算因进入模块的质量流量引起的变化。

### **启用流体惯性** — 是否对流体加速度建模 `off` (默认) | `on`

是否考虑由流体质量引起的质量流量中的加速度。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

### **段数** — 管道离散化 `1` (默认) | 正的无量纲标量

管道分段数。每个分段表示一个单独的段，压力根据管道入口压力、流体可压缩性和管壁柔度（如果适用）在该段上计算。每个段中的流体体积保持固定。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

### **管道总长度** — 总管道长度 `5` `m` (默认) | 以长度为单位的正标量

所有管道段的总管道长度。

### **横截面几何形状** — 管道几何形状 `Circular` (默认) | `Annular` | `Rectangular` | `Elliptical` | `Isosceles triangular` | `Custom`

管道横截面几何形状。根据横截面几何形状计算标称水力直径和标称横截面积。

### **管道直径** — 管道直径 `0.1 m` (默认) | 正标量

圆形横截面管道的直径。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Circular`。

### **管道内径** — 管道内径 `0.05 m` (默认) | 正标量

环形管道流动或两个同心管道之间流动的内径。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Annular`。

### **管道外径** — 管道外径 `0.1 m` (默认) | 正标量

环形管道流动或两个同心管道之间流动的外径。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Annular`。

### **管道宽度** — 矩形管道宽度 `0.1 m` (默认) | 正标量

矩形管道的宽度。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Rectangular`。

### **管道高度** — 矩形管道高度 `0.1 m` (默认) | 正标量

矩形管道的高度。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Rectangular`。

### **管道长轴** — 椭圆形管道长轴 `0.1 m` (默认) | 正标量

椭圆形管道的长轴。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Elliptical`。

### **管道短轴** — 椭圆形管道短轴 `0.05 m` (默认) | 正标量

椭圆形管道的短轴。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Elliptical`。

### **管道边长** — 三角形管道边长 `0.1 m` (默认) | 正标量

等腰三角形管道两条相等边的长度。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Isosceles triangular`。

### **管道顶角** — 三角形管道顶角 `30 deg` (默认) | 正标量

三角形管道的顶角。该值必须小于 180 度。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Isosceles triangular`。

### **横截面积** — 无变形时的管道横截面积 `0.01` `m^2` (默认) | 正标量

无变形管道的横截面积。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Custom`。

### **水力直径** — 非圆形管道的有效直径 `0.1128` `m` (默认) | 以长度为单位的正标量

用于传热、动量平衡和管道柔度方程的有效直径。对于非圆形管道，水力直径是管道中流体的有效直径。对于圆形管道，水力直径和管道直径相同。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 清除 **启用动态可压缩性** 复选框，并将 **横截面几何形状** 设置为 `Custom`。
- 选择 **启用动态可压缩性**，将 **管壁指定** 参数设置为 `Rigid`，并将 **横截面几何形状** 设置为 `Custom`。

### **高程增益指定** — 设置管道高程属性 `Constant` (默认) | `Variable`

将管道高程设置为 `Constant` 或 `Variable`。选择 `Variable` 会显示物理信号端口 **EL**。

### **从端口 A 到端口 B 的高程增益** — 从端口 A 到端口 B 的高程变化 `0 m` (默认) | 以长度为单位的正标量

恒定高程管道的高程差。

#### 依赖关系

要启用此参数，请将 **高程增益指定** 设置为 `Constant`。

### **重力加速度指定** — 加速度指定 `Constant` (默认) | `Variable`

重力加速度是恒定的还是可变的。

### **重力加速度** — 管道平均高程处的重力加速度 `9.81` `m/s^2` (默认) | 标量

管道平均高程处的重力加速度常数。

#### 依赖关系

要启用此参数，请将 **重力加速度指定** 设置为 `Constant`。

### 黏性摩擦

### **黏性摩擦参数化** — 摩擦模型 `Haaland correlation` (默认) | `Nominal pressure drop vs. nominal mass flow rate` | `Tabulated data - Darcy friction factor vs. Reynolds number`

由壁面摩擦引起的压力损失的参数化。提供解析公式和表格公式。

### **局部阻力指定** — 在 Haaland 关联式中量化压力损失的方法 `Aggregate equivalent length` (默认) | `Local loss coefficient`

量化由管道非均匀性引起的压力损失的方法。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Haaland correlation`。

### **总局部损失系数** — 定义管道上的损失系数 `0.1` (默认) | 正标量

与每个管道非均匀性相关的损失系数。您可以输入单个损失系数或沿管道的所有损失系数之和。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Haaland correlation`，并将 **局部阻力指定** 设置为 `Local loss coefficient`。

### **局部阻力的总等效长度** — 以长度表示的管道局部压力损失 `1` `m` (默认) | 正标量

与具有弯头、面积变化或其他非均匀性的管道产生等效水力损失所需的管道长度。管道的有效长度是 **管道长度** 与 **局部阻力的总等效长度** 之和。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Haaland correlation`，并将 **局部阻力指定** 设置为 `Aggregate equivalent length`。

### **表面粗糙度指定** — 用于粗糙度指定的管道材料 `Commercially smooth brass, lead, copper, or plastic pipe: 1.52 um` (默认) | `Steel and wrought iron : 46 um` | `Galvanized iron or steel : 152 um` | `Cast iron : 259 um` | `Custom`

基于管道材料的绝对表面粗糙度。提供的值是 ASHRAE 标准粗糙度值。您也可以通过将 **表面粗糙度指定** 设置为 `Custom` 来输入自己的值。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Haaland correlation`。

### **内表面绝对粗糙度** — 管壁绝对粗糙度 `1.5e-5` `m` (默认) | 以长度为单位的正标量

管壁绝对粗糙度。此参数用于确定 Darcy 摩擦因子，该因子会影响管道中的压力损失。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Haaland correlation`，并将 **表面粗糙度指定** 设置为 `Custom`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流的摩擦常数 `64` (默认) | 正标量

层流的摩擦常数。Darcy 摩擦因子在压力损失计算中体现壁面摩擦的贡献。如果 **横截面几何形状** 未设置为 `Custom`，则此参数在内部设置为 64。

#### 依赖关系

要启用此参数，请将 **横截面几何形状** 设置为 `Custom`。

### **层流上限 Reynolds 数** — 低于该值时流动为层流的 Reynolds 数 `2e+3` (默认) | 正标量

低于该值时流动为层流的 Reynolds 数。高于此阈值，流动转变为湍流，并在 **湍流下限 Reynolds 数** 设置处达到湍流状态。

### **湍流下限 Reynolds 数** — 高于该值时流动为湍流的 Reynolds 数 `4e+3` (默认) | 正标量

高于该值时流动为湍流的 Reynolds 数。低于此阈值，流动逐渐转变为层流，并在 **层流上限 Reynolds 数** 设置处达到层流状态。

### **标称质量流量** — 管道质量流量 `[0.1 1]` `kg/s` (默认) | 以质量/时间为单位的数字标量或向量

用于计算压力损失系数的管道标称质量流量，指定为标量或向量。所有标称值必须大于 0，并且元素数量与 **标称压降** 参数相同。当此参数以向量形式提供时，标量值 *K*p 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **标称压降** — 管道上的压降 `[0.001 0.01]` `MPa` (默认) | 以压力为单位的数字标量或向量

用于计算压力损失系数的管道标称压降，指定为标量或向量。所有标称值必须大于 0，并且元素数量与 **标称质量流量** 参数相同。当此参数以向量形式提供时，标量值 *K*p 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **流动反向的质量流量阈值** — 低于该值时应用数值平滑的阈值 `1e-6` `kg/s` (默认) | 以质量/时间为单位的正标量

反向流动的质量流量阈值。在质量流量阈值的正值和负值之间围绕 0 kg/s 定义了一个过渡区域。在该过渡区域内，对流动响应应用数值平滑。阈值必须大于 0。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Nominal pressure drop vs. nominal mass flow rate`。

### **湍流 Darcy 摩擦因子的 Reynolds 数向量** — 用于表格化 Darcy 摩擦因子的 Reynolds 数 `[ 400 1000 1.5e+3 3e+3 4e+3 6e+3 1e+4 2e+4 4e+4 6e+4 1e+5 1e+8 ]` (默认) | 正数向量

用于 Darcy 摩擦因子表格参数化的 Reynolds 数向量。向量元素与 **Darcy 摩擦因子向量** 参数构成独立轴。向量元素必须按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy 摩擦因子向量** — 在表格化 Reynolds 数处的 Darcy 摩擦因子 `[ 0.264 0.112 0.07099999999999999 0.0417 0.0387 0.0268 0.025 0.0232 0.0226 0.022 0.0214 0.0214 ]` (默认) | 正数向量

用于 Darcy 摩擦因子表格参数化的 Darcy 摩擦因子向量。向量元素必须与 **湍流 Darcy 摩擦因子的 Reynolds 数向量** 参数中的元素一一对应，并且必须唯一且大于或等于 0。

#### 依赖关系

要启用此参数，请将 **黏性摩擦参数化** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### 管壁

### **管壁指定** — 管壁柔度 `Rigid` (默认) | `Flexible`

管道的管壁柔度。此参数与管道横截面几何形状无关。`Flexible` 设置保持初始管道形状，并对横截面积应用均匀膨胀。在高变形下，`Flexible` 设置对于非圆形横截面几何形状可能不准确。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

### **体积膨胀指定** — 线性膨胀关联 `Cross-sectional area vs. pressure` (默认) | `Cross-sectional area vs. pressure - Tabulated` | `Hydraulic diameter vs. pressure` | `Based on material properties`

线性膨胀关联。这些设置将新的横截面积或水力直径与管道压力关联起来。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**，并将 **管壁指定** 设置为 `Flexible`。

### **静态表压到横截面积的增益** — 面积相关管道变形的系数 `1e-6 m^2/MPa` (默认) | 正标量

用于计算管道变形的系数。该模块将此参数的值乘以段压力与大气压力之间的压力差。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**，将 **管壁指定** 设置为 `Flexible`，并将 **体积膨胀指定** 设置为 `Cross-sectional area vs. pressure`。

### **静态表压向量** — 表压向量 `[.1,1] MPa` (默认) | 向量

包含表压的向量。该模块在表查找中使用此向量来计算管道横截面积。向量项必须严格为正且单调递增，并且向量的长度必须与 **横截面积增益向量** 参数相同。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**，将 **管壁指定** 设置为 `Flexible`，并将 **体积膨胀指定** 设置为 `Cross-sectional area vs. pressure - Tabulated`。

### **横截面积增益向量** — 管道横截面积向量 `[1e-05, 1.1e-05] m^2` (default) | vector

向量，包含管道横截面积。模块使用此向量进行查表，以计算其他压力下的管道横截面积。向量元素必须严格为正且单调递增，并且该向量长度必须与 **静态表压向量** 参数相同。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，并将 **体积膨胀规格** 设置为 `Cross-sectional area vs. pressure - Tabulated`。

### **静态表压到水力直径增益** — 直径相关管道变形的系数 `1e-6 m/MPa` (default) | positive scalar

用于计算管道变形的系数。模块将此参数的值乘以段压力与大气压力之间的压差。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，并将 **体积膨胀规格** 设置为 `Hydraulic diameter vs. pressure`。

### **材料行为** — 指定材料行为的方法 `Linear Elastic` (default) | `Multilinear Elastic`

模块用于计算材料行为的方法。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，并将 **体积膨胀规格** 设置为 `Based on material properties`。

### **管壁厚度** — 管壁宽度 `0.05 m` (default) | positive scalar

管壁厚度。模块使用此值计算应力。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，并将 **体积膨胀规格** 设置为 `Based on material properties`。

### **杨氏模量** — 管壁材料的杨氏模量 `69 GPa` (default) | positive scalar

构成管壁的材料的杨氏模量。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，将 **体积膨胀规格** 设置为 `Based on material properties`，并将 **材料行为** 设置为 `Linear Elastic`。

### **泊松比** — 管壁材料的泊松比 `0.33` (default) | positive scalar

构成管壁的材料的泊松比。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，并将 **体积膨胀规格** 设置为 `Based on material properties`。

### **应力向量** — 管壁材料的应力向量 `[276, 310] MPa` (default) | vector

包含构成管壁的材料的应力值的向量。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，将 **体积膨胀规格** 设置为 `Based on material properties`，并将 **材料行为** 设置为 `Multilinear Elastic`。

### **应变向量** — 管壁材料的应变向量 `[.004, .02]` (default) | vector

包含构成管壁的材料的应变值的向量。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，将 **体积膨胀规格** 设置为 `Based on material properties`，并将 **材料行为** 设置为 `Multilinear Elastic`。

### **检查应力是否超过指定的允许水平** — 当应力高于指定的最大值时的通知 `None` (default) | `Warning` | `Error`

当应力高于 **最大许用应力** 参数指定的最大应力时，模块是不执行任何操作、生成警告还是生成错误。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，将 **体积膨胀规格** 设置为 `Based on material properties`，并将 **材料行为** 设置为 `Multilinear Elastic`。

### **最大许用应力** — 管壁上允许的最大应力 `400 MPa` (default) | positive scalar

模块在管壁上允许的最大应力。使用 **检查应力是否超过指定的允许水平** 参数控制当应力超过此值时模块的行为。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，将 **体积膨胀规格** 设置为 `Based on material properties`，将 **材料行为** 设置为 `Multilinear Elastic`，并将 **检查应力是否超过指定的允许水平** 设置为 `Warning` 或 `Error`。

### **体积膨胀时间常数** — 管道变形时间常数 `0.01 s` (default) | positive scalar

管道变形后壁面达到稳态所需的时间。此参数影响管道体积的动态变化。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，并将 **管壁规格** 设置为 `Flexible`。

### **管道热膨胀** — 是否对热膨胀建模 `off` (default) | `on`

是否考虑由温度变化引起的管道膨胀。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，并将 **管壁规格** 设置为 `Flexible`。

### **热膨胀系数** — 管道热膨胀系数 `24 um/(deltaK*m)` (default) | positive scalar

管道材料的线性热膨胀系数。此值是在恒定压力下，温度每变化一度时尺寸的分数变化。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，并选中 **管道热膨胀**。

### **热膨胀参考温度** — 管道热膨胀的参考温度 `293.15 K` (default) | positive scalar

模块在计算管道热膨胀时使用的参考温度。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**，将 **管壁规格** 设置为 `Flexible`，并选中 **管道热膨胀**。

### 传热

### **传热参数化** — 用于捕获与管壁的对流传热的方法 `Gnielinski correlation``Nominal temperature differential vs. nominal mass flow rate` (default) | `Dittus-Boelter correlation` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`

计算流体与管壁之间传热系数的方法。可使用解析和表格数据参数化。

### **层流流动传热的努塞尔数** — 用于层流流动传热计算的努塞尔数 `3.66` (default)

层流流态下对流传热与导热传热的比率。流体努塞尔数影响传热速率。

#### 依赖关系

要启用此参数，请将 **横截面几何** 设置为 `Custom`，并将 **传热参数化** 设置为以下之一：

- `Gnielinski correlation`。
- `Nominal temperature differential vs. nominal mass flow rate`。
- `Dittus-Boelter correlation`。

### **标称质量流量** — 管道质量流量 `[0.1 1]` `kg/s` (default) | scalar or vector of numbers in units of mass/time

用于计算传热系数的管道标称质量流量，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **标称流入温度** 参数相同。当此参数以向量形式提供时，标量值 *h*p 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **标称流入温度** — 管道入口温度 `[293.15 293.15]` `K` (default) | scalar or vector of numbers in units of temperature

用于计算传热系数的标称流体入口温度，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **标称质量流量** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **标称流出温度** — 管道出口温度 `[300 300]` `K` (default) | scalar or vector of numbers in units of temperature

用于计算传热系数的标称流体出口温度，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **标称质量流量** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **标称流入压力** — 管道入口压力 `[0.101325 0.101325]` `MPa` (default) | scalar or vector of numbers in units of pressure

用于计算传热系数的标称流体入口压力，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **标称质量流量** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **标称壁温** — 管道壁温 `[303.15 303.15]` `K` (default) | scalar or vector of numbers in units of temperature

用于计算传热系数的管道壁温，指定为标量或向量。所有标称值必须大于 0，并且元素数量必须与 **标称质量流量** 参数相同。当此参数以向量形式提供时，标量值 *h* 由向量元素的最小二乘拟合确定。

#### 依赖关系

要启用此温度，请将 **传热参数化** 设置为 `Nominal temperature differential vs. nominal mass flow rate`。

### **系数 a** — Dittus-Boelter 关联式的经验常数 *a* `0.023` (default) | positive scalar

用于 Dittus-Boelter 关联式的经验常数 *a*。该关联式将湍流流动中的努塞尔数与传热系数关联起来。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Dittus-Boelter correlation`。

### **指数 b** — Dittus-Boelter 关联式的经验常数 *b* `0.8` (default) | positive scalar

用于 Dittus-Boelter 关联式的经验常数 *b*。该关联式将湍流流动中的努塞尔数与传热系数关联起来。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Dittus-Boelter correlation`。

### **指数 c** — Dittus-Boelter 关联式的经验常数 *c* `0.4` (default) | positive scalar

用于 Dittus-Boelter 关联式的经验常数 *c*。该关联式将湍流流动中的努塞尔数与传热系数关联起来。默认值反映向流体的传热。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Dittus-Boelter correlation`。

### **用于 Colburn 因子的雷诺数向量** — 用于将 Colburn 因子制成表格的雷诺数 `[100 150 1000]` (default) | vector of positive numbers

用于 Colburn 因子表格参数化的雷诺数向量。向量元素与 **Colburn 因子向量** 参数构成一个独立轴。向量元素必须按升序列出，并且必须大于 0。此参数的元素数量必须与 **Colburn 因子向量** 相同。对于反向流动，或从 **B** 到 **A** 的流动，同一数据以相反方向应用。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn 因子向量** — 在制成表格的雷诺数处的 Colburn 因子 `[0.019 0.013 0.002]` (default) | vector of positive numbers

用于 Colburn 因子表格参数化的 Colburn 因子向量。向量元素与 **用于 Colburn 因子的雷诺数向量** 参数构成一个独立轴。此参数的元素数量必须与 **用于 Colburn 因子的雷诺数向量** 相同。

#### 依赖关系

当 **传热参数化** 模块参数设置为 `Tabulated data - Colburn factor vs. Reynolds number` 时，此参数处于活动状态。

### **用于努塞尔数的雷诺数向量** — 用于将努塞尔数制成表格的雷诺数 `[100 150 100]` (default) | vector of positive numbers

用于努塞尔数表格参数化的雷诺数向量。对于二维因变量 **努塞尔数表**，此向量与 **用于努塞尔数的普朗特数向量** 参数构成一个独立轴。向量元素必须按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`。

### **用于努塞尔数的普朗特数向量** — 用于将努塞尔数制成表格的普朗特数 `[1 10]` (default) | vector of positive numbers

用于努塞尔数表格参数化的普朗特数向量。对于二维因变量 **努塞尔数表**，此向量与 **用于努塞尔数的雷诺数向量** 参数构成一个独立轴。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`。

### **努塞尔数表** — 在制成表格的雷诺数和普朗特数处的努塞尔数 `[ 3.72 4.21; 3.75 4.44; 4.21 7.15 ]` (default) | matrix of positive numbers

在指定的雷诺数和普朗特数处的 *M* × *N* 努塞尔数矩阵。表元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **用于努塞尔数的雷诺数向量** 参数中的向量元素数量。
- *N* 是 **用于努塞尔数的普朗特数向量** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请将 **传热参数化** 设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number`。

### 初始条件

### **初始液体温度** — 仿真开始时的液体温度 `293.15` `K` (default)

仿真开始时的液体温度。

### **初始液体压力** — 仿真开始时的管道压力 `0.101325 MPa` (default) | positive scalar

仿真开始时的管道压力。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性**。

### **标称液体温度** — 标称操作条件下的温度 `293.15 K` (default) | scalar

标称操作条件下的液体温度。当动态可压缩性被禁用时，该模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **标称液体压力** — 标称操作条件下的压力 `0.101325 MPa` (default) | scalar

标称操作条件下的液体压力。当动态可压缩性被禁用时，该模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

## 所属库

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：对柔性管壁或可变重力加速度建模

将 **管壁规格** 参数设为 `Flexible`，以对柔性管壁建模。此参数化还考虑由温度变化引起的管壁变形。

将 **重力加速度规格** 参数设为 `Variable`，以启用端口 **G** 并将重力加速度作为物理信号提供。

### R2023b：对长度短于高程增益的管道建模

现在，当 **高程增益规格** 为 `Constant` 时，您可以对长度短于高程变化的管道建模。如果 **从端口 A 到端口 B 的高程增益** 参数的值大于 **管长** 参数的值，该模块会发出警告而不是错误。

### R2023a：对管道特性建模

现在，您可以使用 Pipe (TL) 模块的新参数来控制管道属性。使用 **横截面几何形状** 参数指定管道横截面形状。使用 **表面粗糙度规格** 参数来使用管壁材料确定表面粗糙度。

## 描述

在热液体组件之间输送流体的封闭管道

Pipe (TL) 模块表示通过管道的热液体流动。该模块根据端口之间的差异、管道高程以及端口 **H** 处的任何额外热传递，求出沿管道的温度。

管道在端口 **A** 和 **B** 之间可以具有恒定或变化的高程。对于恒定高程差，请使用 **从端口 A 到端口 B 的高程增益** 参数。您可以通过将 **高程增益规格** 设为 `Variable` 来指定可变高程。这会公开物理信号端口 **EL**。

您可以选择包括流体动态可压缩性、惯性和管壁柔性的影响。当模块包括这些现象时，它会针对您指定的每个管道段数计算流动属性。

### 管道几何形状

使用 **横截面几何形状** 参数指定管道的形状。

**圆形**

标称水力直径 *DN* 和管道直径 *dcircle* 均等于 **管道直径** 参数的值。管道横截面积为 SN=π4dcircle2。

**环形**

标称水力直径是 **管道外径** 和 **管道内径** 参数之差 *DN* = *douter* – *dinner*。管道横截面积为 SN=π4(douter2−dinner2)。

**矩形**

标称水力直径为

DN=2hwh+w，

其中：

- *h* 是 **管道高度** 参数的值。
- *w* 是 **管道宽度** 参数的值。

管道横截面积为 SN=wh。

**椭圆形**

标称水力直径为

DN=2amajbmin(64-16(amaj-bminamaj+bmin)2)(amaj+bmin)(64-3(amaj-bminamaj+bmin)4)，

其中：

- *amaj* 是 **管道长轴** 参数的值。
- *bmin* 是 **管道短轴** 参数的值。

管道横截面积为 SN=π4amajbmin。

**等腰三角形**

标称水力直径为

DN=lsidesin(θ)1+sin(θ2)，

其中：

- *lside* 是 **管道边长** 参数的值。
- *θ* 是 **管道顶点角** 参数的值。

管道横截面积为 SN=lside22sin(θ)。

**自定义**

当 **横截面几何形状** 参数为 `Custom` 时，您可以使用 **横截面面积** 参数指定管道横截面面积。标称水力直径是 **水力直径** 参数的值。

### 管道柔性

您可以为所有横截面几何形状对柔性管壁建模。当将 **管壁规格** 设为 `Flexible` 时，该模块假设沿所有方向均匀膨胀，并保持定义的横截面形状。对于非圆形横截面积在承受相对于大气压力的高压时，此设置可能不会得出物理结果。对柔性管壁建模时，您可以使用 **体积膨胀规格** 参数指定管道横截面积的体积膨胀。

当 **体积膨胀规格** 参数为 `Cross-sectional area vs. pressure` 时，体积变化为

V˙=L(A−Sτ)，

其中：

- A=SN+Kps(p−patm)。
- *L* 是 **管长** 参数。
- *SN* 是为每种形状定义的标称管道横截面积。
- *S* 是当前管道横截面积。
- *p* 是管道内部压力。
- *patm* 是大气压力。
- *Kps* 是 **静态表压到横截面面积增益** 参数。
  为计算 *Kps*，假设薄壁、开口圆柱管道发生均匀弹性变形，使用
  Kps=ΔDΔp=πDN34tE，
  其中 *t* 是管壁厚度，*E* 是杨氏模量。
- *τ* 是 **体积膨胀时间常数**。

当 **体积膨胀规格** 参数为 `Cross-sectional area vs. pressure - Tabulated` 时，该模块对 V˙ 使用与 `Cross-sectional area vs. pressure` 设置相同的方程。该模块使用表查找函数计算 *A*

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear)，

其中 *pps* 是 **静态表压向量** 参数，*Aps* 是 **横截面面积增益向量** 参数。

当 **体积膨胀规格** 参数为 `Hydraulic diameter vs. pressure` 时，体积变化为

V˙=π2DL(Dstatic−Dτ)，

其中：

- Dstatic=DN+Kpd(p−patm)。
- *DN* 是为每种形状定义的标称水力直径。
- *D* 是当前管道水力直径。
- *Kpd* 是 **静态表压到水力直径增益** 参数。为计算 *Kps*，假设薄壁、开口圆柱管道发生均匀弹性变形，使用
  Kpd=ΔDΔp=DN22tE。

当 **体积膨胀规格** 参数为 `Based on material properties` 时，该模块对 V˙ 使用与 `Hydraulic diameter vs. pressure` 设置相同的方程，但根据 **材料行为** 参数的值计算 *Dstatic*

Dstatic=DN(1+ϵhoop)。

此参数化假设为圆柱薄壁压力容器，其中 σradial=0。

当 **材料行为** 参数为 `Linear elastic` 时，

ϵhoop=1E[σhoop−vσlongitudinal]，

其中：

- *E* 是 **杨氏模量** 参数的值。
- *v* 是 **泊松比** 参数的值。
- σhoop=pD2t，其中 *t* 是 **管壁厚度** 参数的值。
- σlongitudinal=pD4t。

当 **材料行为** 参数为 `Multilinear elastic` 时，该模块计算 von Mises 应力 *σv*，其简化为 σv=34pD2t，以确定等效应变。环向应变为

ϵhoop=ϵhoopelastic+ϵhoopplastic

ϵhoopelastic=1E[σhoop−vσlongitudinal]ϵhoopi,jplastic=32(1Es−1E)Si,j

其中：

- 该模块根据 **应力向量** 和 **应变向量** 参数的第一个元素计算杨氏模量 *E*。
- ES=σtotalϵtotal，其中 *σtotal* 和 *εtotal* 分别是等效总应力和等效总应变。该模块根据 von Mises 应力和应力-应变曲线计算等效总应变。
- Si,j=σi,j−[σhoop+σlongitudinal+σradial3]δi,j，其中 *σi,j* 是 Cauchy 应力张量的元素。

如果不对柔性管壁建模，则 *SN* = *S* 且 *DN* = *D*。

**管壁热膨胀**

如果您选择 **管道热膨胀**，该模块使用以下假设对管壁热膨胀建模：

- 管道材料是各向同性的。
- 管道的 Biot 数小于 0.1，并且可以使用集总热容对管道建模。
- 温度变化和管道变形足够小，因此面积膨胀的一阶近似是准确的。

当 **材料行为** 参数为 `Cross-sectional area vs. pressure`、`Cross-sectional area vs. pressure - Tabulated` 或 `Hydraulic diameter vs. pressure` 并且您选择 **管道热膨胀** 时，该模块在计算面积或直径时添加热膨胀项。

当 **材料行为** 为 `Cross-sectional area vs. pressure` 时，

A=SN+Kps(p−patm)+SN2αΔT，

其中：

- *ɑ* 是 **热膨胀系数** 参数的值。
- ΔT=TI−Tref。
- *TI* 是模块内部节点处的流体温度。
- *Tref* 是 **热膨胀参考温度** 参数的值。

当 **材料行为** 为 `Cross-sectional area vs. pressure - Tabulated` 时，

A=SN+tablelookup(pps,Aps,(p−patm),interpolation=linear,extrapolation=linear)+SN2αΔT。

当 **材料行为** 为 `Hydraulic diameter vs. pressure` 时，

Dstatic=DN+Kpd(p−patm)+DNαΔT。

当 **材料行为** 参数为 `Multilinear elastic` 并且您选择 **管道热膨胀** 时，该模块计算 *Dstatic* 如下

Dstatic=DN(1+ϵhoop+ϵthermal)，

其中 ϵthermal=αΔT。

### 管壁传热

你可以通过多种方式包含向管壁和从管壁的传热。有两种解析模型：`Gnielinski correlation`，它将 Nusselt 数建模为 Reynolds 数和 Prandtl 数的函数，并使用预定义系数；以及 `Dittus-Boelter correlation - Nusselt = a*Re^b*Pr^c`，它将 Nusselt 数建模为 Reynolds 数和 Prandtl 数的函数，并使用用户定义的系数。

`Nominal temperature differential vs. nominal mass flow rate`、`Tabulated data - Colburn factor vs. Reynolds number` 和 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number` 是基于用户提供数据的查找表参数化。

流体与管壁之间的传热通过对流 *QConv* 和传导 *QCond* 发生，其中净热流率 *QH* 为 *QH*=*QConv*+*QCond*。

传导引起的传热为：

QCond=kISHD(TH−TI),

其中：

- *D* 是公称水力直径 *DN*（如果管壁刚性），并且是管道稳态直径 *DS*（如果管壁柔性）。
- *kI* 是热液体的热导率，为每个管道段在内部定义。
- *SH* 是管壁的表面积。
- *TH* 是管壁温度。
- *TI* 是模块内部节点处的流体温度。

对流引起的传热为：

QConv=cp,Avg|m˙Avg|(TH−TIn)[1−exp(−hSHcp,Avg|m˙Avg|)],

其中：

- *c*p, Avg 是流体的平均比热，模块使用查找表计算。
- m˙Avg 是通过管道的平均质量流量。
- *TIn* 是流体入口端口温度。
- *h* 是管道传热系数。

传热系数 *h* 为：

h=NukAvgD,

除非使用 `Nominal temperature differential vs. nominal mass flow rate` 进行参数化，其中 *kAvg* 是热液体在整个管道上的平均热导率，*Nu* 是管道中的平均 Nusselt 数。

**解析参数化**

当 **Heat transfer parameterization** 设置为 `Gnielinski correlation` 且流动为湍流时，平均 Nusselt 数计算为：

Nu=f8(Re−1000)Pr1+12.7( f8)1/2(Pr2/3−1),

其中：

- *f* 是平均 Darcy 摩擦因子，根据 Haaland 关联式：

  f={−1.8log10[6.9Re+(ϵR3.7D)1.11]}-2,

  其中 *εR* 是管道 **Internal surface absolute roughness**。
- *Re* 是 Reynolds 数。
- *Pr* 是 Prandtl 数。

当流动为层流时，来自 [1] 的数据决定 Nusselt 数如何取决于 **Cross-sectional geometry** 参数：

- 当 **Cross-sectional geometry** 为 `Circular` 时，Nusselt 数为 3.66。
- 当 **Cross-sectional geometry** 为 `Annular` 时，模块使用带线性插值和最近外推的查找表从表格数据计算 Nusselt 数。

  | DinnerDouter | Nusselt 数 |
  | --- | --- |
  | 1/20 | 17.46 |
  | 1/10 | 11.56 |
  | 1/4 | 7.37 |
  | 1/2 | 5.74 |
  | 1 | 4.86 |

  模块使用修正因子 F = 0.86(DouterDinner)0.16 调整计算得到的 Nusselt 数。
- 当 **Cross-sectional geometry** 为 `Rectangular` 时，模块使用带线性插值和最近外推的查找表从表格数据计算 Nusselt 数。

  | min(h,w)max(h,w) | Nusselt 数 |
  | --- | --- |
  | 0 | 7.54 |
  | 1/8 | 5.60 |
  | 1/6 | 5.14 |
  | 1/4 | 4.44 |
  | 1/3 | 3.96 |
  | 1/2 | 3.39 |
  | 1 | 2.98 |
- 当 **Cross-sectional geometry** 为 `Elliptical` 时，模块使用带线性插值和最近外推的查找表从表格数据计算 Nusselt 数。

  | bminamaj | Nusselt 数 |
  | --- | --- |
  | 1/16 | 3.65 |
  | 1/8 | 3.72 |
  | 1/4 | 3.79 |
  | 1/2 | 3.74 |
  | 1 | 3.66 |
- 当 **Cross-sectional geometry** 为 `Isosceles triangular` 时，模块使用带线性插值和最近外推的查找表从表格数据计算 Nusselt 数。

  | θ | Nusselt 数 |
  | --- | --- |
  | 10π/180 | 1.61 |
  | 30π/180 | 2.26 |
  | 60π/180 | 2.47 |
  | 90π/180 | 2.34 |
  | 120π/180 | 2.00 |
- 当 **Cross-sectional geometry** 为 `Custom` 时，Nusselt 数是 **Nusselt number for laminar flow heat transfer** 参数的值。

当 **Heat transfer parameterization** 设置为 `Dittus-Boelter correlation` 且流动为湍流时，平均 Nusselt 数计算为：

Nu=aRebPrc,

其中：

- *a* 是 **Coefficient a** 参数的值。
- *b* 是 **Exponent b** 参数的值。
- *c* 是 **Exponent c** 参数的值。

模块默认的 Dittus-Boelter 关联式为：

Nu=0.023Re0.8Pr0.4.

当流动为层流时，Nusselt 数取决于 **Cross-sectional geometry** 参数。

**基于表格数据的参数化**

当 **Heat transfer parameterization** 参数设置为 `Tabulated data - Colburn factor vs. Reynolds number` 时，平均 Nusselt 数计算为：

Nu=JM(Re)RePr1/3.

其中 *J*M 是 Colburn-Chilton 因子。

当 **Heat transfer parameterization** 参数设置为 `Tabulated data - Nusselt number vs. Reynolds number & Prandtl number` 时，Nusselt 数从平均 Nusselt 数的三维数组插值，该数组是平均 Reynolds 数和平均 Prandtl 数的函数：

Nu=Nu(Re,Pr).

当 **Heat transfer parameterization** 参数设置为 `Nominal temperature difference vs. nominal mass flow rate` 且流动为湍流时，传热系数计算为：

h=hNDN1.8m˙N0.8m˙Avg0.8D1.8,

其中：

- m˙N 是 **Nominal mass flow rate** 参数的值。
- m˙Avg 是平均质量流量：

  m˙Avg=m˙A−m˙B2.
- *h*N 是公称传热系数，计算为：

  hN=m˙Ncp,NSH,Nln(TH,N−TIn, NTH,N−TOut,N),

  其中：

  - *SH,N* 是公称壁表面积。
  - *TH,N* 是 **Nominal wall temperature** 参数的值。
  - *TIn,N* 是 **Nominal inflow temperature** 参数的值。
  - *TOut,N* 是 **Nominal outflow temperature** 参数的值。

此关系基于如下假设：Nusselt 数与 Reynolds 数成正比：

hDk∝(m˙DSμ)0.8.

如果管壁刚性，则传热系数的表达式变为：

h=hNm˙N0.8m˙Avg0.8.

### 管道效应

该模块允许你包含动态可压缩性和流体惯性效应。启用每种效应都可以提高模型保真度，代价是方程复杂度增加以及可能的仿真成本增加：

- 当你禁用动态可压缩性时，假定液体在管道容积中停留的时间可忽略。因此，管道中没有质量积累，质量流入等于质量流出。这是最简单的选项。当管道中的液体质量占系统中总液体质量的比例可忽略时，适合使用此选项。
- 当你启用动态可压缩性时，质量流入和质量流出的不平衡可能导致液体在管道中积累或减少。因此，管道容积中的压力可以动态上升和下降，这为系统提供了一定的柔量，并调节快速压力变化。这是默认选项。
- 如果启用动态可压缩性，你还可以开启流体惯性。此效应除摩擦阻力外，还会产生额外的流动阻力。此额外阻力与质量流率的变化率成正比。考虑流体惯性会减慢流率的快速变化，但也可能导致流率过冲和振荡。此选项适用于非常长的管道。开启流体惯性并将多个管道段串联，以对压力波沿管道的传播进行建模，例如水锤现象。

### 摩擦引起的压力损失

**Haaland 关联式**

解析 Haaland 关联式通过 *aggregate equivalent length* 或 *local loss coefficient* 对壁面摩擦引起的损失建模。*aggregate equivalent length* 将非均匀性引起的阻力视为附加的直管长度，从而产生等效损失；*local loss coefficient* 直接为管道非均匀性施加损失系数。

当 **Local resistances specification** 参数设置为 `Aggregate equivalent length` 且管道中的流动低于 **Laminar flow upper Reynolds number limit** 时，所有管道段上的压力损失为：

Δpf,A=υλ2D2SL+Ladd2m˙A,

Δpf,B=υλ2D2SL+Ladd2m˙B,

其中：

- *ν* 是流体运动黏度。
- *λ* 是 **Laminar friction constant for Darcy friction factor** 参数的值；当 **Cross-sectional geometry** 参数为 `Custom` 时可以定义该值，否则等于 64。
- *D* 是管道水力直径。
- *L*add 是 **Aggregate equivalent length of local resistances** 参数的值。
- m˙A 是端口 **A** 处的质量流率。
- m˙B 是端口 **B** 处的质量流率。

当 Reynolds 数大于 **Turbulent flow lower Reynolds number limit** 时，管道中的压力损失为：

Δpf,A=f2ρIDS2L+Ladd2m˙A|m˙A|,

Δpf,B=f2ρIDS2L+Ladd2m˙B|m˙B|,

其中：

- *f* 是 Darcy 摩擦因子。它由经验 Haaland 方程近似，并基于 **Surface roughness specification**、*ε* 和管道水力直径：

  f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

  黄铜、铅、铜、塑料、钢、熟铁以及镀锌钢或铁的管道粗糙度以 ASHRAE 标准值提供。你也可以使用 `Custom` 设置提供自己的 **Internal surface absolute roughness**。
- *ρ*I 是内部流体密度。

当 **Local resistances specification** 参数设置为 `Local loss coefficient` 且管道中的流动低于 **Laminar flow upper Reynolds number limit** 时，所有管道段上的压力损失为：

Δpf,A=υλ2D2SL2m˙A.

Δpf,B=υλ2D2SL2m˙B.

当 Reynolds 数大于 **Turbulent flow lower Reynolds number limit** 时，管道中的压力损失为：

Δpf,A=(fL2D+Closs,total)12ρIS2m˙A|m˙A|,

Δpf,B=(fL2D+Closs,total)12ρIS2m˙B|m˙B|,

其中 *C*loss,total 是损失系数，可在 **Total local loss coefficient** 参数中定义为单个系数或沿管道的所有损失系数之和。

**Nominal Pressure Drop vs. Nominal Mass Flow Rate**

Nominal Pressure Drop vs. Nominal Mass Flow Rate 参数化使用损失系数来表征刚性或柔性壁的损失。当流体不可压缩时，由于壁面摩擦，整个管道上的压力损失为：

Δpf,A=Kpm˙Am˙A2+m˙th2,

其中 *K*p 为：

Kp=ΔpNm˙N2,

其中：

- *Δp*N 是 **Nominal pressure drop**，可以定义为标量或向量。
- m˙N 是 **Nominal mass flow rate**，可以定义为标量或向量。

当你将 **Nominal pressure drop** 和 **Nominal mass flow rate** 参数作为向量提供时，标量值 *Kp* 由向量元素的最小二乘拟合确定。

**表格数据 – Darcy 摩擦因子 vs. Reynolds 数**

粘性摩擦引起的压力损失也可以根据用户提供的 **Darcy friction factor vector** 和 **Reynolds number vector for turbulent Darcy friction factor** 参数的表格数据确定。数据点之间采用线性插值。

### 动量平衡

管道上的压差由管道端口处的压力、管壁处的摩擦以及任何高度变化引起的静水压力变化导致：

pA−pB=Δpf+ρIgΔz,

其中：

- *pA* 是端口 **A** 处的压力。
- *pB* 是端口 **B** 处的压力。
- *Δpf* 是粘性摩擦引起的压差，*Δpf,A+Δpf,B*。
- *g* 是 **Gravitational acceleration** 参数的值或端口 **G** 处的信号。
- *Δz* 是端口 **A** 和端口 **B** 之间的高度差。
- *ρI* 是内部流体密度，在每个管道段处测量。如果未对流体动态可压缩性建模，则其为：

  pI=pA+pB2.

当未对流体惯性建模时，端口 **A** 和内部节点 I 之间的动量平衡为：

pA−pI=Δpf,A+ρIgΔz2.

当未对流体惯性建模时，端口 **B** 和内部节点 I 之间的动量平衡为：

pB−pI=Δpf,B−ρIgΔz2.

当对流体惯性建模时，端口 **A** 和内部节点 I 之间的动量平衡为：

pA−pI=Δpf,A+ρIgΔz2+m¨ASL2,

其中：

- m¨A 是端口 **A** 处的流体惯性。
- *L* 是 **Pipe length** 参数的值。
- *S* 是 **Nominal cross-sectional area** 参数的值。

当对流体惯性建模时，端口 **B** 和内部节点 I 之间的动量平衡为：

pB−pI=Δpf,B−ρIgΔz2+m¨BSL2,

其中

m¨B 是端口 **B** 处的流体惯性。

### 管道离散化

你可以将管道划分为多个段。如果管道有多个段，则对每个段计算质量流、能量流和动量平衡方程。当对流体动态可压缩性建模时，具有多个管道段可以让你跟踪流体密度等变量的变化。

如果你希望捕获应用中的特定现象，例如水锤，请选择能够充分分辨瞬态的分段数。以下公式来自 Nyquist 采样定理，提供了将管道离散化为最少 *N* 段的经验法则：

N=2Lfc,

其中：

- *L* 是 **Pipe length**。
- *f* 是瞬态频率。
- *c* 是声速。

对于某些应用，你可能需要串联连接 Pipe (TL) 模块。例如，你可能需要多个管道段来定义沿管道长度的热边界条件。在这种情况下，通过为每个段使用一个 Pipe (TL) 模块来对管道段建模，并使用热端口设置热边界条件。

### 质量平衡

对于具有不可压缩流体的刚性管道，管道质量守恒方程为：

m˙A+m˙B=0,

其中：

- m˙A 是端口 **A** 处的质量流率。
- m˙B 是端口 **B** 处的质量流率。

对于具有不可压缩流体的柔性管道，管道质量守恒方程为：

m˙A+m˙B=ρIV˙,

其中：

- *ρI* 是内部节点 I 处的热液体密度。每个管道段都有一个内部节点。
- V˙ 是管道体积的变形率。

对于具有可压缩流体的柔性管道，管道内的质量可以随压力和温度变化。热液体的体积模量和热膨胀系数考虑了这种依赖性，管道质量守恒方程为：

m˙A+m˙B=ρIV˙+ρIV(p˙IβI+αIT˙I),

其中：

- *pI* 是内部节点 I 处的热液体压力。
- T˙I 是内部节点 I 处热液体温度的变化率。
- *βI* 是热液体体积模量。
- *αI* 是液体热膨胀系数。

### Energy Balance

管道内部节点 I 处的能量累积速率定义为：

E.=ϕA+ϕB+QH−m˙AvggΔz,

其中：

- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。
- *QH* 是通过管壁的热传递。

如果流体不可压缩，能量累积速率的表达式为

E˙=ρ0cpIVdTIdt,

其中：

- *cpI* 是模块内部节点处的流体比热容。
- *V* 是管道体积。
- *ρ0* 是恒定流体密度。模块根据 **标称液体温度** 和 **标称液体压力** 参数计算该值。

如果流体可压缩，能量累积速率的表达式为

E˙=∂(ρIuI)∂p|TdpIdtV+∂(ρIuI)∂T|pdTIdtV,

其中：

∂(ρIuI)∂p|T=(ρIhIβI−TIαI)V∂(ρIuI)∂T|p=(cpI−hIαI)V

并且 *hI* 是模块内部节点处的比焓。

如果流体可压缩且管壁可变形，能量累积速率的表达式为

E˙=∂(ρIuI)∂p|TdpIdtV+∂(ρIuI)∂T|pdTIdtV+ρIhIdVdt.
