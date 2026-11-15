---
type: simulink-block
title: 'RF Data Converter'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'rfdataconverter'
documentation_source_path: 'ref/rfdataconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# RF Data Converter

## 端口

### 输入

### **adcT*`x`*Ch*`y`*** — ADC 输入数据列向量

ADC 输入数据，指定为列向量。

***`x`*** 表示 ADC tile 编号，***`y`*** 表示 ADC 通道编号。**RF interface** 参数设置 **adc** 端口数。例如，如果 **RF interface** 设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有端口 **adcT0Ch0** 和 **adcT0Ch1**，即每个 ADC 通道接口一个输入端口。

此端口的有效值取决于仿真模式和 **Digital interface** 参数值。

- 在 **Pass-through** 仿真模式下，该模块接受 `int16` 和 `uint16` 数据类型的输入。在此模式下：

  - 如果将 **Digital interface** 参数设置为 `Real`，请将此值指定为 *N* 元素列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中设置的每时钟周期采样数。

    使用此选项指定实值数据。例如，考虑 *N* 等于 2，且数据包含两个实值 *D*0 和 *D*1。在这种情况下，请将此端口值指定为形式为 [*D*0 *D*1] 的向量。
  - 如果将 **Digital interface** 参数设置为 `I/Q`，请将此值指定为 2*N* 元素列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中设置的每时钟周期采样数。

    使用此选项指定复值数据。例如，考虑 *N* 等于 2，且数据包含两个复值，其实部为 *I*0 和 *I*1，虚部为 *Q*0 和 *Q*1。在这种情况下，请将此端口值指定为形式为 [*I*0 *Q*0 *I*1 *Q*1] 的向量。

  **数据类型：** `int16` | `uint16`
- 在 **Behavioral** 仿真模式下，该模块接受 `double` 数据类型的输入。请将此值指定为 *R**N* 元素列向量，其中 *R* 是您在 **Decimation mode (xN)** 参数中设置的抽取因子，*N* 是您在 **Samples per clock cycle** 参数中设置的每时钟周期采样数。

  **数据类型：** `double`

**数据类型：** `int16` | `uint16` | `double`

### **dacT*`x`*Ch*`y`*Data** — DAC 输入数据 标量 | 列向量

DAC 输入数据，指定为标量或长度在 [1, *N*] 范围内的列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中指定的每时钟周期采样数。

***`x`*** 表示 DAC tile 编号，***`y`*** 表示 DAC 通道编号。**RF interface** 参数设置 **dacT*`x`*Ch*`y`*Data** 端口数。

有关数据格式的更多信息，请参阅 RF Data Converter 模块与硬件逻辑之间的数据格式。

#### 依赖项

要启用此端口，请将 **Digital interface** 参数设置为 `Real`。

**数据类型：** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dacT*`x`*Ch*`y`*IData** — DAC 输入的实部 标量 | 列向量

DAC 输入的实部，指定为标量或长度在 [1, *N*] 范围内的列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中指定的每时钟周期采样数。

***`x`*** 表示 DAC tile 编号，***`y`*** 表示 DAC 通道编号。**RF interface** 参数设置 **dacT*`x`*Ch*`y`*IData** 端口数。

有关数据格式的更多信息，请参阅 RF Data Converter 模块与硬件逻辑之间的数据格式。

#### 依赖项

要启用此端口，请将 **Digital interface** 参数设置为 `I/Q`。

**数据类型：** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dacT*`x`*Ch*`y`*QData** — DAC 输入的虚部 标量 | 列向量

DAC 输入的虚部，指定为标量或长度在 [1, *N*] 范围内的列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中指定的每时钟周期采样数。

***`x`*** 表示 DAC tile 编号，***`y`*** 表示 DAC 通道编号。**RF interface** 参数设置 **dacT*`x`*Ch*`y`*QData** 端口数。

有关数据格式的更多信息，请参阅 RF Data Converter 模块与硬件逻辑之间的数据格式。

#### 依赖项

要启用此端口，请将 **Digital interface** 参数设置为 `I/Q`。

**数据类型：** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dacT*`x`*Ch*`y`*Valid** — 有效 DAC 输入数据的指示 `Boolean` 标量

有效 DAC 输入数据的指示，指定为标量。

值 `1` 表示 **dacT*`x`*Ch*`y`*Data** 端口上的数据有效，或者 **dacT*`x`*Ch*`y`*IData** 和 **dacT*`x`*Ch*`y`*QData** 端口上的数据有效。

***`x`*** 表示 DAC tile 编号，***`y`*** 表示 DAC 通道编号。**RF interface** 参数设置 **dacT*`x`*Ch*`y`*Valid** 端口数。

**数据类型：** `Boolean`

### **adcT*`x`*Ch*`y`*RealTimeCtrlIn** — ADC 实时控制输入总线

ADC 实时控制输入，指定为总线。

***`x`*** 表示 ADC tile 编号，***`y`*** 表示 ADC 通道编号。**RF interface** 参数设置 **adcT*`x`*Ch*`y`*RealTimeCtrlIn** 端口数。例如，如果将 **RF interface** 参数设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有两个输入端口，每个 ADC 通道接口一个。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上选择 **Real-time ports** 或 **Real-time NCO ports**。

**数据类型：** `DUT2RFDCRealTimeCtrlBusObj`

### **adcT*`x`*NCOUpdateReq** — ADC NCO 更新请求 `Boolean` 标量

ADC 数控振荡器 (NCO) 更新请求，指定为 Boolean 标量。要请求更新 ADC NCO 设置，请将此输入信号设置为 `High`。

***`x`*** 表示 ADC tile 编号。**RF interface** 参数设置 **adcT*`x`*NCOUpdateReq** 端口数。例如，如果将 **RF interface** 参数设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有一个输入端口，每个 ADC tile 一个。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上的 **ADC** 部分下选择 **Real-time NCO ports**。

