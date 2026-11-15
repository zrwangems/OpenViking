---
type: simulink-block
title: 'SDRu Receiver'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Supported Hardware – Software-Defined Radio / USRP Radio / Radio Management'
documentation_page: 'sdrureceiver'
documentation_source_path: 'usrpradio/ug/sdrureceiver.html'
language: zh-CN
chinese_source: worker-translation
---

# SDRu Receiver

## 端口

### 输入

### **fc** — 中心频率设置正标量

中心频率设置，以 Hz 为单位，指定为正标量。

**示例：**
`88.9e6` 将接收机调谐到中心频率 88.9 MHz。

#### 依赖关系

要启用此端口，请将 **Source of center frequency** 设置为 `Input Port`。

**数据类型：** `double`

### **LO offset** — 本振偏移标量

本地振荡器 (LO) 偏移，以 Hz 为单位，指定为标量。

**示例：**
`10` 将 LO 偏移设置为 10 Hz。

#### 依赖关系

要启用此端口，请将 **Source of LO offset** 设置为 `Input Port`。

**数据类型：** `double`

### **gain** — 接收机增益设置 标量 | 向量

接收机增益设置，以 dB 为单位，指定为标量或向量。该增益的有效范围取决于 USRP 设备的 RF 子板。

#### 依赖关系

要启用此端口，请将 **Source of gain** 设置为 `Input Port`。

**数据类型：** `double`

### 输出

### **data** — 复数值输出数据向量

从无线电硬件接收的输出数据，以复数值向量形式返回。复数输出数据值的范围为 -1 到 1。

#### 依赖关系

要指定基础数据类型，请使用 **Output data type** 参数。

**数据类型：** `int8` | `int16` | `single` | `double`
**复数支持：** 是

### **length** — 接收数据长度非负整数

接收数据的长度，以非负整数形式返回。此输出端口提供从 USRP 无线电接收的样本数。

#### 依赖关系

要启用此端口，请选择 **Enable data length output port** 参数。

### **overrun** — 数据不连续标志 `0` | `1`

数据不连续标志，返回：

- `0` — 未丢失数据样本。
- `1` — 丢失数据样本。

将此端口用作诊断工具，以确定 SDRu Receiver 模块的实时操作情况。如果您的模型未实时运行，可以调整参数以减少传输的样本数。要接近或实现实时性能，可以降低基带采样率或增大抽取因子。有关详细信息，请参阅 Detect Underruns and Overruns。

#### 依赖关系

要启用此端口，请选择 **Enable overrun output port** 参数。

**数据类型：** `Boolean`

### **refLocked** — USRP 无线电到 10 MHz 时钟信号的锁定状态 `0` | `1`

USRP 无线电到 10 MHz 时钟信号的锁定状态，返回为以下布尔值之一。

- `0` — USRP 无线电未锁定到外部时钟源或 GPS 驯服振荡器 (GPSDO) 的 10 MHz 时钟信号。
- `1` — USRP 无线电锁定到外部时钟源或 GPSDO 的 10 MHz 时钟信号。

#### 依赖关系

要启用此端口，请选择 **Enable ref\_locked output port** 参数。

**数据类型：** `Boolean`

### **gpsLocked** — GPSDO 到 GPS 星座的锁定状态 `0` | `1`

GPSDO 到 GPS 星座的锁定状态，返回为以下布尔值之一。

- `0` — GPSDO 未锁定到 GPS 星座。
- `1` — GPSDO 锁定到 GPS 星座。

#### 依赖关系

要启用此端口，请选择 **Enable gps\_locked output port** 参数。

**数据类型：** `Boolean`

### **timeStamps** — 每个接收样本的时间戳列向量

每个接收样本的时间戳，以列向量形式返回。**timeStamps** 输出的长度等于接收数据输出 **data** 的长度。

- 要从 USRP 无线电获取每个接收样本的 GPS 时间戳，请将 **PPS Source** 参数设置为 `GPSDO`。
- 要从捆绑无线电获取每个接收样本的时间戳，请将 **PPS Source** 参数设置为 `GPSDO` 或 `External`。

#### 依赖关系

要启用此端口，请选择 **Enable timestamps output port** 参数。

## 参数

设置模块参数值时，SDRu Receiver 模块首先检查这些值是否具有正确的数据类型。即使这些值通过了这些检查，它们对于无线电硬件仍可能超出范围。在这种情况下，无线电硬件会将实际值设置为尽可能接近指定值。当您下次通过点击 **Info** 使模块与无线电硬件同步时，会打开一个对话框，显示实际值以及其他无线电信息。

