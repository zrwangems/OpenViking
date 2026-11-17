---
type: simulink-block
title: 'Battery Single Particle'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cells / Electrochemical'
documentation_page: 'batterysingleparticle'
documentation_source_path: 'ref/batterysingleparticle.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery Single Particle

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: H
  summary: 电池热质量热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与电池正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电池负极端子关联的电气守恒端口。

### **H** — 电池热质量热

与电池热质量关联的热守恒端口。
## 参数
```yaml
parameters:
- name: 所有表格的外推方法
  summary: 表格的外推方法 Nearest（默认）| Linear | Error
  group: 主
  block_parameter: ExtrapolationMethod
  values: '"nearest"（默认）| "linear" | "error"'
- name: 负极厚度
  summary: 负极的厚度 3.4E-5 m（默认）| 正标量
  group: 几何
- name: 负极电解质层数
  summary: 负极的电解质层数 10（默认）| 大于 3 的标量
  group: 几何
- name: 隔膜厚度
  summary: 隔膜的厚度 2.5E-5m（默认）| 正标量
  group: 几何
- name: 隔膜电解质层数
  summary: 隔膜的电解质层数 5（默认）| 大于 3 的标量
  group: 几何
- name: 正极厚度
  summary: 正极的厚度 8E-5m（默认）| 正标量
  group: 几何
- name: 正极电解质层数
  summary: 正极的电解质层数 10（默认）| 大于 3 的标量
  group: 几何
- name: 电极板面积
  summary: 电极板的面积 1.8E-1m^2（默认）| 正标量
  group: 几何
- name: 负极颗粒半径
  summary: 负极的颗粒半径 5E-6m（默认）| 正标量
  group: 几何
- name: 负极壳层数
  summary: 负极的壳层数 10（默认）| 大于 3 的正标量
  group: 几何
- name: 正极颗粒半径
  summary: 正极的颗粒半径 5E-8m（默认）| 正标量
  group: 几何
- name: 正极壳层数
  summary: 正极的壳层数 10（默认）| 大于 3 的正标量
  group: 几何
- name: 负极活性材料体积分数
  summary: 负极中活性材料的体积分数 0.58（默认）| 范围 (0,1) 内的标量
  group: 电极属性
- name: 正极活性材料体积分数
  summary: 正极中活性材料的体积分数 0.374（默认）| 范围 (0,1) 内的标量
  group: 电极属性
- name: 化学计量断点指定
  summary: 用于指定化学计量断点的选项 Normalized（默认）| Absolute
  group: 电极属性
- name: 归一化化学计量断点
  summary: 电极开路电位的归一化化学计量断点 linspace(0.025, 0.975, 39)（默认）| 范围 [0,1] 内元素的向量
  group: 电极属性
- name: 相对于归一化化学计量的负极开路电位
  summary: 相对于归一化化学计量的负极开路电位 [.435; .325; .259; .221; .204; .194; .179; .166; .155; .145; .137; .131; .128; .127; .126; .125;
    .124; .123; .122; .121; .118; .117; .112; .109; .105; .1; .098; .095; .094; .093; .091; .09; .089; .088; .087; .086; .085;
    .084; .083] V（默认）| 正元素向量
  group: 电极属性
- name: 相对于归一化化学计量的正极开路电位
  summary: 相对于归一化化学计量的正极开路电位 [3.598; 3.53; 3.494; 3.474; 3.46; 3.455; 3.454; 3.453; 3.4528; 3.4526; 3.4524; 3.452; 3.4518;
    3.4516; 3.4514; 3.4512; 3.451; 3.4508; 3.4506; 3.4503; 3.45; 3.4498; 3.4495; 3.4493; 3.449; 3.4488; 3.4486; 3.4484; 3.4482;
    3.4479; 3.4477; 3.4475; 3.4473; 3.447; 3.4468; 3.4466; 3.4464; 3.4462; 3.4458] V（默认）| 正元素向量
  group: 电极属性
- name: 绝对负极化学计量断点
  summary: 负极开路电位的绝对化学计量断点 linspace(0.025, 0.975, 39)（默认）| 范围 [0,1] 内元素的向量
  group: 电极属性
- name: 相对于绝对化学计量的负极开路电位
  summary: 相对于绝对化学计量的负极开路电位 [.484; .335; .253; .209; .2; .181; .165; .151; .139; .131; .128; .125; .124; .124; .123; .122;
    .119; .117; .111; .108; .101; .098; .095; .093; .092; .088; .088; .088; .088; .087; .087; .087; .085; .082; .079; .071;
    .064; .049; .026] V（默认）| 正元素向量
  group: 电极属性
- name: 绝对正极化学计量断点
  summary: 正极开路电位的绝对化学计量断点 linspace(0.025, 0.975, 39)（默认）| 范围 [0,1] 内元素的向量
  group: 电极属性
- name: 相对于绝对化学计量的正极开路电位
  summary: 相对于绝对化学计量的正极开路电位 [3.81; 3.608; 3.512; 3.478; 3.459; 3.453; 3.45257; 3.45214; 3.45171; 3.45128; 3.45085; 3.45042;
    3.44999; 3.44956; 3.44913; 3.4487; 3.44827; 3.44784; 3.44741; 3.44698; 3.44655; 3.44612; 3.44569; 3.44526; 3.44483; 3.4444;
    3.44397; 3.44354; 3.44311; 3.44268; 3.44225; 3.44182; 3.44139; 3.44096; 3.44053; 3.44; 3.412; 3.304; 2.968] V（默认）| 正元素向量
  group: 电极属性
- name: 负极最大离子浓度
  summary: 负极中的最大离子浓度 30555 mol/m^3（默认）| 正标量
  group: 电极属性
- name: 负极最大化学计量
  summary: 负极中的最大化学计量 0.811（默认）| 正标量
  group: 电极属性
- name: 负极最小化学计量
  summary: 负极中的最小化学计量 0.0132（默认）| 正标量
  group: 电极属性
- name: 正极最大离子浓度
  summary: 正极中的最大离子浓度 22806 mol/m^3（默认）| 正标量
  group: 电极属性
- name: 正极最大化学计量
  summary: 正极中的最大化学计量 0.74（默认）| 正标量
  group: 电极属性
- name: 正极最小化学计量
  summary: 正极中的最小化学计量 0.035（默认）| 正标量
  group: 电极属性
- name: 负极活性材料扩散系数
  summary: 负极中活性材料的扩散系数 3E-15 m^2/s（默认）| 正标量
  group: 电极属性
- name: 正极活性材料扩散系数
  summary: 正极中活性材料的扩散系数 5.9E-20 m^2/s（默认）| 正标量
  group: 电极属性
- name: 负极电导率
  summary: 负极的电导率 100 S/m（默认）| 正标量
  group: 电极属性
- name: 正极电导率
  summary: 正极的电导率 0.5 S/m（默认）| 正标量
  group: 电极属性
- name: 集流体电阻
  summary: 集流体的电阻 0 Ohm（默认）| 非负标量
  group: 电极属性
- name: 负极中电解质体积分数
  summary: 负极中电解质的体积分数 0.3874（默认）| 范围 (0,1) 内的标量
  group: 电解质属性
- name: 隔膜中电解质体积分数
  summary: 隔膜中电解质的体积分数 0.45（默认）| 范围 (0,1) 内的标量
  group: 电解质属性
- name: 正极中电解质体积分数
  summary: 正极中电解质的体积分数 0.5725（默认）| 范围 (0,1) 内的标量
  group: 电解质属性
- name: 电解质电导率
  summary: 电解质的电导率 0.29 S/m（默认）| 正标量
  group: 电解质属性
- name: 负极 Bruggeman 指数
  summary: 负极的 Bruggeman 指数 1.5（默认）| 大于或等于 1 的标量
  group: 电解质属性
- name: 隔膜 Bruggeman 指数
  summary: 隔膜的 Bruggeman 指数 1.5（默认）| 大于或等于 1 的标量
  group: 电解质属性
- name: 正极 Bruggeman 指数
  summary: 正极的 Bruggeman 指数 1.5（默认）| 大于或等于 1 的标量
  group: 电解质属性
- name: 迁移数
  summary: 离子在电解质中携带的总电流的分数 0.363（默认）| 范围 [0,1] 内的标量
  group: 电解质属性
- name: 电解质扩散系数
  summary: 电解质的扩散系数 2E-10 m^2/s（默认）| 正标量
  group: 电解质属性
- name: 负极电荷转移速率常数
  summary: 负极的电荷转移速率常数 8.8E-11 m^(5/2)/(mol^(1/2)*s)（默认）| 正标量
  group: 反应动力学
- name: 正极电荷转移速率常数
  summary: 正极的电荷转移速率常数 2.8E-13 m^(5/2)/(mol^(1/2)*s)（默认）| 正标量
  group: 反应动力学
- name: 电池热质量
  summary: 与热端口关联的电池热质量 77 J/K（默认）| 正标量
  group: 热
- name: Arrhenius 参考温度
  summary: Arrhenius 参考温度 298.15 K（默认）| 正标量
  group: 热
- name: 负极活性材料扩散活化能
  summary: 负极活性材料内部扩散的活化能 39000 J/mol（默认）| 正标量
  group: 热
- name: 正极活性材料扩散活化能
  summary: 正极活性材料内部扩散的活化能 35000 J/mol（默认）| 正标量
  group: 热
- name: 电解质扩散活化能
  summary: 电解质内部扩散的活化能 26600 J/mol（默认）| 正标量
  group: 热
- name: 负极传导活化能
  summary: 负极内部传导的活化能 3000 J/mol（默认）| 正标量
  group: 热
- name: 正极传导活化能
  summary: 正极内部传导的活化能 3000 J/mol（默认）| 正标量
  group: 热
- name: 电解质传导活化能
  summary: 电解质内部传导的活化能 11000 J/mol（默认）| 正标量
  group: 热
- name: 负极电荷转移活化能
  summary: 负极内部电荷转移的活化能 13000 J/mol（默认）| 正标量
  group: 热
- name: Activation energy for charge transfer in Cathode
  summary: 阴极内部电荷转移的活化能 20000 J/mol（默认）| 正标量
  group: 热
- name: Additional resistance fault
  summary: 对串联电阻进行故障设置的选项 Add fault
  group: 故障
- name: Additional resistance when faulted
  summary: 模块发生故障时的附加电阻 1e5 Ohm（默认）| 正标量
  group: 故障
- name: Trigger type
  summary: 故障触发类型 Always On（默认）| Timed | Additional triggers | Conditional | Manual
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认）| 非负标量
  group: 故障
- name: Trigger Configuration
  summary: 为放热反应故障启用附加触发类型的选项 Open fault properties
  group: 故障
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主

### **所有表格的外推方法** — 表格的外推方法 `Nearest`（默认）| `Linear` | `Error`

基于表格的参数的外推方法：

- `Linear` — 通过在已知数据末端创建切线并将其延伸到该限制之外来估计超出数据的值。
- `Nearest` — 在查询点处外推一个值，该值为最近样本网格点处的值。
- `Error` — 如果值超出已知数据，则返回错误。如果选择此选项，模块不使用外推。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ExtrapolationMethod` |
| **值：** | `"nearest"`（默认）| `"linear"` | `"error"` |