**数据类型：** `Boolean`

### **dacT*`x`*Ch*`y`*RealTimeCtrlIn** — DAC 实时控制输入总线

DAC 实时控制输入，指定为总线。

***`x`*** 表示 DAC tile 编号，***`y`*** 表示 DAC 通道编号。**RF interface** 参数设置 **dacT*`x`*Ch*`y`*RealTimeCtrlIn** 端口数。例如，如果将 **RF interface** 参数设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有两个输入端口，每个 DAC 通道接口一个。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上的 **DAC** 部分下选择 **Real-time NCO ports**。

**数据类型：** `DUT2RFDCRealTimeCtrlBusObj`

### **dacT*`x`*NCOUpdateReq** — DAC NCO 更新请求 `Boolean` 标量

DAC NCO 更新请求，指定为 Boolean 标量。要请求更新 DAC NCO 设置，请将此输入信号设置为 `High`。

***`x`*** 表示 DAC tile 编号。**RF interface** 参数设置 **dacT*`x`*NCOUpdateReq** 端口数。例如，如果将 **RF interface** 参数设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有一个输入端口，每个 DAC tile 一个。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上的 **DAC** 部分下选择 **Real-time NCO ports**。

**数据类型：** `Boolean`

### **dacT0SysrefGating** — MTS 模式的同步时钟门控 `Boolean` 标量

多 tile 同步 (MTS) 模式的同步时钟门控，指定为 Boolean 标量。要使 DAC tile 禁用 `Sysref` 时钟信号，请将此输入信号设置为 `High`。

#### 依赖项

要启用此端口，请在 **Common Parameters** 部分下选择 **Multi tile sync**，并在 **Advanced** 选项卡上的 **DAC** 部分下选择 **Real-time NCO ports**。

**数据类型：** `Boolean`

### **dacT0SysrefReEnable** — MTS 模式的同步时钟重新启用 `Boolean` 标量

MTS 模式的同步时钟重新启用，指定为 Boolean 标量。要重新启用 `Sysref` 时钟信号，请将此输入信号设置为 `High`。

#### 依赖项

要启用此端口，请在 **Common Parameters** 部分下选择 **Multi tile sync**，并在 **Advanced** 选项卡上的 **DAC** 部分下选择 **Real-time NCO ports**。

**数据类型：** `Boolean`

### 输出

### **dacT*`x`*Ch*`y`*** — DAC 输出数据列向量

DAC 输出数据，返回为列向量。

- 在 **Pass-through** 仿真模式下，该模块返回 `int16` 数据类型的输出。在此模式下：

  - 如果将 **Digital interface** 参数设置为 `Real`，该模块返回 *N* 元素列向量形式的输出，其中 *N* 是您在 **Samples per clock cycle** 参数中设置的每时钟周期采样数。

    例如，考虑 *N* 等于 2，并且输入到 **dacT0Ch1Data** 端口的数据大小为 32 位。在这种情况下，此端口返回向量 [*S*0 *S*1]，其中 *S*0 是从 **dacT0Ch1Data** 端口上输入数据的 0 到 15 位切片的 16 位值，*S*1 是从 **dacT0Ch1Data** 端口上输入数据的 16 到 31 位切片的 16 位值。
  - 如果将 **Digital interface** 参数设置为 `I/Q`，该模块返回 2*N* 元素列向量形式的输出，其中 *N* 是您在 **Samples per clock cycle** 参数中设置的每时钟周期采样数。

    例如，考虑 *N* 等于 2，并且输入到 **dacT0Ch1IData** 和 **dacT0Ch1QData** 端口的数据大小为 32 位。在这种情况下，此端口返回向量 [*I*0 *Q*0 *I*1 *Q*1]，其中 *I*0 是从 **dacT0Ch1IData** 端口上输入数据的 0 到 15 位切片的 16 位值，*I*1 是从 **dacT0Ch1IData** 端口上输入数据的 16 到 31 位切片的 16 位值，*Q*0 是从 **dacT0Ch1QData** 端口上输入数据的 0 到 15 位切片的 16 位值，*Q*1 是从 **dacT0Ch1QData** 端口上输入数据的 16 到 31 位切片的 16 位值。

  **数据类型：** `int16`
- 在 **Behavioral** 仿真模式下，该模块返回 `double` 数据类型的输出。该模块返回 *R**N* 元素列向量形式的输出，其中 *R* 是您在 **Interpolation mode (xN)** 参数中设置的插值因子，*N* 是您在 **Samples per clock cycle** 参数中设置的每时钟周期采样数。

  **数据类型：** `double`

***`x`*** 表示 DAC tile 编号，***`y`*** 表示 DAC 通道编号。**RF interface** 参数设置 **dacT*`x`*Ch*`y`*** 端口数。

**数据类型：** `int16` | `double`

### **adcT*`x`*Ch*`y`*Data** — ADC 输出数据 标量 | 列向量

ADC 输出数据，返回为标量或长度在 [1, *N*] 范围内的列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中指定的每时钟周期采样数。

***`x`*** 表示 ADC tile 编号，***`y`*** 表示 ADC 通道编号。**RF interface** 参数设置 **adcT*`x`*Ch*`y`*Data** 端口数。

有关数据格式的更多信息，请参阅 RF Data Converter 模块与硬件逻辑之间的数据格式。

#### 依赖项

要启用此端口，请将 **Digital interface** 参数设置为 `Real`。

**数据类型：** `uint16` | `uint32` | `uint64` | `fixed point`

### **adcT*`x`*Ch*`y`*IData** — ADC 输出的实部 标量 | 列向量

ADC 输出的实部，返回为标量或长度在 [1, *N*] 范围内的列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中指定的每时钟周期采样数。

