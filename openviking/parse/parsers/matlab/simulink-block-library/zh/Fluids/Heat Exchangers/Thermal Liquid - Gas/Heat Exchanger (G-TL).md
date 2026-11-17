---
type: simulink-block
title: 'Heat Exchanger (G-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Gas'
documentation_page: 'heatexchangergtl'
documentation_source_path: 'ref/heatexchangergtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (G-TL)

## 端口
```yaml
ports:
- name: A1
  summary: 气体端口 gas
  direction: conserving
- name: B1
  summary: 气体端口 gas
  direction: conserving
- name: A2
  summary: 热液体端口 thermal liquid
  direction: conserving
- name: B2
  summary: 热液体端口 thermal liquid
  direction: conserving
```

### 守恒端口

### **A1** — 气体端口 gas

气体进入和离开换热器气体侧的开口。

### **B1** — 气体端口 gas

气体进入和离开换热器气体侧的开口。

### **A2** — 热液体端口 thermal liquid

热液体进入和离开换热器热液体侧的开口。

### **B2** — 热液体端口 thermal liquid

热液体进入和离开换热器热液体侧的开口。
## 参数
```yaml
parameters:
- name: Flow arrangement
  summary: 换热器中流动对齐的方式 Parallel or counter flow（默认）| Shell and tube | Cross flow | Generic - effectiveness table
  group: 通用
- name: Wall thermal resistance
  summary: 壁面通过热传导对热流的阻力 0 K/W（默认）| 正标量
  group: 通用
- name: Number of shell passes
  summary: 流体在离开之前穿过壳体的次数 1（默认）| 无量纲标量
  group: 通用
- name: Cross flow type
  summary: 每个流动通道中的混合条件 Both fluids mixed（默认）| Both fluids unmixed | Thermal Liquid 1 mixed & Thermal Liquid 2 unmixed | Thermal
    Liquid 1 unmixed & Thermal Liquid 2 mixed
  group: 通用
- name: Number of heat transfer units vector, NTU
  summary: 换热器效能查找表中每个断点处的传热单元数 无量纲数值数组
  group: 通用
- name: Thermal capacity ratio vector, CR
  summary: 换热器效能查找表中每个断点处的热容量比 无量纲数值数组
  group: 通用
- name: Effectiveness table, E(NTU,CR)
  summary: 换热器效能查找表中每个断点处基于传热单元数和热容量比的效能 无量纲数值数组
  group: 通用
- name: Enable wall thermal mass
  summary: 用于建模壁面热质量的选项 off（默认）| on
  group: 通用
- name: Wall mass
  summary: 换热器壁面质量 1 kg（默认）| 正标量
  group: 通用
- name: Wall specific heat
  summary: 换热器壁面比热 490 J/(K*kg)（默认）| 正标量
  group: 通用
- name: Minimum free-flow area
  summary: 流动通道最窄点处的横截面积 0.01 m^2（默认）| 具有长度平方单位的标量
  group: Gas 1
- name: Hydraulic diameter for pressure loss
  summary: 流动通道最窄点处的有效直径 0.1 m（默认）| 具有长度单位的标量
  group: Gas 1
- name: Gas volume
  summary: 流动通道中包含的流体总体积 0.01 m^3（默认）| 具有长度平方单位的标量
  group: Gas 1
- name: Laminar flow upper Reynolds number limit
  summary: 层流区和湍流区之间过渡的起点 2000（默认）| 无量纲标量
  group: Gas 1
- name: Turbulent flow lower Reynolds number limit
  summary: 层流区和湍流区之间过渡的终点 4000（默认）| 无量纲标量
  group: Gas 1
- name: Pressure loss model
  summary: 黏性摩擦压力损失的数学模型 Pressure loss coefficient（默认）| Correlation for flow inside tubes | Tabulated data - Darcy friction
    factor vs. Reynolds number | Tabulated data - Euler number vs. Reynolds number
  group: Gas 1
- name: Pressure loss coefficient
  summary: 端口之间所有流动阻力的总损失系数 0.1（默认）| 无量纲标量
  group: Gas 1
- name: Length of flow path from inlet to outlet
  summary: 从端口到端口行进的距离 1 m（默认）| 具有长度单位的标量
  group: Gas 1
- name: Aggregate equivalent length of local resistances
  summary: 以长度表示的次要压力损失总和 0.1 m（默认）| 具有长度单位的标量
  group: Gas 1
- name: Internal surface absolute roughness
  summary: 壁面摩擦背后的表面凸起平均高度 15e-6 m（默认）| 具有长度单位的标量
  group: Gas 1
- name: Laminar friction constant for Darcy friction factor
  summary: 层流条件下流动横截面的压力损失修正 64（默认）| 无量纲标量
  group: Gas 1
- name: Reynolds number vector for Darcy friction factor
  summary: Darcy 摩擦因子查找表中每个断点处的雷诺数 无量纲数值数组
  group: Gas 1
- name: Darcy friction factor vector
  summary: Darcy 摩擦因子查找表中每个断点处基于雷诺数的值 无量纲数值数组
  group: Gas 1
- name: Reynolds number vector for Euler number
  summary: Euler 数查找表中每个断点处的雷诺数 无量纲数值数组
  group: Gas 1
- name: Euler number vector
  summary: Euler 数查找表中每个断点处基于雷诺数的值 无量纲数值数组
  group: Gas 1
- name: Heat transfer coefficient model
  summary: 流体与壁面之间传热的数学模型 Constant heat transfer coefficient（默认）| Correlation for flow inside tubes | Tabulated data - Colburn
    factor vs. Reynolds number | Tabulated data - Nusselt number vs. Reynolds number and Prandtl number
  group: Gas 1
- name: Heat transfer surface area
  summary: 流体与壁面之间传热所用的有效表面积 0.4 m^2（默认）| 具有长度平方单位的标量
  group: Gas 1
- name: Gas-wall heat transfer coefficient
  summary: 气体与壁面之间对流传热的传热系数 100 W/(K*m^2)（默认）| 标量
  group: Gas 1
- name: Length of flow path for heat transfer
  summary: 流体与壁面之间传热所经过的特征长度 1 m（默认）| 具有长度单位的标量
  group: Gas 1
- name: Nusselt number for laminar flow heat transfer
  summary: 层流流动传热中努塞尔数的假定常数值 3.66（默认）| 正的无量纲标量
  group: Gas 1
- name: Reynolds number vector for Colburn factor
  summary: 指定 Colburn 因子数据时所对应的雷诺数值 无量纲数值数组
  group: Gas 1
- name: Colburn factor vector
  summary: 查找表中每个断点处相对于雷诺数的 Colburn 因子 无量纲数值数组
  group: Gas 1
- name: Reynolds number vector for Nusselt number
  summary: 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组
  group: Gas 1
- name: Prandtl number vector for Nusselt number
  summary: 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组
  group: Gas 1
- name: Nusselt number table, Nu (Re,Pr)
  summary: 查找表中每个断点处相对于雷诺数和普朗特数的努塞尔数 无量纲数值数组
  group: Gas 1
- name: Fouling factor
  summary: 由污垢沉积引起的热阻度量 1e-4 K*m^2/W（默认）| 具有温度除以功率单位的标量
  group: Gas 1
- name: Minimum gas-wall heat transfer coefficient
  summary: 传热系数的下界 1 W/(m^2 * K)（默认）| 具有功率/面积/温度单位的标量
  group: Gas 1
- name: Minimum free-flow area
  summary: 流动通道最窄处的横截面积 0.01 m^2（默认）| 具有长度平方单位的标量
  group: Thermal Liquid 2
- name: Hydraulic diameter for pressure loss
  summary: 流动通道最窄处的有效直径 0.1 m（默认）| 具有长度单位的标量
  group: Thermal Liquid 2
- name: Liquid volume
  summary: 流动通道中包含的流体总体积 0.01 m^3（默认）| 具有长度平方单位的标量
  group: Thermal Liquid 2
- name: Laminar flow upper Reynolds number limit
  summary: 层流区与湍流区之间过渡的起点 2000（默认）| 无量纲标量
  group: Thermal Liquid 2
- name: Turbulent flow lower Reynolds number limit
  summary: 层流区与湍流区之间过渡的终点 4000（默认）| 无量纲标量
  group: Thermal Liquid 2
- name: Pressure loss model
  summary: 黏性摩擦压降的数学模型 Pressure loss coefficient（默认）| Correlation for flow inside tubes | Tabulated data - Darcy friction
    factor vs. Reynolds number | Tabulated data - Euler number vs. Reynolds number
  group: Thermal Liquid 2
- name: Pressure loss coefficient
  summary: 端口之间所有流动阻力的总损失系数 0.1（默认）| 无量纲标量
  group: Thermal Liquid 2
- name: Length of flow path from inlet to outlet
  summary: 从端口到端口所经过的距离 1 m（默认）| 具有长度单位的标量
  group: Thermal Liquid 2
- name: Aggregate equivalent length of local resistances
  summary: 以长度表示的次要压降总和 0.1 m（默认）| 具有长度单位的标量
  group: Thermal Liquid 2
- name: Internal surface absolute roughness
  summary: 壁面摩擦所对应的表面凸起平均高度 15e-6 m（默认）| 具有长度单位的标量
  group: Thermal Liquid 2
- name: Laminar friction constant for Darcy friction factor
  summary: 层流条件下流动横截面的压降修正 64（默认）| 无量纲标量
  group: Thermal Liquid 2
- name: Reynolds number vector for Darcy friction factor
  summary: Darcy 摩擦因子查找表中每个断点处的雷诺数 无量纲数值数组
  group: Thermal Liquid 2
- name: Darcy friction factor vector
  summary: 查找表中每个断点处相对于雷诺数的 Darcy 摩擦因子 无量纲数值数组
  group: Thermal Liquid 2
- name: Reynolds number vector for Euler number
  summary: 欧拉数查找表中每个断点处的雷诺数 无量纲数值数组
  group: Thermal Liquid 2
- name: Euler number vector
  summary: 欧拉数在雷诺数查找表中每个断点处的值 无量纲数值数组
  group: Thermal Liquid 2
- name: Heat transfer coefficient model
  summary: 流体与壁面之间传热的数学模型 Constant heat transfer coefficient（默认）| Correlation for flow inside tubes | Tabulated data - Colburn
    factor vs. Reynolds number | Tabulated data - Nusselt number vs. Reynolds number and Prandtl number
  group: Thermal Liquid 2
- name: Heat transfer surface area
  summary: 流体与壁面之间传热所用的有效表面积 0.4 m^2（默认）| 单位为长度平方的标量
  group: Thermal Liquid 2
- name: Liquid-wall heat transfer coefficient
  summary: 流体与壁面之间对流传热系数 100 W/(K*m^2)（默认）| 标量
  group: Thermal Liquid 2
- name: Length of flow path for heat transfer
  summary: 流体与壁面之间传热所经过的特征长度 1 m（默认）| 单位为长度的标量
  group: Thermal Liquid 2
- name: Nusselt number for laminar flow heat transfer
  summary: 层流流动传热中努塞尔数的假定常数值 3.66（默认）| 正的无量纲标量
  group: Thermal Liquid 2
- name: Reynolds number vector for Colburn factor
  summary: 指定 Colburn 因子数据时所对应的雷诺数值 无量纲数值数组
  group: Thermal Liquid 2
- name: Colburn factor vector
  summary: Colburn 因子在雷诺数查找表中每个断点处的值 无量纲数值数组
  group: Thermal Liquid 2
- name: Reynolds number vector for Nusselt number
  summary: 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组
  group: Thermal Liquid 2
- name: Prandtl number vector for Nusselt number
  summary: 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组
  group: Thermal Liquid 2
- name: Nusselt number table, Nu (Re,Pr)
  summary: 努塞尔数在雷诺数和普朗特数查找表中每个断点处的值 无量纲数值数组
  group: Thermal Liquid 2
- name: Fouling factor
  summary: 由污垢沉积引起的热阻度量 1e-4 K * m^2 / W（默认）| 单位为温度除以功率的标量
  group: Thermal Liquid 2
- name: Minimum liquid-wall heat transfer coefficient
  summary: 传热系数的下界 1 W/(m^2 * K)（默认）| 单位为功率/面积/温度的标量
  group: Thermal Liquid 2
- name: Enable Gas 1 dynamic compressibility
  summary: 用于对气体通道中的压力动态进行建模的选项 On（默认）| Off
  group: 效应与初始条件
- name: Gas 1 nominal temperature
  summary: 额定工况下的温度 293.15 K（默认）| 标量
  group: 效应与初始条件
- name: Gas 1 nominal pressure
  summary: 额定工况下的压力 0.101325 MPa（默认）| 标量
  group: 效应与初始条件
- name: Gas 1 initial temperature
  summary: 仿真开始时气体通道中的温度 293.15 K（默认）| 单位为温度的标量
  group: 效应与初始条件
- name: Gas 1 initial pressure
  summary: 仿真开始时气体通道中的压力 0.101325 MPa（默认）| 单位为压力的标量
  group: 效应与初始条件
- name: Enable Thermal Liquid 2 dynamic compressibility
  summary: 用于对热液体通道中的压力动态进行建模的选项 On（默认）| Off
  group: 效应与初始条件
- name: Thermal Liquid 2 nominal temperature
  summary: 额定工况下的温度 293.15 K（默认）| 标量
  group: 效应与初始条件
- name: Thermal Liquid 2 nominal pressure
  summary: 额定工况下的压力 0.101325 MPa（默认）| 标量
  group: 效应与初始条件
- name: Thermal Liquid 2 initial temperature
  summary: 仿真开始时热液体通道中的温度 293.15 K（默认）| 单位为温度的标量
  group: 效应与初始条件
- name: Thermal Liquid 2 initial pressure
  summary: 仿真开始时热液体通道中的压力 0.101325 MPa（默认）| 单位为压力的标量
  group: 效应与初始条件
```

