---
type: simulink-block
title: 'Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'transmissionline'
documentation_source_path: 'ref/transmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Transmission Line

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Model type
  summary: 传输线模型 Delay-based and lossless（默认）| Delay-based and lossy | Lumped parameter L-section | Lumped parameter Pi-section
    | Coaxial | Coplanar waveguide | Microstrip | Stripline | Two-wire | Parallel-plate | Equation-based | RLCG | ...
  group: 主要
- name: Transmission delay
  summary: 传输线中的延迟 4.7e-9 s（默认）| 实数标量 | s | ms | us | ns
  group: 主要
- name: Characteristic impedance
  summary: 传输线的阻抗 50 ohm（默认）| 实数标量 | Ohm | kOhm | MOhm | GOhm
  group: 主要
- name: Resistance per unit length
  summary: 传输线单位长度的电阻 0.3 Ohm/m（默认）| 正标量 | Ohm/m | kOhm/m | MOhm/m | GOhm/m
  group: 主要
- name: Number of segments
  summary: 传输线中的段数 10（默认）| 正标量
  group: 主要
- name: Parameterization
  summary: 用于对传输线中的段进行建模的参数类型 By characterisitc impedance and capacitance（默认）| By inductance and capacitance
  group: 主要
- name: Capacitance per unit length
  summary: 传输线单位长度的电容 94e-12 F/m（默认）| 正标量
  group: 主要
- name: Conductance per unit length
  summary: 传输线单位长度的电导 5e-6 S/m（默认）| 正标量 | S/m | mS/m | uS/m | nS/m
  group: 主要
- name: Inductance per unit length
  summary: 传输线单位长度的电感 235e-9 H/m（默认）| 正标量 | H/m | mH/m | uH/m | nH/m
  group: 主要
- name: Outer radius
  summary: 同轴传输线的外半径 2.57 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Inner radius
  summary: 同轴传输线的内半径 2.57 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Conductor width
  summary: 导体的物理宽度 0.6 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Slot width
  summary: 槽的物理宽度 0.2 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Conductor backed
  summary: 无限底部导体 off（默认）| on
  group: 主要
- name: Structure
  summary: 微带传输线的类型 Standard（默认）| Embedded | Inverted | Suspended
  group: 主要
- name: Strip Width
  summary: 微带传输线的宽度 0.6 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Strip thickness
  summary: 导体的物理厚度 5 um（默认）| 非负标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Strip Height
  summary: 微带传输线的带条高度 0.635 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Wire radius
  summary: 双线传输线导线的半径 0.67 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Wire separation
  summary: 双线传输线导线之间的物理距离 1.62 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Plate width
  summary: 平行板传输线的宽度 5 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Plate separation
  summary: 分隔极板的电介质厚度 1 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Phase velocity (m/s)
  summary: 均匀平面波在传输线上的传播速度 299792458（默认）| 正标量
  group: 主要
- name: Loss (dB/m)
  summary: 信号在传输线上传播时的强度衰减 0（默认）| 正标量
  group: 主要
- name: Frequency
  summary: 建模频率 1e9 Hz（默认）| 正标量 | Hz | kHz | MHz | GHz
  group: 主要
- name: Interpolation method
  summary: 用于计算建模频率处值的插值方法 Linear（默认）| Spline | Cubic
  group: 主要
- name: Conductivity of conductor
  summary: 导体的电导率 inf（默认）| 标量 | S/m | mS/m | uS/m | nS/m
  group: 主要
- name: Dielectric Thickness
  summary: 导体所在电介质的厚度 0.635 mm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: Relative permeability of dielectric
  summary: 电介质的相对磁导率 1（默认）| 标量
  group: 主要
- name: Relative permittivity of dielectric
  summary: 电介质的相对介电常数 2.2（默认）| 标量
  group: 主要
- name: Loss tangent of dielectric
  summary: 电介质的损耗角正切 0（默认）| 标量
  group: 主要
- name: 线长
  summary: 传输线的物理长度 1 cm（默认）| 正标量 | m | cm | mm | um | in | ft
  group: 主要
- name: 短截线模式
  summary: 短截线的类型 Not a stub（默认）| Shunt | Series
  group: 主要
- name: 短截线终端
  summary: 短截线的终端类型 Open（默认）| Short
  group: 主要
- name: 接地并隐藏负端子
  summary: 将 RF 电路端子接地 on（默认）| off
  group: 主要
- name: 建模选项
  summary: 用于对 S 参数建模的选项 Frequency domain（默认）| Time domain
  group: 建模
- name: 自动估计冲激响应持续时间
  summary: 自动计算冲激响应持续时间 off（默认）| on
  group: 建模