### 几何

### **负极厚度** — 负极的厚度 `3.4E-5` `m`（默认）| 正标量

负极的厚度。

### **负极电解质层数** — 负极的电解质层数 `10`（默认）| 大于 3 的标量

负极的电解质层数。

### **隔膜厚度** — 隔膜的厚度 `2.5E-5``m`（默认）| 正标量

隔膜的厚度。

### **隔膜电解质层数** — 隔膜的电解质层数 `5`（默认）| 大于 3 的标量

隔膜的电解质层数。

### **正极厚度** — 正极的厚度 `8E-5``m`（默认）| 正标量

正极的厚度。

### **正极电解质层数** — 正极的电解质层数 `10`（默认）| 大于 3 的标量

正极的电解质层数。

### **电极板面积** — 电极板的面积 `1.8E-1``m^2`（默认）| 正标量

电极板的面积。

### **负极颗粒半径** — 负极的颗粒半径 `5E-6``m`（默认）| 正标量

负极的颗粒半径。

### **负极壳层数** — 负极的壳层数 `10`（默认）| 大于 3 的正标量

负极的壳层数。

### **正极颗粒半径** — 正极的颗粒半径 `5E-8``m`（默认）| 正标量

正极的颗粒半径。

### **正极壳层数** — 正极的壳层数 `10`（默认）| 大于 3 的正标量

正极的壳层数。

### 电极属性