***`x`*** 表示 ADC tile 编号，***`y`*** 表示 ADC 通道编号。**RF interface** 参数设置 **adcT*`x`*Ch*`y`*IData** 端口数。

有关数据格式的更多信息，请参阅 RF Data Converter 模块与硬件逻辑之间的数据格式。

#### 依赖项

要启用此端口，请将 **Digital interface** 参数设置为 `I/Q`。

**数据类型：** `uint16` | `uint32` | `uint64` | `fixed point`

### **adcT*`x`*Ch*`y`*QData** — ADC 输出的虚部 标量 | 列向量

ADC 输出的虚部，返回为标量或长度在 [1, *N*] 范围内的列向量，其中 *N* 是您在 **Samples per clock cycle** 参数中指定的每时钟周期采样数。

***`x`*** 表示 ADC tile 编号，***`y`*** 表示 ADC 通道编号。**RF interface** 参数设置 **adcT*`x`*Ch*`y`*Qdata** 端口数。

有关数据格式的更多信息，请参阅 RF Data Converter 模块与硬件逻辑之间的数据格式。

#### 依赖项

要启用此端口，请将 **Digital interface** 参数设置为 `I/Q`。

**数据类型：** `uint16` | `uint32` | `uint64` | `fixed point`

### **adcT*`x`*Ch*`y`*Valid** — 有效 ADC 输出数据的指示 `Boolean` 标量

有效 ADC 输出数据的指示，返回为 Boolean 标量。

值 `1` 表示 **adcT*`x`*Ch*`y`*Data** 端口上的数据有效，或者 **adcT*`x`*Ch*`y`*IData** 和 **adcT*`x`*Ch*`y`*QData** 端口上的数据有效。

***`x`*** 表示 ADC tile 编号，***`y`*** 表示 ADC 通道编号。**RF interface** 设置 **adcT*`x`*Ch*`y`*Valid** 端口数。

**数据类型：** `Boolean`

### **adcT*`x`*Ch*`y`*RealTimeCtrlOut** — ADC 实时控制输出总线

ADC 实时控制输出，返回为总线。在 **Pass-through** 仿真模式下，此端口始终具有值 `Low`。

***`x`*** 表示 ADC tile 编号，***`y`*** 表示 ADC 通道编号。**RF interface** 参数设置 **adcT*`x`*Ch*`y`*RealTimeCtrlOut** 端口数。例如，如果将 **RF interface** 参数设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有两个输出端口，每个 ADC 通道接口一个。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上选择 **Real-time ports**。

**数据类型：** `RFDC2DUTRealTimeCtrlBusObj`

### **dacT*`x`*NCOUpdateBusy** — DAC NCO 更新正在进行的指示 标量

DAC NCO 更新正在进行的指示，返回为 Boolean 标量。在 MTS 模式下，对于 Tile 0，此值以 `fixdt(0,2,0)` 类型的标量返回。在 **Pass-through** 仿真模式下，此端口始终具有值 `Low`。

***`x`*** 表示 DAC tile 编号。**RF interface** 参数设置 **dacT*`x`*NCOUpdateBusy** 端口数。例如，如果将 **RF interface** 参数设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有一个输出端口，每个 DAC tile 一个。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上的 **DAC** 部分下选择 **Real-time NCO ports**。

**数据类型：** `Boolean` | `fixdt(0,2,0)`

### **adcT*`x`*NCOUpdateBusy** — ADC NCO 更新正在进行的指示 `Boolean` 标量

ADC NCO 更新正在进行的指示，返回为 Boolean 标量。在 **Pass-through** 仿真模式下，此端口始终具有值 `Low`。

***`x`*** 表示 ADC tile 编号。**RF interface** 参数设置 **adcT*`x`*NCOUpdateBusy** 端口数。例如，如果将 **RF interface** 参数设置为 `ADC & DAC 2x2 RF Interface`，则该模块具有一个输出端口，每个 ADC tile 一个。

#### 依赖项

要启用此端口，请在 **Advanced** 选项卡上的 **ADC** 部分下选择 **Real-time NCO ports**。

**数据类型：** `Boolean`

## 参数

### **RFDC simulation** — 仿真模式选择 **Pass-through**（默认）| **Behavioral**

选择仿真模式。

- **Pass-through** — 在此仿真模式下，模块输出与输入相同的数据。插值、抽取和混频器设置不影响模块输出值。
- **Behavioral** — 在此仿真模式下，插值、抽取和混频器设置会影响模块输出值。

### **Hardware board** — 查看所选硬件的选项 `None`（默认）| 支持的 Xilinx 开发板

此参数为只读。

有关如何选择硬件开发板并配置其参数的详细信息，请参阅 Hardware Implementation Pane。

### **RF interface** — RF 接口选择 `ADC & DAC 2x2 RF Interface`（默认）| `ADC & DAC 1x1 RF Interface` | `ADC & DAC 4x4 RF Interface` | `ADC & DAC 8x8 RF Interface` | `ADC & DAC 16x16 RF Interface` | `Customize`

指定 RF 通道接口类型。

要选择预定义的 ADC 和 DAC 组合集合，请将此参数设置为 `ADC & DAC 1x1 RF Interface`、`ADC & DAC 2x2 RF Interface`、`ADC & DAC 4x4 RF Interface`、`ADC & DAC 8x8 RF Interface` 或 `ADC & DAC 16x16 RF Interface`。此参数的可用选项因所选硬件开发板而异。要选择所需数量的 DAC 或 ADC 组合，请将此参数设置为 `Customize`。

**示例：** `ADC & DAC 2x2 RF Interface` 指定两个 ADC 和两个 DAC RF 通道接口。

### **Digital interface** — 数字接口选择 `Real`（默认）| `I/Q`

指定数字接口类型。

