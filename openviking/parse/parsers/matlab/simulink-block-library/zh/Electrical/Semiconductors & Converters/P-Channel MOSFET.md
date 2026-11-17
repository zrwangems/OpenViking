---
type: simulink-block
title: 'P-Channel MOSFET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pchannelmosfet'
documentation_source_path: 'ref/pchannelmosfet.html'
language: zh-CN
chinese_source: worker-translation
---

# P-Channel MOSFET

## 端口
```yaml
ports:
- name: G
  summary: 栅极端子电气
  direction: conserving
- name: D
  summary: 漏极端子电气
  direction: conserving
- name: S
  summary: 源极端子电气
  direction: conserving
- name: B
  summary: 体极端子电气
  direction: conserving
- name: H
  summary: 热端口热
  direction: conserving
```

### 守恒端口

### **G** — 栅极端子电气

与晶体管栅极端子关联的电气守恒端口。

### **D** — 漏极端子电气

与晶体管漏极端子关联的电气守恒端口。

### **S** — 源极端子电气

与晶体管源极端子关联的电气守恒端口。

### **B** — 体极端子电气

与晶体管体极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of terminals** 设置为
`Four`。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Threshold-based with thermal` 或
`Surface-potential-based with thermal`。
## 参数
```yaml
parameters:
- name: Modeling Option
  summary: MOSFET 表示方式 Threshold-based（默认）| Threshold-based with thermal | Surface-potential-based | Surface-potential-based
    with thermal
  group: ''
- name: Number of terminals
  summary: 端子参数化 Three（默认）| Four
  group: 主设置（基于阈值建模选项）
- name: Parameterization
  summary: 模块参数化 Specify from a datasheet（默认）| Specify using equation parameters directly | Lookup table (2-D, temperature
    independent) | Lookup table (3-D, temperature dependent)
  group: 主设置（基于阈值建模选项）
- name: Drain-source on resistance, R_DS(on)
  summary: 漏源导通电阻 0.167 Ohm（默认）
  group: 主设置（基于阈值建模选项）
- name: Drain current, Ids, for R_DS(on)
  summary: 用于 R_DS(on) 的漏极电流 Ids -2.5 A（默认）
  group: 主设置（基于阈值建模选项）
- name: Gate-source voltage, Vgs, for R_DS(on)
  summary: 用于 R_DS(on) 的栅源电压 Vgs -4.5 V（默认）
  group: 主设置（基于阈值建模选项）
- name: Gain, K
  summary: 增益 K 2 A/V2（默认）
  group: 主设置（基于阈值建模选项）
- name: Gate-source threshold voltage, Vth
  summary: 栅源阈值电压 -1.4 V（默认）
  group: 主设置（基于阈值建模选项）
- name: Gate-source threshold voltage at zero bulk-source voltage, Vth0
  summary: 零体源电压下的栅源阈值电压 -1.4 V（默认）
  group: 主设置（基于阈值建模选项）
- name: Channel modulation, L
  summary: 沟道调制 0 1/V（默认）
  group: 主设置（基于阈值建模选项）
- name: Gate-source threshold voltage at first non-zero bulk-source voltage, Vth1
  summary: 第一非零体源电压下的栅源阈值电压 -1.6071 V（默认）
  group: 主设置（基于阈值建模选项）
- name: First bulk-source voltage, Vbs1
  summary: 第一体源电压 1 V（默认）
  group: 主设置（基于阈值建模选项）
- name: Gate-source threshold voltage at second non-zero bulk-source voltage, Vth2
  summary: 第二非零体源电压下的栅源阈值电压 -1.7660 V（默认）
  group: 主设置（基于阈值建模选项）
- name: Second bulk-source voltage, Vbs2
  summary: 第二体源电压 2 V（默认）
  group: 主设置（基于阈值建模选项）
- name: Body factor
  summary: 体因子 0.5 V^0.50000（默认）
  group: 主设置（基于阈值建模选项）
- name: Surface potential
  summary: 表面电势 0.5 V（默认）
  group: 主设置（基于阈值建模选项）
- name: Measurement temperature
  summary: 测量温度 25 degC（默认）
  group: 主设置（基于阈值建模选项）
- name: Vector of source-gate voltages, Vsg
  summary: 源栅电压向量 [-.5, 2, 3, 4, 5] V（默认）
  group: 主设置（基于阈值建模选项）
- name: Vector of source-drain voltages, Vsd
  summary: 源漏电压向量 [0, 2, 4, 8, 12, 16, 20] V（默认）
  group: 主设置（基于阈值建模选项）
- name: Vector of source-bulk voltages, Vsb
  summary: 源体电压向量 [0, -4, -6, -12] V（默认）
  group: 主设置（基于阈值建模选项）
- name: Tabulated source-drain currents, Isd(Vsg,Vsd)
  summary: 温度无关的表格化源漏电流 [0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01,
    .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03] A（默认）
  group: 主设置（基于阈值建模选项）
- name: Vector of temperatures, T
  summary: 温度向量 [25 125] degC（默认）
  group: 主设置（基于阈值建模选项）
- name: Tabulated source-drain currents, Isd(Vsg,Vsd,T)
  summary: 温度相关的表格化源漏电流 zeros(5, 7, 2) A（默认）
  group: 主设置（基于阈值建模选项）
- name: Tabulated gate-source threshold voltage, Vth(Vsb)
  summary: 温度无关的栅源阈值电压向量 [.4, 1.2, 1.4, 1.45] V（默认）
  group: 主设置（基于阈值建模选项）
- name: Tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd)
  summary: 零源体电压下温度无关的表格化源漏电流 [0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095,
    .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03] A（默认）
  group: 主设置（基于阈值建模选项）
- name: Tabulated gate-source threshold voltage, Vth(Vsb,T)
  summary: 温度相关的栅源阈值电压向量 [.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4] V（默认）
  group: 主设置（基于阈值建模选项）
- name: Tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd,T)
  summary: 零源体电压下温度相关的表格化源漏电流 zeros(5, 7, 2) A（默认）
  group: 主设置（基于阈值建模选项）
- name: Isd-Vsd parameterization
  summary: Isd-Vsd 表数据作为对称数据 Provide negative and positive Vsd data（默认）| Provide positive Vsd data only
  group: 主设置（基于阈值建模选项）
- name: Number of terminals
  summary: 端子参数化 Three（默认）| Four
  group: 主设置（基于表面电势建模选项）
- name: Gain
  summary: 增益 18 A/V2（默认）
  group: 主设置（基于表面电势建模选项）
- name: Flatband voltage
  summary: 平带电压 -1.1 V（默认）
  group: 主设置（基于表面电势建模选项）
- name: Body factor
  summary: 体因子 3.5 V1/2（默认）
  group: 主设置（基于表面电势建模选项）
- name: Surface potential at strong inversion
  summary: 强反型时的表面电势 1 V（默认值）
  group: 主设置（基于表面电势建模选项）
- name: Velocity saturation factor
  summary: 速度饱和因子 0.4 1/V（默认值）
  group: 主设置（基于表面电势建模选项）
- name: Channel-length modulation factor
  summary: 沟道长度调制因子 0（默认值）
  group: 主设置（基于表面电势建模选项）
- name: Channel-length modulation voltage
  summary: 沟道长度调制电压 5e-2 V（默认值）
  group: 主设置（基于表面电势建模选项）
- name: Surface roughness scattering factor
  summary: 表面粗糙度散射因子 0 1/V（默认值）
  group: 主设置（基于表面电势建模选项）
- name: Linear-to-saturation transition coefficient
  summary: 线性到饱和过渡系数 8（默认值）
  group: 主设置（基于表面电势建模选项）
- name: Measurement temperature
  summary: 测量温度 25 degC（默认值）
  group: 主设置（基于表面电势建模选项）
- name: Source ohmic resistance
  summary: 源极欧姆电阻 1e-4 Ohm（默认值）| 非负标量
  group: Ohmic Resistance
- name: Drain ohmic resistance
  summary: 漏极欧姆电阻 0.01 Ohm（默认值）| 非负标量
  group: Ohmic Resistance
- name: Gate ohmic resistance
  summary: 栅极欧姆电阻 8.4 Ohm（默认值）| 非负标量
  group: Ohmic Resistance
- name: Body ohmic resistance
  summary: 晶体管体电阻 0.001 Ohm（默认值）| 非负标量
  group: Ohmic Resistance
- name: Bulk ohmic resistance
  summary: 晶体管衬底电阻 2e-3 Ohm（默认值）| 非负标量
  group: Ohmic Resistance
- name: Source lead resistance
  summary: 晶体管源极引线电阻 0 Ohm（默认值）| 非负标量
  group: Packaging
- name: Drain lead resistance
  summary: 晶体管漏极引线电阻 0 Ohm（默认值）| 非负标量
  group: Packaging
- name: Gate lead resistance
  summary: 晶体管栅极引线电阻 0 Ohm（默认值）| 非负标量
  group: Packaging
- name: Body lead resistance
  summary: 晶体管体引线电阻 0 Ohm（默认值）| 非负标量
  group: Packaging
- name: Source lead inductance
  summary: 晶体管源极引线电感 0 nH（默认值）| 非负标量
  group: Packaging
- name: Drain lead inductance
  summary: 晶体管漏极引线电感 0 nH（默认值）| 非负标量
  group: Packaging
- name: Gate lead inductance
  summary: 晶体管栅极引线电感 0 nH（默认值）| 非负标量
  group: Packaging
- name: Body lead inductance
  summary: 晶体管体引线电感 0 nH（默认值）| 非负标量
  group: Packaging
- name: Parameterization
  summary: 电容参数化 Specify fixed input, reverse transfer, and output capacitance（默认值）| Specify fixed gate-source, gate-drain,
    and drain-source capacitance | Specify tabulated input, reverse transfer, and output capacitance | Specify tabulated gate-source,
    gate-drain, and drain-source capacitance
  group: Capacitance
- name: Input capacitance, Ciss
  summary: 输入栅源电容 182 pF（默认值）
  group: Capacitance
- name: Input capacitance, Ciss(Vsd)
  summary: 带表格化输入的输入栅源电容 [225 210 200 185 175 170] pF（默认值）
  group: Capacitance
- name: Reverse transfer capacitance, Crss
  summary: 反向传输电容 24 pF（默认值）
  group: Capacitance
- name: Reverse transfer capacitance, Crss(Vsd)
  summary: 带表格化输入的反向传输电容 [75 60 50 35 25 20] pF（默认值）
  group: Capacitance
- name: Output capacitance, Coss
  summary: 输出电容 0 pF（默认值）
  group: Capacitance
- name: Output capacitance, Coss(Vsd)
  summary: 带表格化输入的输出电容 [180 160 125 80 60 45] pF（默认值）
  group: Capacitance
- name: Gate-source capacitance, Cgs
  summary: 栅源电容 158 pF（默认值）
  group: Capacitance
- name: Gate-source capacitance, Cgs(Vsg, Vsd)
  summary: 带表格化值的栅源电容 [150 150 150 150 150 150] pF（默认值）
  group: Capacitance
- name: Gate-drain capacitance, Cgd
  summary: 栅漏电容 24 pF（默认值）
  group: Capacitance
- name: Gate-drain capacitance, Cgd(Vsg,Vsd)
  summary: 带表格化值的栅漏电容 [75 60 50 35 25 20] pF（默认值）
  group: Capacitance
- name: Gate-bulk capacitance, Cgb
  summary: 栅衬底电容 0 pF（默认值）
  group: Capacitance
- name: Gate-bulk capacitance, Cgb(Vsg,Vsd)
  summary: 带表格化值的栅衬底电容 [450 400 300 190 95 55] pF（默认值）
  group: Capacitance
- name: Corresponding source-gate voltages, Vsg
  summary: 对应的源栅电压 0 V（默认值）
  group: Capacitance
- name: Drain-source capacitance, Cds
  summary: 漏源电容 0 pF（默认值）
  group: Capacitance
- name: 漏源电容，Cds(vsd)
  summary: 使用表格值的漏源电容 [105 100 75 45 35 25] pF（默认）
  group: Capacitance
- name: 对应的源漏电压，Vsd
  summary: 对应的源漏电压 [0.1 0.3 1 3 10 30] V（默认）
  group: Capacitance
- name: 源栅电压，Vsg，用于表格化电容
  summary: 源栅电压，Vsg，用于表格化电容 0 V（默认）
  group: Capacitance
- name: 栅漏电荷-电压线性度
  summary: 栅漏电荷-电压线性度 栅漏电容为常数（默认）| 栅漏电荷函数为非线性
  group: Capacitance
- name: 栅漏氧化层电容
  summary: 栅漏氧化层电容 200 pF（默认）
  group: Capacitance
- name: 氧化层电容开始起作用时的漏栅电压
  summary: 氧化层电容开始起作用时的漏栅电压 0.5 V（默认）
  group: Capacitance
- name: 栅体与栅源电荷-电压线性度
  summary: 栅体与栅源电荷-电压线性度 栅体和栅源电容瞬时变化（默认）| 栅体和栅源电容逐渐变化 | 分离栅体和栅源电容
  group: Capacitance
- name: 氧化层电容
  summary: 氧化层电容 1500 pF（默认）
  group: 沟道电容
- name: 栅源重叠电容
  summary: 栅源重叠电容 100 pF（默认）
  group: 沟道电容
- name: 栅漏重叠电容
  summary: 栅漏重叠电容 14 pF（默认）
  group: 沟道电容
- name: 体二极管建模
  summary: 体二极管建模选项 否（默认）| 指数 | 表格化 I-V 曲线
  group: 体二极管
