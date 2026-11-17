---
type: simulink-block
title: 'N-Channel IGBT'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'nchanneligbt'
documentation_source_path: 'ref/nchanneligbt.html'
language: zh-CN
chinese_source: worker-translation
---

# N-Channel IGBT

## 端口

### 守恒

### **C** — 集电极电气端子

与 PNP 发射极端子关联的电气守恒端口。

### **G** — 栅极电气端子

与 IGBT 栅极端子关联的电气守恒端口。

### **E** — 发射极电气端子

与 PNP 集电极端子关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Full I-V and capacitance characteristics | Show thermal port` 或 `Simplified I-V characteristics and event-based timing | Show thermal port`。

## 参数

### **建模选项** — IGBT 表示 `Full I-V and capacitance characteristics | No thermal port`（默认） | `Full I-V and capacitance characteristics | Show thermal port` | `Simplified I-V characteristics and event-based timing | No thermal port` | `Simplified I-V characteristics and event-based timing | Show thermal port`

选择 IGBT 表示：

- `Full I-V and capacitance characteristics | No thermal port` — 详细模型，不模拟生成热量和设备温度的影响。这是默认值。
- `Full I-V and capacitance characteristics | Show thermal port` — 带暴露热端口的详细模型。
- `Simplified I-V characteristics and event-based timing | No thermal port` — 简化的基于事件的模型，也不模拟生成热量和设备温度的影响。
- `Simplified I-V characteristics and event-based timing | Show thermal port` — 带暴露热端口的简化基于事件的模型。

### Main（完整 I-V 和电容特性）

**Main** 设置的此配置对应于详细模块建模选项，这是默认值。如果您使用的是该模块的简化、基于事件的建模选项，请参见 Main（简化 I-V 特性和基于事件的时序）。

### **I-V 特性定义方式** — IGBT 表示 `Fundamental nonlinear equations`（默认） | `Lookup table (2D, temperature independent)` | `Lookup table (3D, temperature dependent)`

选择 IGBT 表示：

- `Fundamental nonlinear equations` — 使用基于 PNP 双极晶体管和 N 沟道 MOSFET 的等效电路。这是默认值。
- `Lookup table (2D, temperature independent)` — 使用二维查表，将集电极电流表示为栅极-发射极电压和集电极-发射极电压的函数。
- `Lookup table (3D, temperature dependent)` — 使用三维查表，将集电极电流表示为栅极-发射极电压、集电极-发射极电压和温度的函数。

### **零栅极电压集电极电流，Ices** — 零栅极电压集电极电流 `2` `mA`（默认）

当栅极-发射极电压设置为零，并施加较大的集电极-发射极电压时流过的集电极电流，即器件处于关断状态。该较大集电极-发射极电压的值由参数 **定义 Ices 时的电压** 定义。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear equations`。

### **定义 Ices 时的电压** — 定义 Ices 时的电压 `600` `V`（默认）

测量 **零栅极电压集电极电流，Ices** 时使用的电压。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear equations`。

### **栅极-发射极阈值电压，Vge(th)** — 栅极-发射极阈值电压 `6` `V`（默认）

MOSFET 方程中使用的阈值电压。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear equations`。

### **集电极-发射极饱和电压，Vce(sat)** — 集电极-发射极饱和电压 `2.6` `V`（默认）

制造商规定的典型导通状态下的集电极-发射极电压。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear equations`。

### **定义 Vce(sat) 时的集电极电流** — 定义 Vce(sat) 时的集电极电流 `400` `A`（默认）

当栅极-发射极电压为 *V*ge(sat) 且集电极-发射极电压为 *V*ce(sat) 时的集电极-发射极电流。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear equations`。

### **定义 Vce(sat) 时的栅极-发射极电压** — 定义 Vce(sat) 时的栅极-发射极电压 `10` `V`（默认）

测量 *V*ce(sat) 和 *I*ce(sat) 时使用的栅极电压。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear equations`。

### **测量温度** — 测量温度 `25` `degC`（默认）

参数所对应的温度（*T*m1）。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear equations`。

### **栅极-发射极电压向量，Vge** — 栅极-发射极电压向量 `[-1 0 0.5 1 1.5 2 2.5 3 3.5 4]` `V`（默认）

用于查表的栅极-发射极电压向量。向量值必须严格递增。这些值可以是非均匀间隔的。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Lookup table (2D, temperature independent)` 或 `Lookup table (3D, temperature dependent)`。

### **集电极-发射极电压向量，Vce** — 集电极-发射极电压向量 `[-2 6 7 8 10 12 15 20]` `V`（默认）

用于查表的集电极-发射极电压向量。向量值必须严格递增。这些值可以是非均匀间隔的。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Lookup table (2D, temperature independent)` 或 `Lookup table (3D, temperature dependent)`。

### **表格化集电极电流，Ic(Vge,Vce)** — 温度无关的表格化集电极电流 `[-1.015e-05, 1.35e-08, .00047135, .0005092, .0005105, .00051175, .00051299, .00051423, .00051548, .00051672; -9.9869e-06, 1.35e-08, .00047135, .0005092, .0005105, .00051175, .00051299, .00051423, .00051548, .00051672; -9.955e-06, 1.35e-08, .0065225, 3.3324, 48.154, 93.661, 105.52, 105.72, 105.93, 106.14; -9.955e-06, 1.35e-08, .0065235, 3.5783, 70.264, 166.33, 252.4, 317.67, 353.38, 357.39; -9.955e-06, 1.35e-08, .006524, 3.7206, 89.171, 228.09, 371.63, 511.02, 642.69, 764.04; -9.9549e-06, 1.35e-08, .0065242, 3.7716, 97.793, 256.21, 424.27, 592.92, 759.2, 921.52; -9.9549e-06, 1.35e-08, .0065243, 3.8067, 104.52, 278.11, 464.6, 654.37, 844.57, 1033.9; -9.9549e-06, 1.35e-08, .0065244, 3.8324, 109.92, 295.67, 496.54, 702.28, 909.96, 1118.3]` `A`（默认）

