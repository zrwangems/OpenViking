---
type: simulink-block
title: '4-Way 2-Position Directional Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way2positiondirectionalvalve2p'
documentation_source_path: 'ref/4way2positiondirectionalvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 2-Position Directional Valve (2P)

## 端口
```yaml
ports:
- name: A
  summary: 两相流体的入口或出口
  direction: conserving
- name: B
  summary: 两相流体的入口或出口
  direction: conserving
- name: P
  summary: 两相流体的入口或出口
  direction: conserving
- name: T
  summary: 两相流体的入口或出口
  direction: conserving
- name: S
  summary: 阀芯位移，m 物理信号
  direction: input
```

### 守恒端口

### **A** — 两相流体的入口或出口

与阀的入口或出口关联的两相流体守恒端口。

### **B** — 两相流体的入口或出口

与阀的入口或出口关联的两相流体守恒端口。

### **P** — 两相流体的入口或出口

与阀的入口或出口关联的两相流体守恒端口。

### **T** — 两相流体的入口或出口

与阀的入口或出口关联的两相流体守恒端口。

### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移关联的物理信号，单位为 m。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 流体相的建模选项 Liquid operating condition（默认）| Vapor operating condition
  group: ''
- name: Positive spool position open connections
  summary: 阀芯处于正位置时打开的流路 P-A, B-T（默认）| P-A, P-B | P-B, A-T | P-A | P-B | P-A, P-B, A-T, B-T
  group: 阀配置
- name: Negative spool position open connections
  summary: 阀芯沿负方向运动时打开的流路 P-B, A-T（默认）| P-A, B-T | P-A, P-B | P-A | P-B | P-A, P-B, A-T, B-T
  group: 阀配置
- name: Area characteristics
  summary: 节流口的流量方程 Identical for all flow paths（默认）| 每条流不同 path
  group: 模型参数化
- name: Orifice parameterization
  summary: 可变或恒定节流口参数化 Linear - Area vs. spool travel（默认）| Linear - Nominal mass flow rate vs. spool travel | Tabulated data
    - Area vs. spool travel | Cv flow coefficient | Kv flow coefficient | Orifice area
  group: 模型参数化
- name: Spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: 模型参数化
- name: Maximum orifice area
  summary: 最大节流口开口面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: Nominal mass flow rate at maximum orifice opening
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: 模型参数化
- name: Nominal pressure drop at maximum orifice opening
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: 模型参数化
- name: Nominal inlet condition specification
  summary: 确定入口流体状态的方法 Temperature（默认）| Vapor quality | Vapor void fraction | Specific enthalpy | Specific internal energy
  group: 模型参数化
- name: Nominal inlet pressure
  summary: 入口流体压力 0.101325 MPa（默认）| 正标量
  group: 模型参数化
- name: Nominal inlet temperature
  summary: 流体温度 293.15 K（默认）| 正标量
  group: 模型参数化
- name: Nominal inlet vapor quality
  summary: 入口蒸汽质量分数 0（默认）| [0,1] 范围内的正标量
  group: 模型参数化
- name: Nominal inlet vapor void fraction
  summary: 入口体积分数 0（默认）| [0,1] 范围内的正标量
  group: 模型参数化
- name: Nominal inlet specific enthalpy
  summary: 入口流体比焓 400 kJ/kg（默认）| 正标量
  group: 模型参数化
- name: Nominal inlet specific internal energy
  summary: 入口比内能 400 kJ/kg（默认）| 正标量
  group: 模型参数化
- name: Opening characteristic
  summary: 将控制信号转换为流量能力度量的方法 Linear（默认）| Tabulated
  group: 模型参数化
- name: Spool travel vector
  summary: 相对于全关位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: 模型参数化
- name: Orifice area vector
  summary: 阀开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 模型参数化
- name: Maximum Cv flow coefficient
  summary: 对应最大开度的 *Cv* 系数 4（默认）| 正标量
  group: 模型参数化
- name: Cv flow coefficient vector
  summary: 构件位置向量中各值对应的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: 模型参数化
- name: Maximum Kv flow coefficient
  summary: 对应最大开度的 *Kv* 系数 3.6（默认）| 正标量
  group: 模型参数化
- name: Kv flow coefficient vector
  summary: 构件位置向量中各值对应的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: 模型参数化
- name: xT pressure differential ratio factor at choked flow
  summary: 压差比系数 0.7（默认）| 正标量
  group: 模型参数化
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: 模型参数化
- name: Leakage flow fraction
  summary: 流量比 1e-6（默认）| 正标量
  group: 模型参数化
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| [0,1] 范围内的正标量
  group: 模型参数化
- name: Pressure recovery
  summary: 是否考虑面积扩大时的压力升高 off（默认）| on
  group: 模型参数化
- name: Laminar flow pressure ratio
  summary: 层流-湍流过渡压力比 0.999（默认）| 正标量
  group: 模型参数化
- name: Inlet phase change time constant
  summary: 混合物比容的时间滞后 0.1 s（默认）| 正标量
  group: 模型参数化
- name: Cross-sectional area at ports P, T, A and B
  summary: 守恒端口处的面积 0.01 m^2（默认）| 正标量
  group: 模型参数化
- name: Spool position at maximum P-A orifice area
  summary: P-A 节流口完全开启时的阀芯偏移 5e-3 m（默认）| 正标量
  group: P-A Orifice