### **负极活性材料体积分数** — 负极中活性材料的体积分数 `0.58`（默认）| 范围 (0,1) 内的标量

负极中活性材料的体积分数。

### **正极活性材料体积分数** — 正极中活性材料的体积分数 `0.374`（默认）| 范围 (0,1) 内的标量

正极中活性材料的体积分数。

### **化学计量断点指定** — 用于指定化学计量断点的选项 `Normalized`（默认）| `Absolute`

*自 R2025a 起*

用于指定化学计量断点的选项。将此参数设置为 `Normalized` 可指定相对于相对化学计量归一化的开路电位。将此参数设置为 `Absolute` 可指定相对于绝对化学计量归一化的开路电位。

### **归一化化学计量断点** — 电极开路电位的归一化化学计量断点 `linspace(0.025, 0.975, 39)`（默认）| 范围 [0,1] 内元素的向量

电极开路电位的归一化化学计量断点。此参数的大小必须等于 **Anode open-circuit potential relative to normalized stoichiometry** 和 **Cathode open-circuit potential relative to normalized stoichiometry** 参数的大小。

**注意**

值 `0` 表示颗粒的化学计量等于电极的最小化学计量，如您在 **Anode minimum stoichiometry** 和 **Cathode minimum stoichiometry** 参数中所指定的。值 `1` 表示颗粒的化学计量等于电极的最大化学计量，如您在 **Anode maximum stoichiometry** 和 **Cathode maximum stoichiometry** 参数中所指定的。

总体而言，模块使用以下方程计算归一化化学计量的值：

NormalizedSurfaceStoichiometry = ElectrodeStoichiometry(end) - MinimumStoichiometryMaximumStoichiometry - MinimumStoichiometry。

#### 依赖关系

要启用此参数，请将 **Stoichiometry breakpoints specifications** 设置为 `Normalized`。

### **相对于归一化化学计量的负极开路电位** — 相对于归一化化学计量的负极开路电位 `[.435; .325; .259; .221; .204; .194; .179; .166; .155; .145; .137; .131; .128; .127; .126; .125; .124; .123; .122; .121; .118; .117; .112; .109; .105; .1; .098; .095; .094; .093; .091; .09; .089; .088; .087; .086; .085; .084; .083]` `V`（默认）| 正元素向量

*自 R2025a 起*

相对于归一化化学计量的负极开路电位。此参数的大小必须等于 **Normalized stoichiometry breakpoints** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Stoichiometry breakpoints specifications** 设置为 `Normalized`。

### **相对于归一化化学计量的正极开路电位** — 相对于归一化化学计量的正极开路电位 `[3.598; 3.53; 3.494; 3.474; 3.46; 3.455; 3.454; 3.453; 3.4528; 3.4526; 3.4524; 3.452; 3.4518; 3.4516; 3.4514; 3.4512; 3.451; 3.4508; 3.4506; 3.4503; 3.45; 3.4498; 3.4495; 3.4493; 3.449; 3.4488; 3.4486; 3.4484; 3.4482; 3.4479; 3.4477; 3.4475; 3.4473; 3.447; 3.4468; 3.4466; 3.4464; 3.4462; 3.4458]` `V`（默认）| 正元素向量

*自 R2025a 起*

相对于归一化化学计量的正极开路电位。此参数的大小必须等于 **Normalized stoichiometry breakpoints** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Stoichiometry breakpoints specifications** 设置为 `Normalized`。

### **绝对负极化学计量断点** — 负极开路电位的绝对化学计量断点 `linspace(0.025, 0.975, 39)`（默认）| 范围 [0,1] 内元素的向量

*自 R2025a 起*

负极开路电位的绝对化学计量断点。此参数的大小必须等于 **Anode open-circuit potential relative to absolute stoichiometry** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Stoichiometry breakpoints specifications** 设置为 `Absolute`。

### **相对于绝对化学计量的负极开路电位** — 相对于绝对化学计量的负极开路电位 `[.484; .335; .253; .209; .2; .181; .165; .151; .139; .131; .128; .125; .124; .124; .123; .122; .119; .117; .111; .108; .101; .098; .095; .093; .092; .088; .088; .088; .088; .087; .087; .087; .085; .082; .079; .071; .064; .049; .026]` `V`（默认）| 正元素向量

*自 R2025a 起*

相对于绝对化学计量的负极开路电位。此参数的大小必须等于 **Absolute anode stoichiometry breakpoints** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Stoichiometry breakpoints specifications** 设置为 `Absolute`。

### **绝对正极化学计量断点** — 正极开路电位的绝对化学计量断点 `linspace(0.025, 0.975, 39)`（默认）| 范围 [0,1] 内元素的向量

*自 R2025a 起*

正极开路电位的绝对化学计量断点。此参数的大小必须等于 **Cathode open-circuit potential relative to absolute stoichiometry** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Stoichiometry breakpoints specifications** 设置为 `Absolute`。

### **相对于绝对化学计量的正极开路电位** — 相对于绝对化学计量的正极开路电位 `[3.81; 3.608; 3.512; 3.478; 3.459; 3.453; 3.45257; 3.45214; 3.45171; 3.45128; 3.45085; 3.45042; 3.44999; 3.44956; 3.44913; 3.4487; 3.44827; 3.44784; 3.44741; 3.44698; 3.44655; 3.44612; 3.44569; 3.44526; 3.44483; 3.4444; 3.44397; 3.44354; 3.44311; 3.44268; 3.44225; 3.44182; 3.44139; 3.44096; 3.44053; 3.44; 3.412; 3.304; 2.968]` `V`（默认）| 正元素向量

*自 R2025a 起*

相对于绝对化学计量的正极开路电位。此参数的大小必须等于 **Absolute cathode stoichiometry breakpoints** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Stoichiometry breakpoints specifications** 设置为 `Absolute`。

### **负极最大离子浓度** — 负极中的最大离子浓度 `30555` `mol/m^3`（默认）| 正标量

负极中的最大离子浓度。

### **负极最大化学计量** — 负极中的最大化学计量 `0.811`（默认）| 正标量

负极中的最大化学计量。此参数的值必须大于 **Anode minimum stoichiometry** 参数的值。

### **负极最小化学计量** — 负极中的最小化学计量 `0.0132`（默认）| 正标量

负极中的最小化学计量。此参数的值必须小于 **Anode maximum stoichiometry** 参数的值。