用于二维查表的集电极电流表格值，作为栅极-发射极电压和集电极-发射极电压的函数。矩阵中的每个值指定了特定栅极-发射极电压和集电极-发射极电压组合下的集电极电流。矩阵大小必须与栅极-发射极电压和集电极-发射极电压向量定义的维度匹配。默认值（单位为 A）为：

    [-1.015e-5 1.35e-8 4.7135e-4 5.092e-4 5.105e-4 5.1175e-4 5.1299e-4 5.1423e-4 5.1548e-4 5.1672e-4;
     -9.9869e-6 1.35e-8 4.7135e-4 5.092e-4 5.105e-4 5.1175e-4 5.1299e-4 5.1423e-4 5.1548e-4 5.1672e-4;
     -9.955e-6 1.35e-8 0.0065225 3.3324 48.154 93.661 105.52 105.72 105.93 106.14;
     -9.955e-6 1.35e-8 0.0065235 3.5783 70.264 166.33 252.4 317.67 353.38 357.39;
     -9.955e-6 1.35e-8 0.006524 3.7206 89.171 228.09 371.63 511.02 642.69 764.04;
     -9.9549e-6 1.35e-8 0.0065242 3.7716 97.793 256.21 424.27 592.92 759.2 921.52;
     -9.9549e-6 1.35e-8 0.0065243 3.8067 104.52 278.11 464.6 654.37 844.57 1.0339e+3;
     -9.9549e-6 1.35e-8 0.0065244 3.8324 109.92 295.67 496.54 702.28 909.96 1.1183e+3]

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Lookup table (2D, temperature independent)`。

### **温度向量，T** — 温度向量 `[25 125]` `degC`（默认）

用于查表的温度向量。向量值必须严格递增。这些值可以是非均匀间隔的。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Lookup table (3D, temperature dependent)`。

### **表格化集电极电流，Ic(Vge,Vce,T)** — 温度相关的表格化集电极电流 `zeros(8, 10, 2)` `A`（默认）

用于三维查表的集电极电流表格值，作为栅极-发射极电压、集电极-发射极电压和温度的函数。矩阵中的每个值指定了特定温度下特定栅极-发射极电压和集电极-发射极电压组合的集电极电流。矩阵大小必须与栅极-发射极电压、集电极-发射极电压和温度向量定义的维度匹配。

#### 依赖关系

要启用此参数，请将 **I-V 特性定义方式** 设置为 `Lookup table (3D, temperature dependent)`。

### 结电容（完整 I-V 和电容特性）

### **参数化** — 结电容参数化 `Specify fixed input, reverse transfer, and output capacitance`（默认） | `Specify fixed gate-emitter, gate-collector, and collector-emitter capacitance` | `Specify tabulated input, reverse transfer, and output capacitance` | `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance`

选择以下方法之一进行模块参数化：

- `Specify fixed input, reverse transfer, and output capacitance` — 提供数据手册中的固定参数值，并让模块将输入、输出和反向传输电容值转换为结电容值，如电荷模型中所述。这是默认方法。
- `Specify fixed gate-emitter, gate-collector, and collector-emitter capacitance` — 直接提供结电容参数的固定值。
- `Specify tabulated input, reverse transfer, and output capacitance` — 基于数据手册图提供表格化电容和集电极-发射极电压值。模块将输入、输出和反向传输电容值转换为结电容值，如电荷模型中所述。
- `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance` — 提供结电容和集电极-发射极电压的表格值。

### **输入电容，Cies** — 输入电容 `26.4` `nF`（默认）

当集电极短接到发射极时的栅极-发射极电容。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **输入电容，Cies (Vce)** — 表格化输入的输入电容 `[80 40 32 28 27.5 27 26.5 26.5 26.5]` `nF`（默认）

当集电极短接到发射极时的栅极-发射极电容，按集电极-发射极电压表格化。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **反向传输电容，Cres** — 反向传输电容 `2.7` `nF`（默认）

当发射极连接到地时的集电极-栅极电容。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **反向传输电容，Cres (Vce)** — 表格化输入的反向传输电容 `[55 9 5.5 3.1 2.5 2.1 1.9 1.8 1.7]` `nF`（默认）

当发射极连接到地时的集电极-栅极电容，按集电极-发射极电压表格化。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **输出电容，Coes** — 输出电容 `0` `nF`（默认）

当栅极和发射极短接时的集电极-发射极电容。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify fixed input, reverse transfer, and output capacitance`。

### **输出电容，Coes (Vce)** — 表格化输入的输出电容 `[60 20 12 8 6 4.8 4 3.5 3.1]` `nF`（默认）

当栅极和发射极短接时的集电极-发射极电容，按集电极-发射极电压表格化。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance`。

### **栅极-发射极电容** — 栅极-发射极电容 `23.7` `nF`（默认）

放置在栅极和发射极之间的电容。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify fixed gate-emitter, gate-collector, and collector-emitter capacitance`。

### **栅极-发射极电容，Cge(Vge,Vce)** — 表格值的栅极-发射极电容 `[25 31 26.5 24.9 25 24.9 24.6 24.7 24.8]` `nF`（默认）

放置在栅极和发射极之间的电容，按栅极-发射极电压和集电极-发射极电压表格化。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance`。

### **栅极-集电极电容** — 栅极-集电极电容 `2.7` `nF`（默认）

放置在栅极和集电极之间的电容。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify fixed gate-emitter, gate-collector, and collector-emitter capacitance`。

### **栅极-集电极电容，Cgc(Vge,Vce)** — 表格值的栅极-集电极电容 `[55 9 5.5 3.1 2.5 2.1 1.9 1.8 1.7]` `nF`（默认）

放置在栅极和集电极之间的电容，按栅极-发射极电压和集电极-发射极电压表格化。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance`。