- name: 冲激响应持续时间
  summary: 手动指定冲激响应持续时间 0 s（默认）| 正标量 | s | ms | us | ns
  group: 建模
- name: 拟合选项
  summary: rationalfit 的拟合选项 Share all poles（默认）| Share poles by columns | Fit individually
  group: 建模
- name: Relative error desired (dB)
  summary: 有理拟合输出中可接受的相对误差 -40（默认）| 实数标量
  group: 建模
- name: Rational fitting results
  summary: rationalfit 计算的值 只读（默认）
  group: 建模
```

### 主要

### **Model type** — 传输线模型 `Delay-based and lossless`（默认）| `Delay-based and lossy` | `Lumped parameter L-section` | `Lumped parameter Pi-section` | `Coaxial` | `Coplanar waveguide` | `Microstrip` | `Stripline` | `Two-wire` | `Parallel-plate` | `Equation-based` | `RLCG` | ...

传输线模型的类型，指定为以下之一。

| 传输线类型 | 描述 |
| --- | --- |
| `Delay-based and lossless` | 对具有延迟但无损耗的传输线进行建模。基于延迟的传输线 |
| `Delay-based and lossy` – | 对具有延迟和损耗的传输线进行建模。基于延迟的有损传输线 |
| `Lumped parameter L-section` | 对具有 RLGC L 型节的传输线进行建模。R、L、G、C 按 L 型节连接。 |
| `Lumped parameter Pi-section` | 对具有 RLGC Pi 型节的传输线进行建模。R、L、G、C 按 Pi 型节连接。 |
| `Coaxial` | 将传输线建模为同轴传输线。同轴传输线的横截面如下图所示。其物理特性包括内导体半径 *a* 和外导体半径 *b*。同轴传输线层：内导体、介质、外导体 |
| `Coplanar waveguide` | 将传输线建模为共面波导。共面波导传输线的横截面如下图所示。其物理特性包括导体宽度 *w*、导体厚度 *t*、槽宽度 *s*、基板高度 *d* 和相对介电常数 *ε*。带导体背板接地平面和不带导体背板接地平面的共面波导横截面 |
| `Microstrip` | 将传输线建模为标准、嵌入式、倒置或悬浮微带传输线。标准、嵌入式、倒置和悬浮微带传输线的横截面如下所示。此类传输线的物理特性包括微带宽度 *w*、微带厚度 *t*、介质厚度 *d* 和相对介电常数 *ε*。标准、嵌入式、倒置和悬浮微带传输线的横截面 |
| `Stripline` | 将传输线建模为带状线传输线。带状线传输线的横截面如下图所示。其物理特性包括带状线宽度 *w*、带状线厚度 *t*、介质厚度 *h* 和相对介电常数 *ε*。带状线传输线 |
| `Two-wire` | 将传输线建模为双线传输线。双线传输线的横截面如下图所示。其物理特性包括导线半径 *a*、导线中心之间的间距或物理距离 *S*，以及导线的相对介电常数和相对磁导率。双线传输线的横截面 |
| `Parallel plate` | 将传输线建模为平行板传输线。平行板传输线的横截面如下图所示。其物理特性包括板宽度 *w* 和板间距 *d*。平行板传输线的横截面 |
| `Equation based` | 将传输线建模为基于方程的传输线。该传输线可以是有损或无损耗的，被视为二端口线性网络。基于方程的传输线 |
| `RLCG` | 将传输线建模为 RLCG 传输线。该线路根据其随频率变化的电阻、电感、电容和电导来定义。该传输线可以是有损或无损耗的，被视为二端口线性网络。RLGC 传输线的横截面 |

### **Transmission delay** — 传输线中的延迟 `4.7e-9 s`（默认）| 实数标量 | `s` | `ms` | `us` | `ns`

传输线中的延迟，指定为以 `s`、`ms`、`us` 或 `ns` 为单位的实数标量。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- **Model type** 中的 `Delay-based and lossless`。
- **Model type** 中的 `Delay-based and lossy`。

### **Characteristic impedance** — 传输线的阻抗 `50 ohm`（默认）| 实数标量 | `Ohm` | `kOhm` | `MOhm` | `GOhm`

传输线的阻抗，指定为以 `Ohm`、`kOhm`、`MOhm` 或 `GOhm` 为单位的实数标量。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- **Model type** 中的 `Delay-based and lossless`、`Delay-based and lossy` 或 `Equation-based`。
- **Model type** 中的 `Lumped parameter L-section` 或 `Lumped parameter Pi-section`，以及 **Parameterization** 中的 `By characterisitc impedance and capacitance`。

### **Resistance per unit length** — 传输线单位长度的电阻 `0.3 Ohm/m`（默认）| 正标量 | `Ohm/m` | `kOhm/m` | `MOhm/m` | `GOhm/m`

传输线单位长度的电阻，指定为以 `Ohm/m`、`kOhm/m`、`MOhm/m` 或 `GOhm/m` 为单位的正标量。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- **Model type** 中的 `Delay-based and lossy` 或 `RLCG`。
- **Model type** 中的 `Lumped parameter L-section` 或 `Lumped parameter Pi-section`，以及 **Parameterization** 中的 `By characterisitc impedance and capacitance`。

### **Number of segments** — 传输线中的段数 `10`（默认）| 正标量

传输线中的段数，指定为正标量。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- **Model type** 中的 `Delay-based and lossy`。
- **Model type** 中的 `Lumped parameter L-section` 或 `Lumped parameter Pi-section`，以及 **Parameterization** 中的 `By characterisitc impedance and capacitance` 或 `By inductance and capacitance`。

### **Parameterization** — 用于对传输线中的段进行建模的参数类型 `By characterisitc impedance and capacitance`（默认）| `By inductance and capacitance`

用于对传输线中的段进行建模的参数类型，指定为 `By characterisitc impedance and capacitance` 或 `By inductance and capacitance`。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Lumped parameter L-section` 或 `Lumped parameter Pi-section`。