- name: 表格类型
  summary: 表格化函数 If(Tj,Vf) 形式的表格（默认）| Vf(Tj,If) 形式的表格
  group: 体二极管
- name: 反向饱和电流，Is
  summary: 反向饱和电流 0 A（默认）
  group: 体二极管
- name: 内建电压，Vbi
  summary: 内建电压 0.6 V（默认）
  group: 体二极管
- name: 理想因子，n
  summary: 理想因子 1（默认）
  group: 体二极管
- name: 零偏结电容，Cj0
  summary: 零偏结电容 0 pF（默认）
  group: 体二极管
- name: 渡越时间，TT
  summary: 渡越时间 50e-9 s（默认）
  group: 体二极管
- name: 测量温度
  summary: 测量温度 25 °C（默认）
  group: 体二极管
- name: 二极管正向电压，Vf(If)
  summary: 二极管正向电压 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85] V（默认）
  group: 体二极管
- name: 二极管正向电流，If
  summary: 二极管正向电流，温度无关 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认）
  group: 体二极管
- name: 二极管正向电流，If(Vf)
  summary: 二极管正向电流，根据正向电压表格化 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2] A（默认）
  group: 体二极管
- name: 二极管正向电压，Vf
  summary: 二极管正向电压，温度无关 [.5, .7, .9, 1.3, 1.7, 2.1, 2.5] V（默认）
  group: 体二极管
- name: 二极管结温，Tj
  summary: 二极管结温 [25, 125] degC（默认）
  group: 体二极管
- name: 二极管正向电流，If(Tj,Vf)
  summary: 二极管正向电流，温度相关 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12] A（默认）
  group: 体二极管
- name: 二极管正向电压，If(Tj,Vf)
  summary: 二极管正向电压，温度相关 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7] V（默认）
  group: 体二极管
- name: 二极管关态电导
  summary: 二极管反向偏置时的电导 1e-12 1/Ohm（默认）| 正标量
  group: 体二极管
- name: 参数化
  summary: 温度依赖性参数化 无 — 在参数测量温度下仿真（默认）| 建模温度依赖性
  group: 温度依赖性（基于阈值的建模选项）
- name: 第二个测量温度下的漏源导通电阻，R_DS(on)
  summary: 第二个测量温度下的漏源导通电阻，R_DS(on) 0.25 Ohm（默认）
  group: 温度依赖性（基于阈值的建模选项）
- name: 第二个测量温度
  summary: 第二个测量温度 125 degC（默认）
  group: 温度依赖性（基于阈值的建模选项）
- name: 栅极阈值电压温度系数，dVth/dT
  summary: 栅极阈值电压温度系数，dVth/dT 2 mV/K（默认）
  group: 温度依赖性（基于阈值的建模选项）
- name: 迁移率温度指数，BEX
  summary: 迁移率温度指数 -1.5（默认）
  group: 温度依赖性（基于阈值的建模选项）
- name: 体二极管反向饱和电流温度指数
  summary: 体二极管反向饱和电流温度指数 3（默认）
  group: 温度依赖性（基于阈值的建模选项）
- name: 器件仿真温度
  summary: 器件仿真温度 25 degC（默认）
  group: 温度依赖性（基于阈值的建模选项）
- name: 参数化
  summary: 温度依赖性参数化 None — Simulate at parameter measurement temperature（默认） | Model temperature dependence
  group: 温度依赖性（基于表面电势的建模选项）
- name: 增益温度指数
  summary: 增益温度指数 1.3（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: 平带电压温度系数
  summary: 平带电压温度系数 5e-4 V/K（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: 强反型表面电势温度系数
  summary: 强反型表面电势温度系数 -8.5e-4 V/K（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: 速度饱和温度指数
  summary: 速度饱和温度指数 1.04（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: 表面粗糙度散射温度指数
  summary: 表面粗糙度散射温度指数 0.65（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: 电阻温度指数
  summary: 电阻温度指数 0.95（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: 体二极管反向饱和电流温度指数
  summary: 体二极管反向饱和电流温度指数 3（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: 器件仿真温度
  summary: 器件仿真温度 25 degC（默认）
  group: 温度依赖性（基于表面电势的建模选项）
- name: PMOS 故障
  summary: 添加故障的选项 Add fault（默认）
  group: 故障
- name: 在以下时间触发故障
  summary: 进入故障状态前的时间 0 s（默认） | 非负标量
  group: 故障
- name: 最大允许源栅电压
  summary: 触发故障转换的源栅电压阈值 inf V（默认） | 正标量
  group: 故障
- name: 最大允许源漏电压
  summary: 触发故障转换的源漏电压阈值 inf V（默认） | 正标量
  group: 故障
- name: 最大允许体漏电压
  summary: 触发故障转换的体漏电压阈值 inf V（默认） | 正标量
  group: 故障
- name: 最大允许源漏电流
  summary: 触发故障转换的电流阈值 inf A（默认） | 正标量
  group: 故障
- name: 超过源漏电流时的失效时间
  summary: 超过源漏电流时的失效时间 1 s（默认） | 正标量
  group: 故障
- name: 最大允许体二极管电流
  summary: 触发故障转换的体二极管电流阈值 inf A（默认） | 正标量
  group: 故障
- name: 超过体二极管电流时的失效时间
  summary: 超过体二极管电流时的失效时间 1 s（默认） | 正标量
  group: 故障
- name: 最大二极管恢复，dV/dt
  summary: 最大二极管恢复 inf V/s（默认） | 正标量
  group: 故障
- name: 最大允许温度
  summary: 触发故障转换的温度阈值 inf K（默认） | 正标量
  group: 故障
- name: 超过温度时的失效时间
  summary: 超过温度时的失效时间 1 s（默认） | 正标量
  group: 故障
- name: 故障转换时间常数，tau
  summary: 故障转换时间常数 1e-3 s（默认）
  group: 故障
- name: 失效模式
  summary: 失效类别 Open circuit（默认） | Drain-source short | Drain-bulk short or source-bulk short | Gate oxide short | Parameter
    shift
  group: 故障
- name: 故障串联栅极电阻，Rg
  summary: 故障串联栅极电阻 1e6 Ohm（默认）
  group: 故障
- name: 故障串联漏极电阻，Rd
  summary: 故障串联漏极电阻 1000 Ohm（默认）
  group: 故障
- name: 故障串联源极电阻，Rs
  summary: 故障串联源极电阻 1000 Ohm（默认）
  group: 故障
- name: 故障串联体电阻，Rb
  summary: 故障串联源极电阻 1000 Ohm（默认）
  group: 故障
- name: Faulted parallel drain-source conductance, Gds
  summary: 故障状态下的并联漏源电导 1000 1/Ohm（默认值）
  group: 故障
- name: Faulted parallel drain-bulk conductance, Gdb
  summary: 故障状态下的并联漏体电导 1000 1/Ohm（默认值）
  group: 故障
- name: Faulted parallel source-bulk conductance, Gsb
  summary: 故障状态下的并联源体电导 1000 1/Ohm（默认值）
  group: 故障
- name: Location of fault node (percentage of total channel length from source)
  summary: 故障节点位置 0（默认值）
  group: 故障
- name: Gate oxide short conductance, G
  summary: 栅氧化层短路电导 1000 1/Ohm（默认值）
  group: 故障
- name: Model gate oxide short diode
  summary: 栅氧化层短路二极管建模选项 No（默认值）| Yes
  group: 故障
- name: Gate oxide short diode reverse saturation current, Is
  summary: 栅氧化层短路二极管反向饱和电流 0 A（默认值）
  group: 故障
- name: Gate oxide short diode built-in voltage, Vbi
  summary: 栅氧化层短路二极管内建电压 0.6 V（默认值）
  group: 故障
- name: Gate oxide short diode ideality factor, n
  summary: 栅氧化层短路二极管理想因子 1（默认值）
  group: 故障
- name: Gate oxide short diode zero-bias junction capacitance, Cj0
  summary: 栅氧化层短路二极管零偏结电容 0 pF（默认值）
  group: 故障
- name: Gate oxide short diode transit time, TT
  summary: 栅氧化层短路二极管渡越时间 50e-9 s（默认值）
  group: 故障
- name: Shifted gain as percentage of unshifted
  summary: 偏移后增益占未偏移的百分比 100（默认值）
  group: 故障
- name: Threshold voltage shift value, dVth
  summary: 阈值电压偏移值 0 V（默认值）
  group: 故障
- name: Faulted channel modulation, L
  summary: 故障状态下的沟道调制 0 1/V（默认值）
  group: 故障
- name: Shifted body factor as percentage of unshifted
  summary: 偏移后体因子占未偏移的百分比 100（默认值）
  group: 故障
- name: Surface potential shift value, dPhib
  summary: 表面电势偏移值 0 V（默认值）
  group: 故障
- name: Faulted source ohmic resistance, Rs
  summary: 故障状态下的源极欧姆电阻 0.0001 Ohm（默认值）
  group: 故障
- name: Faulted drain ohmic resistance, Rd
  summary: 故障状态下的漏极欧姆电阻 0.01 Ohm（默认值）
  group: 故障
- name: Faulted body ohmic resistance, Rb
  summary: 故障状态下的体极欧姆电阻 0.001 Ohm（默认值）
  group: 故障
- name: Faulted vector of source-gate voltages, Vsg
  summary: 故障状态下的源栅电压向量 [-.5, 2, 3, 4, 5] V（默认值）
  group: 故障
- name: Faulted vector of source-drain voltages, Vsd
  summary: 故障状态下的源漏电压向量 [0, 2, 4, 8, 12, 16, 20] V（默认值）
  group: 故障
- name: Faulted vector of source-bulk voltages, Vsb
  summary: 故障状态下的源体电压向量 [0, -4, -6, -12] V（默认值）
  group: 故障
- name: Faulted tabulated gate-source threshold voltage, Vth(Vsb)
  summary: 故障状态下的列表栅源阈值电压 [.4, 1.2, 1.4, 1.45] V（默认值）
  group: 故障
- name: Faulted tabulated gate-source threshold voltage, Vth(Vsb,T)
  summary: 故障状态下的列表栅源阈值电压（依赖于温度） [.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4] V（默认值）
  group: 故障
- name: Faulted tabulated source-drain currents, Isd(Vsg,Vsd)
  summary: 故障状态下的列表源漏电流 [0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01,
    .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03] A（默认值）
  group: 故障
- name: Faulted tabulated source-drain currents, Isd(Vsg,Vsd,T)
  summary: 故障状态下的列表源漏电流（依赖于温度） zeros(5, 7, 2) A（默认值）
  group: 故障
- name: Faulted tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd)
  summary: 故障状态下源体电压为零时的列表源漏电流 [0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095,
    .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03] A（默认值）
  group: 故障
- name: Faulted tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd,T)
  summary: 故障状态下源体电压为零时的列表源漏电流（依赖于温度） zeros(5, 7, 2) A（默认值）
  group: 故障
- name: Faulted gate-source capacitance as percentage of unfaulted
  summary: 故障状态下栅源电容占未故障的百分比 100（默认值）
  group: 故障
- name: Faulted gate-drain capacitance as percentage of unfaulted
  summary: 故障状态下栅-漏电容占未故障状态的百分比 100（默认值）
  group: 故障
- name: Faulted gate-bulk capacitance as percentage of unfaulted
  summary: 故障状态下栅-体电容占未故障状态的百分比 100（默认值）
  group: 故障
- name: Faulted drain-source capacitance as percentage of unfaulted
  summary: 故障状态下漏-源电容占未故障状态的百分比 100（默认值）
  group: 故障
- name: Faulted gate-drain oxide capacitance as percentage of unfaulted
  summary: 故障状态下栅-漏氧化层电容占未故障状态的百分比 100（默认值）
  group: 故障
- name: Faulted drain-gate voltage at which oxide capacitance becomes active
  summary: 故障状态下氧化层电容开始激活时的漏-栅电压 -0.5 V（默认值）
  group: 故障
- name: Faulted input capacitance, Ciss(Vds)
  summary: 故障状态下的输入电容 [720, 700, 590, 470, 390, 310] pF（默认值）
  group: 故障
- name: Faulted reverse transfer capacitance, Crss(Vds)
  summary: 故障状态下的反向传输电容 [450, 400, 300, 190, 95, 55] pF（默认值）
  group: 故障
- name: Faulted output capacitance, Coss(Vds)
  summary: 故障状态下的输出电容 [900, 810, 690, 420, 270, 170] pF（默认值）
  group: 故障
- name: Faulted corresponding source-drain voltages, Vsd
  summary: 故障状态下对应的源-漏电压 [.1, .3, 1, 3, 10, 30] V（默认值）
  group: 故障
- name: Faulted source-gate voltages, Vsg, for tabulated capacitances
  summary: 故障状态下用于表格化电容的源-栅电压 0 V（默认值）
  group: 故障
- name: Faulted gate-source capacitance, Cgs(Vgs,Vds)
  summary: 故障状态下的栅-源电容 [270, 300, 290, 280, 295, 255] pF（默认值）
  group: 故障
- name: Faulted gate-drain capacitance, Cgd(Vgs,Vds)
  summary: 故障状态下的栅-源电容 [450, 400, 300, 190, 95, 55] pF（默认值）
  group: 故障
- name: Faulted gate-bulk capacitance, Cgb(Vgs,Vds)
  summary: 故障状态下的栅-源电容 [270, 300, 290, 280, 295, 255] pF（默认值）
  group: 故障