### 通用

### **Flow arrangement** — 换热器中流动对齐的方式 `Parallel or counter flow`（默认）| `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

换热器中流动对齐的方式。流动可以彼此平行、彼此逆向或彼此交叉。它们也可以在加压壳体内流动，一种流体通过封闭在壳体内的管束，另一种流体围绕这些管束流动。通过基于表格化效能数据的通用参数化方法，还可以实现其他流动布置，且对换热器的细节要求很少。

### **Wall thermal resistance** — 壁面通过热传导对热流的阻力 `0 K/W`（默认）| 正标量

分隔两种换热器流体的界面壁面的热阻。

### **Number of shell passes** — 流体在离开之前穿过壳体的次数 `1`（默认）| 无量纲标量

流体在离开之前穿过壳体的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed`（默认）| `Both fluids unmixed` | `Thermal Liquid 1 mixed & Thermal Liquid 2 unmixed` | `Thermal Liquid 1 unmixed & Thermal Liquid 2 mixed`

每个流动通道中的混合条件。此上下文中的混合是指流体沿其流动通道向出口前进时的横向运动。流动彼此保持分离。未混合流动常见于带有板片、折流板或翅片的通道中。此设置反映在换热器的效能中，未混合流动效能最高，混合流动效能最低。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 换热器效能查找表中每个断点处的传热单元数 无量纲数值数组

换热器效能数查找表中每个断点处的传热单元数。该表是二维的，传热单元数和热容量比均作为独立坐标。模块使用线性插值和最近外推来获得任意传热单元数下的效能。

指定的数值必须大于零，并且从左到右单调递增。向量的大小必须等于 **Effectiveness table** 参数的行数。如果表有 *m* 行和 *n* 列，则传热单元数的向量长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Thermal capacity ratio vector, CR** — 换热器效能查找表中每个断点处的热容量比 无量纲数值数组

换热器效能查找表中每个断点处的热容量比。该表是二维的，传热单元数和热容量率比均作为独立坐标。模块使用线性插值和最近外推来获得任意热容量比下的效能。

热容量比必须大于零，并且从左到右单调递增。向量的大小必须等于 **Nusselt number table** 参数的列数。如果表有 *m* 行和 *n* 列，则热容量比的向量长度必须为 *n* 个元素。热容量比是最小热容量率与最大热容量率的比值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Effectiveness table, E(NTU,CR)** — 换热器效能查找表中每个断点处基于传热单元数和热容量比的效能 无量纲数值数组

换热器效能在其基于传热单元数和热容量比的查找表中每个断点处的值。模块使用线性插值和最近外推来获得任意传热单元数和热容量比组合下的效能。

效能值必须为非负。它们必须从上到下按传热单元数递增的顺序排列，从左到右按热容量比递增的顺序排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Enable wall thermal mass** — 用于建模壁面热质量的选项 `off`（默认）| `on`

是否对换热器壁面热质量进行建模。对壁面热质量进行建模会在壁面对温度或热流变化做出响应时引入瞬态延迟。如果清除 **Enable wall thermal mass**，模块将假定壁面足够薄，以至于在传热的时间尺度上瞬态响应是即时的。

### **Wall mass** — 换热器壁面质量 `1 kg`（默认）| 正标量

换热器壁面的质量。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Wall specific heat** — 换热器壁面比热 `490 J/(K*kg)`（默认）| 正标量

换热器壁面的比热。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### Gas 1

### **Minimum free-flow area** — 流动通道最窄点处的横截面积 `0.01 m^2`（默认）| 具有长度平方单位的标量

入口和出口之间最小的总横截流动面积。如果通道是管道、管子、槽或沟的集合，则此参数的值是最小流动面积点处最小面积的总和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在一个横截面中管子之间间隙总和最小的那些间隙的总和。

### **Hydraulic diameter for pressure loss** — 流动通道最窄点处的有效直径 `0.1 m`（默认）| 具有长度单位的标量

流动在最窄点处的有效内径。对于非圆形横截面的通道，该直径为与流动横截面积相等的假想圆的直径。其值是最小自由流动面积与其总周长四分之一之比。

如果通道是管道、管子、槽或沟的集合，则总周长是该集合中周长的总和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Gas volume** — 流动通道中包含的流体总体积 `0.01 m^3`（默认）| 具有长度平方单位的标量

气体流动通道中包含的流体总体积。

### **Laminar flow upper Reynolds number limit** — 层流区和湍流区之间过渡的起点 `2000`（默认）| 无量纲标量

层流区和湍流区之间过渡的起点。高于此数值时，惯性力占据主导，流动逐渐变为湍流。默认值是具有光滑表面的圆管和管子的特征值。

### **Turbulent flow lower Reynolds number limit** — 层流区和湍流区之间过渡的终点 `4000`（默认）| 无量纲标量

层流区和湍流区之间过渡的终点。低于此数值时，黏性力占据主导，流动逐渐变为层流。默认值是具有光滑表面的圆管和管子的特征值。

### **Pressure loss model** — 黏性摩擦压力损失的数学模型 `Pressure loss coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

