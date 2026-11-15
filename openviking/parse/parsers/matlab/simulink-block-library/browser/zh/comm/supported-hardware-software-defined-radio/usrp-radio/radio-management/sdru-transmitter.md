---
type: simulink-block
title: 'SDRu Transmitter'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Supported Hardware – Software-Defined Radio / USRP Radio / Radio Management'
documentation_page: 'sdrutransmitter'
documentation_source_path: 'usrpradio/ug/sdrutransmitter.html'
language: zh-CN
chinese_source: worker-translation
---

# SDRu Transmitter

## 端口

### 输入

### **data** — 输入数据列向量 | 矩阵

发送到无线电硬件的输入数据，指定为列向量或矩阵。对于单通道无线电，**data** 是列向量。对于多通道无线电，**data** 是矩阵，其中每一列包含一个通道的数据。对于 `double` 或 `single` 精度数据，**data** 的值范围为 `[-1 1]`；对于 `int16` 数据，范围为 `[-32768, 32767]`。

#### 依赖关系

要指定输出数据类型，请使用 **Output data type** 参数。

**数据类型：** `int16` | `single` | `double`
**复数支持：** 是

### **fc** — 中心频率设置正标量

中心频率设置，以 Hz 为单位，指定为正标量。

**示例：**
`88.9e6` 将发射机调谐到 88.9 MHz 的中心频率。

#### 依赖关系

要启用此端口，请将 **Source of center frequency** 参数设置为 `Input Port`。

**数据类型：** `double`

### **LO offset** — 本地振荡器偏移标量

本地振荡器 (LO) 偏移，以 Hz 为单位，指定为标量。

**示例：**
`10` 将 LO 偏移设置为 10 Hz。

#### 依赖关系

要启用此端口，请将 **Source of LO offset** 参数设置为 `Input Port`。

**数据类型：** `double`

### **gain** — 发射机增益设置 标量 | 向量

发射机增益设置，以 dB 为单位，指定为标量或向量。此增益的有效范围取决于 USRP 设备的 RF 子板。

发射机增益设置包含 USRP 硬件的模拟和数字发射机组合增益。

- 对于单通道，请将增益值指定为标量，单位为 dB。
- 对于使用相同增益值的多个通道，请将增益指定为标量，单位为 dB。增益通过标量扩展设置。
- 对于使用不同增益的多个通道，请将这些值指定为向量，例如 `[5 12]`。向量的第 *N* 个元素应用于由 **Channel mapping** 指定的第 *N* 个通道。

**示例：**
`10` 将发射机增益级别设置为 10 dB。

#### 依赖关系

要启用此端口，请将 **Source of gain** 参数设置为 `Input Port`。

**数据类型：** `double`

### 输出

### **underrun** — 数据不连续标志 `0` | `1`

数据不连续标志，返回为以下值之一。

- `0` — 数据样本未丢失。
- `1` — 数据样本丢失。

使用此端口作为诊断工具，以确定 SDRu Transmitter 模块的实时运行情况。如果您的模型未实时运行，可以调整参数以减少传输的样本数。要接近或实现实时性能，可以增大插值因子。有关详细信息，请参阅检测欠载和过载。

#### 依赖关系

要启用此端口，请选中 **Enable overrun output port**。

### **refLocked** — USRP 无线电锁定到 10 MHz 时钟信号的状态 `0` | `1`

USRP 无线电锁定到 10 MHz 时钟信号的状态，返回为以下布尔值之一。

- `0` — USRP 无线电未锁定到外部时钟源或全球定位系统驯服振荡器 (GPSDO) 的 10 MHz 时钟信号。
- `1` — USRP 无线电锁定到外部时钟源或 GPSDO 的 10 MHz 时钟信号。

#### 依赖关系

要启用此端口，请选中 **Enable ref\_locked output port** 参数。

**数据类型：** `Boolean`

### **gpsLocked** — GPSDO 锁定到 GPS 星座的状态 `0` | `1`

GPSDO 锁定到 GPS 星座的状态，返回为以下布尔值之一。

- `0` — GPSDO 未锁定到 GPS 星座。
- `1` — GPSDO 锁定到 GPS 星座。