### **Capacitance per unit length** — 传输线单位长度的电容 `94e-12 F/m`（默认）| 正标量

传输线单位长度的电容，指定为以 `F/m`、`mF/m`、`uF/m`、`nF/m` 或 `pF/m` 为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Lumped parameter L-section`、`Lumped parameter Pi-section` 或 `RLCG`。

### **Conductance per unit length** — 传输线单位长度的电导 `5e-6 S/m`（默认）| 正标量 | `S/m` | `mS/m` | `uS/m` | `nS/m`

传输线单位长度的电导，指定为以 `S/m`、`mS/m`、`uS/m` 或 `nS/m` 为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Lumped parameter L-section`、`Lumped parameter Pi-section` 或 `RLCG`。

### **Inductance per unit length** — 传输线单位长度的电感 `235e-9 H/m`（默认）| 正标量 | `H/m` | `mH/m` | `uH/m` | `nH/m`

传输线单位长度的电感，指定为以 `H/m`、`mH/m`、`uH/m` 或 `nH/m` 为单位的正标量。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- **Model type** 中的 `Lumped parameter L-section` 或 `Lumped parameter Pi-section`，以及 **Parameterization** 中的 `By inductance and capacitance`。
- **Model type** 中的 `RLCG`

### **Outer radius** — 同轴传输线的外半径 `2.57 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

同轴传输线的外半径，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Coaxial`。

### **Inner radius** — 同轴传输线的内半径 `2.57 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

同轴传输线的内半径，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Coaxial`。

### **Conductor width** — 导体的物理宽度 `0.6 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

导体的物理宽度，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Coplanar waveguide`。

### **Slot width** — 槽的物理宽度 `0.2 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

槽的物理宽度，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Coplanar waveguide`。

### **Conductor backed** — 无限底部导体 `off`（默认）| `on`

选择此参数可为共面波导传输线添加无限底部导体。

#### 依赖

要启用此参数，请将 **Model type** 设置为 `Coplanar waveguide`。

### **Structure** — 微带传输线的类型 `Standard`（默认）| `Embedded` | `Inverted` | `Suspended`

微带传输线的类型，指定为 Standard、Embedded、Inverted 或 Suspended。

#### 依赖

要启用此参数，请将 **Model type** 设置为 `Microstrip`。

### **Strip Width** — 微带传输线的宽度 `0.6 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

微带传输线的宽度，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请将 **Model type** 设置为 `Microstrip`。

### **Strip thickness** — 导体的物理厚度 `5 um`（默认）| 非负标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

导体的物理厚度，指定为非负标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Coplanar waveguide` 或 `Microstrip`。

### **Strip Height** — 微带传输线的带条高度 `0.635 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

倒置、悬浮或嵌入式微带传输线的带条高度，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Microstrip`，并在 **Structure** 中选择 `Inverted`、`Suspended` 或 `Embedded`。

### **Wire radius** — 双线传输线导线的半径 `0.67 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

双线传输线导线的半径，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Two-wire`。

### **Wire separation** — 双线传输线导线之间的物理距离 `1.62 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

双线传输线导线之间的物理距离，指定为正标量，单位为 `m`、`cm`、`mm`、`um`、`in` 或 `ft`。

#### 依赖

