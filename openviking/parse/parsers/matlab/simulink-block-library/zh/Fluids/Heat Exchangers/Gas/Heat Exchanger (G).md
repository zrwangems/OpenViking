---
type: simulink-block
title: 'Heat Exchanger (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'heatexchangerg'
documentation_source_path: 'ref/heatexchangerg.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (G)

## 端口
```yaml
ports:
- name: A1
  summary: 气体端口 gas
  direction: conserving
- name: B1
  summary: 气体端口 gas
  direction: conserving
- name: H2
  summary: 受控流体 2 的入口温度 thermal
  direction: conserving
- name: C2
  summary: 热容率 physical signal
  direction: input
- name: HC2
  summary: 传热系数 physical signal
  direction: input
```

### 守恒端口

### **A1** — 气体端口 gas

气体进入和离开换热器其所在侧的开口。

### **B1** — 气体端口 gas

气体进入和离开换热器其所在侧的开口。

### **H2** — 受控流体 2 的入口温度 thermal

受控流体 2 的入口温度。

### 输入

### **C2** — 热容率 physical signal

受控流热容率的瞬时值。

### **HC2** — 传热系数 physical signal

受控流与壁面之间传热系数的瞬时值。
## 参数
```yaml
parameters:
- name: Flow arrangement
  summary: 换热器中流体的排列方式 Parallel or counter flow（默认）| Shell and tube | Cross flow | Generic - effectiveness table
  group: 通用
- name: Number of shell passes
  summary: 流体在离开之前穿过壳体的次数 1（默认）| 无量纲标量
  group: 通用
- name: Cross flow type
  summary: 每个流动通道中的混合条件 Both fluids mixed（默认）| Both fluids unmixed | Gas mixed & Controlled Fluid unmixed | Gas unmixed &
    Controlled Fluid mixed
  group: 通用
- name: Number of heat transfer units vector, NTU
  summary: 换热器有效性查找表中每个断点处的传热单元数 无量纲数值数组
  group: 通用
- name: 热容比向量，CR
  summary: 换热器效能查找表中每个断点处的热容比 无量纲数值数组
  group: 通用
- name: 效能表，E(NTU,CR)
  summary: 换热器效能查找表中每个断点处基于传热单元数和热容比的效能 无量纲数值数组
  group: 通用
- name: 壁面热阻
  summary: 壁面通过热传导对热流的阻力 0 K/W（默认）| 单位为温度除以功率的标量
  group: 通用
- name: 启用壁面热质量
  summary: 用于建模壁面热质量的选项 off（默认）| on
  group: 通用
- name: 壁面质量
  summary: 换热器壁面质量 1 kg（默认）| 正标量
  group: 通用
- name: 壁面比热
  summary: 换热器壁面比热 490 J/(K*kg)（默认）| 正标量
  group: 通用
- name: 最小自由流通面积
  summary: 流道在其最窄点处的横截面积 0.01 m^2（默认）| 带长度平方单位的标量
  group: 气体
- name: 气体体积
  summary: 气体流道中流体的总体积 0.01 m^3（默认）| 带长度平方单位的标量
  group: 气体
- name: 用于压力损失的液压直径
  summary: 流道在其最窄点处的有效直径 0.1 m（默认）| 带长度单位的标量
  group: 气体
- name: 层流上限雷诺数
  summary: 层流区与湍流区之间过渡的起点 2000（默认）| 无量纲标量
  group: 气体
- name: 湍流下限雷诺数
  summary: 层流区与湍流区之间过渡的终点 4000（默认）| 无量纲标量
  group: 气体
- name: 压力损失模型
  summary: 黏性摩擦压力损失的数学模型 Pressure loss coefficient（默认）| Correlation for flow inside tubes | Tabulated data - Darcy friction
    factor vs. Reynolds number | Tabulated data - Euler number vs. Reynolds number
  group: 气体
- name: 压力损失系数
  summary: 端口之间所有流动阻力的总损失系数 0.1（默认）| 无量纲标量
  group: 气体
- name: 从入口到出口的流动路径长度
  summary: 从端口到端口经过的距离 1 m（默认）| 带长度单位的标量
  group: 气体
- name: 局部阻力的总等效长度
  summary: 以长度表示的局部压力损失总和 0.1 m（默认）| 带长度单位的标量
  group: 气体
- name: 内表面绝对粗糙度
  summary: 壁面摩擦背后的表面凸起平均高度 15e-6 m（默认）| 带长度单位的标量
  group: 气体
- name: Darcy 摩擦因子的层流摩擦常数
  summary: 层流条件下流动截面的压力损失修正 64（默认）| 无量纲标量
  group: 气体
- name: Darcy 摩擦因子的 Reynolds 数向量
  summary: Darcy 摩擦因子查找表中每个断点处的 Reynolds 数 无量纲数值数组
  group: 气体
- name: Darcy friction factor vector
  summary: 雷诺数查找表中每个断点处的 Darcy 摩擦因子，无量纲数值数组
  group: 气体
- name: Reynolds number vector for Euler number
  summary: Euler 数查找表中每个断点处的雷诺数，无量纲数值数组
  group: 气体
- name: Euler number vector
  summary: 雷诺数查找表中每个断点处的 Euler 数，无量纲数值数组
  group: 气体
- name: Heat transfer coefficient model
  summary: 流体与壁面之间传热的数学模型 Constant heat transfer coefficient（默认）| Correlation for flow inside tubes | Tabulated data - Colburn
    factor vs. Reynolds number | Tabulated data - Nusselt number vs. Reynolds number and Prandtl number
  group: 气体
- name: Heat transfer surface area
  summary: 流体与壁面之间传热所用的有效表面积 0.4 m^2（默认）| 单位为长度平方的标量
  group: 气体
- name: Gas-wall heat transfer coefficient
  summary: 流体与壁面之间对流传热的传热系数 100 W/(K*m^2)（默认）| 标量
  group: 气体
- name: Length of flow path for heat transfer
  summary: 流体与壁面之间传热所经过的特征长度 1 m（默认）| 带长度单位的标量
  group: 气体
- name: Nusselt number for laminar flow heat transfer
  summary: 层流传热中努塞尔数的假定常数值 3.66（默认）| 正的无量纲标量
  group: 气体
- name: Reynolds number vector for Colburn factor
  summary: 指定 Colburn 因子数据时所对应的雷诺数值 无量纲数值数组
  group: 气体
- name: Colburn factor vector
  summary: 查找表中每个断点处相对于雷诺数的 Colburn 因子 无量纲数值数组
  group: 气体
- name: Reynolds number vector for Nusselt number
  summary: 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组
  group: 气体
- name: Prandtl number vector for Nusselt number
  summary: 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组
  group: 气体
- name: Nusselt number table, Nu (Re,Pr)
  summary: 雷诺数和普朗特数查找表中每个断点处的努塞尔数 无量纲数值数组
  group: 气体
- name: Fouling factor
  summary: 由污垢沉积引起的热阻度量 1e-4 K*m^2/W（默认）| 单位为温度除以功率的标量
  group: 气体
- name: Minimum gas-wall heat transfer coefficient
  summary: 传热系数的下界 1 W/(m^2 * K)（默认）| 单位为功率/面积/温度的标量
  group: 气体
- name: Heat transfer surface area
  summary: 受控流体侧的总传热表面积 0.4 m^2（默认）| 单位为长度平方的标量
  group: Controlled Fluid
- name: Fouling factor
  summary: 由污垢沉积引起的热阻度量 1e-4 K*m^2/W（默认）| 单位为长度平方乘以温度除以功率的标量
  group: Controlled Fluid
- name: Minimum fluid-wall heat transfer coefficient
  summary: 流体-壁面传热系数的下界 1 W/(m^2 * K)（默认）| 具有功率/面积/温度单位的标量
  group: Controlled Fluid
- name: Enable Gas dynamic compressibility
  summary: 对气体通道中压力动态进行建模的选项 On（默认）| Off
  group: 效应与初始条件
- name: Gas nominal temperature
  summary: 标称工况下的温度 293.15 K（默认）| 标量
  group: 效应与初始条件
- name: Gas nominal pressure
  summary: 标称工况下的压力 0.101325 MPa（默认）| 标量
  group: 效应与初始条件
- name: Gas initial temperature
  summary: 仿真开始时气体通道中的温度 293.15 K（默认）| 标量
  group: 效应与初始条件
- name: Gas initial pressure
  summary: 仿真开始时气体通道中的压力 0.101325 MPa（默认）| 标量
  group: 效应与初始条件
```