- name: P-A spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: P-A Orifice
- name: P-A nominal mass flow rate at maximum orifice opening
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: P-A Orifice
- name: P-A nominal pressure drop at maximum orifice opening
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: P-A Orifice
- name: P-A nominal inlet condition specification
  summary: 确定入口流体状态的方法 Temperature（默认）| Vapor quality | Vapor void fraction | Specific enthalpy | Specific internal energy
  group: P-A Orifice
- name: P-A nominal inlet pressure
  summary: 入口流体压力 0.101325 MPa（默认）| 正标量
  group: P-A Orifice
- name: P-A nominal inlet temperature
  summary: 流体温度 293.15 K（默认）| 正标量
  group: P-A Orifice
- name: P-A nominal inlet vapor quality
  summary: 入口蒸汽干度质量分数 0（默认）| [0,1] 范围内的正标量
  group: P-A Orifice
- name: P-A nominal inlet vapor void fraction
  summary: 入口蒸汽空泡率 0（默认）| [0,1] 范围内的正标量
  group: P-A Orifice
- name: P-A nominal inlet specific enthalpy
  summary: 入口流体比焓 400 kJ/kg（默认）| 正标量
  group: P-A Orifice
- name: P-A nominal inlet specific internal energy
  summary: 入口比内能 400 kJ/kg（默认）| 正标量
  group: P-A Orifice
- name: P-A constant orifice nominal mass flow rate
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: P-A Orifice
- name: P-A constant orifice nominal pressure drop
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: P-A Orifice
- name: P-A constant orifice Cv flow coefficient
  summary: 流量系数 4（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice maximum Cv flow coefficient
  summary: 对应组件最大开启状态的 *Cv* 系数 4（默认）| 正标量
  group: P-A Orifice
- name: P-A orifice Cv flow coefficient vector
  summary: 成员位置向量 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）中值的 *Cv* 系数 | 1×*n* 向量
  group: P-A Orifice
- name: P-A constant orifice Kv flow coefficient
  summary: 流量系数 3.6（默认） | 正标量
  group: P-A Orifice
- name: P-A orifice maximum Kv flow coefficient
  summary: 对应最大开启组件的 *Kv* 系数 3.6（默认） | 正标量
  group: P-A Orifice
- name: P-A orifice Kv flow coefficient vector
  summary: 成员位置向量 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）中值的 *Kv* 系数 | 1×*n* 向量
  group: P-A Orifice
- name: P-A orifice spool travel vector
  summary: 相对于完全关闭位置的阀芯开启距离向量 [0, .00125, .0025, .00375, .005] m（默认） | 1×*n* 向量
  group: P-A Orifice
- name: P-A maximum orifice area
  summary: 最大节流孔开启面积 1e-4 m^2（默认） | 正标量
  group: P-A Orifice
- name: P-A orifice area vector
  summary: 阀开启面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认） | 1×*n* 向量
  group: P-A Orifice
- name: P-A constant orifice area
  summary: 恒定节流孔的横截面积 1e-4 m^2（默认） | 正标量
  group: P-A Orifice
- name: P-A orifice xT pressure differential ratio factor at choked flow
  summary: 压差比系数 0.7（默认） | 正标量
  group: P-A Orifice
- name: Spool position at maximum P-B orifice area
  summary: P-B 节流孔完全打开时的阀芯偏移 5e-3 m（默认） | 正标量
  group: P-B Orifice
- name: P-B spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认） | 正标量
  group: P-B Orifice
- name: P-B nominal mass flow rate at maximum orifice opening
  summary: 额定质量流量 0.1 kg/s（默认） | 正标量
  group: P-B Orifice
- name: P-B nominal pressure drop at maximum orifice opening
  summary: 额定压降 0.001 MPa（默认） | 正标量
  group: P-B Orifice
- name: P-B nominal inlet condition specification
  summary: 确定入口流体状态的方法 Temperature（默认） | Vapor quality | Vapor void fraction | Specific enthalpy | Specific internal energy
  group: P-B Orifice
- name: P-B nominal inlet pressure
  summary: 入口流体压力 0.101325 MPa（默认） | 正标量
  group: P-B Orifice
- name: P-B nominal inlet temperature
  summary: 流体温度 293.15 K（默认） | 正标量
  group: P-B Orifice
- name: P-B nominal inlet vapor quality
  summary: 入口蒸汽干度质量分数 0（默认） | [0,1] 范围内的正标量
  group: P-B Orifice
- name: P-B 额定入口蒸汽空泡份额
  summary: 入口蒸汽空泡份额 0（默认）| [0,1] 范围内的正标量
  group: P-B Orifice
- name: P-B 额定入口比焓
  summary: 入口流体比焓 400 kJ/kg（默认）| 正标量
  group: P-B Orifice
- name: P-B 额定入口比内能
  summary: 入口比内能 400 kJ/kg（默认）| 正标量
  group: P-B Orifice
- name: P-B 恒定节流孔额定质量流量
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: P-B Orifice
- name: P-B 恒定节流孔额定压降
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: P-B Orifice
- name: P-B 恒定节流孔 Cv 流量系数
  summary: 流量系数 4（默认）| 正标量
  group: P-B Orifice
- name: P-B 节流孔最大 Cv 流量系数
  summary: 对应于组件最大开度的 *Cv* 系数 4（默认）| 正标量
  group: P-B Orifice