- `Real` — 支持实数数据
- `I/Q` — 通过使用实部和虚部端口支持复数数据

### DAC

**DAC** 选项卡中的窗格数量和每个窗格中的 DAC 数量取决于所选硬件开发板中的 RFSoC 器件。模块掩码上显示的 tile 和 DAC 指示所选硬件开发板上对应的 tile 和 DAC。例如，如果选择 Xilinx Zynq UltraScale+ RFSoC ZCU111 评估套件，**DAC** 选项卡包含两个窗格（**Tile 0** 和 **Tile 1**），每个窗格包含四个 DAC。对于 ZCU111 开发板，**Tile 0** 中的 **DAC 0**、**DAC 1**、**DAC 2** 和 **DAC 3** 分别对应 DAC tile 228 中的 DAC 0、DAC 1、DAC 2 和 DAC 3。**Tile 1** 中的 **DAC 0**、**DAC 1**、**DAC 2** 和 **DAC 3** 分别对应 DAC tile 229 中的 DAC 0、DAC 1、DAC 2 和 DAC 3。

当您将 **RF interface** 参数设置为 `ADC & DAC 1x1 RF Interface`、`ADC & DAC 2x2 RF Interface`、`ADC & DAC 4x4 RF Interface`、`ADC & DAC 8x8 RF Interface` 或 `ADC & DAC 16x16 RF Interface` 时，tile 和相应 DAC 的选择是预定义的。选择这些预定义选项时，您无法修改 tile 和 DAC 选择。要修改 tile 和 DAC 选择，请将 **RF interface** 参数设置为 `Customize`。

### **Match parameters of all DACs** — 匹配所有 DAC 的参数 `on`（默认）| `off`

选择此参数以将相同的参数值应用于所有选定的 DAC。

清除此参数以为每个选定的 DAC 指定不同的参数值。

#### 依赖项

要启用此参数，请将 **RF interface** 参数设置为 `Customize`。

### **Sample rate (MSPS)** — 数据采样率 `1000`（默认）| scalar

根据所选硬件开发板，在范围内以标量形式指定采样率。单位为兆样本每秒。

下表显示了该模块对支持的 Zynq UltraScale+ RFSoC Gen 1、Gen 2、Gen 3 和 DFE 器件的采样率范围。

| 代 | 器件 | 采样率范围 (MSPS) |
| --- | --- | --- |
| Gen 1 | ZU25DR | [500, 6554] |
| ZU27DR |
| ZU28DR |
| ZU29DR |
| Gen 2 | ZU39DR | [500, 6554] |
| Gen 3 | ZU47DR | [500, 7000] |
| ZU48DR |
| ZU49DR |
| DFE | ZU63DR |
| ZU64DR |
| ZU65DR |
| ZU67DR |

### **Interpolation mode (xN)** — 插值因子 `2`（默认）| `1` | `3` | `4` | `5` | `6` | `8` | `10` | `12` | `16` | `20` | `24` | `40`

指定插值因子。

**注意**

Gen 1 和 Gen 2 器件支持 1、2、4 和 8 的插值因子。Gen 3 和 DFE 器件支持 1、2、3、4、5、6、8、10、12、16、20、24 和 40 的插值因子。

### **Samples per clock cycle** — 每个时钟周期的样本数 `2`（默认）| `1` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16`

指定每个时钟周期的样本数。每个时钟周期的样本数的可用选项因所选硬件开发板和数字接口类型而异。

该模块将流数据宽度计算为 16 x **Samples per clock cycle**。

该模块将流时钟频率计算为 **Sample rate (MSPS)** / **Interpolation mode (xN)** x **Samples per clock cycle**。

### **Mixer type** — 混频器类型 `Bypassed`（默认）| `Coarse` | `Fine`

指定混频器类型。

要使用 `Bypassed`，请将 **Digital interface** 参数设置为 `Real`。

要选择 `Coarse` 或 `Fine`，请将 **Digital interface** 参数设置为 `I/Q`。

### **Mixer mode** — 混频器模式类型 `Real->Real`（默认）| `I/Q->Real`

此参数为只读。

要使用 `Real->Real`，请将 **Digital interface** 参数设置为 `Real`。

要使用 `I/Q->Real`，请将 **Digital interface** 参数设置为 `I/Q`。

### **Mixer frequency** — 混频器频率 `Fs/2`（默认）| `Fs/4` | `-Fs/4`

指定混频器频率。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **Mixer type** 参数设置为 `Coarse`。

### **NCO frequency (GHz)** — NCO 频率 `[0 0]`（默认）| 范围 [–10, 10] 中的 integer

将 NCO 频率值指定为标量或 *m* 元行向量，其中 *m* 是 DAC 的数量。

当您将 **RF interface** 参数设置为 `Customize` 并清除 **Match parameters of all DACs** 参数时，*m* 必须为 1。

该模块根据 NCO 频率和采样率 (*F*s) 推导 DAC 通道的 **Analog Nyquist zone**。

- **Zone 1** — 如果 NCO 频率小于 *F*s/2，则 DAC 输出位于奈奎斯特区 1。在此奈奎斯特区中，该模块支持仿真能力。
- **Zone 2** — 如果 NCO 频率大于 *F*s/2，则 DAC 输出位于奈奎斯特区 2。在此奈奎斯特区中，该模块不支持仿真能力。在仿真中，DAC 将输出围绕指定 NCO 频率在 zone 1 中的折叠频率居中。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **Mixer type** 参数设置为 `Fine`。

### **NCO phase** — NCO 相位 `[0 0]`（默认）| 范围 [–180, 180] 中的 integer

将 NCO 相位指定为标量或 *m* 元行向量，其中 *m* 是 DAC 的数量。