### 通用

### **Flow arrangement** — 换热器中流体的排列方式 `Parallel or counter flow`（默认）| `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

换热器中流体的排列方式。流体可以彼此平行流动、彼此逆向流动或彼此交叉流动。它们也可以在加压壳体内流动，一种流体通过壳体内的管道，另一种流体围绕这些管道流动。通过基于表格化有效性数据且几乎不需要换热器详细信息的通用参数化方法，还可以实现其他流动排列方式。

### **Number of shell passes** — 流体在离开之前穿过壳体的次数 `1`（默认）| 无量纲标量

流体在离开之前穿过壳体的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed`（默认）| `Both fluids unmixed` | `Gas mixed & Controlled Fluid unmixed` | `Gas unmixed & Controlled Fluid mixed`

每个流动通道中的混合条件。此处的混合是指流体沿其流动通道向出口前进时的横向运动。各流体彼此保持分离。未混合流动常见于带有板片、折流板或翅片的通道中。此设置会影响换热器的有效性，未混合流动最有效，混合流动最无效。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 换热器有效性查找表中每个断点处的传热单元数 无量纲数值数组

换热器有效性数查找表中每个断点处的传热单元数。该表是二维的，传热单元数和热容量比均作为独立坐标。该模块对断点进行内插和外推，以获得任意传热单元数下的有效性。插值方法为 `linear`，外推方法为 `nearest`。

指定的数值必须大于零，并且从左到右单调递增。向量的大小必须等于 **Effectiveness table** 参数的行数。如果表有 *m* 行和 *n* 列，则传热单元数的向量长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **热容比向量，CR** — 换热器效能查找表中每个断点处的热容比 无量纲数值数组

换热器效能查找表中每个断点处的热容比。该表是二维的，传热单元数和热容率比同时作为独立坐标。该模块对断点进行内插和外推，以获得任意热容比下的效能。插值为 `linear`，外推为 `nearest`。

热容比必须大于零，并且从左到右单调递增。该向量的大小必须等于 **Nusselt number table** 参数的列数。如果该表有 *m* 行和 *n* 列，则热容比向量必须为 *n* 个元素长。热容比是最小热容率与最大热容率的比值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **效能表，E(NTU,CR)** — 换热器效能查找表中每个断点处基于传热单元数和热容比的效能 无量纲数值数组

换热器效能查找表中每个断点处基于传热单元数和热容比的换热器效能。该模块对断点进行内插和外推，以获得任意传热单元数和热容比组合下的效能。插值为 `linear`，外推为 `nearest`。

效能值不得为负。它们必须按传热单元数递增的顺序从上到下排列，并按热容比递增的顺序从左到右排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **壁面热阻** — 壁面通过热传导对热流的阻力 `0 K/W`（默认）| 单位为温度除以功率的标量

壁面通过热传导对热流的阻力，也是热导的倒数，或热导率与表面积和长度之比的乘积。壁面热阻与对流热阻和污垢热阻相加，以确定流体之间的总传热系数。

### **启用壁面热质量** — 用于建模壁面热质量的选项 `off`（默认）| `on`

是否对换热器壁面热质量建模。对壁面热质量建模会在壁面对温度或热流变化的瞬态响应中引入延迟。如果清除 **Enable wall thermal mass**，则该模块假定壁面足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **壁面质量** — 换热器壁面质量 `1 kg`（默认）| 正标量

换热器壁面的质量。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **壁面比热** — 换热器壁面比热 `490 J/(K*kg)`（默认）| 正标量

换热器壁面的比热。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### 气体

### **最小自由流通面积** — 流道在其最窄点处的横截面积 `0.01 m^2`（默认）| 带长度平方单位的标量

入口与出口之间最小的总横截流通面积。如果通道是由管道、管子、槽或沟槽组成的集合，则该参数的值为最小流通面积点处各最小面积之和。该参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则该参数的值为一个横截面中管子之间间隙之和最小的那些间隙之和。

### **气体体积** — 气体流道中流体的总体积 `0.01 m^3`（默认）| 带长度平方单位的标量

气体流道中包含的流体总体积。

### **用于压力损失的液压直径** — 流道在其最窄点处的有效直径 `0.1 m`（默认）| 带长度单位的标量

流体在其最窄点处的有效内径。对于横截面非圆形的通道，该直径为与流通横截面积相等的假想圆的直径。其值为最小自由流通面积与其总周长四分之一之比。

如果通道是由管道、管子、槽或沟槽组成的集合，则总周长为该集合中各周长之和。如果通道是单根管道或管子且其横截面为圆形，则液压直径与真实直径相同。

### **层流上限雷诺数** — 层流区与湍流区之间过渡的起点 `2000`（默认）| 无量纲标量

层流区与湍流区之间过渡的起点。高于此数值时，惯性力占主导，流动逐渐变为湍流。默认值是具有光滑表面的圆管和管道的特征值。

### **湍流下限雷诺数** — 层流区与湍流区之间过渡的终点 `4000`（默认）| 无量纲标量

层流区与湍流区之间过渡的终点。低于此数值时，黏性力占主导，流动逐渐变为层流。默认值是具有光滑表面的圆管和管道的特征值。

### **压力损失模型** — 黏性摩擦压力损失的数学模型 `Pressure loss coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