- name: Faulted corresponding source-gate voltages, Vsg
  summary: 故障状态下对应的源-栅电压 0 V（默认值）
  group: 故障
- name: Faulted diode reverse saturation current, Is
  summary: 故障状态下的二极管反向饱和电流 0 A（默认值）
  group: 故障
- name: Faulted diode built-in voltage, Vbi
  summary: 故障状态下的二极管内建电压 0.6 V（默认值）
  group: 故障
- name: Faulted diode ideality factor, n
  summary: 故障状态下的二极管理想因子 1（默认值）
  group: 故障
- name: Faulted diode zero-bias junction capacitance as percentage of unfaulted
  summary: 故障状态下二极管零偏结电容占未故障状态的百分比 100（默认值）
  group: 故障
- name: Faulted diode transit time, TT
  summary: 故障状态下的二极管渡越时间 50e-9 s（默认值）
  group: 故障
- name: Faulted diode forward currents, If(Vf)
  summary: 故障状态下的二极管正向电流 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2] A（默认值）
  group: 故障
- name: Faulted diode forward voltages, Vf
  summary: 故障状态下的二极管正向电压 [.5, .7, .9, 1.3, 1.7, 2.1, 2.5] V（默认值）
  group: 故障
- name: Faulted diode forward voltages, Vf(If)
  summary: 故障状态下二极管正向电压 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85] V（默认值）
  group: 故障
- name: Faulted diode forward currents, If
  summary: 故障状态下二极管正向电流 [.1, .2, .5, 1, 2, 4, 7, 10] A（默认值）
  group: 故障
- name: Faulted diode forward currents, If(Tj,Vf)
  summary: 带表格输入的故障状态下二极管正向电流 [.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12] A（默认值）
  group: 故障
- name: Faulted diode forward voltages, Vf(Tj,If)
  summary: 带表格输入的故障状态下二极管正向电压 [.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7] V（默认值）
  group: 故障
- name: Faulted diode off conductance
  summary: 故障状态下二极管关断电导 1e-12 1/Ohm（默认值）
  group: 故障
```

### **Modeling Option** — MOSFET 表示方式 `Threshold-based`（默认）| `Threshold-based with thermal` | `Surface-potential-based` | `Surface-potential-based with thermal`

选择 MOSFET 表示方式：

- `Threshold-based` — 基本模型，使用 Shichman-Hodges 方程（基于阈值电压）表示器件，不模拟热效应。此为默认值。
- `Threshold-based with thermal` — 基于阈值电压的模型，并暴露热端口。
- `Surface-potential-based` — 基于表面电势的模型。此模型不模拟热效应。
- `Surface-potential-based with thermal` —
  基于表面电势的模型的热建模选项。

### 主设置（基于阈值建模选项）

**Main** 设置的此配置对应于基于阈值的模块建模选项，此为默认值。如果您使用的是模块的基于表面电势的建模选项，请参阅主设置（基于表面电势建模选项）。

### **Number of terminals** — 端子参数化 `Three`（默认）| `Four`

模块的端子数量。

### **Parameterization** — 模块参数化 `Specify from a datasheet`（默认）| `Specify using equation parameters directly` | `Lookup table (2-D, temperature independent)` | `Lookup table (3-D, temperature dependent)`

选择以下模块参数化方法之一：

- `Specify from a datasheet` — 提供漏源导通电阻以及对应的漏极电流和栅源电压。模块根据此信息计算 Shichman and Hodges 方程的晶体管增益。
- `Specify using equation parameters directly`
  — 提供晶体管增益。
- `Lookup table (2-D, temperature independent)`
  — 使用二维查表获取漏源电流作为栅源电压和漏源电压的函数。
- `Lookup table (3-D, temperature dependent)`
  — 使用三维查表获取漏源电流作为栅源电压、漏源电压和温度的函数。

### **Drain-source on resistance, R\_DS(on)** — 漏源导通电阻 `0.167` `Ohm`（默认）

在指定的漏极电流和栅源电压值下，漏源电压与漏极电流的比值。*RDS(on)* 应为正值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Drain current, Ids, for R\_DS(on)** — 用于 R\_DS(on) 的漏极电流 Ids `-2.5` `A`（默认）

模块用于计算漏源电阻值的漏极电流。*IDS* 应为负值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Gate-source voltage, Vgs, for R\_DS(on)** — 用于 R\_DS(on) 的栅源电压 Vgs `-4.5` `V`（默认）

模块用于计算漏源电阻值的栅源电压。*VGS* 应为负值。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Gain, K** — 增益 K `2` `A/V2`（默认）

Shichman and Hodges 方程的正恒定增益系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify using equation parameters directly`。

### **Gate-source threshold voltage, Vth** — 栅源阈值电压 `-1.4` `V`（默认）

Shichman and Hodges 方程中的栅源阈值电压 *Vth*。对于增强型器件，*Vth* 应为负值。对于耗尽型器件，*Vth* 应为正值。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Three`，并将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Gate-source threshold voltage at zero bulk-source voltage, Vth0** — 零体源电压下的栅源阈值电压 `-1.4` `V`（默认）

Shichman and Hodges 方程中零体源电压下的栅源阈值电压 *Vth0*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Channel modulation, L** — 沟道调制 `0` `1/V`（默认）

沟道长度调制，通常用数学符号 λ 表示。在饱和区，它是漏极电流随漏源电压变化率的负值。对漏极电流的影响通常很小，在根据漏源导通电阻 *RDS(on)* 计算晶体管增益 *K* 时该影响被忽略。典型值为 0.02，但在大多数电路仿真中可以忽略该影响。然而，在某些电路中，一个小的非零值可能有助于数值收敛。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Gate-source threshold voltage at first non-zero bulk-source voltage, Vth1** — 第一非零体源电压下的栅源阈值电压 `-1.6071` `V`（默认）

Shichman and Hodges 方程中第一非零体源电压下的栅源阈值电压 *Vth1*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **First bulk-source voltage, Vbs1** — 第一体源电压 `1` `V`（默认）

第一体源电压 *Vbs1*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Gate-source threshold voltage at second non-zero bulk-source voltage, Vth2** — 第二非零体源电压下的栅源阈值电压 `-1.7660` `V`（默认）

Shichman and Hodges 方程中第二非零体源电压下的栅源阈值电压 *Vth2*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Second bulk-source voltage, Vbs2** — 第二体源电压 `2` `V`（默认）

第二体源电压 *Vbs2*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify from a datasheet`。

### **Body factor** — 体因子 `0.5` `V^0.50000`（默认）

体因子 *γ*。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify using equation parameters directly`。

### **Surface potential** — 表面电势 `0.5` `V`（默认）

表面电势。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Specify using equation parameters directly`。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量 **Drain-source on resistance, R\_DS(on)** 时的温度 *Tm1*。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Specify from a datasheet` 或 `Specify using
equation parameters directly`。

### **Vector of source-gate voltages, Vsg** — 源栅电压向量 `[-.5, 2, 3, 4, 5]` `V`（默认）

源栅电压向量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### **Vector of source-drain voltages, Vsd** — 源漏电压向量 `[0, 2, 4, 8, 12, 16, 20]` `V`（默认）

用于查表的源漏电压向量。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### **Vector of source-bulk voltages, Vsb** — 源体电压向量 `[0, -4, -6, -12]` `V`（默认）

用于查表的源体电压向量。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### **Tabulated source-drain currents, Isd(Vsg,Vsd)** — 温度无关的表格化源漏电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认）

用于二维查表的源漏电流作为源栅电压和源漏电压函数的表格化值。矩阵中的每个值指定了特定源栅电压和源漏电压组合下的源漏电流。矩阵大小必须与源栅电压和源漏电压向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Three`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)`。

### **Vector of temperatures, T** — 温度向量 `[25 125]` `degC`（默认）

用于查表的温度向量。向量值必须严格递增。值可以是非均匀间隔的。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Tabulated source-drain currents, Isd(Vsg,Vsd,T)** — 温度相关的表格化源漏电流 `zeros(5, 7, 2)` `A`（默认）

用于二维查表的源漏电流作为源栅电压、源漏电压和温度函数的表格化值。矩阵中的每个值指定了特定源栅电压、源漏电压和温度组合下的源漏电流。矩阵大小必须与源栅电压、源漏电压和温度向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Three`，并将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Tabulated gate-source threshold voltage, Vth(Vsb)** — 温度无关的栅源阈值电压向量 `[.4, 1.2, 1.4, 1.45]` `V`（默认）

用于二维查表的栅源阈值电压作为源体电压函数的表格化值。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)`。

### **Tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd)** — 零源体电压下温度无关的表格化源漏电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认）

用于二维查表的零源体电压下源漏电流作为源栅电压和源漏电压函数的表格化值。矩阵中的每个值指定了特定源栅电压和源漏电压组合下的源漏电流。矩阵大小必须与源栅电压和源漏电压向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)`。

### **Tabulated gate-source threshold voltage, Vth(Vsb,T)** — 温度相关的栅源阈值电压向量 `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V`（默认）

用于三维查表的栅源阈值电压作为体源电压和温度函数的表格化值。向量值必须严格递增。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd,T)** — 零源体电压下温度相关的表格化源漏电流 `zeros(5, 7, 2)` `A`（默认）

用于三维查表的零源体电压下源漏电流作为源栅电压、源漏电压和温度函数的表格化值。矩阵中的每个值指定了特定源栅电压、源漏电压和温度组合下的源漏电流。矩阵大小必须与源栅电压、源漏电压和温度向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **Number of terminals** 设置为
`Four`，并将 **Parameterization** 设置为
`Lookup table (3-D, temperature dependent)`。

### **Isd-Vsd parameterization** — Isd-Vsd 表数据作为对称数据 `Provide negative and positive Vsd data`（默认）| `Provide positive Vsd data only`

是否将 Isd-Vsd 表数据作为对称数据提供。如果选择 `Provide negative and positive Vsd data`，数据不是对称的。如果选择 `Provide positive Vsd data only`，模块会旋转并翻转正数据以获得负数据。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为
`Lookup table (2-D, temperature independent)` 或
`Lookup table (3-D, temperature dependent)`。

### 主设置（基于表面电势建模选项）

**Main** 设置的此配置对应于基于表面电势的模块建模选项。如果您使用的是模块的基于阈值的建模选项（基于 Shichman and Hodges 方程），请参阅主设置（基于阈值建模选项）。

### **Number of terminals** — 端子参数化 `Three`（默认）| `Four`

模块的端子数量。

### **Gain** — 增益 `18` `A/V2`（默认）

MOSFET 增益 *β*。此参数主要定义 *ID*–*VDS* 特性上的线性工作区。

### **Flatband voltage** — 平带电压 `-1.1` `V`（默认）

平带电压 *VFB* 定义了为在硅表面实现平带条件而必须施加的栅极偏置。您也可以使用此参数来任意偏移阈值电压，以考虑材料功函数差异以及被困界面电荷或氧化物电荷。然而，在实践中，通常建议首先使用 **Body factor** 和 **Surface potential at strong inversion** 参数修改阈值电压，仅使用此参数进行微调。

### **Body factor** — 体因子 `3.5` `V1/2`（默认）

表面电势方程中的体因子 *γ*。此参数主要影响阈值电压。

### **Surface potential at strong inversion** — 强反型时的表面电势 `1` `V`（默认值）

表面电势方程中的 2*ϕB* 项。该参数也主要影响阈值电压。

### **Velocity saturation factor** — 速度饱和因子 `0.4` `1/V`（默认值）

漏极电流方程中的速度饱和，*θsat*。在良好拟合线性工作区导致饱和电流过高的情况下使用该参数。通过增大该参数值，可以降低饱和电流。对于高压器件，通常会出现良好拟合线性工作区导致饱和电流过低的情况。在这种情况下，可以同时增大增益和漏极欧姆电阻，或者改用 P-Channel LDMOS FET 模块。

### **Channel-length modulation factor** — 沟道长度调制因子 `0`（默认值）

*GΔL* 方程中对数项相乘的因子 α。该参数描述沟道长度调制的起始。对于在饱和区表现出正电导的器件特性，增大该参数值以拟合该行为。默认值为 `0`，这意味着默认情况下沟道长度调制处于关闭状态。

### **Channel-length modulation voltage** — 沟道长度调制电压 `5e-2` `V`（默认值）

*GΔL* 方程中的电压 *Vp*。该参数控制沟道长度调制开始生效时的漏极电压。

### **Surface roughness scattering factor** — 表面粗糙度散射因子 `0` `1/V`（默认值）