要启用此参数，请在 **Model type** 中选择 `Two-wire`。

### **Plate width** — 平行板传输线的宽度 `5 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

平行板传输线的宽度，指定为以 `m`、`cm`、`mm`、`um`、`in` 或 `ft` 为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Parallel-plate`。

### **Plate separation** — 分隔极板的电介质厚度 `1 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

分隔极板的电介质厚度，指定为以 `m`、`cm`、`mm`、`um`、`in` 或 `ft` 为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Parallel-plate`。

### **Phase velocity (m/s)** — 均匀平面波在传输线上的传播速度 `299792458`（默认）| 正标量

均匀平面波在传输线上的传播速度，指定为以米每秒为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Equation-based`。

### **Loss (dB/m)** — 信号在传输线上传播时的强度衰减 `0`（默认）| 正标量

信号在传输线上传播时的强度衰减，指定为以米每秒为单位的正标量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Equation-based`。

### **Frequency** — 建模频率 `1e9 Hz`（默认）| 正标量 | `Hz` | `kHz` | `MHz` | `GHz`

建模频率，指定为以 `Hz`、`kHz`、`MHz` 或 `GHz` 为单位的正标量或向量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Equation-based` 或 `RLCG`。

### **Interpolation method** — 用于计算建模频率处值的插值方法 `Linear`（默认）| `Spline` | `Cubic`

用于计算建模频率处值的插值方法，指定为 `Linear`、`Spline` 或 `Cubic`。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Equation-based` 或 `RLCG`。

### **Conductivity of conductor** — 导体的电导率 `inf`（默认）| 标量 | `S/m` | `mS/m` | `uS/m` | `nS/m`

导体的电导率，指定为以 `S/m`、`mS/m`、`uS/m` 或 `nS/m` 为单位的标量。

#### 依赖关系

要启用此参数，请在 **Model type** 中选择 `Coaxial`、`Coplanar waveguide`、`Microstrip`、`Two-wire` 或 `Parallel-plate`。

### **Dielectric Thickness** — 导体所在电介质的厚度 `0.635 mm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

导体所在电介质的厚度，指定为以 `m`、`cm`、`mm`、`um`、`in` 或 `ft` 为单位的正标量。

共面波导以及标准、嵌入式、倒置和悬置微带传输线的电介质厚度默认值列于下表中。

| 模型类型 | 结构 | 默认电介质厚度（mm） |
| --- | --- | --- |
| `Coplanar waveguide` | 不适用 | `0.635` |
| `Microstrip` | `Standard` 和 `Inverted` | `0.635` |
| `'Suspended'` | `0.3175` |
| `'Embedded'` | `1.37` |

#### 依赖关系

要启用此参数，请将 **Model type** 设置为 `Microstrip` 或 `Coplanar waveguide`。

### **Relative permeability of dielectric** — 电介质的相对磁导率 `1`（默认）| 标量

电介质的相对磁导率，指定为标量。

#### 依赖关系

要启用此参数，请将 **Model type** 设置为 `Coaxial`、`Two-wire` 或 `Parallel-plate`。

### **Relative permittivity of dielectric** — 电介质的相对介电常数 `2.2`（默认）| 标量

电介质的相对介电常数，指定为标量。

#### 依赖关系

要启用此参数，请将 **Model type** 设置为 `Coaxial`、`Coplanar waveguide`、`Microstrip`、`Two-wire` 或 `Parallel-plate`。

### **Loss tangent of dielectric** — 电介质的损耗角正切 `0`（默认）| 标量

电介质的损耗角正切，指定为标量。

#### 依赖关系

要启用此参数，请将 **模型类型** 设置为
`Coaxial`、`Coplanar
waveguide`、`Microstrip`、
`Two-wire` 或
`Parallel-plate`。

### **线长** — 传输线的物理长度 `1 cm`（默认）| 正标量 | `m` | `cm` | `mm` | `um` | `in` | `ft`

传输线的物理长度或 *l*，
指定为正标量，单位为 `m`、
`cm`、`mm`、
`um`、`in` 或
`ft`。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- **模型类型** 中的 `Delay-based and lossy`、
  `Coaxial`、
  `Coplanar waveguide`、
  `Microstrip` 或
  `Two-wire`、
  `Parallel-plate`、
  `Equation-based` 或
  `RLCG`。
- **模型类型** 中的 `Lumped parameter L-section`
  或 `Lumped parameter
  Pi-section`，以及
  **参数化** 中的 `By characterisitc
  impedance and capacitance` 或 `By
  inductance and capacitance`。

### **短截线模式** — 短截线的类型 `Not a stub`（默认）| `Shunt` | `Series`