黏性摩擦压力损失的数学模型。此设置决定使用哪些表达式进行计算以及指定哪些模块参数作为输入。有关按参数化进行的计算，请参见 Heat Exchanger Interface (G) 和 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1`（默认）| 无量纲标量

流动通道中所有流动阻力的总损失系数，包括造成主要损失的壁面摩擦以及由弯头、弯管和其他几何变化引起的造成次要损失的局部阻力。

损失系数是经验无量纲数，通常用于表示黏性摩擦引起的压力损失。它可以从实验数据计算得出，或者在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口行进的距离 `1 m`（默认）| 具有长度单位的标量

流动穿过端口所需行进的总距离。在多程管壳式换热器中，总距离是所有壳程的总和。在管束、波纹板和其他流动被分成平行分支的通道中，它是单个分支中覆盖的距离。流动路径越长，壁面处黏性摩擦引起的主要压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的次要压力损失总和 `0.1 m`（默认）| 具有长度单位的标量

以长度表示的次要压力损失总和。此长度是所有局部阻力（如弯头、三通和管接头）如果被简单的壁面延伸替代后，将添加到流动路径中的长度。等效长度越大，局部阻力引起的次要压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 壁面摩擦背后的表面凸起平均高度 `15e-6 m`（默认）| 具有长度单位的标量

壁面摩擦所源自的表面凸起的平均高度。凸起越高意味着壁面越粗糙，摩擦越大，因此压力损失越大。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由此导出，压力损失计算依赖于该关联式。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压力损失修正 `64`（默认）| 无量纲标量

层流条件下流动横截面的压力损失修正。此参数通常称为形状因子。其与雷诺数的比值给出层流区压力损失计算的 Darcy 摩擦因子。默认值属于圆柱形管道和管子。

形状因子对于某些形状可从 Navier-Stokes 方程的解导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长管道也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的雷诺数 无量纲数值数组

Darcy 摩擦因子查找表中每个断点处的雷诺数。模块使用线性插值和最近外推来获得任意雷诺数下的 Darcy 摩擦因子。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流区。它们的数量必须等于 **Darcy friction factor vector** 参数的大小，与之组合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — Darcy 摩擦因子查找表中每个断点处基于雷诺数的值 无量纲数值数组

Darcy 摩擦因子在其基于雷诺数的查找表中每个断点处的值。模块使用线性插值和最近外推来获得任意雷诺数下的 Darcy 摩擦因子。

Darcy 摩擦因子必须为非负，并且它们必须从左到右按雷诺数递增的顺序排列。它们的数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，与之组合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的雷诺数 无量纲数值数组

Euler 数查找表中每个断点处的雷诺数。模块使用线性插值和最近外推来获得任意雷诺数下的 Euler 数。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流区。它们的数量必须等于 **Euler number vector** 参数的大小，与之组合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — Euler 数查找表中每个断点处基于雷诺数的值 无量纲数值数组

Euler 数在其基于雷诺数的查找表中每个断点处的值。模块使用线性插值和最近外推来获得任意雷诺数下的 Euler 数。

Euler 数必须为非负，并且它们必须从左到右按雷诺数递增的顺序排列。它们的数量必须等于 **Reynolds number vector for Euler number** 参数的大小，与之组合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定了传热计算中应用哪些表达式以及需要指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **Heat transfer surface area** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认）| 具有长度平方单位的标量

流体与壁面之间传热所用的有效表面积。有效表面积是主表面积与二次表面积之和，即壁面暴露于流体的表面积与翅片（如果使用）的表面积之和。翅片表面积通常按翅片效率因子进行折算。

### **Gas-wall heat transfer coefficient** — 气体与壁面之间对流传热的传热系数 `100 W/(K*m^2)`（默认）| 标量

气体与壁面之间对流传热的传热系数。污垢引起的热阻在 **Fouling factor** 参数中单独体现。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer coefficient`。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m`（默认）| 具有长度单位的标量

流体与壁面之间传热所经过的特征长度。该长度参与水力直径的计算，而传热系数和雷诺数（如表列传热参数化中所定义）均由水力直径导出。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number for laminar flow heat transfer** — 层流流动传热中努塞尔数的假定常数值 `3.66`（默认）| 正的无量纲标量

层流流动传热中努塞尔数的假定常数值。努塞尔数参与流体与壁面之间传热系数的计算，而传热速率取决于该传热系数。默认值适用于圆柱形管道和管子。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Colburn factor** — 指定 Colburn 因子数据时所对应的雷诺数值 无量纲数值数组

Colburn 因子查找表中每个断点处的雷诺数。该模块使用线性插值和最近邻外推来获得任意雷诺数下的 Colburn 因子。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。其数量必须等于 **Colburn factor vector** 参数的大小，两者结合以构成完整的表列断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — 查找表中每个断点处相对于雷诺数的 Colburn 因子 无量纲数值数组

Colburn 因子在其相对于雷诺数的查找表中每个断点处的值。该模块使用线性插值和最近邻外推来获得任意雷诺数下的欧拉数。

Colburn 因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Colburn factor** 参数的大小，两者结合以构成完整的表列断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组

努塞尔数查找表中每个断点处的雷诺数。该表是二维的，以雷诺数和普朗特数作为独立坐标。该模块使用线性插值和最近邻外推来获得任意雷诺数下的努塞尔数。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。向量的大小必须等于 **Nusselt number table** 参数的行数。如果该表有 *m* 行和 *n* 列，则雷诺数向量必须包含 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组

努塞尔数查找表中每个断点处的普朗特数。该表是二维的，以雷诺数和普朗特数作为独立坐标。该模块使用线性插值和最近邻外推来获得任意普朗特数下的努塞尔数。

普朗特数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。向量的大小必须等于 **Nusselt number table** 参数的列数。如果该表有 *m* 行和 *n* 列，则普朗特数向量必须包含 *n* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu (Re,Pr)** — 查找表中每个断点处相对于雷诺数和普朗特数的努塞尔数 无量纲数值数组

努塞尔数在其相对于雷诺数和普朗特数的查找表中每个断点处的值。该模块使用线性插值和最近邻外推来获得任意雷诺数和普朗特数组合下的努塞尔数。通过确定努塞尔数，该表为流体与壁面之间传热系数的计算提供输入。

努塞尔数必须大于零。它们必须按雷诺数递增的顺序从上到下排列，并按普朗特数递增的顺序从左到右排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的大小，列数必须等于 **Prandtl number vector for Nusselt number** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W`（默认）| 具有温度除以功率单位的标量