表示迁移率降低的强度。迁移率为 *μ* = *μ*/*Gmob*，其中 *μ0* 是不受表面散射影响的低场迁移率。迁移率降低因子 *Gmob* 由 Gmob=1+(θsrVeff)20 给出，其中 *θsr* 是表面粗糙度散射因子，*Veff* 是表示沟道中有效垂直电场强度 *Eeff* 的电压。对于高垂直电场，空穴的迁移率大致与 *Eeff* 成正比。

### **Linear-to-saturation transition coefficient** — 线性到饱和过渡系数 `8`（默认值）

该参数控制 MOSFET 从线性区过渡到饱和区的平滑程度，尤其是在启用速度饱和时。该参数通常可以保留默认值，但您可以使用它来微调 *ID*–*VDS* 特性的拐点。该参数值的预期范围在 2 到 8 之间。

### **Measurement temperature** — 测量温度 `25` `degC`（默认值）

测量模块参数时的温度 *Tm1*。如果 **Temperature Dependence** 设置中的 **Device simulation temperature** 参数与该值不同，则器件参数将根据仿真温度和参考温度从其定义值进行缩放。有关详细信息，请参阅 Temperature Dependence (Surface-Potential-Based Modeling Option)。

### Ohmic Resistance

如果将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`，要启用此设置，请将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。

### **Source ohmic resistance** — 源极欧姆电阻 `1e-4` `Ohm`（默认值）| 非负标量

晶体管源极电阻，即与源极接触相关的串联电阻。该值必须大于或等于 `0`。基于阈值变体的默认值为 `1e-4` Ohm。基于表面电势变体的默认值为 `2e-3` Ohm。

### **Drain ohmic resistance** — 漏极欧姆电阻 `0.01` `Ohm`（默认值）| 非负标量

晶体管漏极电阻，即与漏极接触相关的串联电阻。该值必须大于或等于 `0`。基于阈值变体的默认值为 `0.01` Ohm。基于表面电势变体的默认值为 `0.17` Ohm。

### **Gate ohmic resistance** — 栅极欧姆电阻 `8.4` `Ohm`（默认值）| 非负标量

晶体管栅极电阻，即与栅极接触相关的串联电阻。该值必须大于或等于 `0`。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Surface-potential-based` 或 `Surface-potential-based with thermal`。

### **Body ohmic resistance** — 晶体管体电阻 `0.001` `Ohm`（默认值）| 非负标量

晶体管体电阻，即与体接触相关的串联电阻。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Bulk ohmic resistance** — 晶体管衬底电阻 `2e-3` `Ohm`（默认值）| 非负标量

晶体管体电阻，即与衬底接触相关的串联电阻。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Surface-potential-based` 或 `Surface-potential-based with thermal`。

### Packaging

### **Source lead resistance** — 晶体管源极引线电阻 `0` `Ohm`（默认值）| 非负标量

*Since R2024b*

晶体管的源极引线电阻，即与源极接触相关的串联引线电阻。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Drain lead resistance** — 晶体管漏极引线电阻 `0` `Ohm`（默认值）| 非负标量

*Since R2024b*

晶体管的漏极引线电阻，即与漏极接触相关的串联引线电阻。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Gate lead resistance** — 晶体管栅极引线电阻 `0` `Ohm`（默认值）| 非负标量

*Since R2024b*

晶体管的栅极引线电阻，即与栅极接触相关的串联引线电阻。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Body lead resistance** — 晶体管体引线电阻 `0` `Ohm`（默认值）| 非负标量

*Since R2024b*

晶体管的体引线电阻，即与体接触相关的串联引线电阻。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Source lead inductance** — 晶体管源极引线电感 `0` `nH`（默认值）| 非负标量

*Since R2024b*

晶体管的源极引线电感，即与源极接触相关的串联引线电感。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Drain lead inductance** — 晶体管漏极引线电感 `0` `nH`（默认值）| 非负标量

*Since R2024b*

晶体管的漏极引线电感，即与漏极接触相关的串联引线电感。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Gate lead inductance** — 晶体管栅极引线电感 `0` `nH`（默认值）| 非负标量

*Since R2024b*

晶体管的栅极引线电感，即与栅极接触相关的串联引线电感。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Body lead inductance** — 晶体管体引线电感 `0` `nH`（默认值）| 非负标量

*Since R2024b*

晶体管的体引线电感，即与体接触相关的串联引线电感。使用该参数对晶体管中的寄生效应进行建模。

#### 依赖关系

要启用此参数，请设置：

- **Number of terminals** 为 `Four`。
- **Modeling option** 为 `Threshold-based` 或 `Threshold-based with thermal`。

### Capacitance

要启用此设置，请将 **Modeling option** 设置为 `Threshold-based` 或 `Threshold-based with thermal`。

### **Parameterization** — 电容参数化 `Specify fixed input, reverse transfer, and output capacitance`（默认值）| `Specify fixed gate-source, gate-drain, and drain-source capacitance` | `Specify tabulated input, reverse transfer, and output capacitance` | `Specify tabulated gate-source, gate-drain, and drain-source capacitance`

选择以下电容参数化方法之一：

- `Specify fixed input, reverse transfer, and output capacitance` — 从数据手册提供固定参数值，让模块将输入、输出和反向传输电容值转换为电容值，如 Charge Model for Threshold-Based Modeling Option 中所述。这是默认方法。
- `Specify fixed gate-source, gate-drain, and drain-source capacitance` — 直接为电容参数提供固定值。
- `Specify tabulated input, reverse transfer, and output capacitance` — 基于数据手册图表提供表格化的电容和源漏电压值。模块将输入、输出和反向传输电容值转换为电容值，如 Charge Model for Threshold-Based Modeling Option 中所述。
- `Specify tabulated gate-source, gate-drain, and drain-source capacitance` — 提供电容和源漏电压的表格化值。

### **Input capacitance, Ciss** — 输入栅源电容 `182` `pF`（默认值）

漏极短接到源极时的栅源电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **Input capacitance, Ciss(Vsd)** — 带表格化输入的输入栅源电容 `[225 210 200 185 175 170]` `pF`（默认值）

漏极短接到源极时的栅源电容，以源漏电压为表格化变量。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **Reverse transfer capacitance, Crss** — 反向传输电容 `24` `pF`（默认值）

源极接地时的漏栅电容，也称为米勒电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **Reverse transfer capacitance, Crss(Vsd)** — 带表格化输入的反向传输电容 `[75 60 50 35 25 20]` `pF`（默认值）

源极接地时的漏栅电容，也称为米勒电容，以源漏电压为表格化变量。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **Output capacitance, Coss** — 输出电容 `0` `pF`（默认值）

栅极和源极短接时的漏源电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **Output capacitance, Coss(Vsd)** — 带表格化输入的输出电容 `[180 160 125 80 60 45]` `pF`（默认值）

栅极和源极短接时的漏源电容，以源漏电压为表格化变量。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **Gate-source capacitance, Cgs** — 栅源电容 `158` `pF`（默认值）

置于栅极和源极之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **Gate-source capacitance, Cgs(Vsg, Vsd)** — 带表格化值的栅源电容 `[150 150 150 150 150 150]` `pF`（默认值）

置于栅极和源极之间的电容，以源栅电压和源漏电压为表格化变量。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Gate-drain capacitance, Cgd** — 栅漏电容 `24` `pF`（默认值）

置于栅极和漏极之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **Gate-drain capacitance, Cgd(Vsg,Vsd)** — 带表格化值的栅漏电容 `[75 60 50 35 25 20]` `pF`（默认值）

置于栅极和漏极之间的电容，以源栅电压和源漏电压为表格化变量。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Gate-bulk capacitance, Cgb** — 栅衬底电容 `0` `pF`（默认值）

置于栅极和衬底之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`，并将 **Gate-bulk and gate-source charge-voltage linearity** 设置为 `Separate gate-bulk and gate-source capacitance`。

### **Gate-bulk capacitance, Cgb(Vsg,Vsd)** — 带表格化值的栅衬底电容 `[450 400 300 190 95 55]` `pF`（默认值）

置于栅极和衬底之间的电容，以源栅电压和源漏电压为表格化变量。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`，并将 **Gate-bulk and gate-source charge-voltage linearity** 设置为 `Separate gate-bulk and gate-source capacitance`。

### **Corresponding source-gate voltages, Vsg** — 对应的源栅电压 `0` `V`（默认值）

与表格化电容值对应的源栅电压。

如果该值为标量，则 **Gate-source capacitance, Cgs(Vsg,Vsd)** 和 **Gate-drain capacitance, Cgd(Vsg,Vsd)** 是标量向量。如果该值为向量，则 **Gate-source capacitance, Cgs(Vsg,Vsd)** 和 **Gate-drain capacitance, Cgd(Vsg,Vsd)** 是标量矩阵。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。

### **Drain-source capacitance, Cds** — 漏源电容 `0` `pF`（默认值）

置于漏极和源极之间的电容。

#### 依赖关系

要启用此参数，请在 **Capacitance** 设置中将 **Parameterization** 设置为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。

### **漏源电容，Cds(vsd)** — 使用表格值的漏源电容 `[105 100 75 45 35 25]` `pF`（默认）

放置在漏极和源极之间的电容，根据源漏电压以表格形式给出。

#### 依赖关系

要启用此参数，请在**电容**设置中将**参数化**设置为`指定表格化的栅源、栅漏和漏源电容`。

### **对应的源漏电压，Vsd** — 对应的源漏电压 `[0.1 0.3 1 3 10 30]` `V`（默认）

与表格化电容值对应的源漏电压。

#### 依赖关系

要启用此参数，请在**电容**设置中将**参数化**设置为`指定表格化的输入、反向传输和输出电容`或`指定表格化的栅源、栅漏和漏源电容`。

### **源栅电压，Vsg，用于表格化电容** — 源栅电压，Vsg，用于表格化电容 `0` `V`（默认）

对于表格化电容模型，此参数控制**反向传输电容，Crss**或**栅漏电容，Cgd**参数（取决于所选的参数化选项）的电压依赖性。这些电容是漏栅电压的函数。该模块通过从**对应的源漏电压**参数所指定值的负值中减去此栅源电压值来计算漏栅电压（*Vdg* = –*Vsd* – *Vgs*）。

#### 依赖关系

要启用此参数，请在**电容**设置中将**参数化**设置为`指定表格化的输入、反向传输和输出电容`。

### **栅漏电荷-电压线性度** — 栅漏电荷-电压线性度 `栅漏电容为常数`（默认）| `栅漏电荷函数为非线性`

两个固定电容选项允许您将栅极电容建模为固定的栅源电容*CGS*以及固定或非线性的栅漏电容*CGD*。选择栅漏电容是固定还是非线性：

- `栅漏电容为常数` — 电容值为常数，根据所选的参数化选项直接定义或从数据手册导出。这是默认方法。
- `栅漏电荷函数为非线性` — 栅漏电荷关系根据基于阈值的建模选项的电荷模型中描述的分段非线性函数定义。将出现两个附加参数，用于定义栅漏电荷函数。

#### 依赖关系

要启用此参数，请在**电容**设置中将**参数化**设置为`指定固定输入、反向传输和输出电容`或`指定固定栅源、栅漏和漏源电容`。

### **栅漏氧化层电容** — 栅漏氧化层电容 `200` `pF`（默认）

当漏栅电压小于**氧化层电容开始起作用时的漏栅电压**参数值时，即为栅漏电容。

#### 依赖关系

要启用此参数，请将**栅漏电荷-电压线性度**设置为`栅漏电荷函数为非线性`。

### **氧化层电容开始起作用时的漏栅电压** — 氧化层电容开始起作用时的漏栅电压 `0.5` `V`（默认）

漏栅电容在关态（*CGD*）和开态（*Cox*）电容值之间切换时的漏栅电压。

#### 依赖关系

要启用此参数，请将**栅漏电荷-电压线性度**设置为`栅漏电荷函数为非线性`。

### **栅体与栅源电荷-电压线性度** — 栅体与栅源电荷-电压线性度 `栅体和栅源电容瞬时变化`（默认）| `栅体和栅源电容逐渐变化` | `分离栅体和栅源电容`

栅体和栅源电荷-电压线性度。

#### 依赖关系

要启用此参数，请在**主要**设置中将**端子数量**设置为`四`。

要启用`分离栅体和栅源电容`选项，请在**电容**设置中将**参数化**设置为`指定固定栅源、栅漏和漏源电容`或`指定表格化的栅源、栅漏和漏源电容`。

### 沟道电容

要启用此设置，请将**建模选项**设置为`基于表面电势`或`基于表面电势并包含热效应`。

### **氧化层电容** — 氧化层电容 `1500` `pF`（默认）

平行板栅沟道电容。

### **栅源重叠电容** — 栅源重叠电容 `100` `pF`（默认）

与栅电极和源极阱重叠相关的固定线性电容。

### **栅漏重叠电容** — 栅漏重叠电容 `14` `pF`（默认）

与栅电极和漏极阱重叠相关的固定线性电容。

### 体二极管

### **体二极管建模** — 体二极管建模选项 `否`（默认）| `指数` | `表格化 I-V 曲线`

是否对体二极管进行建模。

### **表格类型** — 表格化函数 `If(Tj,Vf) 形式的表格`（默认）| `Vf(Tj,If) 形式的表格`

是将电流表示为温度和电压的函数，还是将电压表示为温度和电流的函数。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`表格化 I-V 曲线`。

### **反向饱和电流，Is** — 反向饱和电流 `0` `A`（默认）

体二极管方程中由*Is*符号表示的电流。基于阈值的建模选项的默认值为`0` A。基于表面电势的建模选项的默认值为`5.2e-13` A。

对于 MOSFET 电流在仿真过程中改变符号的应用（例如 MOSFET 驱动感性负载时），要使体二极管导通，请将此参数设置为非零值。

对于 MOSFET 电流从不改变符号的应用（例如小信号放大器），请将此参数设置为 0 以提高仿真速度。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`指数`。

### **内建电压，Vbi** — 内建电压 `0.6` `V`（默认）

二极管的内建电压，在体二极管方程中由*Vbi*符号表示。内建电压仅影响结电容方程。它不影响传导电流。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`指数`。

### **理想因子，n** — 理想因子 `1`（默认）

体二极管方程中由*n*符号表示的因子。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`指数`。

### **零偏结电容，Cj0** — 零偏结电容 `0` `pF`（默认）

仅由体二极管引起的、零偏时漏极和体接触之间的电容。在体二极管方程中由*Cj0*符号表示。基于阈值的建模选项的默认值为`0` pF。基于表面电势的建模选项的默认值为`480` pF。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`指数`。

### **渡越时间，TT** — 渡越时间 `50e-9` `s`（默认）

体二极管方程中由*τ*符号表示的时间。

当**反向饱和电流**和**渡越时间**参数均非零时，该模块在体二极管模型中包含反向恢复。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`指数`。

### **测量温度** — 测量温度 `25` `°C`（默认）

测量模块参数时的温度。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`指数`，并在**主要**设置中将**参数化**设置为`查找表（二维，温度无关）`或`查找表（三维，温度相关）`。

### **二极管正向电压，Vf(If)** — 二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V`（默认）

使二极管变为正向偏置所需施加的最小电压的表格值。

#### 依赖关系

要启用此参数，

- 在**主要**设置中，将**参数化**设置为`从数据手册指定`、`直接指定方程参数`或`查找表（二维，温度无关）`。
- 在**体二极管**设置中，将：

  - **体二极管建模**设置为`表格化 I-V 曲线`。

    **表格类型**设置为`Vf(If) 形式的表格`。

### **二极管正向电流，If** — 二极管正向电流，温度无关 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

正向电流的表格值。

#### 依赖关系

要启用此参数，请在**体二极管**设置中将**体二极管建模**设置为`表格化 I-V 曲线`，并将**表格类型**设置为`Vf(If) 形式的表格`或`Vf(Tj,If) 形式的表格`。

### **二极管正向电流，If(Vf)** — 二极管正向电流，根据正向电压表格化 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A`（默认）

正向电流作为正向电压函数的表格值。

#### 依赖关系

要启用此参数，

- 在**主要**设置中，将**参数化**设置为`从数据手册指定`、`直接指定方程参数`或`查找表（二维，温度无关）`。
- 在**体二极管**设置中，将：

  - **体二极管建模**设置为`表格化 I-V 曲线`。

    **表格类型**设置为`If(Vf) 形式的表格`。

### **二极管正向电压，Vf** — 二极管正向电压，温度无关 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

正向电压的表格值。

#### 依赖关系

要启用此参数，请在**体二极管**设置中将**体二极管建模**设置为`表格化 I-V 曲线`，并将**表格类型**设置为`If(Vf) 形式的表格`或`If(Tj,Vf) 形式的表格`。

### **二极管结温，Tj** — 二极管结温 `[25, 125]` `degC`（默认）

结温向量。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`表格化 I-V 曲线`，并在**主要**设置中将**参数化**设置为`查找表（三维，温度相关）`。

### **二极管正向电流，If(Tj,Vf)** — 二极管正向电流，温度相关 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认）

正向电流作为正向电压和结温函数的表格值。

#### 依赖关系

要启用此参数，

- 在**主要**设置中，将**参数化**设置为`查找表（三维，温度相关）`。
- 在**体二极管**设置中，将：

  - **体二极管建模**设置为`表格化 I-V 曲线`。

    **表格类型**设置为`If(Tj,Vf) 形式的表格`。

### **二极管正向电压，If(Tj,Vf)** — 二极管正向电压，温度相关 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）

正向电压作为正向电流和结温函数的表格值。

#### 依赖关系

要启用此参数，

- 在**主要**设置中，将**参数化**设置为`查找表（三维，温度相关）`。
- 在**体二极管**设置中，将：

  - **体二极管建模**设置为`表格化 I-V 曲线`。

    **表格类型**设置为`Vf(Tj,If) 形式的表格`。

### **二极管关态电导** — 二极管反向偏置时的电导 `1e-12` `1/Ohm`（默认）| 正标量

*自 R2024a 起*

二极管反向偏置时的电导。

#### 依赖关系

要启用此参数，请将**体二极管建模**设置为`表格化 I-V 曲线`。

### 温度依赖性（基于阈值的建模选项）

**温度依赖性**设置的此配置对应于基于阈值的模块建模选项，这是默认选项。如果您使用的是该模块的基于表面电势的建模选项，请参阅温度依赖性（基于表面电势的建模选项）。

### **参数化** — 温度依赖性参数化 `无 — 在参数测量温度下仿真`（默认）| `建模温度依赖性`

选择以下温度依赖性参数化方法之一：

- `无 — 在参数测量温度下仿真` — 不对温度依赖性建模。这是默认方法。
- `建模温度依赖性` — 对温度相关效应建模。提供仿真温度*Ts*的值、*BEX*的值以及测量温度*Tm1*的值（使用**主要**设置中的**测量温度**参数）。您还需要根据**主要**设置中**参数化**参数的值，使用两种方法之一提供*α*的值。如果您从数据手册对模块进行参数化，则必须提供第二个测量温度下的*RDS(on)*，模块将据此计算*α*。如果您通过指定方程参数进行参数化，则必须直接提供*α*的值。

### **第二个测量温度下的漏源导通电阻，R\_DS(on)** — 第二个测量温度下的漏源导通电阻，R\_DS(on) `0.25` `Ohm`（默认）

在第二个测量温度下，对于指定的漏极电流和栅源电压值，漏源电压与漏极电流的比值。它必须与**主要**设置中**漏源导通电阻，R\_DS(on)**参数所对应的工作点（漏极电流和栅源电压）相同。

#### 依赖关系

仅当您在**主要**设置中为**参数化**参数选择`从数据手册指定`时，此参数才可见。

### **第二个测量温度** — 第二个测量温度 `125` `degC`（默认）

测量**第二个测量温度下的漏源导通电阻，R\_DS(on)**时的第二个温度*Tm2*。

#### 依赖关系

仅当您在**主要**设置中为**参数化**参数选择`从数据手册指定`时，此参数才可见。

### **栅极阈值电压温度系数，dVth/dT** — 栅极阈值电压温度系数，dVth/dT `2` `mV/K`（默认）

栅极阈值电压随温度的变化率。

#### 依赖关系

仅当您在**主要**设置中为**参数化**参数选择`直接使用方程参数指定`时，此参数才可见。

### **迁移率温度指数，BEX** — 迁移率温度指数 `-1.5`（默认）

迁移率温度系数值。对于大多数 MOSFET，您可以使用默认值。有关其他注意事项，请参阅假设和限制部分。

### **体二极管反向饱和电流温度指数** — 体二极管反向饱和电流温度指数 `3`（默认）

假设体二极管的反向饱和电流与本征载流子浓度的平方成正比，*ni* =
*NC*
exp(–*EG*/2*kB**T*)。*NC* 是随温度变化的
有效态密度，*EG* 是
半导体材料的随温度变化的带隙。为避免引入另一个
温度缩放参数，该模块忽略带隙的温度依赖性，
并对所有器件类型使用硅在 300K 时的带隙（1.12eV）。因此，
温度缩放后的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts))。