如果某个参数被列为可调，则可以在仿真期间更改其值。

### 无线电连接

### **Platform** — 要配置的无线电 `N200/N210/USRP2`（默认） | `B200` | `B210`

要配置的无线电，指定为以下选项之一。

- `N200/N210/USRP2`
- `B200`
- `B210`

### **IP address** — 无线电硬件的 IP 地址 `192.168.10.2`（默认） | 点分四段表达式

无线电硬件的 IP 地址，指定为点分四段表达式。

此参数必须与硬件设置期间分配的无线电硬件的物理 IP 地址匹配。请参阅 Guided USRP Radio Support Package Hardware Setup。如果使用非默认 IP 地址配置无线电硬件，请相应地更新 **IP address**。

**IP address** 列表显示连接到主机的 USRP 设备的 IP 地址。要指定另一个已知的点分四段 IP 地址，请直接在此字段中输入。

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `N200/N210/USRP2`。

### **Serial number** — 无线电硬件的序列号 空字符向量（默认） | 字符向量

无线电硬件的序列号，指定为字符向量。

此参数必须与硬件设置期间分配的无线电硬件的序列号匹配。请参阅 Guided USRP Radio Support Package Hardware Setup。如果使用非默认序列号配置无线电硬件，请相应地更新 **Serial number**。

**Serial number** 列表显示连接到主机的 USRP 设备的序列号。

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `B200` 或 `B210`。

### **Refresh Device List** — 刷新已连接设备列表按钮

刷新所有已连接设备的列表，以更新 **IP address** 或 **Serial number** 列表。更新后的列表会保留在选择 **Refresh Device List** 之前处于焦点的值，即使具有该设置的设备已断开连接。

### **Info** — 提供有关设备信息的按钮

提供与 **IP address** 或 **Serial number** 关联的 **Platform** 的信息。**IP address** 适用于 N 系列，**Serial number** 适用于 B 系列设备。当您选择 **Info** 按钮时，会打开一个新对话框，其中包含有关指定设备的信息。

### 无线电属性

### **Channel mapping** — 无线电或捆绑无线电的通道输出映射 `1`（默认） | 整数 | 向量

无线电或捆绑无线电的通道输出映射，指定为正整数标量或向量。此表显示各种无线电平台的有效值。

| Platform Value | **Channel mapping** 值 |
| --- | --- |
| `N200/N210/USRP2` | 当 **IP address** 包含 *N* 个 IP 地址时：1×*N* 行向量 |
| `B200` | `1` |
| `B210` | `1`、`2` 或 `[1 2]` |

当 **Channel Mapping** 为标量、`1` 或 `2` 时，无线电以单输入单输出 (SISO) 模式工作。当 **Channel Mapping** 为向量时，无线电以多输入多输出 (MIMO) 模式工作。

当 **IP Address** 包含多个 IP 地址时，由 **Channel Mapping** 定义的通道首先按 IP 地址在列表中出现的顺序排序，然后按同一无线电内的通道顺序排序。

例如，如果 **Platform** 为 `"N200/N210/USRP2"` 且 **IP Address** 为 `"192.168.20.2, 192.168.10.3"`，则 **Channel Mapping** 必须为 `[1 2]`。捆绑无线电的通道 1 指的是 IP 地址为 192.168.20.2 的无线电的通道 1。捆绑无线电的通道 2 指的是 IP 地址为 192.168.10.3 的无线电的通道 1。

**数据类型：** `double`

### **Receive antenna port** — 接收天线端口 `RX2`（默认） | `TX/RX`

*自 R2025a 起*

接收机天线端口，指定为以下值之一：

- `'TX/RX'`— 使用无线电的 `TX/RX` 天线端口进行接收。
- `'RX2'`— 使用无线电的 `RX2` 天线端口进行接收。

**注意**

- 此参数适用于除仅发送和仅接收子板之外的所有子板。
- 当发送和接收同时发生时，无线电会自动将接收从 `TX/RX` 端口切换到 `RX2` 端口。您必须检查板上的 LED 以确定当前接收端口。
- 当您在 **Channel mapping** 参数中配置多个通道时，模块会将 **Receive antenna port** 参数中指定的值应用于所有通道。

### **Source of center frequency** — 选择中心频率来源 `Dialog`（默认） | `Input port`

选择中心频率来源，指定为：