- name: P-B 节流孔 Cv 流量系数向量
  summary: 对应于构件位置向量中各值的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B 恒定节流孔 Kv 流量系数
  summary: 流量系数 3.6（默认）| 正标量
  group: P-B Orifice
- name: P-B 节流孔最大 Kv 流量系数
  summary: 对应于组件最大开度的 *Kv* 系数 3.6（默认）| 正标量
  group: P-B Orifice
- name: P-B 节流孔 Kv 流量系数向量
  summary: 对应于构件位置向量中各值的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B 节流孔阀芯行程向量
  summary: 相对于全关位置的阀芯开度距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B 最大节流孔面积
  summary: 最大节流孔开度面积 1e-4 m^2（默认）| 正标量
  group: P-B Orifice
- name: P-B 节流孔面积向量
  summary: 阀开度面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: P-B Orifice
- name: P-B 恒定节流孔面积
  summary: 恒定节流孔横截面积 1e-4 m^2（默认）| 正标量
  group: P-B Orifice
- name: P-B 节流孔 xT 阻塞流压差比系数
  summary: 压差比 0.7（默认）| 正标量
  group: P-B Orifice
- name: Spool position at maximum A-T orifice area
  summary: 完全打开 A-T 节流口时的阀芯偏移 5e-3 m（默认）| 正标量
  group: A-T 节流孔
- name: A-T spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: A-T 节流孔
- name: A-T nominal mass flow rate at maximum orifice opening
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: A-T 节流孔
- name: A-T nominal pressure drop at maximum orifice opening
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: A-T 节流孔
- name: A-T nominal inlet condition specification
  summary: 确定入口流体状态的方法 Temperature（默认）| Vapor quality | Vapor void fraction | Specific enthalpy | Specific internal energy
  group: A-T 节流孔
- name: A-T nominal inlet pressure
  summary: 入口流体压力 0.101325 MPa（默认）| 正标量
  group: A-T 节流孔
- name: A-T nominal inlet temperature
  summary: 流体温度 293.15 K（默认）| 正标量
  group: A-T 节流孔
- name: A-T nominal inlet vapor quality
  summary: 入口蒸汽干度质量分数 0（默认）| 范围 [0,1] 内的正标量
  group: A-T 节流孔
- name: A-T nominal inlet vapor void fraction
  summary: 入口蒸汽空泡率 0（默认）| 范围 [0,1] 内的正标量
  group: A-T 节流孔
- name: A-T nominal inlet specific enthalpy
  summary: 入口流体比焓 400 kJ/kg（默认）| 正标量
  group: A-T 节流孔
- name: A-T nominal inlet specific internal energy
  summary: 入口比内能 400 kJ/kg（默认）| 正标量
  group: A-T 节流孔
- name: A-T constant orifice nominal mass flow rate
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: A-T 节流孔
- name: A-T constant orifice nominal pressure drop
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: A-T 节流孔
- name: A-T constant orifice Cv flow coefficient
  summary: 流量系数 4（默认）| 正标量
  group: A-T 节流孔
- name: A-T orifice maximum Cv flow coefficient
  summary: 对应组件最大开度的 *Cv* 系数 4（默认）| 正标量
  group: A-T 节流孔
- name: A-T orifice Cv flow coefficient vector
  summary: 成员位置向量中各值对应的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T constant orifice Kv flow coefficient
  summary: 流量系数 3.6（默认）| 正标量
  group: A-T 节流孔
- name: A-T orifice maximum Kv flow coefficient
  summary: 对应组件最大开度的 *Kv* 系数 3.6（默认）| 正标量
  group: A-T 节流孔
- name: A-T orifice Kv flow coefficient vector
  summary: 成员位置向量 [1e-06, .72, 1.44, 2.16, 2.88, 3.6] 中值的 *Kv* 系数（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T orifice spool travel vector
  summary: 相对于全关闭位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T maximum orifice area
  summary: 最大节流口开口面积 1e-4 m^2（默认）| 正标量
  group: A-T 节流孔
- name: A-T orifice area vector
  summary: 阀开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: A-T 节流孔
- name: A-T constant orifice area
  summary: 恒定节流口横截面积 1e-4 m^2（默认）| 正标量
  group: A-T 节流孔
- name: A-T orifice xT pressure differential ratio factor at choked flow
  summary: 压差比 0.7（默认）| 正标量
  group: A-T 节流孔
- name: Spool position at maximum B-T orifice area
  summary: 全开 B-T 节流口的阀芯偏移 5e-3 m（默认）| 正标量
  group: B-T Orifice
- name: B-T spool travel between closed and open orifice
  summary: 最大阀芯行程 0.005 m（默认）| 正标量
  group: B-T Orifice
- name: B-T nominal mass flow rate at maximum orifice opening
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: B-T Orifice
- name: B-T nominal pressure drop at maximum orifice opening
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: B-T Orifice
- name: B-T nominal inlet condition specification
  summary: 确定入口流体状态的方法 Temperature（默认）| Vapor quality | Vapor void fraction | Specific enthalpy | Specific internal energy
  group: B-T Orifice
- name: B-T nominal inlet pressure
  summary: 入口流体压力 0.101325 MPa（默认）| 正标量
  group: B-T Orifice
- name: B-T nominal inlet temperature
  summary: 流体温度 293.15 K（默认）| 正标量
  group: B-T Orifice