*Is,m1* 是 **Body Diode**
设置中 **Reverse
saturation current** 参数的值，*kB* 是玻尔兹曼常数
(8.617x10-5eV/K)，并且
*ηIs* 是 **Body diode reverse
saturation current temperature exponent**。默认值为
`3`，因为硅的 *NC*
大致与 T3/2 成正比。你可以通过务实地选择
*ηIs* 来弥补忽略带隙温度依赖性的影响。

### **器件仿真温度** — 器件仿真温度 `25` `degC`（默认）

器件仿真时的温度 *Ts*。

### 温度依赖性（基于表面电势的建模选项）

**Temperature Dependence** 设置的此配置对应于
基于表面电势的模块建模选项。如果你使用的是该模块的基于阈值的
建模选项，请参阅温度依赖性（基于阈值的建模选项）

### **参数化** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认） | `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement
  temperature` — 不对温度依赖性建模。这是
  默认方法。
- `Model temperature dependence` — 对
  温度依赖效应建模。为器件仿真温度
  *Ts* 以及其他模块参数的
  温度缩放系数提供值。

### **增益温度指数** — 增益温度指数 `1.3`（默认）

假设 MOSFET 增益 *β* 随
温度按指数缩放，*β* = *βm1*
(*Tm1*/*Ts*)^*ηβ*。*βm1* 是
**Main** 设置中 **Gain** 参数的值，
*ηβ* 是 **Gain temperature
exponent**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### **平带电压温度系数** — 平带电压温度系数 `5e-4` `V/K`（默认）

假设平带电压 *VFB* 随
温度线性缩放，*VFB* =
*VFBm1* +
(*Ts* –
*Tm1*)*ST,VFB*。*VFBm1* 是
**Main** 设置中 **Flatband voltage** 参数的值，
*ST,VFB* 是
**Flatband voltage temperature coefficient**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### **强反型表面电势温度系数** — 强反型表面电势温度系数 `-8.5e-4` `V/K`（默认）

假设强反型表面电势
2*ϕ*B 随
温度线性缩放，*2ϕB* =
2*ϕBm1* +
(*Ts* –
*Tm1*)*ST,ϕB*。2*ϕBm1* 是
**Main** 设置中 **Surface potential at strong inversion** 参数的值，
*S*T,ϕB 是
**Surface potential at strong inversion temperature
coefficient**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### **速度饱和温度指数** — 速度饱和温度指数 `1.04`（默认）

假设速度饱和 *θsat* 随
温度按指数缩放，*θsat* =
*θsat,m1*
(*Tm1*/*Ts*)^*ηθ*。*θsat,m1* 是
**Main** 设置中 **Velocity saturation factor** 参数的值，
*ηθ* 是 **Velocity saturation temperature exponent**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### **表面粗糙度散射温度指数** — 表面粗糙度散射温度指数 `0.65`（默认）

此参数会导致高栅极电压下 MOSFET 跨导随温度降低。假设表面粗糙度散射
*θsr* 随
温度按指数缩放，*θsr* =
*θsr,m1*
(*Tm1*/*Ts*)^*ηsr*。*θsr,m1* 是
**Main** 设置中 **Surface roughness scattering factor** 参数的值，
*ηsr* 是 **Surface roughness scattering temperature exponent**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### **电阻温度指数** — 电阻温度指数 `0.95`（默认）

假设串联电阻对应于半导体电阻。
因此，它们随温度升高按指数减小。*Ri* =
*Ri,m1*
(*Tm1*/*Ts*)^*ηR*，其中 *i* 分别为 S、D 或 G，对应于源极、漏极或
栅极串联电阻。*Ri,m1*
是 **Ohmic
Resistance** 设置中相应串联电阻参数的值，*ηR* 是
**Resistance temperature exponent**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### **体二极管反向饱和电流温度指数** — 体二极管反向饱和电流温度指数 `3`（默认）

假设体二极管的反向饱和电流与本征载流子浓度的平方成正比，*ni* =
*NC*
exp(–*EG*/2*kB**T*)。*NC* 是随温度变化的
有效态密度，*EG* 是
半导体材料的随温度变化的带隙。为避免引入另一个
温度缩放参数，该模块忽略带隙的温度依赖性，
并对所有器件类型使用硅在 300K 时的带隙（1.12eV）。因此，
温度缩放后的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts))。

*Is,m1* 是 **Body Diode**
设置中 **Reverse
saturation current** 参数的值，*kB* 是玻尔兹曼常数
(8.617x10-5eV/K)，并且
*ηIs* 是 **Body diode reverse
saturation current temperature exponent**。默认值为
`3`，因为硅的 *NC*
大致与 T3/2 成正比。你可以通过务实地选择
*ηIs* 来弥补忽略带隙温度依赖性的影响。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### **器件仿真温度** — 器件仿真温度 `25` `degC`（默认）

器件仿真时的温度 *Ts*。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature
dependence` 时，此参数才可见。

### 故障

故障接口包括 **Fault Inspector** 窗口
以及支持故障的模块的 **Blocks** 选项卡中的 **Faults** 部分。你定义什么会触发故障
以及故障在发生该触发时如何表现。创建和编辑故障时，
你需要对故障行为进行参数化。

要添加故障，请点击 **Add fault**
超链接。

创建故障后，你可以在
**Fault Inspector** 窗口中更改属性。当你打开一个带有故障的模块时，
会出现 **Open Fault Inspector** 超链接，而不是 **Add
fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **PMOS 故障** — 添加故障的选项 `Add fault`（默认）

在 P-Channel MOSFET 模块中添加故障的选项。

### **在以下时间触发故障** — 进入故障状态前的时间 `0` `s`（默认） | 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Timed`。

### **最大允许源栅电压** — 触发故障转换的源栅电压阈值 `inf` `V`（默认） | 正标量

最大允许源栅电压值，高于该值时可能
触发故障。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **最大允许源漏电压** — 触发故障转换的源漏电压阈值 `inf` `V`（默认） | 正标量

最大允许源漏电压值，高于该值时可能
触发故障。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **最大允许体漏电压** — 触发故障转换的体漏电压阈值 `inf` `V`（默认） | 正标量

最大允许体漏电压值，高于该值时可能
触发故障。

#### 依赖关系

要启用此参数：

- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。
- 在 **Main** 设置中，将 **Number of
  terminals** 设置为 `Four`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分中。有关更多信息，请参阅 Set Fault Triggers。

### **最大允许源漏电流** — 触发故障转换的电流阈值 `inf` `A`（默认） | 正标量

最大允许源漏电流值。如果电流超过此值的时间
长于 **Time to fail when exceeding drain-source
current** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **超过源漏电流时的失效时间** — 超过源漏电流时的失效时间 `1` `s`（默认） | 正标量

在触发行为故障之前，源漏电流必须连续超过最大
允许漏源电流的时间量。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为
`Behavioral`。