- `Dialog` — 使用 **Center frequency (Hz)** 参数设置中心频率。
- `Input port` — 使用 **fc** 输入端口设置中心频率。

### **Center frequency (Hz)** — RF 中心频率 `2.45e9`（默认） | 非负有限标量 | 非负有限标量向量

RF 中心频率，以 Hz 为单位，指定为非负有限标量或非负有限标量向量。此参数的有效范围取决于 USRP 设备的 RF 子板。

- 对于单通道 (SISO)，将中心频率值指定为标量。
- 对于使用相同中心频率的多通道 (MIMO)，将中心频率值指定为标量。中心频率通过标量扩展设置。
- 对于使用不同中心频率的多通道 (MIMO)，在向量中指定这些值。向量的第 *i* 个元素应用于由 **Channel mapping** 指定的第 *i* 个通道。

**注意**

对于 MIMO 场景，USRP B210 无线电的中心频率必须为标量。不能将频率指定为向量。

#### 依赖关系

要启用此参数，请将 **Source of center frequency** 设置为 `Dialog`。

**数据类型：** `double`

### **Source of LO offset** — 选择 LO 偏移来源 `Dialog`（默认） | `Input port`

选择 LO 偏移来源，指定为：

- `Dialog` — 使用 **LO offset (Hz)** 参数设置 LO 偏移。
- `Input port` — 使用 **LO offset** 输入端口设置 LO 偏移。

### **LO offset (Hz)** — 本振偏移频率 `0`（默认） | 标量 | 向量

本振的偏移频率，指定为标量或向量。此参数的有效范围取决于 USRP 设备的 RF 子板。

此图显示本振偏移会影响 USRP 硬件中的中频中心频率。它不会影响接收的中心频率。

- *f*RF 表示接收的 RF 频率。
- *f*center 表示由模块指定的中心频率。
- *f*LO offset 是本振偏移频率。
- 理想情况下，*f*RF – *f*center = 0。

要使中心频率远离 USRP 硬件产生的干扰或谐波，请使用 LO 偏移。

- 对于单通道 (SISO)，将 LO 偏移值指定为标量。
- 对于多通道 (MIMO)，LO 偏移必须为零。此限制是由于 UHD 限制。您可以将 LO 偏移指定为标量或向量。

#### 依赖关系

要启用此参数，请将 **Source of LO offset** 设置为 `Dialog`。

### **Source of gain** — 选择增益来源 `Dialog`（默认） | `Input port`

选择增益来源，指定为：

- `Dialog` — 使用 **Gain (dB)** 参数指定增益。
- `Input port` — 使用 **gain** 输入端口指定增益。

### **Gain (dB)** — 接收机增益 `32`（默认） | 标量 | 向量

接收机增益，以 dB 为单位，指定为标量或向量。此增益的有效范围取决于 USRP 设备的 RF 子板。

根据 **Channel Mapping** 配置设置增益值：

- 对于单通道 (SISO)，将增益指定为标量。
- 对于使用相同增益值的多通道 (MIMO)，将增益指定为标量。增益通过标量扩展设置。
- 对于使用不同增益的多通道 (MIMO)，在行向量中指定这些值。向量的第 *i* 个元素应用于由 **Channel Mapping** 指定的第 *i* 个通道。

#### 依赖关系

要启用此参数，请将 **Source of gain** 设置为 `Dialog`。

**数据类型：** `double`

### **PPS source** — PPS 信号源 `Internal`（默认） | `External` | `GPSDO`

每秒脉冲 (PPS) 信号源，指定为以下值之一。

- `Internal` — 使用 USRP 无线电的内部 PPS 信号。
- `External` — 使用来自外部信号发生器的 PPS 信号。
- `GPSDO` — 使用来自 GPSDO 的 PPS 信号。

要同步捆绑无线电所有通道的时间，您可以：

- 向所有捆绑无线电提供公共外部 PPS 信号，并将此参数设置为 `External`。
- 通过将此参数设置为 `GPSDO`，使用 USRP 无线电上可用的 GPSDO 的 PPS 信号。

要将 USRP 时间同步到有效 GPS 时间，请将此参数设置为 `GPSDO`。如果 GPSDO 在仿真开始时未锁定到 GPS 星座，则还必须启用 **Ensure sync GPS time** 参数。

### **Enable gps\_locked output port** — 启用 GPSDO 到 GPS 星座锁定状态的选项 `off`（默认） | `on`

选择此参数以启用 **gpsLocked** 输出端口，该端口指示 GPSDO 到 GPS 星座的锁定状态。