黏性摩擦压力损失的数学模型。此设置决定用于计算的表达式以及需要指定为输入的模块参数。有关按参数化进行的计算，请参见 Heat Exchanger Interface (G) 模块。

### **压力损失系数** — 端口之间所有流动阻力的总损失系数 `0.1`（默认）| 无量纲标量

流道中所有流动阻力的总损失系数，包括造成沿程损失（major loss）的壁面摩擦，以及由弯头、肘部和其他几何变化引起、造成局部损失（minor loss）的局部阻力。

损失系数是一个经验无量纲数，常用于表示黏性摩擦引起的压力损失。它可以根据实验数据计算，或者在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **从入口到出口的流动路径长度** — 从端口到端口经过的距离 `1 m`（默认）| 带长度单位的标量

流体必须经过以跨越各端口的距离总和。在多程管壳式换热器中，总距离是所有壳程距离的总和。在管束、波纹板和其他流动被分成并联支路的通道中，它是单个支路中经过的距离。流动路径越长，由于壁面黏性摩擦引起的主要压力损失越陡。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 和 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **局部阻力的总等效长度** — 以长度表示的局部压力损失总和 `0.1 m`（默认）| 带长度单位的标量

以长度表示的局部压力损失总和。该长度是指所有局部阻力（如弯头、三通和管接头）在流动路径中所增加的等效长度，就好像它们的位置被一段简单的壁面延长段所替代一样。等效长度越大，由于局部阻力引起的局部压力损失越陡。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **内表面绝对粗糙度** — 壁面摩擦背后的表面凸起平均高度 `15e-6 m`（默认）| 带长度单位的标量