由污垢沉积引起的热阻度量，污垢随时间倾向于在壁面的暴露表面上积聚。这些沉积物在流体与壁面之间形成新的固体层，热量必须穿过该层，从而在传热路径中增加了额外的热阻。污垢沉积物增长缓慢，因此其热阻在仿真期间假定为常数。

### **Minimum gas-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)`（默认）| 具有功率/面积/温度单位的标量

流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则用此边界值替代计算值。

### Thermal Liquid 2

### **Minimum free-flow area** — 流动通道最窄处的横截面积 `0.01 m^2`（默认）| 具有长度平方单位的标量

入口与出口之间最小的总横截流动面积。如果通道是由管道、管子、槽或沟组成的集合，则此参数的值为最小流动面积点处各最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值为一个横截面中管子之间间隙之和最小的那个截面处的间隙总和。

### **Hydraulic diameter for pressure loss** — 流动通道最窄处的有效直径 `0.1 m`（默认）| 具有长度单位的标量

流动在最窄处的有效内径。对于非圆形横截面的通道，该直径为与流动横截面积相等的假想圆的直径。其值为最小自由流动面积与其总周长四分之一之比。

如果通道是由管道、管子、槽或沟组成的集合，则总周长为该集合中各周长之和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Liquid volume** — 流动通道中包含的流体总体积 `0.01 m^3`（默认）| 具有长度平方单位的标量