### **用于表格化栅极电容的对应栅极-发射极电压，Vge** — 对应的集电极-发射极电压 `0` `V`（默认）

与表格化栅极电容值对应的栅极-发射极电压。

如果此值是标量，则 **栅极-发射极电容，Cge(Vge,Vce)** 和 **栅极-集电极电容，Cgc(Vge,Vce)** 是标量向量。如果此值是向量，则 **栅极-发射极电容，Cge(Vge,Vce)** 和 **栅极-集电极电容，Cgc(Vge,Vce)** 是标量矩阵。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance`。

### **集电极-发射极电容** — 集电极-发射极电容 `0` `nF`（默认）

放置在集电极和发射极之间的电容。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify fixed gate-emitter, gate-collector, and collector-emitter capacitance`。

### **集电极-发射极电容，Cce(Vce)** — 表格值的集电极-发射极电容 `[5 11 6.5 4.9 3.5 2.7 2.1 1.7 1.4]` `nF`（默认） | `nF`

放置在集电极和发射极之间的电容，按集电极-发射极电压表格化。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance`。

### **对应的集电极-发射极电压** — 对应的集电极-发射极电压 `[0 1 2 5 10 15 20 25 30]` `V`（默认）

与表格化电容值对应的集电极-发射极电压。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify tabulated input, reverse transfer, and output capacitance` 或 `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance`。

### **电荷-电压线性度** — 电荷-电压线性度 `Gate-collector capacitance is constant`（默认）| `Gate-collector charge function is nonlinear`

栅极-漏极电容是固定还是非线性：

- `Gate-collector capacitance is
  constant` — 电容值为常量，并根据所选参数化选项直接定义或从数据手册推导得到。这是默认方法。
- `Gate-collector charge function is
  nonlinear` — 栅极-集电极电荷关系根据 Charge Model 中所述的分段非线性函数定义。此时会出现两个附加参数，用于定义栅极-集电极电荷函数。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify fixed input, reverse transfer and output
  capacitance` 或 `Specify fixed
  gate-emitter, gate-collector and output
  capacitance`。

### **栅极-集电极氧化层电容** — 栅极-集电极氧化层电容 `20` `nF`（默认）

当器件导通且集电极-栅极电压较小时的栅极-集电极电容。

#### 依赖关系

要启用此参数，请将 **电荷-电压线性度** 设置为 `Gate-collector charge
  function is nonlinear`。

### **集电极-栅极电压，低于该值时氧化层电容生效** — 集电极-栅极电压，低于该值时氧化层电容生效 `-5` `V`（默认）

集电极-栅极电容在断态 (*C*GC) 和通态 (*C*ox) 电容值之间切换时的集电极-栅极电压。

#### 依赖关系

要启用此参数，请将 **电荷-电压线性度** 设置为 `Gate-collector charge
  function is nonlinear`。

### **总正向渡越时间** — 总正向渡越时间 `0` `us`（默认）

作为底层 IGBT 模型一部分使用的 PNP 晶体管的正向渡越时间。它影响 IGBT 关断时电荷从沟道中移除的速度。

#### 依赖关系

要启用此参数，请在 **Main** 设置中，将 **I-V 特性定义方式** 设置为 `Fundamental nonlinear
  equations`。

### **关断尾电流渡越时间** — 总正向渡越时间 `0` `us`（默认）

尾电流的关断渡越时间。

#### 依赖关系

要启用此参数，请在 **Main** 设置中，将 **I-V 特性定义方式** 设置为 `Lookup table (2D, temperature
  independent)` 或 `Lookup table (3D,
  temperature dependent)`。

### 封装（完整 I-V 和电容特性）

### **集电极引线电阻** — 晶体管的集电极引线电阻 `0` `Ohm`（默认）| 非负标量

*自 R2024b 起*

晶体管的集电极引线电阻，即与集电极触点相关的串联引线电阻。使用此参数可对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Full I-V and capacitance characteristics | No
  thermal port` 或 `Full I-V and
  capacitance characteristics | Show thermal
  port`。

### **发射极引线电阻** — 晶体管的发射极引线电阻 `0` `Ohm`（默认）| 非负标量

*自 R2024b 起*

晶体管的发射极引线电阻，即与发射极触点相关的串联引线电阻。使用此参数可对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Full I-V and capacitance characteristics | No
  thermal port` 或 `Full I-V and
  capacitance characteristics | Show thermal
  port`。

### **栅极引线电阻** — 晶体管的栅极引线电阻 `0` `Ohm`（默认）| 非负标量

*自 R2024b 起*

晶体管的栅极引线电阻，即与栅极触点相关的串联引线电阻。使用此参数可对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Full I-V and capacitance characteristics | No
  thermal port` 或 `Full I-V and
  capacitance characteristics | Show thermal
  port`。

### **集电极引线电感** — 晶体管的集电极引线电感 `0` `nH`（默认）| 非负标量

*自 R2024b 起*

晶体管的集电极引线电感，即与集电极触点相关的串联引线电感。使用此参数可对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Full I-V and capacitance characteristics | No
  thermal port` 或 `Full I-V and
  capacitance characteristics | Show thermal
  port`。

### **发射极引线电感** — 晶体管的发射极引线电感 `0` `nH`（默认）| 非负标量

*自 R2024b 起*

晶体管的发射极引线电感，即与发射极触点相关的串联引线电感。使用此参数可对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Full I-V and capacitance characteristics | No
  thermal port` 或 `Full I-V and
  capacitance characteristics | Show thermal
  port`。

### **栅极引线电感** — 晶体管的栅极引线电感 `0` `nH`（默认）| 非负标量

*自 R2024b 起*