#### 依赖关系

要启用此端口，请选中 **Enable gps\_locked output port** 参数。

**数据类型：** `Boolean`

## 参数

设置模块参数值时，SDRu Transmitter 模块首先检查这些值是否具有正确的数据类型。即使这些值通过了这些检查，这些值仍可能超出无线电硬件的范围。在这种情况下，无线电硬件会将实际值设置为尽可能接近指定值。当您下次通过点击 **Info** 将模块与无线电硬件同步时，会打开一个对话框，显示实际值以及其他无线电信息。

如果参数被列为可调，则可以在仿真期间更改其值。

### 无线电连接

### **Platform** — 要配置的无线电 `N200/N210/USRP2` (默认) | `B200` | `B210`

要配置的无线电，指定为以下选项之一。

- `N200/N210/USRP2`
- `B200`
- `B210`

### **IP address** — 无线电硬件的 IP 地址 `192.168.10.2` (默认) | 点分四段表达式

无线电硬件的 IP 地址，指定为点分四段表达式。

此参数必须与硬件设置期间分配的无线电硬件物理 IP 地址匹配。请参阅 Guided USRP Radio Support Package Hardware Setup。如果使用非默认 IP 地址配置无线电硬件，请相应地更新 **IP address**。

**IP address** 列表显示连接到主机的 USRP 设备的 IP 地址。要指定另一个已知的点分四段 IP 地址，请直接在此字段中输入。

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `N200/N210/USRP2`。

### **Serial number** — 无线电硬件的序列号 空字符向量 (默认) | 字符向量

无线电硬件的序列号，指定为字符向量。

此参数必须与硬件设置期间分配的无线电硬件序列号匹配。请参阅 Guided USRP Radio Support Package Hardware Setup。如果使用非默认序列号配置无线电硬件，请相应地更新 **Serial number**。

**Serial number** 列表显示连接到主机的 USRP 设备的序列号。

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `B200` 或 `B210`。

### **Refresh Device List** — 刷新已连接设备列表 按钮

刷新所有已连接设备的列表，以更新 **IP address** 或 **Serial number** 列表。更新后的列表会保留在选中 **Refresh Device List** 之前处于焦点的值，即使具有该设置的设备已断开连接。

### **Info** — 提供有关设备的信息 按钮

提供有关与 **IP address** 或 **Serial number** 关联的 **Platform** 的信息。**IP address** 适用于 N 系列，**Serial number** 适用于 B 系列设备。选中 **Info** 按钮时，会打开一个新对话框，其中包含有关指定设备的信息。

### 无线电属性

### **Channel mapping** — 无线电或捆绑无线电的通道输出映射 `1` (默认) | 整数 | 向量

无线电或捆绑无线电的通道输出映射，指定为正整数标量或向量。此表显示了各种无线电平台的有效值。

| Platform 值 | **Channel mapping** 值 |
| --- | --- |
| `N200/N210/USRP2` | 当 **IP address** 包含 *N* 个 IP 地址时：1-by-*N* 行向量 |
| `B200` | `1` |
| `B210` | `1`、`2` 或 `[1 2]` |

当 **Channel Mapping** 为标量、`1` 或 `2` 时，无线电以单输入单输出 (SISO) 模式运行。当 **Channel Mapping** 为向量时，无线电以多输入多输出 (MIMO) 模式运行。

当 **IP Address** 包含多个 IP 地址时，由 **Channel Mapping** 定义的通道先按 IP 地址在列表中出现的顺序排序，然后按同一无线电内的通道顺序排序。

例如，如果 **Platform** 为 `"N200/N210/USRP2"` 且 **IP Address** 为 `"192.168.20.2, 192.168.10.3"`，则 **Channel Mapping** 必须为 `[1 2]`。捆绑无线电的通道 1 指 IP 地址为 192.168.20.2 的无线电的通道 1。捆绑无线电的通道 2 指 IP 地址为 192.168.10.3 的无线电的通道 1。

**数据类型：** `double`

### **Source of center frequency** — 选择中心频率的来源 `Dialog` (默认) | `Input port`