产生壁面摩擦的表面凸起平均高度。凸起越高，壁面越粗糙，摩擦越大，因此压力损失越陡。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，压力损失计算也依赖于该关联式。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流条件下流动截面的压力损失修正 `64`（默认）| 无量纲标量

层流条件下流动截面的压力损失修正。该参数通常称为形状因子。其与 Reynolds 数的比值给出了层流区压力损失计算中的 Darcy 摩擦因子。默认值属于圆柱形管道和管子。

某些形状的形状因子可由 Navier-Stokes 方程的解导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长导管也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的 Reynolds 数向量** — Darcy 摩擦因子查找表中每个断点处的 Reynolds 数 无量纲数值数组

Darcy 摩擦因子查找表中每个断点处的 Reynolds 数。该模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Darcy 摩擦因子。插值为 `linear`，外推为 `nearest`。

Reynolds 数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区。其数量必须等于 **Darcy friction factor vector** 参数的大小，二者结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — 雷诺数查找表中每个断点处的 Darcy 摩擦因子，无量纲数值数组

雷诺数查找表中每个断点处的 Darcy 摩擦因子。该模块对断点进行内插和外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值方法为 `linear`，外推方法为 `nearest`。

Darcy 摩擦因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，并与该参数组合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的雷诺数，无量纲数值数组