晶体管的栅极引线电感，即与栅极触点相关的串联引线电感。使用此参数可对晶体管中的寄生效应建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Full I-V and capacitance characteristics | No
  thermal port` 或 `Full I-V and
  capacitance characteristics | Show thermal
  port`。

### 高级（完整 I-V 和电容特性）

查找表表示将所有等效电路组件组合到一个查找表中，因此此设置为空。如果使用等效电路表示，此设置具有以下参数。

### **发射系数，N** — 发射系数 `1`（默认）

双极晶体管的发射系数或理想因子。

### **正向 Early 电压，VAF** — 正向 Early 电压 `200` `V`（默认）

IGBT 模型中使用的 PNP 晶体管的正向 Early 电压。有关详细信息，请参阅 PNP Bipolar Transistor 模块参考页。

### **集电极电阻，RC** — 集电极电阻 `0.001` `Ohm`（默认）

集电极处的电阻。

### **发射极电阻，RE** — 发射极电阻 `0.001``Ohm`（默认）

发射极处的电阻。

### **内部栅极电阻，RG** — 内部栅极电阻 `0.001``Ohm`（默认）

测量温度下内部栅极电阻的电阻值。这不是外部电路串联栅极电阻的值，后者应在 IGBT 外部建模。

### **正向电流传输比，BF** — 正向电流传输比 `50`（默认）

IGBT 模型中使用的 PNP 晶体管的理想最大正向电流增益。有关详细信息，请参阅 PNP Bipolar Transistor 模块参考页。

### 温度依赖性（完整 I-V 和电容特性）

对于二维查找表表示，电气方程不依赖于温度，因此此设置为空。对于暴露热端口的三维查找表表示，此设置也为空，因为 **Main** 设置上的三维矩阵已捕获温度依赖性。如果三维查找表表示未暴露模块热端口，则此设置仅包含 **器件仿真温度** 参数。如果使用等效电路表示，此设置具有以下参数。

### **参数化** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Specify Ices and Vce(sat) at second measurement temperature` | `Specify Vce(sat) at second measurement temperature plus the energy gap, EG`

选择以下用于温度依赖性参数化的方法之一：

- `None — Simulate at parameter measurement temperature` — 不建模温度依赖性，并且此设置上的其他参数均不可见。这是默认方法。
- `Specify Ices and Vce(sat) at second measurement temperature` — 通过提供第二测量温度下的零栅压集电极电流 *Ices* 和集电极-发射极电压 *V*ce(sat) 的值来建模温度相关效应。
- `Specify Vce(sat) at second measurement temperature plus the energy gap, EG` — 当数据手册未提供更高测量温度下的零栅压集电极电流 *Ices* 信息时，使用此选项。

### **能隙，EG** — 能隙 `1.11` `eV`（默认）

能隙值。

#### 依赖关系

要启用此参数，请在 **温度依赖性** 设置中，将 **参数化** 设置为 `Specify
  Vce(sat) at second measurement temperature plus the energy gap,
  EG`。

### **第二测量温度下的零栅压集电极电流，Ices** — 第二测量温度下的零栅压集电极电流，Ices `100` `mA`（默认）

第二测量温度下的零栅压集电极电流值。

#### 依赖关系

要启用此参数，请在 **温度依赖性** 设置中，将 **参数化** 设置为 `Specify
  Ices and Vce(sat) at second measurement
  temperature`。

### **第二测量温度下的集电极-发射极饱和电压，Vce(sat)** — 第二测量温度下的集电极-发射极饱和电压，Vce(sat) `3` `V`（默认）

第二测量温度下的集电极-发射极饱和电压值，此时集电极电流和栅极-发射极电压由 **Main** 设置上的相应参数定义。

### **第二测量温度** — 第二测量温度 `125` `degC`（默认）

第二温度 *T*m2，在该温度下测量 **第二测量温度下的零栅压集电极电流，Ices** 和 **第二测量温度下的集电极-发射极饱和电压，Vce(sat)**。

### **饱和电流温度指数，XTI** — 饱和电流温度指数 `3`（默认）

适用于您的器件类型的饱和电流指数值。如果您有 *Ices* 随温度变化的图形数据，可以使用它来微调 *XTI* 的值。

### **迁移率温度指数，BEX** — 迁移率温度指数 `-1.5`（默认）

迁移率温度系数值。对于大多数器件，可以使用默认值。如果您有不同温度下 *Vce(sat)* 的图形数据，可以使用它来微调 *BEX* 的值。

### **内部栅极电阻温度系数** — 内部栅极电阻温度系数 `0` `1/K`（默认）

表示内部栅极电阻 (RG) 随温度变化的分数变化率 (*α*)。因此栅极电阻为 *R* = *R*meas(1 + *α* (*T*s – Tm1 ))，其中 *R*meas 是 **内部栅极电阻，RG** 参数值。

### **器件仿真温度** — 器件仿真温度 `25` `degC`（默认）

仿真器件时的温度 *T*s。

### Main（简化 I-V 特性和基于事件的时序）

**Main** 设置的此配置对应于简化的、基于事件的模块建模选项。如果您使用的是模块的详细建模选项，请参阅 Main（完整 I-V 和电容特性）。

### **集电极电流向量，Ic** — 集电极电流向量 `[0, 10, 50, 100, 200, 400, 600]` `A`（默认）

定义了通态集电极-发射极电压所对应的集电极电流。第一个元素必须为零。

要并行建模多个 N-Channel IGBT 模块，请使用单个 N-Channel IGBT 模块，并将此参数的值乘以您想要并行建模的 IGBT 器件数量。

### **温度向量，Tj** — 温度向量 `[298.15, 398.15]` `K`（默认）

给出集电极-发射极损耗以及开通/关断损耗时所对应的温度值。

#### 依赖关系

要启用此参数，请通过将 **建模选项** 设置为 `Simplified
  I-V characteristics and event-based timing | Show thermal
  port` 来暴露热端口。

### **对应的通态集电极-发射极电压** — 对应的通态集电极-发射极电压 `[0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7]` `V`（默认）