当您将 **RF interface** 参数设置为 `Customize` 并清除 **Match parameters of all DACs** 参数时，*m* 必须为 1。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **Mixer type** 参数设置为 `Fine`。

### **Inverse sinc filter** — 平坦输出响应 `off`（默认）| `on`

选择此参数以将 DAC 的模拟 sinc 输出响应转换为平坦输出响应。

### ADC

**ADC** 选项卡中的窗格数量和每个窗格中的 ADC 数量取决于所选硬件开发板。模块掩码上显示的 tile 和 ADC 指示所选硬件开发板上对应的 tile 和 ADC。例如，如果选择 Xilinx Zynq UltraScale+ RFSoC ZCU111 评估套件，**ADC** 选项卡包含四个窗格（**Tile 0**、**Tile 1**、**Tile 2** 和 **Tile 3**），每个窗格包含两个 ADC。对于 ZCU111 开发板，**Tile 0** 中的 **ADC 0** 和 **ADC 1** 分别对应 ADC tile 224 中的 ADC 0 和 ADC 1。**Tile 1** 中的 **ADC 0** 和 **ADC 1** 分别对应 ADC tile 225 中的 ADC 0 和 ADC 1。**Tile 2** 中的 **ADC 0** 和 **ADC 1** 分别对应 ADC tile 226 中的 ADC 0 和 ADC 1。**Tile 3** 中的 **ADC 0** 和 **ADC 1** 分别对应 ADC tile 227 中的 ADC 0 和 ADC 1。

当您将 **RF interface** 参数设置为 `ADC & DAC 1x1 RF Interface`、`ADC & DAC 2x2 RF Interface`、`ADC & DAC 4x4 RF Interface`、`ADC & DAC 8x8 RF Interface` 或 `ADC & DAC 16x16 RF Interface` 时，tile 和相应 ADC 的选择是预定义的。选择这些预定义选项时，您无法修改 tile 和 ADC 选择。要修改 tile 和 ADC 选择，请将 **RF interface** 参数设置为 `Customize`。

### **Output data as frame** — 将数据作为样本帧输出的选项 `on`（默认）| `off`

选择此参数以将数据作为样本帧输出。清除此参数以将数据作为标量输出。

### **Match parameters of all ADCs** — 匹配所有 ADC 的参数 `on`（默认）| `off`

选择此参数以将相同的参数值应用于所有选定的 ADC。

清除此参数以为每个选定的 ADC 指定不同的参数值。

#### 依赖项

要启用此参数，请将 **RF interface** 参数设置为 `Customize`。

### **Sample rate (MSPS)** — 数据采样率 `1000`（默认）| scalar

根据所选硬件开发板，在范围内以标量形式指定采样率。单位为兆样本每秒。

下表显示了该模块对支持的 Zynq UltraScale+ RFSoC Gen 1、Gen 2、Gen 3 和 DFE 器件的采样率范围。

| 代 | 器件 | 采样率范围 (MSPS) |
| --- | --- | --- |
| Gen 1 | ZU25DR | [1000, 4096] |
| ZU27DR | [1000, 4096] |
| ZU28DR | [1000, 4096] |
| ZU29DR | [500, 2058] |
| Gen 2 | ZU39DR | [500, 2220] |
| Gen 3 | ZU47DR | [1000, 5000] |
| ZU48DR | [1000, 5000] |
| ZU49DR | [500, 2500] |
| DFE | ZU63DR | [500, 2950] — 对于四 ADC tile  [1000, 5900] — 对于双 ADC tile |
| ZU64DR | [500, 2950] — 对于四 ADC tile  [1000, 5900] — 对于双 ADC tile |
| ZU65DR | [1000, 5900] |
| ZU67DR | [500, 2950] — 对于四 ADC tile  [1000, 5900] — 对于双 ADC tile |

### **Decimation mode (xN)** — 抽取因子 `2`（默认）| `1` | `3` | `4` | `5` | `6` | `8` | `10` | `12` | `16` | `20` | `24` | `40`

指定抽取因子。

**注意**

Gen 1 和 Gen 2 器件支持 1、2、4 和 8 的抽取因子。Gen 3 和 DFE 器件支持 1、2、3、4、5、6、8、10、12、16、20、24 和 40 的抽取因子。

### **Samples per clock cycle** — 每个时钟周期的样本数 `2`（默认）| `1` | `3` | `4` | `5` | `6` | `7` | `8` | `10` | `11` | `12` | `14` | `16`

指定每个时钟周期的样本数。每个时钟周期的样本数的可用选项因所选硬件开发板和数字接口类型而异。

该模块将流数据宽度计算为：16 x **Samples per clock cycle**。

该模块将流时钟频率计算为：**Sample rate (MSPS)** / **Decimation mode (xN)** x **Samples per clock cycle**。

### **Mixer type** — 混频器类型 `Bypassed`（默认）| `Coarse` | `Fine`

指定混频器类型。

要使用 `Bypassed`，请将 **Digital interface** 参数设置为 `Real`。

要选择 `Coarse` 或 `Fine`，请将 **Digital interface** 参数设置为 `I/Q`。

### **Mixer mode** — 混频器模式类型 `Real->Real`（默认）| `Real->I/Q`

此参数为只读。

要使用 `Real->Real`，请将 **Digital interface** 参数设置为 `Real`。

要使用 `Real->I/Q`，请将 **Digital interface** 参数设置为 `I/Q`。

### **Mixer frequency** — 混频器频率 `Fs/2`（默认）| `Fs/4` | `-Fs/4`

指定混频器频率。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **Mixer type** 参数设置为 `Coarse`。

### **NCO frequency (GHz)** — NCO 频率 `[0 0]`（默认）| 范围 [–10, 10] 中的 integer

将 NCO 频率值指定为标量或 *m* 元行向量，其中 *m* 是 ADC 的数量。