热液体流动通道中包含的流体总体积。

### **Laminar flow upper Reynolds number limit** — 层流区与湍流区之间过渡的起点 `2000`（默认）| 无量纲标量

层流区与湍流区之间过渡的起点。高于此数值时，惯性力占据主导，流动逐渐变为湍流。默认值适用于表面光滑的圆形管道和管子。

### **Turbulent flow lower Reynolds number limit** — 层流区与湍流区之间过渡的终点 `4000`（默认）| 无量纲标量

层流区与湍流区之间过渡的终点。低于此数值时，黏性力占据主导，流动逐渐变为层流。默认值适用于表面光滑的圆形管道和管子。

### **Pressure loss model** — 黏性摩擦压降的数学模型 `Pressure loss coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

黏性摩擦压降的数学模型。此设置决定了用于计算的表达式以及需要指定为输入的模块参数。有关按参数化进行的计算，请参见 Heat Exchanger Interface (G) 和 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1`（默认）| 无量纲标量

流动通道中所有流动阻力的总损失系数，包括造成主要损失的壁面摩擦以及由弯头、肘管和其他几何变化引起的造成次要损失的局部阻力。

损失系数是一个经验无量纲数，通常用于表示黏性摩擦引起的压降。它可以通过实验数据计算得出，或者在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口所经过的距离 `1 m`（默认）| 具有长度单位的标量

流动跨越端口所必须经过的总距离。在多程管壳式换热器中，总距离是所有壳程距离之和。在管束、波纹板和其他流动被分成并联支路的通道中，它是单条支路中经过的距离。流动路径越长，壁面处黏性摩擦引起的主要压降越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的次要压降总和 `0.1 m`（默认）| 具有长度单位的标量

以长度表示的次要压降总和。该长度是所有局部阻力（如弯头、三通和管接头）在其位置替换为简单壁面延伸时所增加的流动路径长度。等效长度越大，局部阻力引起的次要压降越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 壁面摩擦所对应的表面凸起平均高度 `15e-6 m`（默认）| 具有长度单位的标量

壁面摩擦所对应的表面凸起平均高度。凸起越高意味着壁面越粗糙，摩擦越大，因此压降越大。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，压降计算依赖于该关联式。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压降修正 `64`（默认）| 无量纲标量

层流条件下流动横截面的压降修正。此参数通常称为形状因子。其与雷诺数的比值给出了层流区压降计算所用的 Darcy 摩擦因子。默认值适用于圆柱形管道和管子。

形状因子对于某些形状可从 Navier-Stokes 方程的解中导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长通道也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的雷诺数 无量纲数值数组

Darcy 摩擦因子查找表中每个断点处的雷诺数。该模块使用线性插值和最近邻外推来获得任意雷诺数下的 Darcy 摩擦因子。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。其数量必须等于 **Darcy friction factor vector** 参数的大小，两者结合以构成完整的表列断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — 查找表中每个断点处相对于雷诺数的 Darcy 摩擦因子 无量纲数值数组

Darcy 摩擦因子在其相对于雷诺数的查找表中每个断点处的值。该模块使用线性插值和最近邻外推来获得任意雷诺数下的 Darcy 摩擦因子。

Darcy 摩擦因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，两者结合以构成完整的表列断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — 欧拉数查找表中每个断点处的雷诺数 无量纲数值数组

欧拉数查找表中每个断点处的雷诺数。该模块使用线性插值和最近邻外推来获取任意雷诺数下的欧拉数。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。其数量必须等于 **Euler number vector** 参数的大小，两者结合以完成表格化的断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — 欧拉数在雷诺数查找表中每个断点处的值 无量纲数值数组

欧拉数在其关于雷诺数的查找表中每个断点处的值。该模块使用线性插值和最近邻外推来获取任意雷诺数下的欧拉数。

欧拉数不得为负，并且必须按照雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Euler number** 参数的大小，两者结合以完成表格化的断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定了传热计算中应用哪些表达式以及指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **Heat transfer surface area** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认）| 单位为长度平方的标量

流体与壁面之间传热所用的有效表面积。有效表面积是主表面积和次表面积之和，即壁面暴露于流体的表面积与翅片（如果使用）表面积之和。翅片表面积通常按翅片效率因子进行缩放。

### **Liquid-wall heat transfer coefficient** — 流体与壁面之间对流传热系数 `100 W/(K*m^2)`（默认）| 标量

流体与壁面之间对流传热系数。污垢引起的热阻在 **Fouling factor** 参数中单独体现。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer coefficient`。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m`（默认）| 单位为长度的标量

流体与壁面之间传热所经过的特征长度。该长度参与水力直径的计算，而传热系数和雷诺数（如表格化传热参数化中所定义）由水力直径推导得出。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number for laminar flow heat transfer** — 层流流动传热中努塞尔数的假定常数值 `3.66`（默认）| 正的无量纲标量

层流流动传热中努塞尔数的假定常数值。努塞尔数参与流体与壁面之间传热系数的计算，传热速率取决于该传热系数。默认值适用于圆柱形管道和管子。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Colburn factor** — 指定 Colburn 因子数据时所对应的雷诺数值 无量纲数值数组

Colburn 因子查找表中每个断点处的雷诺数。该模块使用线性插值和最近邻外推来获取任意雷诺数下的 Colburn 因子。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。其数量必须等于 **Colburn factor vector** 参数的大小，两者结合以完成表格化的断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — Colburn 因子在雷诺数查找表中每个断点处的值 无量纲数值数组

Colburn 因子在其关于雷诺数的查找表中每个断点处的值。该模块使用线性插值和最近邻外推来获取任意雷诺数下的欧拉数。

Colburn 因子不得为负，并且必须按照雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Colburn factor** 参数的大小，两者结合以完成表格化的断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组

努塞尔数查找表中每个断点处的雷诺数。该表是二维的，雷诺数和普朗特数均作为独立坐标。该模块使用线性插值和最近邻外推来获取任意雷诺数下的努塞尔数。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。向量的大小必须等于 **Nusselt number table** 参数的行数。如果表有 *m* 行和 *n* 列，则雷诺数向量必须包含 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组

努塞尔数查找表中每个断点处的普朗特数。该表是二维的，雷诺数和普朗特数均作为独立坐标。该模块使用线性插值和最近邻外推来获取任意普朗特数下的努塞尔数。

普朗特数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。向量的大小必须等于 **Nusselt number table** 参数的列数。如果表有 *m* 行和 *n* 列，则普朗特数向量必须包含 *n* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu (Re,Pr)** — 努塞尔数在雷诺数和普朗特数查找表中每个断点处的值 无量纲数值数组

努塞尔数在其关于雷诺数和普朗特数的查找表中每个断点处的值。该模块使用线性插值和最近邻外推来获取任意雷诺数和普朗特数组合下的努塞尔数。通过确定努塞尔数，该表为流体与壁面之间传热系数的推导计算提供输入。

努塞尔数必须大于零。它们必须按照雷诺数递增的顺序从上到下排列，并按照普朗特数递增的顺序从左到右排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的大小，列数必须等于 **Prandtl number vector for Nusselt number** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K * m^2 / W`（默认）| 单位为温度除以功率的标量