与集电极电流向量对应的集电极-发射极电压。第一个元素必须为零。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Simplified I-V characteristics
  and event-based timing | No thermal port`。

### **集电极-发射极通态电压，Vce=fcn(Tj,Ic)** — 集电极-发射极通态电压 `[0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7; 0, 1.0, 1.15, 1.35, 1.7, 2.35, 3.0]` `V`（默认）

处于通态时的集电极-发射极电压，定义为温度和电流两者的函数。

#### 依赖关系

要启用此参数，请通过将 **建模选项** 设置为 `Simplified
  I-V characteristics and event-based timing | Show thermal
  port` 来暴露热端口。

### **米勒电阻** — 米勒电阻 `0.1` `Ohm`（默认）

当器件开通时，它具有一个恒定值的米勒电阻，与所需电压斜坡串联。该电阻表示开通期间通过器件的部分导电路径，可用于匹配重新连接载流电感和相应续流二极管时观察到的电压尖峰。典型值为有效通态电阻的 10 到 50 倍。

### **断态电导** — 断态电导 `1e-5` `Ohm`（默认）

器件处于断态时的电导。

### **栅极-发射极阈值电压，Vge(th)** — 阈值电压 `6` `V`（默认）

要使器件开通，栅极-发射极电压必须大于该值。

### 开关损耗（简化 I-V 特性和基于事件的时序）

### **开关损耗温度向量，Tj** — 开关损耗温度 `[298.15, 398.15]` `K`（默认）

将开关损耗制成表格时所对应的温度。

#### 依赖关系

要启用此参数，请通过将 **建模选项** 设置为 `Simplified
  I-V characteristics and event-based timing | Show thermal
  port` 来暴露热端口。

### **开关损耗集电极电流向量，Ic** — 开关损耗集电极电流 `[0, 10, 50, 100, 200, 400, 600]` `A`（默认）

将开关损耗制成表格时所对应的集电极电流。

#### 依赖关系

要启用此参数，请通过将 **建模选项** 设置为 `Simplified
  I-V characteristics and event-based timing | Show thermal
  port` 来暴露热端口。

### **开通开关损耗，Eon=fcn(Tj,Ic)** — 开通开关损耗 `[0, 0.2, 1, 2, 4, 8, 15; 0, 0.3, 1.3, 2.5, 5, 11, 18]*1e-3` `J`（默认）

开通器件时的能量损耗，定义为温度和最终通态电流的函数。

#### 依赖关系

要启用此参数，请通过将 **建模选项** 设置为 `Simplified
  I-V characteristics and event-based timing | Show thermal
  port` 来暴露热端口。

### **关断开关损耗，Eoff=fcn(Tj,Ic)** — 关断开关损耗 `[0, 0.3, 1.5, 3, 6, 15, 25; 0, 0.7, 3.3, 6.5, 13, 25, 35]*1e-3` `J`（默认）

关断器件时的能量损耗，定义为温度和最终通态电流的函数。

#### 依赖关系

要启用此参数，请通过将 **建模选项** 设置为 `Simplified
  I-V characteristics and event-based timing | Show thermal
  port` 来暴露热端口。

### 动态特性（简化 I-V 特性和基于事件的时序）

### **开通延迟** — 开通延迟 `0.07` `us`（默认）

器件开始斜升开通之前的时间。

### **电流上升时间** — 电流上升时间 `0.7` `us`（默认）

驱动阻性负载时电流斜升所需的时间。

### **Turn-off delay** — 关断延迟 `0.2` `us`（默认）

器件开始斜坡关断之前的时间。

### **Current fall time** — 电流下降时间 `0.5` `us`（默认）

驱动电阻负载时电流斜坡下降所需的时间。

### **Off-state voltage for rise and fall times** — 上升和下降时间的关断状态电压 `300` `V`（默认）

指定上升和下降时间时使用的关断状态集电极-发射极电压。默认值为 `300` V。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Simplified I-V characteristics and event-based timing | No thermal port`。

### **Off-state voltage for rise and fall times** — 上升和下降时间的关断状态电压 `300` `V`（默认）

指定上升时间、下降时间和损耗数据时使用的关断状态集电极-发射极电压。

#### 依赖关系

要启用此参数，请通过将 **Modeling option** 设置为 `Simplified I-V characteristics and event-based timing | Show thermal port` 来暴露热端口。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024b：对每个晶体管端子的寄生引线电阻和电感建模

现在，您可以通过使用以下参数指定引线电阻和电感，对 N-Channel IGBT 模块每个端子的寄生效应建模：

- **Collector lead resistance**
- **Emitter lead resistance**
- **Gate lead resistance**
- **Collector lead inductance**
- **Emitter lead inductance**
- **Gate lead inductance**

## 描述

N-Channel 绝缘栅双极型晶体管

N-Channel IGBT 模块对绝缘栅双极型晶体管 (IGBT) 建模。通过将 **Modeling option** 参数设置为以下任一值，该模块提供两个主要建模选项：

- **Full I-V and capacitance characteristics** — 此建模选项是一种详细的组件模型，适合仿真详细开关特性和预测组件损耗。此建模选项又提供两种对 IGBT 建模的方式：

  - 作为基于 PNP 双极型晶体管和 N-channel MOSFET 的等效电路。有关使用此模型的详细信息，请参阅通过等效电路表示、微调电流-电压特性和对温度依赖性建模。
  - 通过 I-V（电流-电压）曲线的二维查找表近似。有关详细信息，请参阅通过二维查找表表示。
  - 通过包含温度数据的 I-V（电流-电压）曲线的三维查找表近似。有关详细信息，请参阅通过三维查找表表示。

  详细模型中的栅极电容表示为固定的栅极-发射极电容 *CGE* 以及固定或非线性的栅极-集电极电容 *C*GC。有关详细信息，请参阅电荷模型。
- **Simplified I-V characteristics and event-based timing** — 此建模选项仅使用作为集电极-发射极电压函数的导通状态 I-V 数据，以更简单的方式对 IGBT 建模。在关断状态（栅极-发射极电压小于 **Threshold voltage, Vth**）下，IGBT 由恒定 **Off-state conductance** 建模。当近似动态特性已足够且仿真速度至关重要时，此简化模型适用。有关详细信息，请参阅基于事件的 IGBT 建模选项。