短截线的类型，指定为 `Not a stub`、
`Shunt` 或
`Series`。请参阅带短截线的传输线的参数计算。

#### 依赖关系

要启用此参数，请在 **模型类型** 中选择
`Coaxial`、`Coplanar
waveguide`、`Microstrip`
`Two-wire`、
`Parallel-plate`、
`Equation-based` 或
`RLCG`。

### **短截线终端** — 短截线的终端类型 `Open`（默认）| `Short`

短截线的终端类型，指定为
`Open` 或
`Short`。

#### 依赖关系

要启用此参数，请在 **短截线模式** 中选择 `Series`
或 `Shunt`。

### **接地并隐藏负端子** — 将 RF 电路端子接地 `on`（默认）| `off`

选择此参数可将负端子内部接地并隐藏。要暴露负端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。

### 建模

### **建模选项** — 用于对 S 参数建模的选项 `Frequency domain`（默认）| `Time domain`

用于对 S 参数建模的选项，指定为：

- `Frequency domain` – 独立计算每个载波频率的基带
  冲激响应。此技术基于卷积。可以选择指定冲激响应的
  持续时间。有关详细信息，请参阅 S 参数的时域和频域仿真选项比较。
- `Time domain` – 计算近似整个数据范围的解析有理
  模型。

对于 Amplifier、Antenna 和 S-Parameters 模块，默认
值为 `Time domain`。对于 Transmission
Line 模块，默认值为 `Frequency
domain`。

### **自动估计冲激响应持续时间** — 自动计算冲激响应持续时间 `off`（默认）| `on`

选择 **自动估计冲激响应持续时间** 以
自动计算冲激响应持续时间。清除该选择以指定
冲激响应持续时间。

#### 依赖关系

要启用此参数，请在
**建模选项** 中选择 `Frequency domain`。

### **冲激响应持续时间** — 手动指定冲激响应持续时间 `0 s`（默认）| 正标量 | `s` | `ms` | `us` | `ns`

手动指定冲激响应持续时间，指定为正标量，单位为
`s`、`ms`、
`us` 或 `ns`。

#### 依赖关系

要启用此参数，请清除 **自动估计冲激响应
持续时间**。

### **拟合选项** — rationalfit 的拟合选项 `Share all poles`（默认）| `Share poles by columns` | `Fit individually`

rationalfit 的拟合选项，指定为 `Share all
poles`、`Share poles by columns` 或
`Fit individually`。

对于 Amplifier 模块，默认值为 `Fit
individually`。对于 S-parameters 模块和
Transmission Line 模块，默认值为 `Share all
poles`。

#### 依赖关系

要启用此参数，请在
**建模选项** 中选择 `Time domain`。

### **Relative error desired (dB)** — 有理拟合输出中可接受的相对误差 `-40`（默认）| 实数标量

有理拟合输出中可接受的相对误差，指定为以分贝为单位的实数标量。

#### 依赖关系

要启用此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Rational fitting results** — rationalfit 计算的值 只读（默认）

显示 **Number of independent fits**、**Number of required poles** 和 **Relative error achieved (dB)** 的值。

使用 `Time domain` 建模时，`Visualization` 选项卡中的 **Plot** 会绘制 `Data Source` 中定义的数据以及 `rationalfit` 函数中的值。

#### 依赖关系

要启用此参数，请在 **Modeling options** 中选择 `Time domain`。

**Note**

Modeling 选项卡对所有传输线类型均启用，但 `Delay-based and lossless`、`Delay-based and lossy`、`Lumped parameter L-section` 和 `Lumped parameter pi-section` 除外。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

### R2024b: `Time domain (rationalfit)` 参数已重命名

Transmission Line 模块中 **Modeling options** 参数的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当您打开在 R2024b 之前创建的包含 Transmission Line 模块的模型时，参数名称显示为 `Time domain`。

### R2022a: 三个模块参数已重命名

Transmission Line 模块中的 **Substrate height**、**Relative permittivity constant** 和 **Relative permeability constant** 参数已分别重命名为 **Dielectric thickness**、**Relative permittivity of dielectric** 和 **Relative permeability of dielectric**。

当您打开在 R2022a 之前创建的包含 Transmission Line 模块的模型时，软件会将旧参数名称替换为新名称。

### R2022a: 对传输线建模

使用 Transmission Line 模块对以下对象建模：

- 嵌入式、倒置和悬置微带传输线
- 导体背衬共面波导传输线
- 带状线传输线

## 描述

对传输线建模

使用 Transmission Line 模块对基于延迟的、集总和分布式的传输线进行建模。Mask 对话框选项会自动更改，以适应模型类型选择。