### **正极最大离子浓度** — 正极中的最大离子浓度 `22806` `mol/m^3`（默认）| 正标量

正极中的最大离子浓度。

### **正极最大化学计量** — 正极中的最大化学计量 `0.74`（默认）| 正标量

正极中的最大化学计量。此参数的值必须大于 **Cathode minimum stoichiometry** 参数的值。

### **正极最小化学计量** — 正极中的最小化学计量 `0.035`（默认）| 正标量

正极中的最小化学计量。此参数的值必须小于 **Cathode maximum stoichiometry** 参数的值。

### **负极活性材料扩散系数** — 负极中活性材料的扩散系数 `3E-15` `m^2/s`（默认）| 正标量

负极中活性材料的扩散系数。

### **正极活性材料扩散系数** — 正极中活性材料的扩散系数 `5.9E-20` `m^2/s`（默认）| 正标量

正极中活性材料的扩散系数。

### **负极电导率** — 负极的电导率 `100` `S/m`（默认）| 正标量

负极的电导率。

### **正极电导率** — 正极的电导率 `0.5` `S/m`（默认）| 正标量

正极的电导率。

### **集流体电阻** — 集流体的电阻 `0` `Ohm`（默认）| 非负标量

集流体的电阻。

### 电解质属性

### **负极中电解质体积分数** — 负极中电解质的体积分数 `0.3874`（默认）| 范围 (0,1) 内的标量

负极中电解质的体积分数。

### **隔膜中电解质体积分数** — 隔膜中电解质的体积分数 `0.45`（默认）| 范围 (0,1) 内的标量

隔膜中电解质的体积分数。

### **正极中电解质体积分数** — 正极中电解质的体积分数 `0.5725`（默认）| 范围 (0,1) 内的标量

正极中电解质的体积分数。

### **电解质电导率** — 电解质的电导率 `0.29` `S/m`（默认）| 正标量

电解质的电导率。

### **负极 Bruggeman 指数** — 负极的 Bruggeman 指数 `1.5`（默认）| 大于或等于 1 的标量

负极的 Bruggeman 指数。

### **隔膜 Bruggeman 指数** — 隔膜的 Bruggeman 指数 `1.5`（默认）| 大于或等于 1 的标量

隔膜的 Bruggeman 指数。

### **正极 Bruggeman 指数** — 正极的 Bruggeman 指数 `1.5`（默认）| 大于或等于 1 的标量

正极的 Bruggeman 指数。

### **迁移数** — 离子在电解质中携带的总电流的分数 `0.363`（默认）| 范围 [0,1] 内的标量

离子在电解质中携带的总电流的分数。

### **电解质扩散系数** — 电解质的扩散系数 `2E-10` `m^2/s`（默认）| 正标量

模块在 Fick 定律方程中使用的电解质扩散系数。

### 反应动力学

### **负极电荷转移速率常数** — 负极的电荷转移速率常数 `8.8E-11` `m^(5/2)/(mol^(1/2)*s)`（默认）| 正标量

负极的电荷转移速率常数。模块在 Butler-Volmer 方程中使用此值来模拟电极-电解质界面处的电化学动力学。

### **正极电荷转移速率常数** — 正极的电荷转移速率常数 `2.8E-13` `m^(5/2)/(mol^(1/2)*s)`（默认）| 正标量

正极的电荷转移速率常数。模块在 Butler-Volmer 方程中使用此值来模拟电极-电解质界面处的电化学动力学。

### 热

### **电池热质量** — 与热端口关联的电池热质量 `77` `J/K`（默认）| 正标量

热端口 **H** 处的热质量。此参数表示将热端口温度升高一开尔文所需的能量。

### **Arrhenius 参考温度** — Arrhenius 参考温度 `298.15` `K`（默认）| 正标量

Arrhenius 参考温度。

### **负极活性材料扩散活化能** — 负极活性材料内部扩散的活化能 `39000` `J/mol`（默认）| 正标量

负极活性材料内部扩散的活化能。

### **正极活性材料扩散活化能** — 正极活性材料内部扩散的活化能 `35000` `J/mol`（默认）| 正标量

正极活性材料内部扩散的活化能。

### **电解质扩散活化能** — 电解质内部扩散的活化能 `26600` `J/mol`（默认）| 正标量

电解质内部扩散的活化能。

### **负极传导活化能** — 负极内部传导的活化能 `3000` `J/mol`（默认）| 正标量

负极内部传导的活化能。

### **正极传导活化能** — 正极内部传导的活化能 `3000` `J/mol`（默认）| 正标量

正极内部传导的活化能。

### **电解质传导活化能** — 电解质内部传导的活化能 `11000` `J/mol`（默认）| 正标量

电解质内部传导的活化能。

### **负极电荷转移活化能** — 负极内部电荷转移的活化能 `13000` `J/mol`（默认）| 正标量

负极内部电荷转移的活化能。

### **Activation energy for charge transfer in Cathode** — 阴极内部电荷转移的活化能 `20000` `J/mol`（默认）| 正标量

阴极内部电荷转移的活化能。

### 故障

### **Additional resistance fault** — 对串联电阻进行故障设置的选项 `Add fault`

*自 R2025a 起*

对串联电阻进行故障设置的选项。使用此故障可在附加电阻大于 1000 ohm 时对开路电池建模，或对异常内阻建模。

要添加故障，请点击 **Add fault** 超链接。

### **Additional resistance when faulted** — 模块发生故障时的附加电阻 `1e5` `Ohm`（默认）| 正标量

*自 R2025a 起*

模块处于故障状态时的附加电阻值。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 故障触发类型 `Always On`（默认）| `Timed` | `Additional triggers` | `Conditional` | `Manual`

*自 R2025a 起*

触发类型。请选择以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Additional triggers` — 由于模块对话框中不可用的附加触发器而注入故障。选择此选项并点击 **Open fault properties** 超链接，以在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 由于反映与信号相关行为的条件而注入故障。条件在每个时间步计算 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的其余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

*自 R2025a 起*

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Trigger Configuration** — 为放热反应故障启用附加触发类型的选项 `Open fault properties`

*自 R2025a 起*

启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请点击 **Additional resistance fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Additional Triggers`。
## 所属库

Simscape / Battery / Cells

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a: Inject additional resistance fault and configure fault behaviors