由污垢沉积引起的热阻度量，污垢随时间倾向于在壁面暴露表面上积聚。沉积物在流体与壁面之间形成新的固体层，热量必须穿过该层，从而在传热路径中增加额外的热阻。污垢沉积物增长缓慢，因此其引起的热阻在仿真期间假定为常数。

### **Minimum liquid-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)`（默认）| 单位为功率/面积/温度的标量

流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则此下界将替代计算值。

### 效应与初始条件

### **Enable Gas 1 dynamic compressibility** — 用于对气体通道中的压力动态进行建模的选项 `On`（默认）| `Off`

用于对气体通道中的压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas 1 nominal temperature** — 额定工况下的温度 `293.15 K`（默认）| 标量

额定工况下的气体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程中的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 nominal pressure** — 额定工况下的压力 `0.101325 MPa`（默认）| 标量

额定工况下的气体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程中的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 initial temperature** — 仿真开始时气体通道中的温度 `293.15 K`（默认）| 单位为温度的标量

仿真开始时气体通道中的温度

### **Gas 1 initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa`（默认）| 单位为压力的标量

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas 1 dynamic compressibility**。

### **Enable Thermal Liquid 2 dynamic compressibility** — 用于对热液体通道中的压力动态进行建模的选项 `On`（默认）| `Off`