当您将 **RF interface** 参数设置为 `Customize` 并清除 **Match parameters of all ADCs** 参数时，*m* 必须为 1。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **Mixer type** 参数设置为 `Fine`。

### **NCO phase** — NCO 相位 `[0 0]`（默认）| 范围 [–180, 180] 中的 integer

将 NCO 相位指定为标量或 *m* 元行向量，其中 *m* 是 ADC 的数量。

当您将 **RF interface** 参数设置为 `Customize` 并清除 **Match parameters of all ADCs** 参数时，*m* 必须为 1。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **Mixer type** 参数设置为 `Fine`。

### 高级

**常用参数**

### **Multi tile sync** — 多 tile 同步 `off`（默认）| `on`

选择此参数以启用 MTS。

在生成过程中，Xilinx RF Data Converter 工具向 RF Data Converter 硬件 IP 提供同步时钟以及 ADC 和 DAC 时钟。在 MTS 模式下，这些同步时钟取决于 ADC 和 DAC 采样率。因为 Xilinx RF Data Converter 工具在 MTS 模式下提供一组固定的默认同步时钟，并且仅支持以下采样率：`737.28`、`1474.56`、`1966.08`、`2457.6`、`2949.12`、`3072`、`3932.16`、`4669.44`、`4915.2`、`5898.24` 和 `6144`。

有关 MTS 模式的更多信息，请参阅 AMD 文档中的 Zynq UltraScale+ RFSoC RF Data Converter Gen 1/2/3/DFE LogiCORE IP Product Guide (PG269)。

### **External PLL** — 启用外部 PLL 的选项 `off`（默认）| `on`

选择此参数以启用外部锁相环 (PLL)。

每个 ADC 和 DAC tile 都包含一个内部 PLL。此内部 PLL 与时钟实例一起，根据 ADC 或 DAC 采样率为每个 tile 提供 ADC 和 DAC 时钟。选择此参数时，内部 PLL 禁用，时钟电路直接为每个 tile 提供 ADC 和 DAC 时钟。Xilinx RF Data Converter 工具仅支持以下外部 PLL 时钟频率：`737.28`、`1474.56`、`1966.08`、`2048`、`2457.6`、`2949.12`、`3072`、`3194.88`、`3276.8`、`3686.4`、`3932.16`、`4096`、`4423.68`、`4669.44`、`4915.2`、`5734.4`、`5898.24`、`6144`、`6389.76`、`6400` 和 `6553.6`。

**DAC**

### **Real-time NCO ports** — 为 DAC 添加实时 NCO 端口的选项 `off`（默认）| `on`

选择此参数可为 DAC 添加实时 NCO 端口。您可以使用这些端口在运行时修改 NCO 频率和相位。

根据 MTS 模式选择，按照以下说明修改 DAC 的 NCO 频率和相位。

****Multi tile sync** 为 `off`**

1. 使用 **dacTxChyRealTimeCtrlIn** 端口的 **NCOFrequency**、**NCOPhase** 和 **NCOPhaseReset** 信号，分别设置所需的 NCO 频率、相位和相位复位值。
2. 使用 **dacTxChyRealTimeCtrlIn** 端口的 **NCOUpdateEnable** 信号设置更新使能位，以确定要更新哪些 NCO 频率和相位位。
3. 通过将 **dacTxNCOUpdateReq** 端口设置为 `High`，请求更新 DAC NCO 设置。
4. 保持频率、相位和相位复位值，直到 **dacTxNCOUpdateBusy** 端口保持 `High`。

****Multi tile sync** 为 `on`**

1. 使用您要更新的所有 **dacTxChyRealTimeCtrlIn** 端口的 **NCOFrequency**、**NCOPhase** 和 **NCOPhaseReset** 信号，分别设置所需的 NCO 频率、相位和相位复位值。同时，使用所有 **dacTxChyRealTimeCtrlIn** 端口的 **NCOUpdateEnable** 信号设置更新使能位，以确定要更新哪些 NCO 频率和相位位。
2. 通过将 **dacT0SysrefGating** 端口设置为 `High`，从 `Sysref` 时钟信号禁用 DAC。让此端口保持 `High`，或在更新完成后将其设置为 `Low`。
3. 通过将 **dacT0NCOUpdateReq** 端口设置为 `High`，请求更新 Tile 0 的 DAC NCO 设置。它会将 **dacT0NCOUpdateBusy** 端口的 Bit 1 设置为 `High`。
4. 将 MTS 模式下的所有 **dacTxNCOUpdateReq** 端口设置为 `High`。

   当 MTS 模式下所有 **dacTxNCOUpdateBusy** 端口（**dacT0NCOUpdateBusy** 端口的 Bit 1 除外）均为 `Low` 时，NCO 寄存器写入完成。
5. 通过将 **dacT0SysrefReEnable** 端口设置为 `High`，重新启用 `Sysref` 时钟信号。当 **dacT0NCOUpdateBusy** 端口的 Bit 1 变为 `Low` 时，NCO 更新完成。

有关 NCO 设置的详细信息，请参阅 AMD 文档中的 NCO Frequency Hopping。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **DAC** 选项卡上的 **Mixer type** 参数设置为 `Fine`。

**ADC**

### **Real-time NCO ports** — 为 ADC 添加实时 NCO 端口的选项 `off`（默认）| `on`

选择此参数可为 ADC 添加实时 NCO 端口。您可以使用这些端口在运行时修改 NCO 频率和相位。

根据 MTS 模式选择，按照以下说明修改 ADC 的 NCO 频率和相位。

****Multi tile sync** 为 `off`**