Euler 数查找表中每个断点处的雷诺数。该模块对断点进行内插和外推，以获得任意雷诺数下的 Euler 数。插值方法为 `linear`，外推方法为 `nearest`。

雷诺数必须大于零，并且必须从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Euler number vector** 参数的大小，并与该参数组合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — 雷诺数查找表中每个断点处的 Euler 数，无量纲数值数组

雷诺数查找表中每个断点处的 Euler 数。该模块对断点进行内插和外推，以获得任意雷诺数下的 Euler 数。插值方法为 `linear`，外推方法为 `nearest`。

Euler 数不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Euler number** 参数的大小，并与该参数组合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定了传热计算中应用哪些表达式以及指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **Heat transfer surface area** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认）| 单位为长度平方的标量

流体与壁面之间传热所用的有效表面积。有效表面积是一次表面积和二次表面积之和，即壁面暴露于流体部分的表面积与翅片（如果使用）表面积之和。翅片表面积通常按翅片效率因子进行缩放。

### **Gas-wall heat transfer coefficient** — 流体与壁面之间对流传热的传热系数 `100 W/(K*m^2)`（默认）| 标量

流体与壁面之间对流传热的传热系数。污垢引起的热阻在 **Fouling factor** 参数中单独体现。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer coefficient`。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m`（默认）| 带长度单位的标量

流体与壁面之间传热所经过的特征长度。该长度参与水力直径的计算，而表列传热参数化中定义的对流传热系数和雷诺数均由水力直径推导得出。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number for laminar flow heat transfer** — 层流传热中努塞尔数的假定常数值 `3.66`（默认）| 正的无量纲标量

层流传热中努塞尔数的假定常数值。努塞尔数参与流体与壁面之间对流传热系数的计算，而传热速率取决于该系数。默认值适用于圆柱形管道和圆管。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Colburn factor** — 指定 Colburn 因子数据时所对应的雷诺数值 无量纲数值数组

Colburn 因子查找表中每个断点处的雷诺数。该模块对断点进行内插和外推，以获得任意雷诺数下的 Colburn 因子。插值方法为 `linear`，外推方法为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其元素数量必须与 **Colburn factor vector** 参数的大小相等，二者结合以构成完整的表列断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — 查找表中每个断点处相对于雷诺数的 Colburn 因子 无量纲数值数组

Colburn 因子在其相对于雷诺数的查找表中每个断点处的值。该模块对断点进行内插和外推，以获得任意雷诺数下的欧拉数。插值方法为 `linear`，外推方法为 `nearest`。

Colburn 因子不得为负值，并且必须按雷诺数递增的顺序从左到右排列。其元素数量必须与 **Reynolds number vector for Colburn factor** 参数的大小相等，二者结合以构成完整的表列断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组

努塞尔数查找表中每个断点处的雷诺数。该表是二维的，以雷诺数和普朗特数作为独立坐标。该模块对断点进行内插和外推，以获得任意雷诺数下的努塞尔数。插值方法为 `linear`，外推方法为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。该向量的长度必须等于 **Nusselt number table** 参数的行数。如果该表有 *m* 行和 *n* 列，则雷诺数向量的长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组

努塞尔数查找表中每个断点处的普朗特数。该表是双向的，雷诺数和普朗特数均作为独立坐标。该模块对断点进行内插和外推，以获得任意普朗特数下的努塞尔数。插值方法为 `linear`，外推方法为 `nearest`。

普朗特数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。该向量的长度必须等于 **Nusselt number table** 参数中的列数。如果该表有 *m* 行和 *n* 列，则普朗特数向量的长度必须为 *n* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu (Re,Pr)** — 雷诺数和普朗特数查找表中每个断点处的努塞尔数 无量纲数值数组

努塞尔数在其雷诺数和普朗特数查找表中每个断点处的值。该模块对断点进行内插和外推，以获得任意雷诺数和普朗特数组合下的努塞尔数。插值方法为 `linear`，外推方法为 `nearest`。通过确定努塞尔数，该表为流体与壁面之间传热系数的计算提供输入。