Battery Single Particle 模块现在支持用于故障建模的新接口。此接口将系统模型文件与存储故障信息的文件分开。当附加串联电阻较高（大于 1000 ohm）或存在异常内阻时，您可以系统地将故障建模为开路电池。您还可以安全地将标称模型行为与故障模型行为分开，以避免安全任务干扰设计任务。有关更多信息，请参阅 Introduction to Simscape Faults。

### R2025a: Specify open-circuit potentials normalized to absolute stoichiometry

新的 **Stoichiometry breakpoints specification** 参数允许您指定归一化为相对或绝对化学计量比的电极开路电位。要指定归一化为绝对化学计量比的开路电位，请将 **Stoichiometry breakpoints specification** 设置为 `Absolute`。然后，模块会公开以下四个参数：

- **Absolute anode stoichiometry breakpoints**
- **Anode open-circuit potential relative to absolute stoichiometry**
- **Absolute cathode stoichiometry breakpoints**
- **Cathode open-circuit potential relative to absolute stoichiometry**

## 描述

单粒子方法的电池模型

Battery Single Particle 模块使用单粒子模型表示电池。此实现考虑了液相电解质和固相电极中的欧姆过电位和传质过电位。此外，它还考虑了反应动力学和集流体电阻。

该电池包括两个电极，即阳极和阴极，以及电极之间的多孔隔膜。在此模块中，*anode* 指放电期间的负电极，*cathode* 指放电期间的正电极。该模块在一维框架中对电极和电解质的欧姆过电位，以及从阳极集流体到阴极集流体的电池横截面上的浓度进行建模。

此图展示了放电期间电解质中的代表性浓度。该模型包括阳极（*x*=[0 …
*L*-]）、隔膜（*x*=[*L*- …
*L*-+*L*sep]）和阴极（*x*=[*L*-+*L*sep…
*L*-+*L*sep+*L*+]）。

放电期间电解质中的代表性浓度。该模型包括阳极、隔膜和阴极。

该模块在径向维度 *r* 上的代表性球形粒子中计算电极中的浓度。此图展示了电池连续放电期间代表性粒子中的浓度梯度：

电池连续放电期间代表性粒子中的浓度梯度。

### Species Conservation in Solid Phase

当模块处于固相时，单粒子方法将正电极和负电极建模为单个代表性球形粒子。

**Note**

这些方程中的上标指相应的电极。*+* 上标指阴极。*-* 上标指阳极。*sep* 上标指隔膜。*±* 上标表示该方程同时适用于阳极和阴极。例如，*c+s* 是阴极的固相浓度，*c-s* 是阳极的固相浓度。

此方程使用 Fick 定律描述负电极或正电极中阳离子的浓度 *c*。该模块仅使用径向坐标来计算电极中的浓度。球形粒子中的扩散驱动质量传递，

∂cs±∂t(r,t)=∂∂r[Ds±∂cs±∂r(r,t)],

其中：

- *cs* 是固相浓度。
- *Ds* 是固相中的扩散系数。
- *r* 是半径。
- *t* 是时间。

在粒子中心，浓度梯度等于 0：

Ds±∂cs±∂r(0,t)=0.

此方程计算粒子表面的离子浓度梯度：

Ds±∂cs±∂r(Rs±,t)=∓Js±as± F.

在此方程中，*F* 是法拉第常数，*J* 是摩尔通量，

J±(t)=I(t)A L±,

其中：

- *I* 是施加到电池的电流。
- *A* 是集流体的总面积。
- *L* 是相应电极的长度。

此外，*a* 是每电极单位体积的活性表面积，

a±=3ε±R±,

其中：

- *ε* 是电极的活性材料分数。
- *R* 是活性粒子的总半径。

为求解微分方程，Battery Single Particle 模块将半径为 *R* 的粒子离散为 *n* 个壳层。每个壳层与相邻球体的径向距离等于 δr=Rn。

对于第 *i* 个球体，此方程计算浓度变化率 *δc/δt*：

c˙si=Dsδr2{(i−1i)csi−1−2csi+(i+1i)csi+1}.

对于粒子中最内层的壳层，该模块实现以下边界条件：

c˙1=2Dsδr2{cs2−cs1}.

为实现粒子表面的边界条件，该模块在表面周围添加一个附加节点。该模块不计算此节点的浓度，因为它在物理上不存在。该模块使用此节点，通过 Neumann 边界条件计算粒子中最外层壳层与其周围不存在的壳层之间的边界条件。此方程描述了粒子表面的离散化结果：

c˙send=2Dsδr2{csend−1−csend}−2n+1nJF A δr.

### Mass Transport Overpotential in Solid Phase

当模块处于固相时，开路电位取决于浓度。为计算电极处的传质过电位，Battery Single Particle 模块从粒子表面平均相对浓度的开路电位中减去粒子中平均相对浓度的开路电位，

η±diffusion,s=ocp±(cs,surface,relative±)−ocp±(c¯s,relative±),

其中：

- *η*diffusion,*s* 是固相传质过电位。
- *ocp(cs*,surface,relative*)* 是粒子表面浓度的开路电位。
- *ocp(cs*relative*)* 是粒子平均浓度的开路电位。

该模块使用相同的方程计算阳极和阴极的传质过电位。

### Ohmic Overpotential in Solid Phase

为计算模块处于固相时的欧姆过电位，Battery Single Particle 模块将电极上的电流和集流体处的电流线性近似为等于施加到电池的电流的值。电流隔膜与电极之间界面处的电流为零。此方程定义了固相中的欧姆过电位，

η±ohmic,s=Ibatt2A∗L±κ±,

其中：

- *ηohmic,s* 是固相欧姆过电位。
- *Ibatt/A* 是电池横截面。
- *L* 是相应电极的长度，取决于阳极或阴极的厚度。
- *κ* 是电导率。电导率取决于电池温度。当模块计算阳极的欧姆过电位时，*κ* 等于 **Anode conductivity** 参数；当模块计算阴极的欧姆过电位时，*κ* 等于 **Cathode conductivity** 参数。

该模块使用相同的方程计算阳极和阴极在固相中的欧姆过电位。

### 液相中的物质守恒

当模块处于液相时，该方程描述电解质在两端电极和隔膜中的浓度。为了计算隔膜中的浓度，模块考虑由浓度梯度引起的扩散流，

∂cε±∂t(x,t)=∂∂x[Dε∂cε±∂x(x,t)],

其中：

- *cε* 是电解质中的浓度。
- *Dε* 是液相中的扩散系数。
- *x* 是电池厚度方向上的位置，从负极集流体到正极集流体。
- *t* 是时间。