1. 使用 **adcTxChyRealTimeCtrlIn** 端口的 **NCOFrequency**、**NCOPhase** 和 **NCOPhaseReset** 信号，分别设置所需的 NCO 频率、相位和相位复位值。
2. 使用 **adcTxChyRealTimeCtrlIn** 端口的 **NCOUpdateEnable** 信号设置更新使能位，以确定要更新哪些 NCO 频率和相位位。
3. 通过将 **adcTxNCOUpdateReq** 端口设置为 `High`，请求更新 ADC NCO 设置。
4. 保持频率、相位和相位复位值，直到 **adcTxNCOUpdateBusy** 端口保持 `High`。

当 **Multi tile sync** 为 `on` 时，按照以下说明修改 ADC 的 NCO 频率和相位。

****Multi tile sync** 为 `on`**

1. 使用您要更新的所有 **adcTxChyRealTimeCtrlIn** 端口的 **NCOFrequency**、**NCOPhase** 和 **NCOPhaseReset** 信号，分别设置所需的 NCO 频率、相位和相位复位值。同时，使用所有 **adcTxChyRealTimeCtrlIn** 端口的 **NCOUpdateEnable** 信号设置更新使能位，以确定要更新哪些 NCO 频率和相位位。
2. 通过将 **dacT0SysrefGating** 端口设置为 `High`，从 `Sysref` 时钟信号禁用 ADC。让此端口保持 `High`，或在更新完成后将其设置为 `Low`。
3. 通过将 **dacT0NCOUpdateReq** 端口设置为 `High`，请求更新 Tile 0 的 DAC NCO 设置。它会将 **dacT0NCOUpdateBusy** 端口的 Bit 1 设置为 `High`。
4. 将 MTS 模式下的所有 **adcTxNCOUpdateReq** 端口设置为 `High`。

   当 MTS 模式下所有 **adcTxNCOUpdateBusy** 端口（**dacT0NCOUpdateBusy** 端口的 Bit 1 除外）均为 `Low` 时，NCO 寄存器写入完成。
5. 通过将 **dacT0SysrefReEnable** 端口设置为 `High`，重新启用 `Sysref` 时钟信号。当 **dacT0NCOUpdateBusy** 端口的 Bit 1 变为 `Low` 时，NCO 更新完成。

有关 NCO 设置的详细信息，请参阅 AMD 文档中的 NCO Frequency Hopping。

#### 依赖项

要启用此参数，请将 **Digital interface** 参数设置为 `I/Q`，并将 **ADC** 选项卡上的 **Mixer type** 参数设置为 `Fine`。

### **Real-time ports** — 为 ADC 添加实时端口的选项 `off`（默认）| `on`

选择此参数可为 ADC 添加实时端口。选择此参数会启用阈值监测电路，该电路会将 ADC 采样数据与指定的阈值进行比较。

有关实时端口和阈值设置的详细信息，请参阅 AMD 文档中的 Zynq UltraScale+ RFSoC RF Data Converter Gen 1/2/3/DFE LogiCORE IP Product Guide (PG269)。

### **Threshold1 mode** — 第一个阈值的阈值模式 `Sticky over`（默认）| `Sticky under` | `Hysteresis`

选择第一个阈值的阈值模式作为以下选项之一。

- `Sticky over` — 当 ADC 采样数据超过您在 **Threshold1** 参数中设置的阈值时，将阈值状态信号设置为 `High`。阈值状态信号保持 `High`，直到您将 **adcT*`x`*Ch*`y`*RealTimeCtrlIn** 输入总线端口中的 `PLEvent` 信号设置为 `High`。
- `Sticky under` — 当 ADC 采样数据在 **Number of sample(s) below threshold1** 参数中设置的采样数内保持低于您在 **Threshold1** 参数中设置的阈值时，将阈值状态信号设置为 `High`。阈值状态信号保持 `High`，直到您将 **adcT*`x`*Ch*`y`*RealTimeCtrlIn** 输入总线端口中的 `PLEvent` 信号设置为 `High`。
- `Hysteresis` — 当 ADC 采样数据超过上限阈值时，将阈值状态信号设置为 `High`。当 ADC 采样数据在 **Number of sample(s) below threshold1** 参数中指定的采样数内保持低于下限阈值时，将阈值状态信号设置为 `Low`。

#### 依赖项

要启用此参数，请选择 **Real-time ports**。

### **Threshold1** — 第一个阈值的阈值 `0`（默认）| scalar | column vector

指定第一个阈值的阈值。对于 sticky over 阈值模式，此值用作上限阈值。对于 sticky under 阈值模式，此值用作下限阈值。对于 hysteresis 阈值模式，按格式 [*T*lower *T*upper] 指定阈值，其中 *T*lower 是下限阈值，*T*upper 是上限阈值。

#### 依赖项

要启用此参数，请选择 **Real-time ports**。

### **Number of sample(s) below threshold1** — 第一个阈值的低于阈值采样数 `0`（默认）| positive integer

指定第一个阈值的低于阈值的采样数。

#### 依赖项

要启用此参数，请将 **Threshold1 mode** 参数设置为 `Sticky under` 或 `Hysteresis`。

### **Threshold2 mode** — 第二个阈值的阈值模式 `Sticky over`（默认）| `Sticky under` | `Hysteresis`

选择第二个阈值的阈值模式作为以下选项之一。

- `Sticky over` — 当 ADC 采样数据超过您在 **Threshold2** 参数中设置的阈值时，将阈值状态信号设置为 `High`。阈值状态信号保持 `High`，直到您将 **adcT*`x`*Ch*`y`*RealTimeCtrlIn** 输入总线端口中的 `PLEvent` 信号设置为 `High`。
- `Sticky under` — 当 ADC 采样数据在 **Number of sample(s) below threshold2** 参数中设置的采样数内保持低于您在 **Threshold2** 参数中设置的阈值时，将阈值状态信号设置为 `High`。阈值状态信号保持 `High`，直到您将 **adcT*`x`*Ch*`y`*RealTimeCtrlIn** 输入总线端口中的 `PLEvent` 信号设置为 `High`。
- `Hysteresis` — 当 ADC 采样数据超过上限阈值时，将阈值状态信号设置为 `High`。当 ADC 采样数据在 **Number of sample(s) below threshold2** 参数中指定的采样数内保持低于下限阈值时，将阈值状态信号设置为 `Low`。