- name: B-T nominal inlet vapor quality
  summary: 入口蒸汽干度质量分数 0（默认）| [0,1] 范围内的正标量
  group: B-T Orifice
- name: B-T nominal inlet vapor void fraction
  summary: 入口蒸汽空泡率 0（默认）| [0,1] 范围内的正标量
  group: B-T Orifice
- name: B-T nominal inlet specific enthalpy
  summary: 入口流体比焓 400 kJ/kg（默认）| 正标量
  group: B-T Orifice
- name: B-T nominal inlet specific internal energy
  summary: 入口比内能 400 kJ/kg（默认）| 正标量
  group: B-T Orifice
- name: B-T constant orifice nominal mass flow rate
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: B-T Orifice
- name: B-T constant orifice nominal pressure drop
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: B-T Orifice
- name: B-T constant orifice Cv flow coefficient
  summary: 流量系数 4（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice maximum Cv flow coefficient
  summary: 对应最大开度的 *Cv* 系数 4（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice Cv flow coefficient vector
  summary: 对应构件位置向量中各值的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T constant orifice Kv flow coefficient
  summary: 流量系数 3.6（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice maximum Kv flow coefficient
  summary: 对应最大开度的 *Kv* 系数 3.6（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice Kv flow coefficient vector
  summary: 对应构件位置向量中各值的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T orifice spool travel vector
  summary: 相对于全关位置的阀芯开口距离向量 [0, .00125, .0025, .00375, .005] m（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T maximum orifice area
  summary: 最大节流口开口面积 1e-4 m^2（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice area vector
  summary: 阀口开口面积向量 [1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2（默认）| 1×*n* 向量
  group: B-T Orifice
- name: B-T constant orifice area
  summary: 恒定节流口横截面积 1e-4 m^2（默认）| 正标量
  group: B-T Orifice
- name: B-T orifice xT pressure differential ratio factor at choked flow
  summary: 压差比系数 0.7（默认）| 正标量
  group: B-T Orifice
```

### **Modeling option** — 流体相的建模选项 `Liquid operating condition`（默认）| `Vapor operating condition`

阀处流体相的建模选项。如果模块位置处的两相流体处于液态，则将此参数设置为 `Liquid operating condition`。如果模块位置处的两相流体处于气态，则将此参数设置为 `Vapor operating condition`。

### 阀配置

### **Positive spool position open connections** — 阀芯处于正位置时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

阀芯处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### **Negative spool position open connections** — 阀芯沿负方向运动时打开的流路 `P-B, A-T`（默认）| `P-A, B-T` | `P-A, P-B` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

阀芯沿负方向运动时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### 模型参数化

### **Area characteristics** — 节流口的流量方程 `Identical for all flow paths`（默认）| `每条流不同 path`

是对阀节流口面积应用统一的流量方程还是各自的流量方程。当将此参数设置为 `Identical for all flow paths` 时，模块对所有阀节流口使用相同的节流口和阀芯几何参数、流量、压力和面积向量。当将此参数设置为 `每条流不同 path` 时，可以为每个节流口单独指定这些参数。对于这两种设置，当将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流口 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **Orifice parameterization** — 可变或恒定节流口参数化 `Linear - Area vs. spool travel`（默认）| `Linear - Nominal mass flow rate vs. spool travel` | `Tabulated data - Area vs. spool travel` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

模块用于根据节流口两端的压差计算质量流量或根据质量流量计算压差的方法。

当 **Modeling option** 为 `Liquid operating condition` 时，此参数的选项为：

- `Linear - Area vs. spool travel`
- `Linear - Nominal mass flow rate vs. spool travel`
- `Tabulated data - Area vs. spool travel`

当 **Modeling option** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯的最大行程距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀运行期间每个节流口的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，且 **Opening characteristic** 设置为 `Linear`。

### **Nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` kg/s（默认）| 正标量

节流口最大开口位置处的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` MPa（默认）| 正标量

节流口最大开口位置处的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **Nominal inlet pressure** 和 **Nominal inlet condition specification** 参数的值，从表格化流体属性数据中确定节流口额定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet pressure** — 入口流体压力 `0.101325` MPa（默认）| 正标量

额定工况下的入口压力。模块根据 **Nominal inlet pressure** 和 **Nominal inlet condition specification** 参数的值，从表格化流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet temperature** — 流体温度 `293.15` K（默认）| 正标量

额定工况下的入口流体温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 入口蒸汽质量分数 `0`（默认）| [0,1] 范围内的正标量

额定工况下入口混合物的蒸汽质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Vapor quality`。

### **Nominal inlet vapor void fraction** — 入口体积分数 `0`（默认）| [0,1] 范围内的正标量

额定工况下入口混合物的体积分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Vapor void fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg（默认）| 正标量

额定工况下的入口比焓。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg（默认）| 正标量

额定工况下的入口比内能。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Specific internal energy`。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`。

### **Spool travel vector** — 相对于全关位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格化阀面积数据对节流口进行参数化时的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

根据表格化阀面积数据对节流口进行参数化时的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大开度的 *Cv* 系数 `4`（默认）| 正标量

节流口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Cv flow coefficient`，且 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 构件位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Cv flow coefficient`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

节流口完全打开且可用流动面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Kv flow coefficient`，且 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 构件位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Kv flow coefficient`，且 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞流时的值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition` 且 **Orifice parameterization** 设置为 `Orifice area`，或将 **Modeling option** 设置为 `Liquid operating condition` 且 **Orifice parameterization** 设置为以下任一选项：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流口关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀处于接近开启和接近关闭位置时，基于流量响应引入一层渐变变化。
为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`，或者将 **Modeling option** 设置为 `Vapor operating condition`，并将 **Opening characteristic** 设置为 `Linear`。

### **Pressure recovery** — 是否考虑面积扩大时的压力升高 `off`（默认）| `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力升高。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流工况之间过渡时的节流口出口压力与节流口入口压力之比。
在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Inlet phase change time constant** — 混合物比容的时间滞后 `0.1` `s`（默认）| 正标量

计算流体比容时液-汽混合物的时间滞后。当入口流体为完全过冷液体或完全过热蒸汽时，此参数不影响比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`。

### **Cross-sectional area at ports P, T, A and B** — 守恒端口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用该值。

### P-A Orifice

### **Spool position at maximum P-A orifice area** — P-A 节流口完全开启时的阀芯偏移 `5e-3 m`（默认）| 正标量

P-A 节流口完全开启时阀芯从中位开始的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

将 **Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

或将 **Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-A spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `每条流不同 path`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `每条流不同 path`，且 **Opening characteristic** 设置为 `Linear`。

### **P-A nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开启 P-A 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开启 P-A 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-A 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

额定工况下 P-A 节流口的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

额定工况下 P-A 节流口的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Temperature`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

额定工况下 P-A 节流口入口混合物的蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor quality`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal inlet vapor void fraction** — 入口蒸汽空泡率 `0`（默认）| [0,1] 范围内的正标量

额定工况下 P-A 节流口入口混合物的蒸汽空泡率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor void fraction`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

额定工况下 P-A 节流口的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Specific enthalpy`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

额定工况下 P-A 节流口的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Specific internal energy`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A constant orifice nominal mass flow rate** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 P-A 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-A constant orifice nominal pressure drop** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过恒定 P-A 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-A constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

P-A 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Cv flow coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-A orifice maximum Cv flow coefficient** — 对应组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

P-A 节流口完全开启且可用流通面积为最大值时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `每条流不同 path`
3. **Orifice parameterization** 设置为 `Cv flow coefficient`
4. **Opening characteristic** 设置为 `Linear`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice Cv flow coefficient vector** — 成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）中值的 *Cv* 系数 | 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Cv flow coefficient`
4. **Opening characteristic** 为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认） | 正标量

P-A 节流孔的恒定 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-A orifice maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认） | 正标量

P-A 节流孔完全打开且可用流动面积最大时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient`
4. **Opening characteristic** 为 `Linear`
5. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice Kv flow coefficient vector** — 成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）中值的 *Kv* 系数 | 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient`
4. **Opening characteristic** 为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Tabulated`。

### **P-A maximum orifice area** — 最大节流孔开启面积 `1e-4 m^2`（默认） | 正标量

阀门运行期间 P-A 节流孔的最大开启面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

同时将 **Area characteristics** 设置为 `每条流不同 path`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Linear`。

### **P-A orifice area vector** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1×*n* 向量

用于阀面积表格化参数化的开启面积向量。向量元素必须与 **P-A orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

同时将 **Area characteristics** 设置为 `每条流不同 path`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Tabulated`。

### **P-A constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认） | 正标量

当正负阀芯位置包含相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下设置之一：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Tabulated`。

**注意：**

仅当 P-A 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-A orifice xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认） | 正标量

P-A 节流孔首次发生阻塞时，入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中至少一个：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### P-B Orifice

### **Spool position at maximum P-B orifice area** — P-B 节流孔完全打开时的阀芯偏移 `5e-3 m`（默认） | 正标量

P-B 节流孔完全打开时阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | 正标量

阀芯行程的最大距离。该值作为计算的上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Linear`。

### **P-B nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认） | 正标量

通过最大开启 P-B 节流孔的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认） | 正标量

通过最大开启 P-B 节流孔的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-B 节流孔入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认） | 正标量

P-B 节流孔在额定条件下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet temperature** — 流体温度 `293.15` `K`（默认） | 正标量

P-B 节流孔在额定运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Temperature`
5. 以下参数中至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认） | [0,1] 范围内的正标量

P-B 节流孔在额定运行条件下的入口混合物蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Vapor quality`
5. 以下参数中至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 额定入口蒸汽空泡份额** — 入口蒸汽空泡份额 `0`（默认）| [0,1] 范围内的正标量

P-B 节流孔在额定工况下的入口混合物蒸汽空泡份额。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Vapor void fraction`
5. 以下参数中的至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 额定入口比焓** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

P-B 节流孔在额定工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Specific enthalpy`
5. 以下参数中的至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 额定入口比内能** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

P-B 节流孔在额定工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Specific internal energy`
5. 以下参数中的至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 恒定节流孔额定质量流量** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 P-B 节流孔的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-B 恒定节流孔额定压降** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过恒定 P-B 节流孔的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-B 恒定节流孔 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

P-B 节流孔的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Cv flow coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-B 节流孔最大 Cv 流量系数** — 对应于组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

P-B 节流孔完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Cv flow coefficient`
4. **Opening characteristic** 为 `Linear`
5. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流孔 Cv 流量系数向量** — 对应于构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Cv flow coefficient`
4. **Opening characteristic** 为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 恒定节流孔 Kv 流量系数** — 流量系数 `3.6`（默认）| 正标量

P-B 节流孔的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-B 节流孔最大 Kv 流量系数** — 对应于组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

P-B 节流孔完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient`
4. **Opening characteristic** 为 `Linear`
5. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流孔 Kv 流量系数向量** — 对应于构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient`
4. **Opening characteristic** 为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流孔阀芯行程向量** — 相对于全关位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Tabulated`。

### **P-B 最大节流孔面积** — 最大节流孔开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-B 节流孔的最大开度面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

同时将 **Area characteristics** 设置为 `每条流不同 path`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Linear`。

### **P-B 节流孔面积向量** — 阀开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格化参数化的开度面积向量。向量元素必须与 **P-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

同时将 **Area characteristics** 设置为 `每条流不同 path`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Tabulated`。

### **P-B 恒定节流孔面积** — 恒定节流孔横截面积 `1e-4 m^2`（默认）| 正标量

当正负阀芯位置包含相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下设置之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Tabulated`。

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **P-B 节流孔 xT 阻塞流压差比系数** — 压差比 `0.7`（默认）| 正标量

P-B 节流孔首次发生阻塞时入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中的至少一个：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### A-T 节流孔

### **Spool position at maximum A-T orifice area** — 完全打开 A-T 节流口时的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 A-T 节流口时阀芯从中位开始的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **Positive spool position open
  connections** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。

**Note:**

仅当 A-T 节流口设置未同时出现在 **Positive spool position open connections** 和
**Negative spool position open
connections** 参数中时，才启用此参数。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，以使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。

并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流不同 path`，
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel` 或 `Linear - Nominal
  mass flow rate vs. spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Linear`。

### **A-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开度 A-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开度 A-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 A-T 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

A-T 节流口在额定条件下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

A-T 节流口在额定运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为
   `Temperature`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| 范围 [0,1] 内的正标量

A-T 节流口在额定运行条件下的入口混合物蒸汽干度质量分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor
   quality`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal inlet vapor void fraction** — 入口蒸汽空泡率 `0`（默认）| 范围 [0,1] 内的正标量

A-T 节流口在额定运行条件下的入口混合物蒸汽空泡率。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor void
   fraction`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

A-T 节流口在额定运行条件下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   enthalpy`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

A-T 节流口在额定运行条件下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   internal energy`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T constant orifice nominal mass flow rate** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 A-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**Note:**

仅当 A-T 节流口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **A-T constant orifice nominal pressure drop** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过恒定 A-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**Note:**

仅当 A-T 节流口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **A-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

A-T 节流口的恒定 *Cv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**Note:**

仅当 A-T 节流口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **A-T orifice maximum Cv flow coefficient** — 对应组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

A-T 节流口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice Cv flow coefficient vector** — 成员位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **A-T orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

A-T 节流口的恒定 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**Note:**

仅当 A-T 节流口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **A-T orifice maximum Kv flow coefficient** — 对应组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

A-T 节流口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice Kv flow coefficient vector** — 成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` 中值的 *Kv* 系数（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **A-T orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-T orifice spool travel vector** 参数相同。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient`
4. **Opening characteristic** 为 `Tabulated`
5. 以下参数之一：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice spool travel vector** — 相对于全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Tabulated`。

### **A-T maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-T 节流口的最大开口面积。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

同时将 **Area characteristics** 设置为 `每条流不同 path`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Linear`。

### **A-T orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格化参数化的开口面积向量。向量元素必须与 **A-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

同时将 **Area characteristics** 设置为 `每条流不同 path`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Tabulated`。

### **A-T constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖

要启用此参数，请在每个参数中设置以下设置之一：

- **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Tabulated`。

**注意：**

仅当 A-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **A-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

A-T 节流口首次发生阻塞时，入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Vapor operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### B-T Orifice

### **Spool position at maximum B-T orifice area** — 全开 B-T 节流口的阀芯偏移 `5e-3 m`（默认）| 正标量

全开 B-T 节流口相对于中位位置的阀芯偏移。

#### 依赖

要启用此参数，请设置以下参数之一。

- **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流口设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Orifice parameterization** 为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Area characteristics** 为 `每条流不同 path`，且 **Opening characteristic** 为 `Linear`。

### **B-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开度 B-T 节流口的典型、额定或设计质量流量。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开度 B-T 节流口的典型、额定或设计压降。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 B-T 节流口入口流体状态的方法。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

B-T 节流口在额定条件下的入口压力。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

B-T 节流口在额定运行条件下的入口流体温度。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Temperature`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

B-T 节流口在额定运行条件下的入口混合物蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Vapor quality`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet vapor void fraction** — 入口蒸汽空泡率 `0`（默认）| [0,1] 范围内的正标量

B-T 节流口在额定运行条件下的入口混合物蒸汽空泡率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Vapor void fraction`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

B-T 节流口在额定运行条件下的入口比焓。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Specific enthalpy`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

B-T 节流口在额定运行条件下的入口比内能。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 为 `Specific internal energy`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T constant orifice nominal mass flow rate** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 B-T 节流口的典型、额定或设计质量流量。

#### 依赖

要启用此参数，请设置：

1. **Modeling option** 为 `Liquid operating condition`
2. **Area characteristics** 为 `每条流不同 path`
3. **Orifice parameterization** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在每个参数中设置以下之一：

   - **Positive spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - **Negative spool position open connections** 为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，此参数才启用。

### **B-T constant orifice nominal pressure drop** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过恒定 B-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流口设置在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中同时出现时，此参数才启用。

### **B-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

B-T 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流口设置在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中同时出现时，此参数才启用。

### **B-T orifice maximum Cv flow coefficient** — 对应最大开度的 *Cv* 系数 `4`（默认）| 正标量

B-T 节流口完全打开且可用流通面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice Cv flow coefficient vector** — 对应构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **B-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **B-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

B-T 节流口的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流口设置在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中同时出现时，此参数才启用。

### **B-T orifice maximum Kv flow coefficient** — 对应最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

B-T 节流口完全打开且可用流通面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice Kv flow coefficient vector** — 对应构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **B-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **B-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice spool travel vector** — 相对于全关位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流不同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **B-T maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 B-T 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

同时设置 **Area characteristics** 为
`每条流不同 path`，并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Linear`。

### **B-T orifice area vector** — 阀口开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的开口面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

同时设置 **Area characteristics** 为
`每条流不同 path`，并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **B-T constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流不同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel` 或 `Linear - Area vs.
  spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

**注意：**

仅当 B-T 节流口设置在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中同时出现时，此参数才启用。

### **B-T orifice xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

B-T 节流口首次发生阻塞流时的入口压力 *pin* 与出口压力 *pout* 之比，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流不同
   path`
3. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. 以下参数中至少一个：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

两相流体域中的四通两位方向阀

四通两位方向阀 (2P) 对两相流体网络中具有四个开口的阀进行建模——例如执行器、泵与油箱之间的阀。单个阀芯根据端口 **S** 处的信号控制阀的操作。您可以通过分别在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中指定阀芯向正方向和负方向移动时打开的节流口来设置阀的基线配置。您可以在 **Orifice parameterization** 参数中将阀开口模型设置为线性关系或用户提供数据的函数，并可将其应用于阀中的一个或所有流路。

此模块是一个复合组件，由多个 Orifice
(2P) 模块实例组成。有关阀参数化和模块计算的更多详细信息，请参阅 Orifice
(2P) 模块。在某些配置中，该阀类似于三通阀。要在阀芯处于中位时设置额外的流路，请参阅 4-Way 3-Position
Directional Valve (2P) 模块。

此图显示了一个阀设置示例，其中阀连接到油箱、执行器和泵，且 **Positive spool position open connections** 参数为 `P-B, A-T`：

此图显示了当 **Negative spool position open
connections** 参数为 `P-A, B-T` 时的阀：

在此配置中，当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径打开以允许流动。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径关闭以阻止流动。

此图显示了当 **Positive spool position open
connections** 参数为 `P-B, A-T` 时的阀：

在此配置中，当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径打开以允许流动，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭。

表示此配置的示意图为：

左侧对应正位置，右侧对应负位置。阀通过中位中间段过渡。

### 阀芯位移与阀配置

*阀芯行程*是指节流口从关闭位置到完全打开所需的阀芯移动量。您可以使用**节流口参数化**和**面积特性**参数来指定流路特性：

| 节流口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | **Spool travel between closed and open orifice** 参数定义阀芯行程 | **Spool travel between closed and open orifice** 参数定义每条节流口的阀芯行程 |
| `Tabulated data - Area vs. spool travel` | **Spool travel vector** 参数第一个和最后一个元素之间的差值定义阀芯行程 | 每条节流口的 **Spool travel vector** 参数第一个和最后一个元素之间的差值定义阀芯行程 |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **Spool travel vector, ds** 参数第一个和最后一个元素之间的差值定义阀芯行程 | 每条节流口的 **Spool travel vector, ds** 参数第一个和最后一个元素之间的差值定义阀芯行程 |

阀芯移动方向取决于阀芯行程、节流口方向和端口 **S** 处的信号。下表显示了节流口的阀芯行程如何取决于 **Positive spool position open connection** 和 **Negative spool position open connection** 参数的选择：

| 节流口打开时的阀芯位置 | 阀芯行程，*ΔS* |
| --- | --- |
| 节流口始终关闭：节流口未在 **Positive spool position open connection** 或 **Negative spool position open connection** 参数中选择 | 不适用 |
| 节流口始终打开：节流口同时在 **Positive spool position open connection** 和 **Negative spool position open connection** 参数中选择 | 不适用 |
| 负：节流口仅在 **Negative spool position open connection** 参数中选择 | *S*orifice\_max + 阀芯行程 – **S** |
| 正：节流口仅在 **Positive spool position open connection** 参数中选择 | *S*orifice\_max – 阀芯行程 + **S** |

其中 *S*orifice\_max 是每条节流口定义的最大节流口面积处的阀芯位置。当 *ΔS* 为负时，节流口面积饱和于泄漏面积；当节流口完全打开时，节流口面积饱和于最大节流口面积。当节流口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程不会进一步增加节流口面积。

下表显示了 4-Way 2-Position Directional Valve (TL) 的可能配置：

| 配置 | 参数值 |
| --- | --- |
| 过渡期间所有四条流路均关闭。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < –P-B 阀芯行程 - **Spool position at maximum A-T orifice area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice area** > B-T 阀芯行程 |
| 过渡期间所有四条流路均打开。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > –A-T 阀芯行程 - **Spool position at maximum B-T orifice area** < B-T 阀芯行程 |
| 过渡期间 A-T 和 B-T 关闭。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice area** > B-T 阀芯行程 |
| 过渡期间 P-A 和 P-B 关闭。 | - **Positive spool position open connections**：`P-A` - **Negative spool position open connections**：`P-B` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < –P-B 阀芯行程 |
| 过渡期间 P-B 和 B-T 关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice area** < –B-T 阀芯行程 |
| 过渡期间 P-A 和 A-T 关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice area** > –B-T 阀芯行程 |
| 过渡期间 P-A、P-B 和 B-T 打开。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 阀芯行程 |
| 过渡期间 P-A、A-T 和 B-T 打开。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** > –P-A 阀芯行程 - **Spool position at maximum A-T orifice area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice area** = 任意值 |
| 过渡期间 P-A 和 P-B 关闭。A-T 始终关闭。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum B-T orifice area** < –B-T 阀芯行程 |
| 过渡期间所有流路均关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > A-T 阀芯行程 |
| 过渡期间 A-T 打开。过渡期间 P-A 关闭。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-A, B-T` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 阀芯行程 |
| 过渡期间 B-T 打开。过渡期间 P-B 关闭。 | - **Positive spool position open connections**：`P-B, A-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice area** = 任意值 |
| 过渡期间 P-A 关闭。 | - **Positive spool position open connections**：`P-A, B-T` - **Negative spool position open connections**：`P-A, P-B` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** < –P-B 阀芯行程 - **Spool position at maximum B-T orifice area** > B-T 阀芯行程 |
| 过渡期间 P-B 关闭。 | - **Positive spool position open connections**：`P-A, P-B` - **Negative spool position open connections**：`P-B, A-T` - **Spool position at maximum P-A orifice area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice area** > –A-T 阀芯行程 |

### 阀节流口参数化

**Modeling option** 参数控制为建模蒸汽或液体而设计的阀的参数化选项，但不影响流体属性。该模块根据入口条件计算阀内流体属性。

**Orifice parameterization** 参数指定一个或所有阀节流口的打开面积或流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，则该模块对所有流路应用相同的数据。当您选择 `Different for all flow paths` 时，该模块对每条流路使用单独的参数化。

**液体阀参数化**

当 **Modeling option** 为 `Liquid operating condition` 时，模块参数化设计用于控制液体流量的阀。

当 **Orifice parameterization** 为 `Linear - Area vs. spool travel` 时，打开面积是端口 **S** 处接收的阀芯位置信号的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

其中：

- *ΔS* 是阀芯行程。

  *Aorifice* 在 *ΔS* 为负时饱和于 *Aleak*，在节流口完全打开时饱和于 *Amax*。当节流口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程的值不会增加节流口面积。
- *ΔSmax* 是 **Spool travel between closed and open orifice** 参数的值。
- *Amax* 是 **Maximum orifice area** 参数的值。
- *Aleak* 是 **Leakage area** 参数的值。

  当阀在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，则该模块在 *Aleak* 和 *Amax* 之间平滑地饱和打开面积。有关详细信息，请参阅数值平滑。

当 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 时，您可以为系统或端口 **P**、**A**、**B** 和 **T** 之间的各条流路提供阀芯行程向量。该模块使用此数据计算节流口面积与阀芯位移之间的关系。该模块使用插值确定给定数据点之间的打开面积。*A*leak 和 *A*max 分别是打开面积向量的第一个和最后一个参数。

当 **Orifice parameterization** 为 `Tabulated data - Nominal mass flow rate vs. spool travel` 时，该模块根据您在模块参数中指定的标称条件计算每条节流口的质量流量。来自端口 **S** 的阀芯位置信号缩放节流口打开面积，这也可以缩放质量流量。

**蒸汽阀参数化**

当 **Modeling option** 为 `Vapor operating condition` 时，模块参数化设计用于建模控制蒸汽流量的阀。

该模块用于控制每条节流口的方法取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量取决于端口 **S** 处的阀芯位置。当阀芯位移以打开节流口时，流量能力的度量从指定的最小值缩放到指定的最大值。
- `Tabulated` — 该模块将流量能力的度量计算为端口 **S** 处阀芯位置的函数。此函数使用一维查找表。

**Orifice parameterization** 参数确定该模块如何计算每条节流口中的流量：

- `Cv flow coefficient` — 流量系数 *C*v 缩放每条节流口中的流量。流量系数衡量流体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，缩放每条节流口中的流量。流量系数衡量流体在特定压差驱动下流动的难易程度。
- `Orifice area` — 节流口面积的大小缩放每条节流口中的流量。

### 可视化节流口开度

要可视化阀芯偏移和最大位移，请右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示由 **Valve Configuration** 部分中的参数指定的节流口。当您将 **Valve Configuration** 选项卡中的参数设置为同一条节流口时，节流口开度为常数。

单击 **Reload Data** 以更新图中的数据。

此图显示了该模块的默认配置：

- **Positive spool position open connections** 为 `P-A, B-T`
- **Negative spool position open connections** 为 `P-B, A-T`

所有其他阀芯位置均为默认值。

### 假设与限制

- 阀与环境之间没有热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，结果在过冷液体区域之外可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，结果在过热蒸汽区域之外可能不准确。要对液-汽混合物中的阀进行建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