用于对热液体通道中的压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。换热器内部的压力随后被简化为两个端口压力的加权平均值。

### **Thermal Liquid 2 nominal temperature** — 额定工况下的温度 `293.15 K`（默认）| 标量

额定工况下的热液体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程中的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 nominal pressure** — 额定工况下的压力 `0.101325 MPa`（默认）| 标量

额定工况下的热液体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程中的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K`（默认）| 单位为温度的标量

仿真开始时热液体通道中的温度

### **Thermal Liquid 2 initial pressure** — 仿真开始时热液体通道中的压力 `0.101325 MPa`（默认）| 单位为压力的标量

仿真开始时热液体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Thermal Liquid 2 dynamic compressibility**。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a：可选地对动态可压缩性进行建模

Heat Exchanger (G-TL) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性进行建模。此前，该模块始终对压力动态进行建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2024a：Heat Exchanger (G-TL) 模块仅对 E-NTU 建模选项进行建模

**Modeling option** 参数已被移除，建模选项现在为两个独立的模块。Heat Exchanger (G-TL) 模块使用此前当 **Modeling option** 为 `E-NTU Model` 时所使用的传热模型。要使用此前当 **Modeling option** 为 `Simple model` 时所使用的模块模型，请参见 Specific Dissipation Heat Exchanger (G-TL) 模块。

## 描述

用于具有气体和热液体流动的系统的换热器

Heat Exchanger (G-TL) 模块对短暂保持在薄导热壁两侧热接触的流体进行互补冷却和加热进行建模。壁面可以在其边界内存储热量，为传热增加轻微的瞬态延迟，该延迟与其热质量成比例。流体为单相，一侧为纯气体，另一侧为纯液体。两种流体均不能发生相变，因此由于潜热永远不会释放，交换严格为显热交换。

显热换热器在机械中比比皆是。在某些喷气式飞机中，防止冰在燃油管路中析出并堵塞燃油滤的燃油加热器，其工作原理是将仍来自压气机的高温引气吹过燃油管路。在某些摩托车中，防止润滑油过热的机油冷却器同样通过将环境温度的冲压空气吹过油路来工作。引气和冲压空气是气体流，燃油和机油是热液体流。

### Heat Transfer Model

该模块的传热模型源自效能-传热单元数（Effectiveness-NTU）方法。稳态下的传热随后以理想速率的一部分进行；如果各股流体各自保持其入口温度，并且清除其间所有热阻，则理论上可支持该理想速率：

Q=ϵ QMax，

其中 *Q* 为实际传热速率，
*Q*Max 为理想传热速率，
*ε* 为在带有损失的真实换热器中实际观测到的理想速率占比。该占比即为换热器效能，它是传热单元数（NTU）的函数；NTU 衡量热量在两股流体之间传递的容易程度相对于流体吸收该热量的容易程度：

NTU=1RCMin，

其中该占比为流体之间的总热导，*C*Min 为属于最不具备吸热能力的流体的热容率中的最小值。流体的热容率取决于流体的比热（*c*p）及其通过换热器的质量流量（m˙）：

C=cpm˙。

效能还取决于流体的相对布置、流体之间的程数以及各自的混合条件。这种依赖性体现在所使用的效能表达式中，不同的流动布置对应不同的表达式。有关效能表达式列表，请参见 E-NTU Heat Transfer 模块。

该模块在传热计算中使用的流体物性为入口处的值与流体体积中的值之间的平均值。

### Flow Arrangement

使用 **Flow arrangement** 模块参数设置流体在换热器中的相遇方式。流体可以彼此平行流动、彼此逆流流动或彼此交叉流动。它们也可以在带压壳体中流动，一股流体通过封装在壳体中的管束，另一股流体围绕这些相同的管束流动。图中给出了一个示例。管侧流体可以单程通过壳侧流体（如右图所示），或者为了提高换热器效能而采用多程（如左图所示）。

通过基于表格化效能数据的通用参数化，还可以实现其他流动布置，并且几乎不需要关于换热器的详细信息。如果与换热器相关，则假定流动布置、混合条件以及壳程或管程数体现在表格化数据中。

### Mixing Condition

使用 **Cross flow arrangement** 参数来混合各股流体、其中一股流体或不混合任何流体。在此上下文中，混合是指流体在没有内部屏障（通常为导流板、折流板、翅片或壁面）的通道中的横向运动。这种运动用于均衡横向平面内的温度变化。混合流体的温度仅在纵向平面内变化。未混合流体的温度在横向和纵向平面内均变化。图中显示了混合流（**i**）和未混合流（**ii**）。

混合流与未混合流之间的区别仅在叉流布置中考虑。在那里，一种流体中的纵向温度变化会在第二种流体中产生横向温度变化，而混合可以将其均衡。在逆流和平行流布置中，一种流体中的纵向温度变化会在第二种流体中产生纵向温度变化，而混合在这里影响很小，因此被忽略。

### Effectiveness Curves

具有多程的壳管式换热器（图中 **iv.b**-**e** 分别对应 2、3 和 4 程）最有效。在单程换热器中，逆流换热器（**ii**）最有效，平行流换热器（**i**）最差。

叉流换热器的效能介于两者之间，其中混合条件起一定作用。当两股流体均未混合（**iii.a**）时最有效，当两股流体均混合（**iii.b**）时最差。仅混合热容率最小的流体（**iii.c**）比仅混合热容率最大的流体（**iii.d**）更能降低效能。

### Thermal Resistance

总热阻 *R* 是沿传热路径排列的局部热阻之和。局部热阻来自壁面表面的对流、通过壁面的导热，以及如果壁面两侧发生污垢沉积，则还包括通过污垢层的导热。按从气体侧（侧 1）到热液体侧（侧 2）的顺序表示为：

R=1U1A1+F1A1+RW+F2A2+1U2A2，

其中 *U* 为对流换热系数，*F* 为污垢系数，*A* 为换热表面积，各自对应下标所示的流体。*R*W 为壁面的热阻。

壁面热阻和污垢系数是从模块参数获得的简单常数。换热系数是流体物性、流动几何和壁面摩擦的复杂函数，并源自 Reynolds 数、Nusselt 数和 Prandtl 数之间的标准经验关联式。这些关联式取决于流动布置和混合条件，并在该模块模型所基于的 E-NTU Heat Transfer 模块中针对每种情况进行了详细说明。

### Wall Thermal Mass

如果选择 **Enable wall thermal mass**，该模块会对换热器壁面热质量建模，这会在壁面对温度或热流变化的热瞬态响应中引入延迟。如果对热质量建模，壁面会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率达到平衡。

如果选择 **Enable wall thermal mass**，则壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁面温度。该模块使用此值来建模瞬态响应。你无法测量此值。

传递给每种流体的热量为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是换热系数。

### Composite Structure

该模块是由更简单的模块构建而成的复合组件。Heat Exchanger Interface (G) 模块对气体流动建模，Heat Exchanger Interface (TL) 模块对热液体流动建模，E-NTU Heat Transfer 模块对流体之间通过壁面交换的热量建模。