#### 依赖关系

要启用此参数，请将 **PPS source** 参数设置为 `GPDSO`。

### **Ensure sync GPS time** — 确保 GPS 时间同步的选项 `off`（默认） | `on`

选择此参数以确保 USRP 无线电时间同步到有效 GPS 时间。

当您选择此参数时，模块会检查 GPSDO 的锁定状态。当 GPSDO 锁定到 GPS 星座时，模块会将 USRP 无线电时间设置为有效 GPS 时间。

#### 依赖关系

要启用此参数，请将 **PPS source** 参数设置为 `GPSDO`。

### **Clock source** — 时钟源 `Internal`（默认） | `External` | `GPSDO`

时钟源，指定为以下值之一。

- `Internal` — 使用 USRP 无线电的内部时钟信号。
- `External` — 使用来自外部时钟发生器的 10 MHz 时钟信号。
- `GPSDO` — 使用来自 GPSDO 的 10 MHz 时钟信号。

对于 B 系列无线电，外部时钟端口标记为 *10 MHz*。对于 USRP N2xx 和 USRP2 无线电，外部时钟端口标记为 *REF IN*。

要同步捆绑无线电所有通道的频率，您可以：

- 向所有捆绑无线电提供公共外部 10 MHz 时钟信号，并将此参数设置为 `External`。
- 从每个 GPSDO 向对应无线电提供 10 MHz 时钟信号，并将此参数设置为 `GPSDO`。

### **Enable ref\_locked output port** — 启用 USRP 无线电到 10 MHz 时钟信号锁定状态的选项 `off`（默认） | `on`

选择此参数以启用 **refLocked** 输出端口，该端口指示 USPR 无线电到 10 MHz 时钟信号的锁定状态。

#### 依赖关系

要启用此参数，请将 **Clock source** 参数设置为 `External` 或 `GPDSO`。

### **Master clock rate (Hz)** — 主时钟速率标量

主时钟速率，以 Hz 为单位指定为标量。主时钟速率是 A/D 和 D/A 时钟速率。此属性的有效值范围取决于所连接的无线电平台。

| Platform Value | 支持的 **Master clock rate (Hz)** 值 |
| --- | --- |
| `N200/N210/USRP2` | `100e6`（只读）。 |
| `B200` 或 `B210` | 范围 `5e6` 到 `61.44e6` 内的标量。在多通道下使用 B210 时，时钟速率不得高于 `30.72e6` Hz。此限制是 B210 无线电在双通道操作时的硬件限制。默认值为 `32e6`。 |

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `B200` 或 `B210`。

**数据类型：** `double`

### **Decimation factor** — SDRu Receiver 的抽取因子 `512`（默认） | 整数

SDRu 接收机的抽取因子，指定为范围 `[1,1024]` 内的整数，具体限制取决于您使用的无线电。

| `DecimationFactor` 属性值 | B 系列 | N2xx 系列 |
| --- | --- | --- |
| `1` | 有效 | 无效 |
| `2` | 有效 | 仅当将 TransportDataType 属性设置为 `int8` 时有效。 |
| `3` | 有效 | 无效 |
| 从 4 到 128 的奇整数 | 有效 | 有效 |
| 范围 `[4,256]` 内的偶整数 | 有效 | 有效 |
| 范围 `[256,512]` 内的 4 的整数倍 | 有效 | 有效 |
| 范围 `[512,1024]` 内的 8 的整数倍 | 无效 | 无效 |

当无线电将中频 (IF) 信号下变频为复基带信号时，会使用抽取因子。

### **Enable time trigger** — 启用定时发送和接收的选项 off（默认） | on

启用定时发送和接收的选项。要使无线电在指定时间之后发送或接收数据，请选择 **Enable time trigger**。

当您选择 **Enable time trigger** 参数时，您可以：

- 在 **Trigger time** 参数指定的时间之后发送或接收。
- 如果您将 **PPSSource** 参数设置为 `GPSDO`，则在 **Trigger time** 参数中指定的 GPS 时间发送或接收。
- 在 **Trigger time** 参数指定的时间之后同时发送和接收。

### **Trigger time** — 触发时间（秒） `5`（默认） | 非负标量

触发时间，以秒为单位，指定为非负标量。指定您希望无线电在其后发送或接收数据的触发时间。**Trigger time** 值必须大于当前 USRP 无线电时间。

当您将 **PPS Source** 参数设置为 `GPSDO` 时，请将 **Trigger time** 参数指定为无线电发送和接收数据时的精确 GPS 时间（秒）。