在正极和负极处，模块同时考虑扩散流和从固体电极进入电解质的阳离子通量，

∈ε±∂cε±∂t(x,t)=∂∂x[Dεeff∂cε±∂x(x,t)±(1−t+0)JF],

其中：

- *∈* 是电解质的体积分数。
- *Deffε* 是考虑材料孔隙率的液相扩散系数。液体电解质的扩散率取决于周围固体电极材料的性质。电极由多种组分构成，例如活性材料和填料，它们形成特征性的多孔材料。
- *J* 是摩尔通量。
- *t+* 是阳离子的迁移数。
- *F* 是法拉第常数。

由于电解质是连续流体，负极和正极与隔膜交界处的阳离子浓度必须相等。对于负极-隔膜和正极-隔膜界面处电解质中的浓度，模块必须定义电池三个部分之间的边界条件。模块将两个电极和隔膜都表示为长方体。

该模块将电解质视为跨电极和隔膜的连续介质。由于界面两侧的浓度必须相等，因此电极与隔膜之间的界面存在连续性边界条件。

该方程描述负极与隔膜之间界面处浓度的连续性边界条件，

cε−(L−,t)=cεsep(L−,t),

其中：

- cε−(L−,t) 是负极与隔膜交界处负极中的浓度。
- cεsep(L−,t) 是负极与隔膜交界处隔膜中的浓度。

该方程描述隔膜与正极之间界面处浓度的连续性边界条件，

cεsep(L−+Lsep,t)=cε+(L−+Lsep,t),

其中：

- cεsep(L−+Lsep,t) 是隔膜与正极交界处隔膜中的浓度。
- cε+(L−+Lsep,t) 是隔膜与正极交界处正极中的浓度。

模块还对电极与隔膜之间的界面施加通量边界条件。界面两侧的通量必须相等，

Deff−∂cε−∂x(L−,t)=Deffsep∂cεsep∂x(L−,t)Deff+∂cε+∂x(L−+Lsep,t)=Deffsep∂cεsep∂x(L−+Lsep,t)

其中：

- Deff− 是负极的扩散系数。
- Deff+ 是正极的扩散系数。
- Deffsep 是隔膜的扩散系数。
- ∂cε−∂x(L−,t) 是负极与隔膜交界处负极的浓度梯度。
- ∂cεsep∂x(L−,t) 是负极与隔膜交界处隔膜的浓度梯度。
- ∂cε+∂x(L−+Lsep,t) 是正极与隔膜交界处正极的浓度梯度。
- ∂cεsep∂x(L−+Lsep,t) 是正极与隔膜交界处隔膜的浓度梯度。

该方程指定电极与集流体之间边界处的浓度。通量与集流体处的通量成正比，而集流体处的通量等于零，因为模块不在该处存储任何离子。因此界面处的合成通量为零，

∂cε−∂x(0,t)=∂cε+∂x(L−+Lsep+L+,t)=0,

其中：

- ∂cε−∂x(0,t) 是负极与最左侧集流体交界处负极的浓度梯度。
- ∂cε+∂x(L−+Lsep+L+,t) 是正极与最右侧集流体交界处正极的浓度梯度。

与固相类似，模块通过将电解质划分为 *n* 个等尺寸区段来求解微分方程。该方程表示第 *i* 个区段中的浓度，区段间距为 *δx*，且对所有 [1,Ms-1] 区段有效：

∂cε∂t(x,t)=Dε,eff±ci+1+ci−1−2ci∂x2+(1−t+0)JF.

模块使用以下方程对隔膜进行离散化：

∂cε∂t(x,t)=Dε,effsepci+1+ci−1−2ciδx2.

为了计算电极与隔膜之间界面处的浓度，模块应用所有边界条件。例如，对于负极与隔膜之间的界面，模块应用以下方程：

cε,i=1sep=εε−εεsepcε,i=0−cε,i=−1sep∂x∂x−cε,i=0.

### 液相中的质量传输过电位

当模块处于液相时，它使用集流体与负极之间界面处以及正极与集流体之间界面处的浓度，通过以下方程计算电解质中的质量传输过电位，

ηdiffusion,ε=2RTF(1−tε0)lncε(L−+Lsep+L+,t)cε(0,t),

其中：

- *R* 是通用气体常数。
- *T* 是温度。
- *F* 是法拉第常数。

### 液相中的欧姆过电位

当模块处于液相时，它通过对电池每个区段中的离子电流进行线性近似来计算欧姆过电位。对于电极，与集流体界面处的离子电流为零。在与隔膜的界面处，离子电流等于电池的电流，*Ibatt*。在隔膜中，模块将离子电流近似为常数，且等于施加到电池的电流。模块使用以下方程计算欧姆过电位

ηohmic,ε=−Ibatt2A∗(L+κeff++2Lsepκeffsep+L−κeff−),

其中 *κeff* 是模块使用 Bruggeman 系数计算的有效电导率。有关有效参数的更多信息，请参阅有效电解质属性部分。

### 电荷转移过电位

为了对电荷转移过电位进行建模，该模块使用 Butler-Volmer 方程。Butler-Volmer 方程描述电流密度 *j* 与过电位 *η* 之间的关系，其中过电位是实际电极电位与热力学平衡电位之间的差值。Butler-Volmer 方程为

J±(t)=j0,k(t)[exp(αnεFRTη±(t))−exp(−(1−α)nεFRTη±(t))],

其中：

- *α* 是氧化和还原的电荷转移系数。
- *j0* 是交换电流密度。

求解电极过电位的方程得到以下方程：

ηkinetic,s=RTαFln(ξ±+(ξ±)2+1)ξ±=j±2a±i0±

*i±0* 是负极和正极中的交换电流密度，等于

i0±=k±[c¯ε±(cs,max±−cs,surf±)cs,surf±]α,

其中：

- *k* 是电荷转移速率常数，对于负极等于 **Charge transfer rate constant for Anode** 参数的值，对于正极等于 **Charge transfer rate constant for Cathode** 参数的值。
- c¯ε± 是平均电解质浓度。
- *cs,max* 是最大电极浓度。
- *cs,surf* 是电极表面浓度。

为了计算整个电池的动力学过电位，模块从正极的动力学过电位中减去负极的动力学过电位：

ηkinetic,s=η+kinetic,s−η−kinetic,s.