结合热端口建模选项（请参阅热端口），该模块由此为您提供四种选择。要选择所需的建模选项，请将 **Modeling option** 参数设置为以下任一值：

- `Full I-V and capacitance characteristics | No thermal port` — 不仿真生成热和器件温度影响的详细模型。这是默认值。
- `Full I-V and capacitance characteristics | Show thermal port` — 具有暴露热端口的详细模型。
- `Simplified I-V characteristics and event-based timing | No thermal port` — 简化的事件型模型，也不仿真生成热和器件温度的影响。
- `Simplified I-V characteristics and event-based timing | Show thermal port` — 具有暴露热端口的简化事件型模型。

### 通过等效电路表示

详细模块建模选项的等效电路由一个 PNP Bipolar Transistor 模块组成，该模块由 N-Channel MOSFET 模块驱动，如下图所示：

MOSFET 源极连接到双极型晶体管集电极，MOSFET 漏极连接到双极型晶体管基极。MOSFET 使用 N-Channel MOSFET 模块参考页中所示的基于阈值的方程。双极型晶体管使用 PNP Bipolar Transistor 模块参考页中所示的方程，但增加了用于缩放 *kT/q* 的发射系数参数 *N*。

N-Channel IGBT 模块使用您在模块对话框中指定的导通和关断特性，来估计底层 N-Channel MOSFET 和 PNP 双极型晶体管的参数值。

该模块使用关断特性计算基极-发射极电压 *Vbe* 和饱和电流 *IS*。

当晶体管关断时，栅极-发射极电压为零，并且 IGBT 基极-集电极电压很大，因此 PNP 基极和集电极电流方程简化为：

Ib=0=−Is[1βF(e−qVbe/(NkT)−1)−1βR]Ic=−Is[e−qVbe/(NkT)(1+VbcVAF)+1βR]

其中 *N* 是 **Emission coefficient, N** 参数值，*VAF* 是正向 Early 电压，*Ic* 和 *Ib* 定义为分别流入集电极和基极时为正。其余变量的定义请参阅 PNP Bipolar Transistor 参考页。第一个方程可用于求解 *Vbe*。

在关断条件下基极电流为零，因此 *Ic* = –*Ices*，其中 *Ices* 是零栅极电压集电极电流。基极-集电极电压 *Vbc* 由 *Vbc* = *Vces* + *Vces* 给出，其中 *Vces* 是测量 *Ices* 时的电压。因此，我们可以将第二个方程重写如下：

Ices=Is[e−qVbe/(NkT)(1+Vces+VbeVAF)+1βR]

该模块将 *βR* 和 *βF* 设置为典型值 1 和 50，因此可以使用这两个方程求解 *Vbe* 和 *IS*：

Vbe=−NkTqlog(1+βFβR)Is=Ice−qVbe/(NkT)+1βR

**注意**

该模块不需要 *βF* 的精确值，因为它可以调整 MOSFET 增益 *K* 以确保整体器件增益正确。

模块参数 **Collector-emitter saturation voltage, Vce(sat)** 和 **Collector current at which Vce(sat) is defined** 用于通过求解以下方程确定 *Vbe(sat)*：

Ice(sat)=Is[e−qVbe(sat)/(NkT)(1+Vce(sat)+Vbe(sat)VAF)+1βR]

根据此值，该模块使用以下方程计算 MOSFET 增益 *K*：

Itf=TFdIcdtIds=Ib−Itf=K[(VGE(sat)−Vth)Vds−Vds22]

其中 *Vth* 是 **Gate-emitter threshold voltage, Vge(th)** 参数值，*VGE(sat)* 是 **Gate-emitter voltage at which Vce(sat) is defined** 参数值，*TF* 是 **Total forward transit time** 参数值。

*Vds* 与晶体管电压的关系为 *Vds* = *Vce* – *Vbe*。该模块将此关系代入 *Vds*，将基极-发射极电压和基极电流设置为其饱和值，并重新排列 MOSFET 方程得到

K=Ib(sat)[(VGE(sat)−Vth)(Vbe(sat)+Vce(sat))−(Vbe(sat)+Vce(sat))22]

其中 *Vce(sat)* 是 **Collector-emitter saturation voltage, Vce(sat)** 参数值。

这些计算确保在这两个指定条件下精确满足零栅极电压集电极电流和集电极-发射极饱和电压。然而，电流-电压图对发射系数 *N* 和 *Vth* 的精确值非常敏感。如果制造商数据手册给出了不同 *VGE* 值的电流-电压图，则可以手动调整 *N* 和 *Vth* 以改善匹配。

### 通过二维查找表表示

对于详细模块建模选项的查找表表示，您需要提供作为栅极-发射极电压和集电极-发射极电压函数的集电极电流表格值。使用此选项的主要优点是仿真速度。它还允许您根据测量数据或从另一个仿真环境获得的数据来参数化器件。要从等效电路表示生成您自己的数据，可以使用测试框架，例如 IGBT Characteristics 示例中所示。

查找表表示将所有等效电路组件（PNP 晶体管、N-channel MOSFET、集电极电阻和发射极电阻）组合为一个等效查找表。

**注意**

为确保集电极-发射极电流和集电极-发射极电压的符号一致：

- 如果集电极-发射极电压等于 `0`，则 **Tabulated collector currents, Ic(Vge,Vce)** 参数的值必须等于 `0`。
- 表格功率（即 **Tabulated collector currents, Ic(Vge,Vce)** 参数与集电极-发射极电压的乘积）必须大于或等于 `0`。
- 表格电导（即 **Tabulated collector currents, Ic(Vge,Vce)** 参数相对于集电极-发射极电压 *Vce* 的梯度）必须大于或等于 `0`。
- **Tabulated collector currents, Ic(Vge,Vce)** 参数相对于栅极-发射极电压 *Vge* 的一阶梯度必须等于 `0`。