选择中心频率的来源，指定为：

- `Dialog` — 使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input port` — 使用 **fc** 输入端口设置中心频率。

### **Center frequency (Hz)** — RF 中心频率 `2.45e9` (默认) | 非负有限标量 | 非负有限标量向量

RF 中心频率，以 Hz 为单位，指定为非负有限标量或非负有限标量向量。此参数的有效范围取决于 USRP 设备的 RF 子板。

- 对于单通道 (SISO)，请将中心频率值指定为标量。
- 对于使用相同中心频率的多通道 (MIMO)，请将中心频率值指定为标量。中心频率通过标量扩展设置。
- 对于使用不同中心频率的多通道 (MIMO)，请将这些值指定为向量。向量的第 *i* 个元素应用于由 **Channel mapping** 指定的第 *i* 个通道。

**注意**

对于 MIMO 场景，USRP B210 无线电的中心频率必须为标量。不能将频率指定为向量。

#### 依赖关系

要启用此参数，请将 **Source of center frequency** 设置为 `Dialog`。

**数据类型：** `double`

### **Source of LO offset** — 选择 LO 偏移的来源 `Dialog` (默认) | `Input port`

选择 LO 偏移的来源，指定为：

- `Dialog` — 使用 **LO offset (Hz)** 参数设置 LO 偏移。
- `Input port` — 使用 **LO offset** 输入端口设置 LO 偏移。

### **LO offset (Hz)** — 本地振荡器偏移频率 `0` (默认) | 标量 | 向量

本地振荡器的偏移频率，指定为标量或向量。此参数的有效范围取决于 USRP 设备的 RF 子板。

此图显示本地振荡器偏移会影响 USRP 硬件中的中频中心频率。它不影响发射中心频率。

- *f*LO offset 是本地振荡器偏移频率。
- *f*center 表示模块指定的中心频率。

要使中心频率远离 USRP 硬件产生的干扰或谐波，请使用 LO 偏移。

- 对于单通道 (SISO)，请将 LO 偏移值指定为标量。
- 对于多通道 (MIMO)，LO 偏移必须为零。此限制是由于 UHD 限制。可以将 LO 偏移指定为标量或向量。

#### 依赖关系

要启用此参数，请将 **Source of LO offset** 设置为 `Dialog`。

### **Source of gain** — 选择增益的来源 `Dialog` (默认) | `Input port`

选择增益的来源，指定为：

- `Dialog` — 使用 **Gain (dB)** 参数指定增益。
- `Input port` — 使用 **gain** 输入端口指定增益。

### **Gain (dB)** — 发射机增益 `8` (默认) | 标量 | 向量

发射机增益，以 dB 为单位，指定为标量或向量。此增益的有效范围取决于 USRP 设备的 RF 子板。

根据 **Channel Mapping** 配置设置增益值：

- 对于单通道 (SISO)，请将增益指定为标量。
- 对于使用相同增益值的多通道 (MIMO)，请将增益指定为标量。增益通过标量扩展设置。
- 对于使用不同增益的多通道 (MIMO)，请将这些值指定为行向量。向量的第 *i* 个元素应用于由 **Channel Mapping** 指定的第 *i* 个通道。

#### 依赖关系

要启用此参数，请将 **Source of gain** 设置为 `Dialog`。

**数据类型：** `double`

### **PPS source** — PPS 信号源 `Internal` (默认) | `External` | `GPSDO`

每秒脉冲 (PPS) 信号源，指定为以下值之一。

- `Internal` — 使用 USRP 无线电的内部 PPS 信号。
- `External` — 使用来自外部信号发生器的 PPS 信号。
- `GPSDO` — 使用来自 GPSDO 的 PPS 信号。

要同步捆绑无线电所有通道的时间，您可以：

- 向所有捆绑无线电提供公共外部 PPS 信号，并将此参数设置为 `External`。
- 通过将此参数设置为 `GPSDO`，使用 USRP 无线电上可用的 GPSDO 的 PPS 信号。

要将 USRP 时间同步到有效 GPS 时间，请将此参数设置为 `GPSDO`。如果 GPSDO 在仿真开始时未锁定到 GPS 星座，还必须启用 **Ensure sync GPS time** 参数。

### **Enable gps\_locked output port** — 启用 GPSDO 到 GPS 星座锁定状态的选项 `off` (默认) | `on`

选中此参数以启用 **gpsLocked** 输出端口，该端口指示 GPSDO 锁定到 GPS 星座的状态。

#### 依赖关系

要启用此参数，请将 **PPS source** 参数设置为 `GPDSO`。

### **Ensure sync GPS time** — 确保 GPS 时间同步的选项 `off` (默认) | `on`

选中此参数以确保 USRP 无线电时间同步到有效 GPS 时间。

选中此参数时，模块检查 GPSDO 的锁定状态。当 GPSDO 锁定到 GPS 星座时，模块将 USRP 无线电时间设置为有效 GPS 时间。

#### 依赖关系

要启用此参数，请将 **PPS source** 参数设置为 `GPSDO`。

### **Clock source** — 时钟源 `Internal` (默认) | `External` | `GPSDO`

时钟源，指定为以下值之一。

- `Internal` — 使用 USRP 无线电的内部时钟信号。
- `External` — 使用来自外部时钟发生器的 10 MHz 时钟信号。
- `GPSDO` — 使用来自 GPSDO 的 10 MHz 时钟信号。

对于 B 系列无线电，外部时钟端口标记为 *10 MHz*。对于 USRP N2xx 和 USRP2 无线电，外部时钟端口标记为 *REF IN*。

要同步捆绑无线电所有通道的频率，您可以：

- 向所有捆绑无线电提供公共外部 10 MHz 时钟信号，并将此参数设置为 `External`。
- 将来自每个 GPSDO 的 10 MHz 时钟信号提供给相应的无线电，并将此参数设置为 `GPSDO`。

### **Enable ref\_locked output port** — 启用 USRP 无线电到 10 MHz 时钟信号锁定状态的选项 `off` (默认) | `on`

选中此参数以启用 **refLocked** 输出端口，该端口指示 USPR 无线电锁定到 10 MHz 时钟信号的状态。

#### 依赖关系

要启用此参数，请将 **Clock source** 参数设置为 `External` 或 `GPDSO`。

### **Master clock rate (Hz)** — 主时钟速率 标量

主时钟速率，以 Hz 为单位指定为标量。主时钟速率是 A/D 和 D/A 时钟速率。此属性的有效值范围取决于所连接的无线电平台。

| Platform 值 | 支持的 **Master clock rate (Hz)** 值 |
| --- | --- |
| `N200/N210/USRP2` | `100e6`（只读）。 |
| `B200` 或 `B210` | `5e6` 到 `61.44e6` 范围内的标量。将 B210 与多个通道一起使用时，时钟速率不得高于 `30.72e6` Hz。此限制是 B210 无线电仅在使用双通道操作时的硬件限制。默认值为 `32e6`。 |

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `B200` 或 `B210`。

**数据类型：** `double`

### **Interpolation factor** — SDRu Transmitter 的插值因子 `512` (默认) | 整数

SDRu 发射机的插值因子，指定为范围 `[1,1024]` 中的整数，具体限制取决于您使用的无线电。

| 插值因子 | B 系列 | N2xx 系列 |
| --- | --- | --- |
| `1` | 有效 | 无效 |
| `2` | 有效 | 仅当将 `TransportDataType` 属性设置为 `"int8"` 时有效。 |
| `3` | 有效 | 无效 |
| 4 到 128 的奇整数 | 有效 | 有效 |
| 4 到 128 的偶整数 | 有效 | 有效 |
| 128 到 256 的偶整数 | 有效 | 有效 |
| 256 到 512 的 4 的整数倍 | 有效 | 有效 |
| 512 到 1024 的 8 的整数倍 | 无效 | 无效 |

无线电在将复基带信号上变频为中频 (IF) 信号时使用插值因子。

### **Enable time trigger** — 启用定时发射和接收的选项 off (默认) | on

启用定时发射和接收的选项。要使无线电在指定时间后发射或接收数据，请选中 **Enable time trigger**。

选中 **Enable time trigger** 参数时，您可以：

- 在 **Trigger time** 参数指定的时间之后发射或接收。
- 如果将 **PPSSource** 参数设置为 `GPSDO`，则在 **Trigger time** 参数中指定的 GPS 时间发射或接收。
- 在 **Trigger time** 参数指定的时间之后同时发射和接收。

### **Trigger time** — 触发时间（秒） `5` (默认) | 非负标量

触发时间（以秒为单位），指定为非负标量。指定您希望无线电在该时间之后发射或接收数据的触发时间。**Trigger time** 值必须大于当前 USRP 无线电时间。

当将 **PPS Source** 参数设置为 `GPSDO` 时，请将 **Trigger time** 参数指定为无线电发射和接收数据的确切 GPS 时间（秒）。

**注意**

对于基于 AD936x 的 B2xx USRP 无线电，可以预期在指定的触发时间与发射或接收开始之间存在一致的延迟。

#### 依赖关系

要启用此参数，请选中 **Enable trigger time** 参数。

### **Enable MIMO cable sync** — 启用 MIMO 电缆同步的选项 off (默认) | on

*自 R2024b 起*

启用 MIMO 电缆同步的选项。要启用 MIMO 电缆同步，请选中 **Enable MIMO cable sync**。

选中 **Enable MIMO cable sync** 参数时，您可以：

- 同步两个 N200/N210 USRP 无线电。
- 跨多个通道发射或接收频率、相位和时间同步的数据。
- 在两个 USRP N200/N210 无线电之间共享以太网。

要构建更大的 MIMO 系统（最高 16 x 16），请将 **PPS Source** 参数设置为 `"External"` 或 `"GPSDO"`，并将 **Clock Source** 参数设置为 `"External"`。

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `N200/N210/USRP2`。

### 数据

### **Baseband sample rate (Hz)** — 输出信号的基带采样率 标量

此参数为只读。

输出信号的基带采样率，以 Hz 为单位，指定为标量。

此参数显示根据 **Master clock rate (Hz)** 和 **Interpolation factor** 参数值计算出的基带采样率。此计算使用公式 **Baseband sample rate** = Master clock rate/Interpolation factor。如果在仿真期间更改 **Interpolation factor**，则模块会更改硬件数据速率，但不会更改 Simulink 采样时间。

有关采样时间的详细信息，请参阅什么是采样时间？(Simulink)。

**数据类型：** `double`

### **Transport data type** — 传输数据类型 `int16` (默认) | `int8`

传输数据类型，指定为：

- `int16` — 使用 16 位传输。比 8 位传输实现更高精度。
- `int8` — 使用 8 位传输。使用的量化步长比 16 位传输大 256 倍，并且传输数据速率大约比 16 位传输快两倍。

将传输数据速率数据类型指定为 `int16` 时，会为同相分量分配 16 位，为正交分量分配 16 位，从而使每个复传输数据样本为 32 位。

### **Enable underrun output port** — 启用 underrun 输出端口的选项 off (默认) | on

要测量传输期间丢失的样本数，请选中此参数。

如果您的模型未实时运行，可以调整参数以减少传输的样本数。要接近或实现实时性能，可以增大插值因子。有关详细信息，请参阅检测欠载和过载。

### **Enable burst mode** — 启用突发模式的选项 off (默认) | on

启用突发模式的选项。要生成一组连续帧而不会向无线电产生过载或欠载，请选中 **Enable burst mode**。启用突发模式有助于仿真无法实时运行的模型。

启用突发模式后，请使用 **Number of frames in burst** 参数指定所需数量的连续数据。有关详细信息，请参阅检测欠载和过载。

### **Number of frames in burst** — 连续突发中的帧数 `100` (默认) | 非负整数

连续突发中的帧数，指定为非负整数。

#### 依赖关系

要启用此参数，请选中 **Enable burst mode**。

**数据类型：** `double`

## 所属库

Communications Toolbox Support Package for USRP Radio

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

### R2024b：使用共享 MIMO 电缆同步 N2xx 系列 USRP 无线电

使用 MIMO 电缆捆绑两个 N2xx 系列 USRP 无线电，以共享时钟参考、定时参考和以太网接口。要使用捆绑的 N2xx 无线电同步多通道发射和接收，请在 Simulink 的 SDRu Transmitter 和 SDRu Receiver 模块中使用 **Enable MIMO Cable Sync** 参数。

### R2024a：对 N3xx 和 X3xx 系列无线电设备的支持已移至 Wireless Testbench

对 NI USRP N3xx 和 X3xx 系列无线电设备的支持已从 Communications Toolbox Support Package for USRP Radio 移至 Wireless Testbench Support Package for NI USRP Radios。

要将这些无线电配置为与 Wireless Testbench 一起使用，请参阅 Install Support Package for NI USRP Radios (Wireless Testbench)。

### R2023b：增强了对 SDRu 模块中时间触发的支持

现在，您可以指定触发时间，以便在指定时间对 USRP 无线电进行数据发射和接收。此属性在 SDRu Transmitter 和 SDRu Receiver Simulink 模块中可用。

### R2020a：interp 输入端口已移除

从 R2020a 开始，SDRu Transmitter 模块移除了 **interp** 输入端口。不能通过输入端口为该模块设置插值因子值。请改用 **Interpolation factor** 参数。

### R2020a：Sample time 参数已移除

从 R2020a 开始，SDRu Transmitter 模块移除了 **Sample time** 参数。请改用只读 **Baseband sample rate (Hz)** 参数。此参数显示根据 **Master clock rate (Hz)** 和 **Interpolation factor** 参数计算出的基带采样率。

## 描述

将数据发送到 USRP 设备

SDRu Transmitter 模块支持 Simulink® 与通用软件无线电外设 (USRP™) 设备之间的通信，从而支持各种软件定义无线电应用的仿真和开发。SDRu Transmitter 模块和 USRP 板必须位于同一以太网子网中。

SDRu Transmitter 模块接受来自 Simulink 的列向量或矩阵输入信号，并使用 Ettus Research™ 的通用硬件驱动程序 (UHD™) 将信号和控制数据传输到 USRP 板。SDRu Transmitter 模块是一个 Simulink 接收器，它从模型获取数据并将其发送到 USRP 板。对此模块的首次调用可能包含瞬态值，在这种情况下，生成的数据包包含未定义数据。

此框图说明了 Simulink、SDRu Transmitter 和 Receiver 模块以及 USRP 硬件如何接口。

要通过空中传输无线电信号，请将 Simulink 中生成的信号传递到 SDRu transmitter 模块。发射机模块将信号转发到无线电硬件。要通过空中接收无线电信号，请使用 SDRu receiver 模块。接收器模块将从无线电硬件接收的信号转发到 Simulink 中进行后处理。

如果您的计算机未连接到任何 USRP 硬件，您仍可使用此模块开发可传播采样时间和数据类型信息的模型。要传播此信息，请选择 **Simulation** >> **Update diagram**。

有关与此模块接口的 USRP 硬件产品的信息，请参阅 Ettus Research 网站。

此图标显示所有端口，包括可选端口：带有所有端口的 SDRu transmitter 模块

**注意**

从 R2024a 开始，使用此 Simulink 模块所需的 MathWorks® 产品和支持包取决于您的无线电设备。

| 无线电设备 | 所需的 MathWorks 产品 | 支持包安装 |
| --- | --- | --- |
| USRP2™  USRP N200, N210  USRP B200, B210 | - Communications Toolbox™ Support Package for USRP Radio | 安装 Communications Toolbox Support Package for USRP Radio |
| USRP E320 *(自 R2025a 起)*  USRP N300, N310, N320, N321  USRP X300, X310  USRP X410 *(自 R2025a 起)* | - Wireless Testbench™ - Wireless Testbench Support Package for NI™   USRP Radios | 安装 Support Package for NI USRP Radios (Wireless Testbench) |

有关如何将此 Simulink 模块与 Wireless Testbench Support Package for NI USRP Radios 支持的无线电设备一起使用的详细信息，请参阅 SDRu Transmitter (Wireless Testbench)。