### 集流体电阻

该模块将集流体电阻建模为单个电阻。您可以通过指定 **Current collector resistance** 参数来设置集流体电阻。

### 电池电压

为了对电池电压进行建模，该模块考虑每个电极表面的电位、过电位以及由集流体电阻引起的电压损失，使用以下方程

V(t)=ocp+(csurface,relative+)−ocp−(csurface,relative−)+ηdiffusion,ε+ηohmic,ε+ηkinetic,s+ηohmic−+ηohmic++IbattRCurrentCollector,

其中：

- *ocp+(c+surface,relative)* 是正极颗粒表面浓度对应的开路电位。
- *ocp-(c-surface,relative)* 是负极颗粒表面浓度对应的开路电位。
- *η*diffusion,ε 是电解质中的质量传输过电位。
- *η*ohmic,ε 是电解质中的欧姆过电位。
- *η*kinetic,s 是电极中的电荷转移过电位。
- *η*-ohmic 是负极中的欧姆过电位。
- *η*+ohmic 是正极中的欧姆过电位。
- *I*batt 是电池电流。
- *R*CurrentCollector 是集流体的电阻。

您可以通过使用归一化或绝对化学计量断点将开路电位参数化为表格数据：

- 如果将 **Stoichiometry breakpoints specification** 参数设置为 `Normalized`，则通过设置 **Anode open-circuit potential**、**Cathode open-circuit potential** 和 **Normalized stoichiometry breakpoints** 参数来指定归一化到相对化学计量的开路电位。负极和正极的化学计量断点相同。
- 如果将 **Stoichiometry breakpoints specification** 参数设置为 `Absolute`，则指定归一化到绝对化学计量的开路电位。使用此选项，您可以通过设置 **Absolute anode stoichiometry breakpoints** 和 **Absolute cathode stoichiometry breakpoints** 参数来分别指定负极和正极的化学计量断点。*(自 R2025a 起)*

为了计算相对浓度，模块考虑每个电极的最大浓度以及最大和最小化学计量。**Anode maximum ion concentration** 和 **Cathode maximum ion concentration** 参数表示每个电极理论上可能的最大浓度。为了获得可达到的最大和最小浓度，模块将这些参数的值分别与 **Anode maximum stoichiometry**、**Anode minimum stoichiometry**、**Cathode maximum stoichiometry** 和 **Cathode minimum stoichiometry** 参数的值相乘。然后，模块使用以下方程计算相对浓度

cs,relative=cscs,max−ΝminΝmax−Νmin,

其中：

- *cs*,max 是最大浓度。
- *N*max 是最大化学计量。
- *N*min 是最小化学计量。

### 有效电解质属性

根据您要建模的多孔电极的微观结构设置这些参数的值：

- **Diffusion coefficient of electrolyte** — 将此参数设置为影响电解质中质量传输的电解质扩散系数的值。
- **Electrolyte conductivity** — 将此参数设置为电解质的电导率的值。

为了对该依赖性进行建模，该模块使用 Bruggeman 关联式，

Parametereffective=Parameterblock∗φεα,

其中：

- *φε* 是电解质的体积分数。该值相应地等于 **Volume fraction of electrolyte in anode**、**Volume fraction of electrolyte in separator** 和 **Volume fraction of electrolyte in cathode** 参数的值。
- *α* 是 Bruggeman 指数。该值相应地等于 **Anode Bruggeman exponent**、**Separator Bruggeman exponent** 和 **Cathode Bruggeman exponent** 参数的值。

### 热

模块将整个电池的温度视为常数。以下模块参数取决于电池的温度：

- **Diffusion coefficient of anode active material** 和 **Diffusion coefficient of cathode active material** — 这些参数是影响电极中质量传输的电极扩散系数。
- **Diffusion coefficient of electrolyte** — 该参数是影响电解质中质量传输的电解质扩散系数。
- **Electrolyte conductivity** — 该参数是电解质的电导率。
- **Anode conductivity** 和 **Cathode conductivity** — 这些参数是电极的电导率。
- **Charge transfer rate constant for Anode** 和 **Charge transfer rate constant for Cathode** — 这些参数是电极的电荷转移速率常数。

为了计算这些参数的温度调整值，模块使用 Arrhenius 方程，

ParameterT-adjusted=Parameterblock∗eEaR(1Tref−1T),

其中：

- *Parameterblock* 是温度相关参数的值。
- *Ea* 是活化能，等于 **Thermal** 设置中活化能参数的值。
- *Tref* 是 **Arrhenius reference temperature** 参数的值。
- *T* 是电池温度。

### 电池发热

该模块将电池建模为集总热质量。单颗粒模型使用以下方程计算过电位在电池中引起的不可逆发热：

Q=Ibatt(ηdiffusion,ε+ηohmic,ε+ηohmic,s−+ηohmic,s++IbattRCurrentCollector+ηkinetic,s+η+diffusion+η−diffusion).

### 模型故障

*自 R2025a 起*

要对 Battery Single Particle 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

当附加串联电阻较高（大于 1000 欧姆）或存在异常内阻时，Battery Single Particle 模块将该故障建模为开路电池。

**故障触发器**

您通过 **Trigger Type** 参数指定故障发生的方式和时间。

如果将 **Trigger Type** 参数设置为 `Timed`，则当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，Battery Single Particle 模块触发故障事件。

如果将 **Trigger Type** 设置为 `Conditional`，您可以选择 Battery Single Particle 模块中的故障是否可逆 *(自 R2025a 起)*。要对不可逆故障进行建模，请单击 **Open fault properties** 打开 Property Inspector，然后选中 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障进行建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。

有关向模块添加故障和指定故障触发器的更多信息，请参阅 Introduction to Simscape Faults。

### 公共变量

您可以使用 Probe 模块在 Battery Single Particle 模块中访问这些变量。单位均为默认值。