努塞尔数必须大于零。它们必须按雷诺数递增的顺序从上到下排列，并按普朗特数递增的顺序从左到右排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的长度，列数必须等于 **Prandtl number vector for Nusselt number** 参数的长度。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W`（默认）| 单位为温度除以功率的标量

由污垢沉积引起的热阻度量，污垢随时间倾向于在壁面的暴露表面上积聚。这些沉积物在流体与壁面之间形成新的固体层，热量必须穿过该层，从而在传热路径中增加了额外的热阻。污垢沉积物增长缓慢，因此其引起的热阻在仿真期间假定为常数。

### **Minimum gas-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)`（默认）| 单位为功率/面积/温度的标量

流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则此下界将替代计算值。

### Controlled Fluid

### **Heat transfer surface area** — 受控流体侧的总传热表面积 `0.4 m^2`（默认）| 单位为长度平方的标量

受控流体侧的传热表面积总和

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W`（默认）| 单位为长度平方乘以温度除以功率的标量

由污垢沉积引起的热阻度量，污垢随时间倾向于在壁面的暴露表面上积聚。这些沉积物在受控流体与壁面之间形成新的固体层，热量必须穿过该层，从而在传热路径中增加了额外的热阻。污垢沉积物增长缓慢，因此其引起的热阻在仿真期间假定为常数。

### **Minimum fluid-wall heat transfer coefficient** — 流体-壁面传热系数的下界 `1 W/(m^2 * K)`（默认）| 具有功率/面积/温度单位的标量

受控流体与壁面之间传热系数的下界。如果计算返回的传热系数低于此下界，则该下界将替换计算值。

### 效应与初始条件

### **Enable Gas dynamic compressibility** — 对气体通道中压力动态进行建模的选项 `On`（默认）| `Off`

对气体通道中压力动态进行建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas nominal temperature** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的气体温度。当动态可压缩性被禁用时，该模块使用此值计算标称密度，以用于质量和能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas nominal pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的气体压力。当动态可压缩性被禁用时，该模块使用此值计算标称密度，以用于质量和能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas initial temperature** — 仿真开始时气体通道中的温度 `293.15 K`（默认）| 标量

仿真开始时气体通道中的温度。

### **Gas initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa`（默认）| 标量

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas dynamic compressibility**。
## 所属库

Simscape / Fluids / Heat Exchangers / Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：可选择对动态可压缩性建模

Heat Exchanger (G) 模块现在可以通过 **Enable dynamic compressibility** 参数选择对动态可压缩性建模。此前，该模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数可防止动态可压缩性建模。

### R2025a：对换热器壁面的热质量建模

选择 **Wall thermal dynamics** 以对换热器壁面的热质量建模。

### R2024a：Heat Exchanger (G) 模块仅对 E-NTU 建模选项建模

**Modeling option** 参数已被移除，建模选项现在是两个独立的模块。Heat Exchanger (G) 模块使用此前当 **Modeling option** 为 `E-NTU Model` 时所使用的传热模型。要使用此前当 **Modeling option** 为 `Simple model` 时所使用的模块模型，请参见 Specific Dissipation Heat Exchanger (G) 模块。

## 描述

用于具有气体和受控流量的系统的换热器

Heat Exchanger (G) 模块通过物理信号对在端口 **A1** 和 **B1** 之间流动的气体与外部*受控*流体之间的热交换进行建模。

### Heat Transfer Model

该模块的传热模型源自效能-传热单元数（Effectiveness-NTU）方法。稳态下的传热以理想速率的一个分数进行，理想速率是指若各流体均保持其入口温度，且消除其间所有热阻，理论上可支持的速率：

Q=ϵ QMax，

其中 *Q* 为实际传热速率，*Q*Max 为理想传热速率，*ε* 为带有损失的真实换热器中实际观测到的理想速率分数。该分数即为换热器效能，它是传热单元数（NTU）的函数，NTU 衡量热量在流体之间传递的容易程度相对于流体吸收该热量的容易程度：

NTU=1RCMin，