**注意**

对于基于 AD936x 的 B2xx USRP 无线电，您可以预期指定触发时间与发送或接收开始之间存在一致的延迟。

#### 依赖关系

要启用此参数，请选择 **Enable trigger time** 参数。

### **Enable MIMO cable sync** — 启用 MIMO 电缆同步的选项 off（默认） | on

*自 R2024b 起*

启用 MIMO 电缆同步的选项。要启用 MIMO 电缆同步，请选择 **Enable MIMO cable sync**。

当您选择 **Enable MIMO cable sync** 参数时，您可以：

- 同步两个 N200/N210 USRP 无线电。
- 跨多个通道发送或接收频率、相位和时间同步的数据。
- 在两个 USRP N200/N210 无线电之间共享以太网。

要构建更大的 MIMO 系统（最高 16 x 16），请将 **PPS Source** 参数设置为 `"External"` 或 `"GPSDO"`，并将 **Clock Source** 参数设置为 `"External"`。

#### 依赖关系

要启用此参数，请将 **Platform** 设置为 `N200/N210/USRP2`。

### 数据

### **Baseband sample rate (Hz)** — 输出信号的基带采样率标量

此参数为只读。

输出信号的基带采样率，以 Hz 为单位，指定为标量。

此参数显示根据 **Master clock rate (Hz)** 和 **Decimation factor** 参数值计算得出的基带采样率。此计算使用公式：**Baseband sample rate** = Master clock rate/Decimation factor。如果在仿真期间更改 **Decimation factor**，则模块会更改硬件数据速率，但不会更改 Simulink 采样时间。

要获取有关采样时间的更多信息，请参阅 What Is Sample Time? (Simulink)。

**数据类型：** `double`

### **Transport data type** — 传输数据类型 `int16`（默认） | `int8`

传输数据类型，指定为：

- `int16` — 使用 16 位传输。比 8 位传输实现更高的精度。
- `int8` — 使用 8 位传输。使用大 256 倍的量化步长，并实现比 16 位传输快约两倍的传输数据速率。

将传输数据速率数据类型指定为 `int16` 时，会为同相分量分配 16 位，为正交分量分配 16 位，从而使每个传输数据的复数样本为 32 位。

### **Output data type** — 输出信号的数据类型 `Same as transport data type`（默认） | `double` | `single`

输出信号的数据类型，指定为 `Same as transport data type`、`double` 或 `single`。复数输出数据值的范围为 –1 到 1。

### **Samples per frame** — 输出信号每帧的样本数 `362` | 正整数

对象生成的输出信号每帧的样本数，指定为正整数标量。此值可最佳利用底层以太网数据包，其大小为 1500 个 8 位字节。

### **Enable data length output port** — 启用数据长度输出端口的选项 off（默认） | on

要指示从 USRP 无线电接收的样本数，请选择此参数。

### **Enable overrun output port** — 启用溢出输出端口的选项 off（默认） | on

要测量接收期间丢失的样本数，请选择此参数。

如果您的模型未实时运行，可以调整参数以减少传输的样本数。要接近或实现实时性能，可以增大抽取因子。有关详细信息，请参阅 Detect Underruns and Overruns。

### **Enable timestamps output port** — 启用时间戳输出端口的选项 off（默认） | on

要从 USRP 无线电获取每个接收样本的时间戳，请选择此参数。

### **Enable burst mode** — 启用突发模式的选项 off（默认） | on

启用突发模式的选项。要生成一组连续帧而不会对无线电造成溢出或欠载，请选择 **Enable burst mode**。启用突发模式可帮助您仿真无法实时运行的模型。

启用突发模式后，请使用 **Number of frames in burst** 参数指定所需的连续数据量。有关详细信息，请参阅 Detect Underruns and Overruns。

### **Number of frames in burst** — 连续突发中的帧数 `100`（默认） | 非负整数

连续突发中的帧数，指定为非负整数。

#### 依赖关系

要启用此参数，请选择 **Enable burst mode**。

**数据类型：** `double`

## 所属库

Communications Toolbox Support Package for USRP Radio

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2011b 中引入**

### R2025a: 在 USRP 接收机 Simulink 模块的 TX/RX 端口上接收信号

您可以使用 SDRu Receiver Simulink 模块在 USRP 无线电的 `TX/RX` 天线端口上接收信号。您可以配置 Simulink 模块的 **Receive antenna port** 参数，以在无线电的 `TX/RX` 天线端口上接收信号。