#### 依赖项

要启用此参数，请选择 **Real-time ports**。

### **Threshold2** — 第二个阈值的阈值 `0`（默认）| scalar | column vector

指定第二个阈值的阈值。对于 sticky over 阈值模式，此值用作上限阈值。对于 sticky under 阈值模式，此值用作下限阈值。对于 hysteresis 阈值模式，按格式 [*T*lower *T*upper] 指定阈值，其中 *T*lower 是下限阈值，*T*upper 是上限阈值。

#### 依赖项

要启用此参数，请选择 **Real-time ports**。

### **Number of sample(s) below threshold2** — 第二个阈值的低于阈值采样数 `0`（默认）| positive integer

指定第二个阈值的低于阈值的采样数。

#### 依赖项

要启用此参数，请将 **Threshold2 mode** 参数设置为 `Sticky under` 或 `Hysteresis`。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2020a 中引入**

### R2025a：DFE 设备支持

该模块现在支持 Zynq UltraScale+ RFSoC DFE 设备。有关支持的设备的完整列表，请参阅 Supported RFSoC Devices for RF Data Converter。

### R2024b：实时端口仿真支持

该模块现在支持 DAC 和 ADC 的实时端口的行为仿真。

### R2023b：仿真支持

该模块现在支持仿真功能。打开模块封装并选择以下仿真模式之一。

- **Pass-through**（默认）— 在此仿真模式下，模块输出与输入相同的数据。当模块计算输出值时，插值、抽取和混频器设置不会影响输入数据。
- **Behavioral** — 在此仿真模式下，当模块计算输出值时，插值、抽取和混频器设置会影响输入数据。

### R2022a：每时钟周期最多 16 个采样、实时 NCO 端口、实时端口以及 ZCU208 板的 I/Q 数字接口支持

- 支持每时钟周期超过八个采样 — 在 R2022a 之前，该模块支持每时钟周期最多八个采样。从 R2022a 开始，该模块支持 DAC 和 ADC 每时钟周期最多 16 个采样。
- 支持实时 NCO 端口 — 该模块现在支持 DAC 和 ADC 的实时 NCO 端口。
- 支持实时端口 — 该模块现在支持 ADC 的实时端口。
- 支持 ZCU208 板的 I/Q 数字接口 — 该模块现在支持 Xilinx Zynq UltraScale+ RFSoC ZCU208 Evaluation Kit 的 I/Q 数字接口。

### R2021a：外部 PLL 和扩展设备支持

从 R2021a 开始，您可以使用外部 PLL 时钟源为每个 tile 提供 ADC 和 DAC 时钟。要使用此功能，请选择 RF Data Converter 模块的 **External PLL** 参数。

从 R2021a 开始，RF Data Converter 模块支持以下几代 Zynq UltraScale+ RFSoC 设备。有关支持的设备的完整列表，请参阅 Supported RFSoC Devices for RF Data Converter。

| 代 | 设备 |
| --- | --- |
| Gen 1 | ZU25DR |
| ZU27DR |
| ZU29DR |
| Gen 2 | ZU39DR |
| Gen 3 | ZU47DR |
| ZU48DR |
| ZU49DR |

### R2020b：RF Data Converter 模块输出有效端口的变化

在 R2020a 中，RF Data Converter 模块有两个有效端口 **adc*`x`*IValid** 和 **adc*`x`*QValid**，分别对应于 I 和 Q 数据端口 **adc***`x`***IData** 和 **adc***`x`***Qdata**。

在 R2020b 中，两个有效输出端口 **adc*`x`*IValid** 和 **adc*`x`*QValid** 被移除，并由一个输出端口 **adc*`x`*Valid** 替换，该端口对应于 I 和 Q 数据端口两者。当您打开一个包含 RF Data Converter 模块的模型，该模块是在 R2020a 中创建且其 **Digital interface** 参数设置为 `I/Q` 时，模块的输出端口可能未正确连接。

在这种情况下，请手动检查并更正模型中的端口连接，以便继续。

## 描述

为硬件逻辑提供 RF 数据路径接口

RF Data Converter 模块为硬件逻辑提供 RF 数据路径接口。在生成时，SoC Builder 工具将模块参数映射到硬件上的 RF Data Converter IP。

该模块由插值和抽取滤波器、复数混频器、模数转换器（ADC）和数模转换器（DAC）组成。

- 插值滤波器按指定的插值因子对输入信号进行上采样。使用 **Interpolation mode (xN)** 参数指定插值因子。
- 抽取滤波器按指定的抽取因子对输入信号进行下采样。使用 **Decimation mode (xN)** 参数指定抽取因子。
- 复数混频器将输入信号的中心频率搬移到指定的载波频率。使用 **Mixer frequency** 和 **NCO frequency (GHz)** 参数指定载波频率。

该模块支持最多 16 个 ADC 和 16 个 DAC 数据路径连接到硬件逻辑。在 **Behavioral** 仿真模式下，您可以仿真插值和抽取滤波器以及复数混频器。

该模块支持 Zynq® UltraScale+™ RFSoC Gen 1、Gen 2、Gen 3 和 DFE 设备。有关支持的设备的完整列表，请参阅 Supported RFSoC Devices for RF Data Converter。有关特定 Zynq UltraScale+ RFSoC 设备信息，请参阅 AMD® 网站上的 Zynq UltraScale+ RFSoC Product Information。