### 通过三维查找表表示

对于详细模块建模选项的温度相关查找表表示，您需要提供作为栅极-发射极电压、集电极-发射极电压和温度函数的集电极电流表格值。

查找表表示将所有等效电路组件（PNP 晶体管、N-channel MOSFET、集电极电阻和发射极电阻）组合为一个等效查找表。

如果未暴露模块热端口，则 **Temperature Dependence** 设置上的 **Device simulation temperature** 参数允许您指定仿真温度。

**注意**

为确保集电极-发射极电流和集电极-发射极电压的符号一致：

- 如果集电极-发射极电压等于 `0`，则 **Tabulated collector currents, Ic(Vge,Vce,T)** 参数的值必须等于 `0`。
- 表格功率（即 **Tabulated collector currents, Ic(Vge,Vce,T)** 参数与集电极-发射极电压的乘积）必须大于或等于 `0`。
- 表格电导（即 **Tabulated collector currents, Ic(Vge,Vce,T)** 参数相对于集电极-发射极电压 *Vce* 的梯度）必须大于或等于 `0`。
- **Tabulated collector currents, Ic(Vge,Vce,T)** 参数相对于栅极-发射极电压 *Vge* 的一阶梯度必须等于 `0`。

### 电荷模型

该模块的详细建模选项通过固定电容值，或通过作为集电极-发射极电压函数的表格值来对电容建模。无论哪种情况，您都可以直接指定栅极-发射极和栅极-集电极电容值，也可以让该模块根据输入电容和反向传输电容值推导这些值。因此，在 **Junction Capacitance** 设置中，电荷模型的 **Parameterization** 选项包括：

- `Specify fixed input, reverse transfer and output capacitance` — 从数据手册提供固定参数值，并让该模块按如下所述将输入电容和反向传输电容值转换为电容值。这是默认方法。
- `Specify fixed gate-emitter, gate-collector and collector-emitter capacitance` — 直接提供电容参数的固定值。
- `Specify tabulated input, reverse transfer and output capacitance` — 基于数据手册图提供表格电容和集电极-发射极电压值。该模块按如下所述将输入电容和反向传输电容值转换为电容值。
- `Specify tabulated gate-emitter, gate-collector and collector-emitter capacitance` — 提供电容和集电极-发射极电压的表格值。

当数据手册提供电容作为集电极-发射极电压函数的图时，请使用其中一个表格电容选项（`Specify tabulated input, reverse transfer and output capacitance` 或 `Specify tabulated gate-emitter, gate-collector and collector-emitter capacitance`）。使用表格电容值将获得更准确的动态特性，并避免为了拟合动态特性而迭代调整参数。

如果使用 `Specify fixed gate-emitter, gate-collector and collector-emitter capacitance` 或 `Specify tabulated gate-emitter, gate-collector and collector-emitter capacitance` 选项，则 **Junction Capacitance** 设置允许您直接指定 **Gate-emitter capacitance**、**Gate-collector capacitance** 和 **Collector-emitter capacitance** 参数值（固定或表格）。否则，该模块会根据 **Input capacitance, Cies**、**Reverse transfer capacitance, Cres** 和 **Output capacitance, Coes** 参数值推导这些值。这两种参数化方法的关系如下：

- *CGC* = *Cres*
- *CGE* = *Cies* – *Cres*
- *C*CE = *Coes* – *Cres*

这两个固定电容选项（`Specify fixed input, reverse transfer and output capacitance` 或 `Specify fixed gate-emitter, gate-collector and collector-emitter capacitance`）允许您将栅极电容建模为固定栅极-发射极电容 *C*GE，以及固定或非线性的栅极-集电极电容 *C*GC。如果您为 **Charge-voltage linearity** 参数选择 `Gate-collector charge function is nonlinear` 选项，则栅极-集电极电荷关系由下图所示的分段线性函数定义。

使用此非线性电容时，栅极-发射极和集电极-发射极电压曲线采用下一图所示的形式，其中集电极-发射极电压下降有两个区域（标记为 2 和 3），栅极-发射极电压有两个时间常数（在阈值电压 *V*th 之前和之后）：

假设 IGBT 栅极通过外部电阻 *R*G 驱动，您可以按如下方式确定 *Cies*、*Cres* 和 *C*ox 的电容值：

1. 设置 *Cies*，以获得区域 1 中 *V*GE 的正确时间常数。该时间常数由 *Cies* 与 *R*G 的乘积定义。或者，您也可以使用数据手册中的 *Cies* 值。
2. 设置 *Cres*，以实现区域 2 中正确的 *VCE* 梯度。该梯度由 (*VGE* – *Vth*)/(*Cres* · *R*G) 给出。
3. 将 *VCox* 设置为 *VCE* 梯度发生变化时的电压减去阈值电压 *V*th。
4. 设置 *Cox*，以获得区域 4 中正确的 Miller 长度和时间常数。

由于底层模型是对实际电荷分布的简化，可能需要迭代这四个步骤，才能获得与测量数据最佳的整体拟合。

如果将 **I-V characteristics defined by** 参数设置为 `Fundamental nonlinear equation`，则 IGBT 关断时的集电极电流拖尾由 **Total forward transit time** 参数确定。

如果将 **I-V characteristics defined by** 参数设置为 `Lookup table (2D, temperature independent)` 或 `Lookup table (3D, temperature dependent)`，则 IGBT 关断时的集电极电流拖尾由 **Turn-off tail current transit time** 参数确定：

ic=ioff+(ion−ioff)exp(−t−toffTT)

其中 *ioff* 是 IGBT 关断电流，*ion* 是 IGBT 开通电流，*toff* 是关断时间，*TT* 是 **Turn-off tail current transit time** 参数的值。

**注意**

由于此模块实现包含电荷模型，您必须对驱动栅极的电路阻抗进行建模，以获得具有代表性的开通和关断动态特性。因此，如果您通过将栅极驱动电路表示为受控电压源来简化该电路，则必须在电压源与栅极之间包含合适的串联电阻。