### R2024b: 使用共享 MIMO 电缆同步 N2xx 系列 USRP 无线电

使用 MIMO 电缆捆绑两个 N2xx 系列 USRP 无线电，以共享时钟参考、定时参考和以太网接口。要使用捆绑的 N2xx 无线电同步多通道发送和接收，请在 Simulink 中的 SDRu Transmitter 和 SDRu Receiver 模块中使用 **Enable MIMO Cable Sync** 参数。

### R2024a: 对 N3xx 和 X3xx 系列无线电设备的支持已移至 Wireless Testbench

对 NI USRP N3xx 和 X3xx 系列无线电设备的支持已从 Communications Toolbox Support Package for USRP Radio 移至 Wireless Testbench Support Package for NI USRP Radios。

要将这些无线电配置为与 Wireless Testbench 一起使用，请参阅 Install Support Package for NI USRP Radios (Wireless Testbench)。

### R2023b: 增强了对 SDRu Blocks 中时间触发的支持

您现在可以指定触发时间，以便为 USRP 无线电在指定时间发送和接收数据。此属性在 SDRu Transmitter 和 SDRu Receiver Simulink 模块中可用。

### R2020a: 已移除 decim 输入端口

从 R2020a 开始，SDRu Receiver 模块移除了 **decim** 输入端口。您不能通过使用输入端口为此模块设置抽取因子值。请改用 **Decimation factor** 参数。

### R2020a: 已移除 Sample time 参数

从 R2020a 开始，SDRu Receiver 模块移除了 **Sample time** 参数。请改用只读的 **Baseband sample rate (Hz)** 参数。此参数显示根据 **Master clock rate (Hz)** 和 **Decimation factor** 参数计算得出的基带采样率。

## 描述

从 USRP 设备接收数据

SDRu Receiver 模块支持 Simulink® 与 Universal Software Radio Peripheral (USRP™) 设备之间的通信，从而支持各种软件定义无线电应用的仿真和开发。SDRu Receiver 模块和 USRP 板必须位于同一以太网子网。

SDRu Receiver 模块使用来自 Ettus Research™ 的 Universal Hardware Driver (UHD™) 从 USRP 板接收信号和控制数据。SDRu Receiver 模块是一个 Simulink 源，它从 USRP 板接收数据，并输出具有固定行数的列向量或矩阵信号。对此模块的第一次调用可能包含瞬态值，在这种情况下，生成的数据包包含未定义数据。

此框图说明了 Simulink、SDRu Transmitter 和 Receiver 模块以及 USRP 硬件如何连接。

要通过空中发送无线电信号，请将 Simulink 中生成的信号传递到 SDRu transmitter 模块。发射器模块将信号转发到无线电硬件。要通过空中接收无线电信号，请使用 SDRu receiver 模块。接收器模块转发从无线电硬件接收的信号，以便在 Simulink 中进行后处理。

当调用此模块时，主机可能尚未从 USRP 硬件接收到任何数据。数据长度端口 **length** 指示何时存在有效数据。当数据长度端口包含零值时，没有数据。要限定模型某部分的执行，请将数据长度与使能子系统一起使用。

如果您的计算机未连接到任何 USRP 硬件，您仍可以使用此模块开发可传播采样时间和数据类型信息的模型。要传播此信息，请选择 **Simulation** > **Update diagram**。

有关与此模块接口的 USRP 硬件产品的信息，请参阅 Ettus Research 网站。

此图标显示所有端口，包括可选端口：具有所有端口的 SDRu receiver 模块

**注意**

从 R2024a 开始，使用此 Simulink 模块所需的 MathWorks® 产品和支持包取决于您的无线电设备。

| 无线电设备 | 所需的 MathWorks 产品 | 支持包安装 |
| --- | --- | --- |
| USRP2™  USRP N200, N210  USRP B200, B210 | - Communications Toolbox™ Support Package for USRP Radio | Install Communications Toolbox Support Package for USRP Radio |
| USRP E320 *(自 R2025a 起)*  USRP N300, N310, N320, N321  USRP X300, X310  USRP X410 *(自 R2025a 起)* | - Wireless Testbench™ - Wireless Testbench Support Package for NI™   USRP Radios | Install Support Package for NI USRP Radios (Wireless Testbench) |

有关如何将此 Simulink 模块与 Wireless Testbench Support Package for NI USRP Radios 支持的无线电设备一起使用的详细信息，请参阅 SDRu Receiver (Wireless Testbench)。