其中该分数为流体之间的总热导，*C*Min 为属于吸热能力最弱的流体中最小热容量率。流体的热容量率取决于流体的比热（*c*p）及其通过换热器的质量流量（m˙）：

C=cpm˙。

效能还取决于流体的相对布置、它们之间的程数以及各自的混合条件。这种依赖性反映在所使用的效能表达式中，不同的流动布置对应不同的表达式。有关效能表达式的列表，请参见 E-NTU Heat Transfer 模块。

该模块在传热计算中使用的流体物性为入口值与流体体积内值的平均值。

### Flow Arrangement

使用 **Flow arrangement** 模块参数设置流体在换热器中的相遇方式。流体可以彼此平行流动、彼此逆流流动或彼此交叉流动。它们也可以在加压壳体内流动，一种流体通过封装在壳体内的管道，另一种流体围绕这些相同的管道流动。图中显示了一个示例。管程流体可以单次通过壳程流体（右图所示），或者为了获得更高的换热器效能，可以多次通过（左图）。

通过基于表格化效能数据的通用参数化方法，还可以实现其他流动布置，且几乎不需要关于换热器的详细信息。流动布置、混合条件以及壳程或管程数（如果与换热器相关）假定已在表格化数据中体现。

### Mixing Condition

使用 **Cross flow type** 参数来混合每种流体、其中一种流体或不混合任何流体。此上下文中的混合是指流体在没有内部屏障（通常为指导板、折流板、翅片或壁面）的通道中的横向运动。这种运动用于消除横向平面上的温度变化。混合流体的温度仅在纵向平面上变化。未混合流体的温度在横向和纵向平面上均变化。图中显示了混合流（**i**）和未混合流（**ii**）。

混合流与未混合流之间的区别仅在叉流布置中考虑。在叉流中，一种流体中的纵向温度变化会在第二种流体中产生横向温度变化，而混合可以消除这种变化。在逆流和平行流布置中，一种流体中的纵向温度变化会在第二种流体中产生纵向温度变化，而混合在此处影响甚微，因此被忽略。

### 效能曲线

多程管壳式换热器（图中 **iv.b**-**e**，对应 2、3 和 4 程）效能最高。在单程换热器中，逆流（**ii**）效能最高，顺流（**i**）效能最低。

交叉流换热器的效能介于两者之间，混合条件是一个影响因素。当两股流体均不混合（**iii.a**）时效能最高，当两股流体均混合（**iii.b**）时效能最低。仅使热容量率最小的流体混合（**iii.c**）比仅使热容量率最大的流体混合（**iii.d**）更能降低效能。

### 热阻

总热阻 *R* 是沿传热路径各局部热阻之和。局部热阻来自壁面表面的对流、通过壁面的导热，以及如果壁面两侧有污垢，通过污垢层的导热。按从气体侧（下标 1）到受控流体侧（下标 2）的顺序表示为：

R=1U1A1+F1A1+RW+F2A2+1U2A2，

其中 *U* 是对流传热系数，*F* 是污垢系数，*A* 是传热表面积，各自对应下标所指示的流体。*R*W 是壁面的热阻。

壁面热阻和污垢系数是从模块参数获得的简单常数。传热系数是流体属性、流动几何和壁面摩擦的复杂函数，来源于雷诺数、努塞尔数和普朗特数之间的标准经验关联式。这些关联式取决于流动布置和混合条件，并在该模块模型所基于的 E-NTU Heat Transfer 模块中针对每种情况进行了详细说明。

### 壁面热质量

如果选择 **Enable wall thermal mass**，模块将对换热器壁面热质量进行建模，这会引入壁面对温度或热流变化瞬态响应的延迟。如果对热质量建模，壁面会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁面温度。模块使用该值来建模瞬态响应。你无法测量该值。

传递给每种流体的热量为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容量率。

每一侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是传热系数。

### 复合结构

该模块是由更简单的模块构建而成的复合组件。Heat Exchanger Interface (G) 模块对气体流动进行建模。热容量率和传热系数的物理信号，以及用于温度的热端口，捕获受控流动。E-NTU Heat Transfer 模块对两股流体之间通过壁面交换的热量进行建模。