### 微调电流-电压特性

对于详细模型的等效电路表示，使用 **Advanced** 设置上的参数来微调所建模器件的电流-电压特性。为了有效使用这些附加参数，您需要制造商数据手册，其中提供不同栅极-发射极电压值下的集电极电流与集电极-发射极电压关系图。**Advanced** 设置上的参数具有以下影响：

- **Emission coefficient, N** 参数控制原点附近电流-电压曲线的形状。
- **Collector resistance, RC** 和 **Emitter resistance, RE** 参数影响较高电流下以及由高栅极-发射极电压完全开通时电流-电压曲线的斜率。
- **Forward Early voltage, VAF** 参数影响栅极-发射极电压在 **Gate-emitter threshold voltage, Vge(th)** 附近时电流-电压曲线的形状。

### 温度依赖性建模

对于 2-D 查找表表示，电气方程不依赖温度。但是，您可以通过使用 3-D 查找表表示，或通过使用详细模型的等效电路表示来对温度依赖性建模。

对于等效电路表示，温度依赖性通过对组成元件的温度依赖性来建模。有关定义方程的更多信息，请参阅 N-Channel MOSFET 和 PNP Bipolar Transistor 模块参考页。

有些数据手册不提供较高测量温度下零栅极电压集电极电流 *Ices* 的信息。在这种情况下，您也可以使用该半导体类型的典型值来指定器件的能隙 *EG*。对于硅，能隙通常为 `1.11` eV。

### 基于事件的 IGBT 建模选项

与具有完整 I-V 和电容特性的实现相比，此实现具有简单得多的方程。当分析重点是理解整体电路行为，而不是验证精确的 IGBT 时序或损耗特性时，请使用基于事件的建模选项。

该器件始终处于以下四种状态之一：

- Off
- Turning on
- On
- Turning off

在 off 状态下，集电极电流 (*i*c) 与集电极-发射极电压 (*vce*) 之间的关系为

|  |  |
| --- | --- |
| *ic* = *Goff**vce* | **(1)** |

在 on 状态下，集电极电流 (*ic*) 与集电极-发射极电压 (*vce*) 之间的关系为

|  |  |
| --- | --- |
| *vce* = tablelookup(*ic*) | **(2)** |

在 turning on 时，集电极-发射极电压在上升时间内斜降至零，当电压降至表格导通值以下时，器件进入 on 状态。类似地，在 turning off 时，集电极-发射极电压在（电流）下降时间内斜升至指定的阻断电压值。

下图显示了驱动电阻负载时得到的电压和电流曲线。

### 热端口

该模块有一个可选热端口，默认隐藏。要显示热端口，请将 **Modeling option** 参数设置为：

- `Full I-V and capacitance characteristics | Show thermal port` — 详细模型。此操作会在模块图标上显示热端口 **H**，并显示 **Thermal Port** 参数。
- `Simplified I-V characteristics and event-based timing | Show thermal port` — 简化的事件建模模型。此操作会在模块图标上显示热端口 **H**，显示 **Thermal Port** 参数以及附加的 **Main** 参数。要模拟热效应，您必须为开通和关断损耗提供附加表格数据，并将集电极-发射极导通电压定义为同时取决于电流和温度的函数。

使用热端口来模拟产生的热量和器件温度的影响。有关使用热端口以及 **Thermal Port** 参数的更多信息，请参阅模拟半导体中的热效应。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅设置模块变量的优先级和初始目标。

使用标称值来指定模型中变量的预期量值。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅通过标称值进行系统缩放。

下表显示了模块电容与初始目标之间的关系：

| Defined Capacitance | Initial Targets |
| --- | --- |
| Gate-emitter capacitance, *Cge* | 仅设置栅极-发射极电容电压的初始目标。将集电极-发射极电容电压的初始目标设置为 `0`，或将其优先级设置为 `None`。 |
| Collector-emitter capacitance, *Cce* | 仅设置集电极-发射极电容电压的初始目标。将栅极-发射极电容电压的初始目标设置为 `0`，或将其优先级设置为 `None`。 |
| Gate-collector capacitance, *Cgc* | 通过对栅极-发射极和集电极-发射极电压施加约束，设置栅极-集电极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |
| Gate-emitter capacitance, *Cge*, and gate-collector capacitance, *Cgc* | 通过对栅极-发射极和集电极-发射极电压施加约束，设置栅极-发射极和栅极-集电极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |
| Gate-emitter capacitance, *Cge*, and collector-emitter capacitance, *Cce* | 设置栅极-发射极和集电极-发射极电容的初始目标。 |
| Gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | 通过对栅极-发射极和集电极-发射极电压施加约束，设置栅极-集电极和集电极-发射极电压的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |
| Gate-emitter capacitance, *Cge*, gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | 通过对栅极-发射极和集电极-发射极电压施加约束，设置栅极-发射极、栅极-集电极和集电极-发射极电容的初始目标。栅极-集电极电容电压的初始条件等于栅极-发射极与集电极-发射极之间的电压。 |

**注意**

在您的模型中，**Priority** 等于 `Low` 或 `High` 的初始目标数量必须与微分变量数量匹配。微分变量来自模型中的电感和电容。

### 绘制基本 I-V 特性

您无需构建完整模型即可绘制 N-Channel IGBT 模块的基本 I-V 特性。使用这些图来探究您的参数选择对器件特性的影响。如果您根据数据手册对模块进行参数化，可以将图与数据手册进行比较，以检查是否正确地对模块进行了参数化。如果您有一个完整的工作模型，但不知道使用哪个制造器件，可以将图与数据手册进行比较，以帮助您做出决定。

要启用此选项，请将 N-Channel IGBT 模块的 **Modeling option** 参数设置为 `Full I-V and capacitance characteristics | No thermal port`。要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的更多信息，请参阅绘制半导体模块的基本 I-V 特性。