### **最大允许体二极管电流** — 触发故障转换的体二极管电流阈值 `inf` `A`（默认） | 正标量

最大允许体二极管电流值。如果电流超过此值的时间
长于 **Time to fail when exceeding body diode
current** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数：

- 将 **Model body diode** 设置为
  `Exponential` 或 `Tabulated I-V
  curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分中。有关更多信息，请参阅 Set Fault Triggers。

### **超过体二极管电流时的失效时间** — 超过体二极管电流时的失效时间 `1` `s`（默认） | 正标量

在触发行为故障之前，体二极管电流必须连续超过最大
允许体二极管电流的时间量。

#### 依赖关系

要启用此参数：

- 将 **Model body diode** 设置为
  `Exponential` 或 `Tabulated I-V
  curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分中。有关更多信息，请参阅 Set Fault Triggers。

### **最大二极管恢复，dV/dt** — 最大二极管恢复 `inf` `V/s`（默认） | 正标量

每秒最大二极管恢复量。

#### 依赖关系

要启用此参数：

- 将 **Model body diode** 设置为
  `Exponential` 或 `Tabulated I-V
  curve`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分中。有关更多信息，请参阅 Set Fault Triggers。

### **最大允许温度** — 触发故障转换的温度阈值 `inf` `K`（默认） | 正标量

最大允许温度值。如果温度超过此值的时间
长于 **Time to fail when exceeding
temperature** 参数的值，则模块进入故障状态。

#### 依赖关系

要启用此参数：

- 将 **Modeling option** 设置为 `Threshold-based
  with thermal`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分中。有关更多信息，请参阅 Set Fault Triggers。

### **超过温度时的失效时间** — 超过温度时的失效时间 `1` `s`（默认） | 正标量

在触发行为故障之前，温度必须连续超过最大
允许温度的时间量。

#### 依赖关系

要启用此参数：

- 将 **Modeling option** 设置为 `Threshold-based
  with thermal`。
- 在 **Fault Inspector** 窗口中，将 **Trigger Type** 设置为
  `Behavioral`。

此参数出现在 **Fault Inspector** 窗口的 **Trigger**
部分中。有关更多信息，请参阅 Set Fault Triggers。

### **故障转换时间常数，tau** — 故障转换时间常数 `1e-3` `s`（默认）

转换到故障状态的时间常数。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

### **失效模式** — 失效类别 `Open circuit`（默认） | `Drain-source short` | `Drain-bulk short or source-bulk short` | `Gate oxide short` | `Parameter shift`

失效类型。你可以将此参数设置为：

- `Open circuit` — 由于
  金属化烧毁导致的失效。
- `Drain-source short` — 由于
  漏源沟道上的雪崩击穿导致的失效。
- `Drain-bulk short or source-bulk short` —
  由于漏体或源体沟道上的雪崩击穿导致的失效。
- `Gate oxide short` — 栅极
  氧化物介电层失效。
- `Parameter shift` — 由于
  老化导致的失效。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

要启用 `Drain-source short` 选项，请在
**Main** 设置中，将 **Number of terminals** 设置为
`Three`。

要启用 `Drain-bulk short or source-bulk short`
选项，请在 **Main** 设置中，将 **Number of
terminals** 设置为 `Four`。

### **故障串联栅极电阻，Rg** — 故障串联栅极电阻 `1e6` `Ohm`（默认）

故障状态下的串联栅极电阻。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open
circuit`。

### **故障串联漏极电阻，Rd** — 故障串联漏极电阻 `1000` `Ohm`（默认）

故障状态下的串联漏极电阻。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open
circuit`。

### **故障串联源极电阻，Rs** — 故障串联源极电阻 `1000` `Ohm`（默认）

故障状态下的串联源极电阻。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault**
参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Open
circuit`。

### **故障串联体电阻，Rb** — 故障串联源极电阻 `1000` `Ohm`（默认）

故障状态下的串联源极电阻。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open circuit`。

### **Faulted parallel drain-source conductance, Gds** — 故障状态下的并联漏源电导 `1000` `1/Ohm`（默认值）

故障状态下的并联漏源电导。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Three`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Drain-source short`。

### **Faulted parallel drain-bulk conductance, Gdb** — 故障状态下的并联漏体电导 `1000` `1/Ohm`（默认值）

故障状态下的并联漏体电导。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Drain-bulk short or source-bulk short`。

### **Faulted parallel source-bulk conductance, Gsb** — 故障状态下的并联源体电导 `1000` `1/Ohm`（默认值）

故障状态下的并联源体电导。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Drain-bulk short or source-bulk short`。

### **Location of fault node (percentage of total channel length from source)** — 故障节点位置 `0`（默认值）

故障节点的位置，以距源极的总沟道长度百分比表示。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault** 参数中的 **Add fault** 超链接向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Gate oxide short`。

### **Gate oxide short conductance, G** — 栅氧化层短路电导 `1000` `1/Ohm`（默认值）

栅氧化层短路电导。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault** 参数中的 **Add fault** 超链接向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Gate oxide short`。

### **Model gate oxide short diode** — 栅氧化层短路二极管建模选项 `No`（默认值）| `Yes`

是否对栅氧化层短路二极管进行建模。

#### 依赖关系

要启用此参数，请通过点击 **PMOS fault** 参数中的 **Add fault** 超链接向 P-Channel MOSFET 模块添加故障，并将 **Failure mode** 设置为 `Gate oxide short`。

### **Gate oxide short diode reverse saturation current, Is** — 栅氧化层短路二极管反向饱和电流 `0` `A`（默认值）

栅氧化层短路二极管的反向饱和电流。

#### 依赖关系

要启用此参数：

- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Gate oxide short`。
- 将 **Model gate oxide short diode** 设置为 `Yes`。

### **Gate oxide short diode built-in voltage, Vbi** — 栅氧化层短路二极管内建电压 `0.6` `V`（默认值）

栅氧化层短路二极管的内建电压。

#### 依赖关系

要启用此参数：

- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Gate oxide short`。
- 将 **Model gate oxide short diode** 设置为 `Yes`。

### **Gate oxide short diode ideality factor, n** — 栅氧化层短路二极管理想因子 `1`（默认值）

栅氧化层短路二极管的理想因子。

#### 依赖关系

要启用此参数：

- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Gate oxide short`。
- 将 **Model gate oxide short diode** 设置为 `Yes`。

### **Gate oxide short diode zero-bias junction capacitance, Cj0** — 栅氧化层短路二极管零偏结电容 `0` `pF`（默认值）

栅氧化层短路二极管的零偏结电容。

#### 依赖关系

要启用此参数：

- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Gate oxide short`。
- 将 **Model gate oxide short diode** 设置为 `Yes`。

### **Gate oxide short diode transit time, TT** — 栅氧化层短路二极管渡越时间 `50e-9` `s`（默认值）

栅氧化层短路二极管的渡越时间。

#### 依赖关系

要启用此参数：

- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Gate oxide short`。
- 将 **Model gate oxide short diode** 设置为 `Yes`。

### **Shifted gain as percentage of unshifted** — 偏移后增益占未偏移的百分比 `100`（默认值）

偏移后增益占未偏移的百分比。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Threshold voltage shift value, dVth** — 阈值电压偏移值 `0` `V`（默认值）

阈值电压的偏移值。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted channel modulation, L** — 故障状态下的沟道调制 `0` `1/V`（默认值）

故障状态下的沟道调制。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Shifted body factor as percentage of unshifted** — 偏移后体因子占未偏移的百分比 `100`（默认值）

偏移后体因子占未偏移的百分比。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Surface potential shift value, dPhib** — 表面电势偏移值 `0` `V`（默认值）

表面电势的偏移值。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted source ohmic resistance, Rs** — 故障状态下的源极欧姆电阻 `0.0001` `Ohm`（默认值）

故障状态下的晶体管源极电阻。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted drain ohmic resistance, Rd** — 故障状态下的漏极欧姆电阻 `0.01` `Ohm`（默认值）

故障状态下的晶体管漏极电阻。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted body ohmic resistance, Rb** — 故障状态下的体极欧姆电阻 `0.001` `Ohm`（默认值）

故障状态下的晶体管体极电阻。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet` 或 `Specify using equation parameters directly`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted vector of source-gate voltages, Vsg** — 故障状态下的源栅电压向量 `[-.5, 2, 3, 4, 5]` `V`（默认值）

故障状态下的源栅电压。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted vector of source-drain voltages, Vsd** — 故障状态下的源漏电压向量 `[0, 2, 4, 8, 12, 16, 20]` `V`（默认值）

故障状态下的源漏电压。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted vector of source-bulk voltages, Vsb** — 故障状态下的源体电压向量 `[0, -4, -6, -12]` `V`（默认值）