- `anodeModel.averageStoichiometry` — 负极中的平均化学计量比。
- `anodeModel.massTransportOverpotential` — 质量传输过电位，单位为伏特。
- `anodeModel.normalizedAverageStoichiometry` — 归一化到最小值和最大值的平均化学计量比。
- `anodeModel.normalizedSurfaceStoichiometry` — 归一化到最小值和最大值的表面化学计量比。
- `anodeModel.ohmicOverpotential` — 负极的欧姆过电位，单位为伏特。
- `anodeModel.shellConcentration` — 所建模壳层的浓度，单位为 mol/m^3。壳层数等于 **Anode Shell Count** 参数的值。
- `anodeModel.shellStoichiometry` — 所建模壳层的化学计量比。壳层数等于 **Anode Shell Count** 参数的值。
- `anodeModel.surfaceConcentration` — 颗粒表面的浓度，单位为 mol/m^3。
- `anodeModel.surfacePotential` — 颗粒表面的电位，单位为伏特。
- `anodeModel.temperatureAdjustedConductivity` — 根据电池温度调整后的电导率，单位为 S/m。
- `anodeModel.temperatureAdjustedDiffusionCoefficient` — 根据电池温度调整后的扩散系数，单位为 m^2/s。
- `averageElectrolyteConcentration` — 颗粒中的平均浓度，单位为 mol/m^3。
- `batteryCurrent` — 通过电池端子测得的总电流，单位为安培。
- `batteryTemperature` — 模块用于电阻和开路电压查表的电池平均温度。如果将 **Thermal model** 参数设置为 `Constant temperature`，则 `batteryTemperature` 变量等于指定的温度值。如果将 **Thermal model** 参数设置为 `Lumped thermal mass`，则 `batteryTemperature` 变量是一个在仿真过程中变化的微分状态。
- `batteryVoltage` — 电池端子电压，即正极端子与负极端子之间的电压差，单位为伏特。
- `cathodeModel.averageStoichiometry` — 正极中的平均化学计量比。
- `cathodeModel.massTransportOverpotential` — 质量传输过电位，单位为伏特。
- `cathodeModel.normalizedAverageStoichiometry` — 归一化到最小值和最大值的平均化学计量比。
- `cathodeModel.normalizedSurfaceStoichiometry` — 归一化到最小值和最大值的表面化学计量比。
- `cathodeModel.ohmicOverpotential` — 正极的欧姆过电位，单位为伏特。
- `cathodeModel.shellConcentration` — 所建模壳层的浓度，单位为 mol/m^3。壳层数等于 **Anode Shell Count** 参数的值。
- `cathodeModel.shellStoichiometry` — 所建模壳层的化学计量比。壳层数等于 **Anode Shell Count** 参数的值。
- `cathodeModel.surfaceConcentration` — 颗粒表面的浓度，单位为 mol/m^3。
- `cathodeModel.surfacePotential` — 颗粒表面的电位，单位为伏特。
- `cathodeModel.temperatureAdjustedConductivity` — 根据电池温度调整后的电导率，单位为 S/m。
- `cathodeModel.temperatureAdjustedDiffusionCoefficient` — 根据电池温度调整后的扩散系数，单位为 m^2/s。
- `electrolyteModel.averageConcentration` — 整个电池中电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.averageConcentrationAnode` — 负极内部电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.averageConcentrationCathode` — 正极内部电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.averageConcentrationSeparator` — 隔膜内部电解质的平均浓度，单位为 mol/m^3。
- `electrolyteModel.concentrationAnode` — 负极中电解质所建模层的浓度，单位为 mol/m^3。元素数等于 **Electrolyte layer count of anode** 参数。
- `electrolyteModel.concentrationCathode` — 正极中电解质所建模层的浓度，单位为 mol/m^3。元素数等于 **Electrolyte layer count of cathode** 参数。
- `electrolyteModel.concentrationSeparator` — 隔膜中电解质所建模层的浓度，单位为 mol/m^3。元素数等于 **Electrolyte layer count of electrolyte** 参数。
- `electrolyteModel.currentDensityAnode` — 负极中的电流密度，单位为 A/m^3。
- `electrolyteModel.currentDensityCathode` — 正极中的电流密度，单位为 A/m^3。
- `electrolyteModel.diffusionCoefficientAnode` — 负极中电解质的温度调整有效扩散系数，单位为 m^s/s。
- `electrolyteModel.diffusionCoefficientCathode` — 正极中电解质的温度调整有效扩散系数，单位为 m^s/s。
- `electrolyteModel.diffusionCoefficientSeparator` — 隔膜中电解质的温度调整有效扩散系数，单位为 m^s/s。
- `electrolyteModel.conductivityAnode` — 负极中电解质的温度调整有效电导率，单位为 S/m。
- `electrolyteModel.conductivityCathode` — 正极中电解质的温度调整有效电导率，单位为 S/m。
- `electrolyteModel.effectiveConductivitySeparator` — 隔膜中电解质的温度调整有效电导率，单位为 S/m。
- `electrolyteModel.massTransportOverpotential` — 电解质的质量传输过电位，单位为伏特。
- `electrolyteModel.ohmicOverpotential` — 电解质的欧姆过电位，单位为伏特。
- `electrolyteModel.temperatureAdjustedConductivity` — 电解质的温度调整电导率，单位为 S/m。
- `electrolyteModel.temperatureAdjustedDiffusionCoefficient` — 电解质的温度调整扩散系数，单位为 m^s/s。
- `heatGenerationRate` — 电池总产热速率，单位为瓦特。模块通过将电阻损耗和可逆热贡献相加来计算产热速率。
- `power_dissipated` — 电阻产热速率或耗散功率，单位为瓦特。
- `reactionKineticsModel.chargeTransferOverpotential` — 电池的电荷转移过电位，单位为伏特。
- `reactionKineticsModel.exchangeCurrentDensityAnode` — 负极中的交换电流密度，单位为 C/(m^2\*s)。
- `reactionKineticsModel.exchangeCurrentDensityCathode` — 正极中的交换电流密度，单位为 C/(m^2\*s)。
- `reactionKineticsModel.temperatureAdjustedChargeTransferRateAnode` — 负极的温度调整电荷转移速率常数，单位为 m^(5/2)/(mol^(1/2) \* s)。
- `reactionKineticsModel.temperatureAdjustedChargeTransferRateCathode` — 正极的温度调整电荷转移速率常数，单位为 m^(5/2)/(mol^(1/2) \* s)。
- `stateOfCharge` — 通过库仑计数获得的电池荷电状态。
- `thermalModel.batteryTemperature` — 电池温度，单位为 K。
- `thermalModel.cellTemperature` — 电芯输出的温度。
- `thermalModel.heatDissipationRate` — 电池散热速率，单位为瓦特。
- `thermalModel.heatGeneration` — 电池产生的热量，单位为瓦特。
- `thermalModel.thermalMass` — 电池的热质量，单位为 J/K。