故障状态下的源体电压。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (2-D, temperature independent)` 或 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted tabulated gate-source threshold voltage, Vth(Vsb)** — 故障状态下的列表栅源阈值电压 `[.4, 1.2, 1.4, 1.45]` `V`（默认值）

故障状态下的列表栅源阈值电压。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (2-D, temperature independent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted tabulated gate-source threshold voltage, Vth(Vsb,T)** — 故障状态下的列表栅源阈值电压（依赖于温度） `[.4, .35; 1.2, 1.15; 1.4, 1.35; 1.45, 1.4]` `V`（默认值）

故障状态下的栅源阈值电压，按体源电压和温度列表。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted tabulated source-drain currents, Isd(Vsg,Vsd)** — 故障状态下的列表源漏电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认值）

故障状态下的列表源漏电流。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Three`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (2-D, temperature independent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted tabulated source-drain currents, Isd(Vsg,Vsd,T)** — 故障状态下的列表源漏电流（依赖于温度） `zeros(5, 7, 2)` `A`（默认值）

故障状态下的源漏电流，按源栅电压、源漏电压和温度列表。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Three`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd)** — 故障状态下源体电压为零时的列表源漏电流 `[0, 0, 0, 0, 0, 0, 0; 0, .003, .0038, .0043, .0046, .0048, .0049; 0, .0055, .008, .009, .0095, .01, .0101; 0, .0115, .016, .018, .019, .0195, .02; 0, .0152, .0225, .0265, .028, .0295, .03]` `A`（默认值）

故障状态下的列表源漏电流，当源体电压为零时。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (2-D, temperature independent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted tabulated source-drain currents at zero source-bulk voltage, Isd(Vsg,Vsd,T)** — 故障状态下源体电压为零时的列表源漏电流（依赖于温度） `zeros(5, 7, 2)` `A`（默认值）

故障状态下的列表源漏电流，当源体电压为零时，按源栅电压、源漏电压和温度列表。

#### 依赖关系

要启用此参数：

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D, temperature dependent)`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted gate-source capacitance as percentage of unfaulted** — 故障状态下栅源电容占未故障的百分比 `100`（默认值）

故障状态下栅源电容占未故障的百分比。

#### 依赖关系

要启用此参数，请满足以下条件之一：

**条件集一**

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

**条件集二**

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open circuit`、`Drain-source short`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **Faulted gate-drain capacitance as percentage of unfaulted** — 故障状态下栅-漏电容占未故障状态的百分比 `100`（默认值）

故障状态下的栅-漏电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请满足以下条件之一：

**条件集一**

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

**条件集二**

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open circuit`、`Drain-source short`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **Faulted gate-bulk capacitance as percentage of unfaulted** — 故障状态下栅-体电容占未故障状态的百分比 `100`（默认值）

故障状态下的栅-体电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请满足以下条件之一：

**条件集一**

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - **Parameterization** 为 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
  - **Gate-bulk and gate-source charge-voltage linearity** 为 `Separate gate-bulk and gate-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

**条件集二**

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - **Parameterization** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **Gate-bulk and gate-source charge-voltage linearity** 为 `Separate gate-bulk and gate-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open circuit`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **Faulted drain-source capacitance as percentage of unfaulted** — 故障状态下漏-源电容占未故障状态的百分比 `100`（默认值）

故障状态下的漏-源电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，请满足以下条件之一：

**条件集一**

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。

**条件集二**

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Open circuit`、`Drain-source short`、`Drain-bulk short or source-bulk short` 或 `Gate oxide short`。

### **Faulted gate-drain oxide capacitance as percentage of unfaulted** — 故障状态下栅-漏氧化层电容占未故障状态的百分比 `100`（默认值）

故障状态下的栅-漏氧化层电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，设置：

  - **Parameterization** 为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
  - **Gate-drain charge-voltage linearity** 为 `Gate-drain charge function is non linear`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted drain-gate voltage at which oxide capacitance becomes active** — 故障状态下氧化层电容开始激活时的漏-栅电压 `-0.5` `V`（默认值）

故障状态下氧化层电容开始激活时的漏-栅电压。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，设置：

  - **Parameterization** 为 `Specify fixed input, reverse transfer, and output capacitance` 或 `Specify fixed gate-source, gate-drain, and drain-source capacitance`。
  - **Gate-drain charge-voltage linearity** 为 `Gate-drain charge function is non linear`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted input capacitance, Ciss(Vds)** — 故障状态下的输入电容 `[720, 700, 590, 470, 390, 310]` `pF`（默认值）

故障状态下的输入电容。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted reverse transfer capacitance, Crss(Vds)** — 故障状态下的反向传输电容 `[450, 400, 300, 190, 95, 55]` `pF`（默认值）

故障状态下的反向传输电容。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted output capacitance, Coss(Vds)** — 故障状态下的输出电容 `[900, 810, 690, 420, 270, 170]` `pF`（默认值）

故障状态下的输出电容。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted corresponding source-drain voltages, Vsd** — 故障状态下对应的源-漏电压 `[.1, .3, 1, 3, 10, 30]` `V`（默认值）

故障状态下对应的漏-源电压。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted source-gate voltages, Vsg, for tabulated capacitances** — 故障状态下用于表格化电容的源-栅电压 `0` `V`（默认值）

故障状态下用于表格化电容的源-栅电压。

#### 依赖关系

要启用此参数，请满足以下条件之一：

**条件集一**

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

**条件集二**

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - **Parameterization** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **Gate-bulk and gate-source charge-voltage linearity** 为 `Gate-bulk and gate-source capacitance change instantly` 或 `Gate-bulk and gate-source capacitance change gradually`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted gate-source capacitance, Cgs(Vgs,Vds)** — 故障状态下的栅-源电容 `[270, 300, 290, 280, 295, 255]` `pF`（默认值）

故障状态下的栅-源电容，以栅-源电压和漏-源电压为表格索引。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted gate-drain capacitance, Cgd(Vgs,Vds)** — 故障状态下的栅-源电容 `[450, 400, 300, 190, 95, 55]` `pF`（默认值）

故障状态下的栅-漏电容，以栅-源电压和漏-源电压为表格索引。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，将 **Parameterization** 设置为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted gate-bulk capacitance, Cgb(Vgs,Vds)** — 故障状态下的栅-源电容 `[270, 300, 290, 280, 295, 255]` `pF`（默认值）

故障状态下的栅-体电容，以栅-源电压和漏-源电压为表格索引。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Number of terminals** 设置为 `Four`。
- 在 **Capacitance** 设置中，设置：

  - **Parameterization** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **Gate-bulk and gate-source charge-voltage linearity** 为 `Separate gate-bulk and gate-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted corresponding source-gate voltages, Vsg** — 故障状态下对应的源-栅电压 `0` `V`（默认值）

故障状态下对应的源-栅电压。

#### 依赖关系

要启用此参数，

- 在 **Capacitance** 设置中，设置：

  - **Parameterization** 为 `Specify tabulated gate-source, gate-drain, and drain-source capacitance`。
  - **Gate-bulk and gate-source charge-voltage linearity** 为 `Separate gate-bulk and gate-source capacitance`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode reverse saturation current, Is** — 故障状态下的二极管反向饱和电流 `0` `A`（默认值）

故障状态下二极管的反向饱和电流。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，将 **Model body diode** 设置为 `Exponential`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode built-in voltage, Vbi** — 故障状态下的二极管内建电压 `0.6` `V`（默认值）

故障状态下二极管的内建电压。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，将 **Model body diode** 设置为 `Exponential`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode ideality factor, n** — 故障状态下的二极管理想因子 `1`（默认值）

故障状态下二极管的理想因子。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，将 **Model body diode** 设置为 `Exponential`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode zero-bias junction capacitance as percentage of unfaulted** — 故障状态下二极管零偏结电容占未故障状态的百分比 `100`（默认值）

故障状态下二极管零偏结电容占未故障状态的百分比。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，将 **Model body diode** 设置为 `Exponential`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode transit time, TT** — 故障状态下的二极管渡越时间 `50e-9` `s`（默认值）

故障状态下二极管的渡越时间。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，将 **Model body diode** 设置为 `Exponential`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode forward currents, If(Vf)** — 故障状态下的二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2]` `A`（默认值）

故障状态下二极管的正向电流，以正向电压为表格索引。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a datasheet`、`Specify using equation parameters directly` 或 `Lookup table (2-D, temperature independent)`。
- 在 **Body Diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V curve`。
  - **Table type** 为 `Table in If(Vf) form`。
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode forward voltages, Vf** — 故障状态下的二极管正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认值）

故障状态下二极管的正向电压。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V curve`。
  - **Table type** 为 `Table in If(Vf) form` 或 `Table in If(Tj,Vf) form`
- 通过点击 **PMOS fault** 参数中的 **Add fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter shift`。

### **Faulted diode forward voltages, Vf(If)** — 故障状态下二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85]` `V`（默认值）

故障状态下二极管的正向电压，与正向电流一起以表格形式列出。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Specify from a
  datasheet`、`Specify using equation parameters
  directly` 或 `Lookup table (2-D, temperature
  independent)`。
- 在 **Body Diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V
    curve`。
  - **Table type** 为 `Table in Vf(If)
    form`。
- 通过点击 **PMOS fault** 参数中的 **Add
  fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode forward currents, If** — 故障状态下二极管正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认值）

故障状态下二极管的正向电流。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V
    curve`。
  - **Table type** 为 `Table in Vf(If)
    form` 和 `Table in Vf(Tj,If)
    form`。
- 通过点击 **PMOS fault** 参数中的 **Add
  fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode forward currents, If(Tj,Vf)** — 带表格输入的故障状态下二极管正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认值）

故障状态下二极管的正向电流，与正向电压和结温一起以表格形式列出。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D,
  temperature dependent)`。
- 在 **Body Diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V
    curve`。
  - **Table type** 为 `Table in If(Tj,Vf)
    form`。
- 通过点击 **PMOS fault** 参数中的 **Add
  fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode forward voltages, Vf(Tj,If)** — 带表格输入的故障状态下二极管正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认值）

故障状态下二极管的正向电压，与正向电流和结温一起以表格形式列出。

#### 依赖关系

要启用此参数，

- 在 **Main** 设置中，将 **Parameterization** 设置为 `Lookup table (3-D,
  temperature dependent)`。
- 在 **Body Diode** 设置中，设置：

  - **Model body diode** 为 `Tabulated I-V
    curve`。
  - **Table type** 为 `Table in Vf(Tj,If)
    form`。
- 通过点击 **PMOS fault** 参数中的 **Add
  fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。

### **Faulted diode off conductance** — 故障状态下二极管关断电导 `1e-12` `1/Ohm`（默认值）

*自 R2024a 起*

故障状态下二极管的关断电导。

#### 依赖关系

要启用此参数，

- 在 **Body Diode** 设置中，将 **Model body
  diode** 设置为 `Tabulated I-V curve`。
- 通过点击 **NMOS fault** 参数中的 **Add
  fault** 超链接，向 P-Channel MOSFET 模块添加故障。
- 将 **Failure mode** 设置为 `Parameter
  shift`。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024b：对每个晶体管端子的寄生引线电阻和电感进行建模

您现在可以通过以下参数指定引线电阻和电感，对 P-Channel MOSFET 模块每个端子的寄生效应进行建模：

- **Source lead resistance**
- **Drain lead resistance**
- **Gate lead resistance**
- **Body lead resistance**
- **Source lead inductance**
- **Drain lead inductance**
- **Gate lead inductance**
- **Body lead inductance**

### R2024a：指定表格化二极管的关断电导值

您现在可以使用 **Diode off conductance** 参数指定表格化二极管的关断电导值。

在 R2024a 之前，要指定表格化二极管的关断电导，必须将 Environment Parameters 模块连接到电气网络。然后，通过设置 Environment Parameters 模块的 **GMIN** 参数来设置 P-Channel MOSFET 模块和其他 SPICE 兼容模块的最小电导。

## 描述

使用 Shichman-Hodges 方程或基于表面势模型的 P 沟道金属氧化物半导体场效应晶体管

P-Channel MOSFET 模块提供两种主要建模选项：

- 基于阈值电压 — 使用 Shichman-Hodges 方程表示器件。这种基于阈值电压的建模方法具有参数化简单和电流-电压表达式简单的优点。然而，这些模型难以准确捕捉跨阈值电压的过渡，并且缺少一些重要效应，例如速度饱和。有关详细信息，请参阅基于阈值的模型。

  此建模选项提供四种对 P-Channel MOSFET 进行参数化的方法：

  - 通过从数据手册指定参数。
  - 通过直接指定方程参数。
  - 通过 I-V（电流-电压）曲线的 2-D 查找表近似。有关详细信息，请参阅通过 2-D 查找表表示。
  - 通过包含温度数据的 I-V（电流-电压）曲线的 3-D 查找表近似。有关详细信息，请参阅通过 3-D 查找表表示。
- 基于表面势 — 使用表面势方程表示器件。这种建模方法比简单的平方律（基于阈值电压的）模型提供更高水平的模型保真度。代价是需要提取更多参数。有关详细信息，请参阅基于表面势的模型。

结合热端口变体（请参阅热端口），该模块因此为您提供四种选择。要选择所需的建模选项，请将 **Modeling option** 参数设置为以下之一：

- **Threshold-based** — 基本模型，使用 Shichman-Hodges 方程（基于阈值电压）表示器件，不模拟热效应。这是默认值。
- **Threshold-based with thermal** — 基于阈值电压并暴露热端口的模型。
- **Surface-potential-based** — 基于表面势的模型。此模型不模拟热效应。
- **Surface-potential-based with thermal** — 基于表面势的模型的热建模选项。

### 基于阈值的模型

该模块的基于阈值建模选项使用绝缘栅场效应晶体管的 Shichman 和 Hodges 方程 [1] 来表示 P-Channel MOSFET。

漏源电流 *IDS* 取决于工作区域：

- 在截止区（–*VGS* <
  –*Vth*）中，漏源电流为：

  IDS=0
- 在线性区（0 < –*VDS* <
  –*VGS*
  +*Vth*）中，漏源电流为：

  IDS=−K((VGS−Vth)VDS−VDS2/2)(1+λ|VDS|)
- 在饱和区（0 < –*VGS*
  +*Vth* <
  –*VDS*）中，漏源电流为：

  IDS=−(K/2)(VGS−Vth)2(1+λ|VDS|)

在上述方程中：

- *K* 是晶体管增益。
- *VDS* 是负漏源电压。
- *VGS* 是栅源电压。
- *Vth* 是阈值电压。对于四端子参数化，*Vth* 使用以下方程获得：

  | *VBS* 范围 | *Vth* 方程 |
  | --- | --- |
  | VBS≤0 | Vth=VT0+γ(2ϕB)−γ(2ϕB+VBS) |
  | 0<VBS≤4ϕB | Vth=VT0−γVBS2ϕB |
  | VBS>4ϕB | Vth=VT0+γ(2ϕB) |
- *λ* 是沟道调制。

要指定沟道的并联电导，请将 Environment Parameters 模块连接到电气网络。然后，通过设置 Environment Parameters 模块的 **GMIN** 参数来设置 P-Channel MOSFET 模块和其他 SPICE 兼容模块的最小电导。

### 基于阈值建模选项的电荷模型

该模块通过固定电容值或作为漏源电压函数的表格值来对电容进行建模。在任一情况下，您都可以直接指定栅源和栅漏电容值，或让模块从输入电容和反向传输电容值推导它们。因此，**Capacitance** 设置上电荷模型的 **Parameterization** 选项为：

- `指定固定输入、反向传递和输出
  capacitance` — 从数据手册提供固定参数值，让模块将输入电容和反向传输电容值转换为电容值，如下所述。这是默认方法。
- `Specify fixed gate-source, gate-drain and drain-source
  capacitance` — 直接为电容参数提供固定值。
- `指定表格化输入、反向传递和输出
  capacitance` — 基于数据手册图表提供表格化电容和漏源电压值。模块将输入电容和反向传输电容值转换为电容值，如下所述。
- `Specify tabulated gate-source, gate-drain and drain-source
  capacitance` — 为电容和漏源电压提供表格化值。

当数据手册提供电容作为漏源电压函数的图表时，请使用表格化电容选项之一（`Specify tabulated input, reverse
transfer and output capacitance` 或 `Specify tabulated
gate-source, gate-drain and drain-source capacitance`）。使用表格化电容值可获得更准确的动态特性，并避免为拟合动态特性而迭代调整参数的需要。

如果您使用 `Specify fixed gate-source, gate-drain and drain-source
capacitance` 或 `Specify tabulated gate-source, gate-drain and
drain-source capacitance` 选项，**Capacitance** 设置允许您直接指定 **Gate-drain capacitance, Cgd**、**Gate-source capacitance, Cgs** 和 **Drain-source capacitance, Cds** 参数值（固定或表格化）。否则，模块从 **Input capacitance, Ciss**、**Reverse
transfer capacitance, Crss** 和 **Output capacitance, Coss** 参数值推导它们。这两种参数化方法的关系如下：

- *CGD* = *Crss*
- *CGS* = *Ciss* –
  *Crss*
- *CDS* = *Coss* –
  *Crss*

对于四端子参数化，**Input capacitance,
Ciss**、**Reverse transfer capacitance, Crss** 和 **Output capacitance, Coss** 使用以下方程获得：

- *CGD* = *Crss*
- *CGS* +
  *CGB* = *Ciss* –
  *Crss*
- *CDB* = *Coss* –
  *Crss*

使用简化的 Meyer 电容模型来描述栅源电容 *CGS*、栅体电容 *CGB* 和栅漏电容 *CGD*。这些图显示了栅体和栅源电容如何瞬时变化，而

栅体和栅源电容瞬时变化。

两种固定电容选项（`Specify fixed input, reverse transfer and
output capacitance` 或 `Specify fixed gate-source, gate-drain and
drain-source capacitance`）允许您将栅极电容建模为固定栅源电容 *CGS* 以及固定或非线性栅漏电容 *CGD*。如果您为 **Gate-drain charge-voltage linearity** 参数选择 `Gate-drain charge function is nonlinear` 选项，则栅漏电荷关系由下图所示的分段线性函数定义。

有关如何将时间响应映射到器件电容值的说明，请参阅 N-Channel IGBT 模块参考页。但是，此映射仅为近似，因为 Miller 电压通常比 IGBT 情况下偏离阈值电压更多。

**注意**

由于此模块实现包含电荷模型，您必须对驱动栅极的电路阻抗进行建模，以获得具有代表性的开通和关断动态特性。因此，如果您通过将栅极驱动电路表示为受控电压源来简化它，则必须在电压源和栅极之间包含合适的串联电阻。

### 通过 2-D 查找表表示

对于详细模块建模选项的查找表表示，您需要提供源漏电流作为源栅电压和源栅电压函数的表格值。使用此选项的主要优点是仿真速度。它还允许您从测量数据或从其他仿真环境获得的数据对器件进行参数化。

此图显示了当您将 **Isd-Vsd parameterization** 设置为 `Provide negative and
positive Vsd data` 时 2-D 查找表选项的实现：

此图显示了当您将 **Isd-Vsd parameterization** 设置为 `Provide positive Vsd data
only` 时 2-D 查找表选项的实现：

对于四端子 MOSFET，表面势和体因子值基于最近的阈值电压计算，如下图所示：

**注意**

为确保源漏电流和源漏电压的符号一致：

- 如果源漏电压等于 `0`，则 **Tabulated source-drain currents, Isd(Vsg,Vsd)** 参数的值必须等于 `0`。
- 表格化功率，即 **Tabulated
  source-drain currents, Isd(Vsg,Vsd)** 参数与源漏电压的乘积，必须大于或等于 `0`。
- 表格化电导，即 **Tabulated
  source-drain currents, Isd(Vsg,Vsd)** 参数关于源漏电压 *Vsd* 的梯度，必须大于或等于 `0`。
- **Tabulated source-drain currents,
  Isd(Vsg,Vsd)** 参数关于源栅电压 *Vsg* 的一阶梯度必须等于 `0`。

### 通过 3-D 查找表表示

对于详细模块建模选项的温度相关查找表表示，您需要提供源漏电流作为源栅电压、源栅电压和温度函数的表格值。

**注意**

为确保源漏电流和源漏电压的符号一致：

- 如果源漏电压等于 `0`，则 **Tabulated source-drain currents, Isd(Vsg,Vsd,T)** 参数的值必须等于 `0`。
- 表格化功率，即 **Tabulated
  source-drain currents, Isd(Vsg,Vsd,T)** 参数与源漏电压的乘积，必须大于或等于 `0`。
- 表格化电导，即 **Tabulated
  source-drain currents, Isd(Vsg,Vsd,T)** 参数关于源漏电压 *Vsd* 的梯度，必须大于或等于 `0`。
- **Tabulated source-drain currents,
  Isd(Vsg,Vsd,T)** 参数关于源栅电压 *Vsg* 的一阶梯度必须等于 `0`。

### Surface-Potential-Based Model

该模块的基于表面电势的建模选项比简单的平方律（基于阈值电压）模型提供更高水平的模型保真度。基于表面电势的模块建模选项包括以下效应：

- 完全非线性电容模型（包括非线性密勒电容）
- 模型内部的电荷守恒，因此您可以将该模型用于电荷敏感仿真
- 速度饱和与沟道长度调制
- 本征体二极管
- 体二极管模型中的反向恢复
- 物理参数的温度缩放
- 对于热建模选项，动态自热（即，您可以仿真自热对器件电气特性的影响）

该模型是世界标准 PSP 模型的最小版本（参见 https://briefs.techconnect.org/papers/introduction-to-psp-mosfet-model/），仅包含 PSP 模型中的某些效应，以在模型保真度和复杂度之间取得平衡。有关该模型中包含的现象的物理背景详细信息，请参见 [2]。

表面电势方程的推导方式与 N-Channel MOSFET 模块参考页面上描述的方式类似，所有电压、电荷和电流均乘以 -1。

整体模型由通过表面电势公式定义的本征 MOSFET、体二极管、串联电阻和固定重叠电容组成，如原理图所示。

### Modeling Body Diode

该模块将体二极管建模为理想指数二极管或表格化二极管。

**Exponential Diode**

该模块将体二极管建模为理想指数二极管或表格化二极管。

当您将 **Model body diode** 设置为 `Exponential` 时，结电容和扩散电容为：

Idio=Is[exp(−VBDnϕT)−1]

Cj=Cj01+VBDVbi

Cdiff=τIsnϕTexp(−VBDnϕT)

其中：

- *Idio* 是流过二极管的电流。
- *Is* 是反向饱和电流。
- *VBD* 是体漏电压。
- *n* 是理想因子。
- *ϕT* 是热电压。
- *Cj* 是二极管的结电容。
- *Cj0* 是零偏结电容。
- *Vbi* 是内建电压。
- *Cdiff* 是二极管的扩散电容。
- *τ* 是渡越时间。

这些电容通过电荷的显式计算来定义，然后对其进行微分以给出上述电容表达式。该模块将电容二极管电流计算为相关电荷的时间导数，类似于基于表面电势的 MOSFET 模型中的计算。

**Tabulated Diode**

要对表格化二极管建模，请将 **Model body diode** 参数设置为 `Tabulated I-V curve`。下图显示了表格化二极管选项的实现：

选择此参数化时，您必须仅提供正向偏置的数据。

该模块使用平滑插值选项来实现二极管。如果二极管超出所提供的表格化数据范围，该模块将在最后一个电压-电流数据点处使用线性外推技术。

要指定表格化二极管的关断电导，请设置 **Diode off conductance** 参数。*(since R2024a)*

**Note**

表格化二极管不对反向击穿建模。

### Modeling Temperature Dependence

默认行为是不对温度依赖性建模，器件在您提供模块参数的温度下进行仿真。要在仿真期间对温度依赖性建模，请在 **Temperature Dependence** 设置中为 **Parameterization** 参数选择 `Model temperature dependence`。

**Threshold-Based Model**

对于基于阈值的建模选项，您可以包括在仿真期间对晶体管静态行为温度依赖性的建模。结电容的温度依赖性不建模，因为这是一个小得多的效应。

当包括温度依赖性时，定义晶体管的方程保持不变。增益 *K* 和阈值电压 *Vth* 根据以下方程成为温度的函数：

KTs=KTm1(TsTm1)BEX

*V*ths =
*Vth1* + *α* (
*Ts* – *Tm1*)

其中：

- *Tm1* 是指定晶体管参数时的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *KTm1* 是测量温度下的晶体管增益。
- *KTs* 是仿真温度下的晶体管增益。这是当对温度依赖性建模时在 MOSFET 方程中使用的晶体管增益值。
- *Vth1* 是测量温度下的阈值电压。
- *Vths* 是仿真温度下的阈值电压。这是当对温度依赖性建模时在 MOSFET 方程中使用的阈值电压值。
- *BEX* 是迁移率温度指数。*BEX* 的典型值为 -1.5。
- *α* 是栅极阈值电压温度系数，*d**Vth*/*d**T*。

对于四端子参数化，*Vth* 使用以下方程获得：

| *VBS* Range | *Vth* Equation |
| --- | --- |
| VBS≤0 | dVthdT=dVT0dT−γ22ϕBd2ϕBdT+γ22ϕB−VBSd2ϕBdT |
| 0<VBS≤4ϕB | dVthdT=dVT0dT−γVBS4(2ϕB)−32d2ϕBdT |
| VBS>4ϕB | dVthdT=dVT0dT−γ22ϕBd2ϕBdT |

其中：

- ϕB=kTqln(NBni) 是表面电势，且 d2ϕBdT=−1T[2ϕB−(Eg(0)q+3kTq)]。
- *Eg(0)* 是外推的零度带隙，对于硅等于 `1.16` `eV`。
- *VBS* 是体源电压。

对于大多数 MOSFET，您可以使用 *BEX* 的默认值 `-1.5`。一些数据手册给出了 *α* 的值，但最典型的是它们提供漏源导通电阻 *RDS(on)* 的温度依赖性。根据模块参数化方法，您有两种指定 *α* 的方式：

- 如果您从数据手册参数化模块，您必须提供第二个测量温度下的 *RDS(on)*。然后该模块基于此数据计算 *α* 的值。
- 如果您通过指定方程参数来参数化，您必须直接提供 *α* 的值。

如果您有更多数据，包括多个温度下漏极电流作为栅源电压的函数，那么您还可以使用 Simulink® Design Optimization™ 软件来帮助调整 *α* 和 *BEX* 的值。

**Surface-Potential-Based Model**

基于表面电势的模型包括温度对电容特性的影响，以及在仿真期间对晶体管静态行为温度依赖性的建模。

**Main** 设置上的 **Measurement temperature** 参数指定了提取其他器件参数时的温度 *Tm1*。**Temperature Dependence** 设置提供了仿真温度 *Ts* 以及其他器件参数的温度缩放系数。有关更多信息，请参见 Temperature Dependence (Surface-Potential-Based Modeling Option)。

### 故障

要对 P-Channel MOSFET 模块中的故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参见 Fault Behavior Modeling and Fault Triggering。

P-Channel MOSFET 模块对五种类型的故障建模：

- `Open circuit` — 由于金属化烧毁导致的故障
- `Drain-source short` — 由于漏源沟道雪崩击穿导致的故障
- `Drain-bulk short or source-bulk short` — 由于漏体或源体沟道雪崩击穿导致的故障
- `Gate oxide short` — 栅极氧化物介电层故障
- `Parameter shift` — 由于老化导致的故障

该模块可以在特定时间触发故障事件，或者当电流或电压超过限值的时间长于特定时间间隔时触发。

**Parameter Shift Fault**

如果在 **Faults** 设置中将 **Failure mode** 参数设置为 `Parameter shift`，则 MOSFET 由于其组件老化而失效。此方程定义了偏移参数的值：

Parameter(t)=Parameterfaulted−(Parameterfaulted−Parameterunfaulted)sech(t−tthτ),

其中 *tth* 是触发故障的时间阈值，*τ* 是 **Fault transition time constant, tau** 参数的值。

**Gate Oxide Short Fault**

如果在 **Faults** 设置中将 **Failure mode** 参数设置为 `Gate oxide short`，则栅极氧化物介电层失效。这些图显示了未故障和故障状态下三端子 MOSFET 的等效电路：

这些图显示了未故障和故障状态下四端子 MOSFET 的等效电路：

### Thermal Port

该模块有一个可选的热端口，默认隐藏。要暴露热端口，请将 **Modeling option** 参数设置为：

- `Threshold-based with thermal` — 基于阈值电压并暴露热端口的模型
- `Surface-potential-based with thermal` — 基于表面电势并暴露热端口的模型

此操作会在模块图标上显示热端口 **H**，并暴露 **Thermal Port** 参数。

使用热端口来仿真生成的热量和器件温度的影响。有关使用热端口和 **Thermal Port** 参数的更多信息，请参见 Simulating Thermal Effects in Semiconductors。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参见 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参见 System Scaling by Nominal Values。

此表显示了模块电容与初始目标之间的关系：

| Defined Capacitance | Initial Targets |
| --- | --- |
| Gate-emitter capacitance, *Cge* | 仅设置栅极-发射极电容电压的初始目标。将集电极-发射极电容电压的初始目标设置为 `0` 或将其优先级设置为 `None`。 |
| Collector-emitter capacitance, *Cce* | 仅设置集电极-发射极电容电压的初始目标。将栅极-发射极电容电压的初始目标设置为 `0` 或将其优先级设置为 `None`。 |
| Gate-collector capacitance, *Cgc* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-集电极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极和集电极-发射极之间的电压。 |
| Gate-emitter capacitance, *Cge*, and gate-collector capacitance, *Cgc* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-发射极和栅极-集电极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极和集电极-发射极之间的电压。 |
| Gate-emitter capacitance, *Cge*, and collector-emitter capacitance, *Cce* | 设置栅极-发射极和集电极-发射极电容的初始目标。 |
| Gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-集电极和集电极-发射极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极和集电极-发射极之间的电压。 |
| Gate-emitter capacitance, *Cge*, gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | 通过对栅极-发射极和集电极-发射极电压施加约束来设置栅极-发射极、栅极-集电极和集电极-发射极电容的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极和集电极-发射极之间的电压。 |

**Note**

在您的模型内部，**Priority** 等于 `Low` 或 `High` 的初始目标数量必须与微分变量数量匹配。微分变量来自模型中的电感和电容。

### Plot Device Characteristics

您可以在不构建完整模型的情况下绘制 P-Channel MOSFET 模块的基本 I-V 特性。使用这些图来探索您的参数选择对器件特性的影响。如果您从数据手册参数化模块，您可以将您的图与数据手册进行比较，以检查您是否正确参数化了模块。如果您有一个完整的工作模型但不知道使用哪个制造零件，您可以将您的图与数据手册进行比较以帮助您决定。

要启用此选项，请将 P-Channel MOSFET 模块的 **Modeling option** 参数设置为 `Threshold Based` 或 `Surface potential based`。要绘制基本特性，请右键单击模块并从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的更多信息，请参见 Plot Basic I-V Characteristics of Semiconductor Blocks。

P-Channel MOSFET 模块还支持 **Explore characteristics** 选项。使用此选项对模块特性进行深入研究，并将模块行为与一组目标特性匹配。要启用此选项，请将模块的 **Modeling option** 参数设置为 `Surface potential based`。然后，右键单击模块并从上下文菜单中选择 **Electrical** > **Explore characteristics**。有关此选项的更多信息，请参见 MOSFET Characteristics Viewer。
