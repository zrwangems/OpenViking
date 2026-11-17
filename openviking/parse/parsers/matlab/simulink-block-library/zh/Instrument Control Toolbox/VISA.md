---
type: simulink-block
title: 'VISA'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'visablock'
documentation_source_path: 'visablock.html'
language: zh-CN
chinese_source: worker-translation
---

# VISA

## 端口

### 输入

### **Input** — 要发送的数据 vector | matrix | array

要从模块发送到 VISA 资源的数据值，指定为向量、矩阵或数组。

#### 依赖关系

- 要启用此端口，请在 **Send or Query** 选项卡中将 **Send command type** 设置为 **Compose command from input data** 或 **Send input port data as is**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Data** — 接收到的数据 vector | matrix | array

模块从 VISA 资源接收到的数据，以向量、矩阵或数组形式返回。

#### 依赖关系

- 要启用此端口，请在 **Send or Query** 选项卡中将 **Use block to** 设置为 **Query instrument** 或 **Receive response**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Status** — 仪器状态 `1` | `0`

仪器状态，以 `1` 或 `0` 返回，其中 `1` 表示成功，`0` 表示失败。

#### 依赖关系

- 要启用此端口，请在 **Handle Error** 选项卡中将 **Action when error occurs** 设置为 `Continue simulation`。

**数据类型：** `double`

### **Instrument error** — 来自仪器的错误消息 string

来自仪器的错误消息，以字符串形式返回。

#### 依赖关系

- 要启用此端口，请在 **Handle Error** 选项卡中将 **Action when error occurs** 设置为 `Continue simulation`，并选中 **Check instrument error** 参数。

**数据类型：** `string`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 模块参数

### **Block sample time** — 采样之间的时间间隔 -1（默认）| 数值

模块在仿真期间的采样时间。这是模块在仿真期间执行的速率。有关详细信息，请参阅 Timing in Hardware Interface Models。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的数值 |

**Example:** `set_param(gcb,"SampleTime","1")`

### 硬件配置

#### 从资源列表中选择

### **Resource name** — VISA 资源名称 可用的 VISA 资源

您机器上要连接并与之通信的 VISA 资源。每种 VISA 接口类型都有不同的格式。有关详细信息，请参阅 ResourceName。

#### 依赖关系

- 要启用此参数，请从 **Select and configure hardware** 中选择 **Select from resource list** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ResourceName` |
| **值**：| 资源名称 |

**Example:** `set_param(gcb,"ResourceName","ASRL4::INSTR")`

### **Vendor** — 仪器制造商 只读：仪器制造商名称

此参数为只读。

仪器制造商。如果 VISA 接口类型不提供有关制造商的信息，则此参数为空。

#### 依赖关系

- 要启用此参数，请从 **Select and configure hardware** 中选择 **Select from resource list** 选项。

#### 编程使用

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `VendorName` |
| **值**：| 只读：供应商名称 |

**Example:** `get_param(gcb,"VendorName")`

### **Model** — 仪器型号 只读：仪器型号名称

此参数为只读。

仪器型号。如果 VISA 接口类型不提供型号信息，则此参数为空。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **从资源列表中选择** 选项。

#### 编程使用

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ModelName` |
| **值：** | 只读：型号名称 |

**示例：** `get_param(gcb,"ModelName")`

### **Serial Number** — 与仪器关联的唯一序列号 只读：仪器序列号

此参数为只读。

与仪器关联的唯一序列号。如果 VISA 接口类型不提供序列号信息，则此参数为空。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **从资源列表中选择** 选项。

#### 编程使用

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SlNumber` |
| **值：** | 只读：序列号 |

**示例：** `get_param(gcb,"SlNumber")`

#### 配置新的 VISA 资源

### **VISA resource type** — 要配置的 VISA 资源类型 `TCP/IP Socket`（默认）| `TCP/IP HiSLIP` | `TCP/IP VXI-11`

要手动配置以建立连接的 VISA 资源类型。为要连接的资源选择 VISA 资源类型后，可以指定该资源的参数并创建到它的连接。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **配置新的 VISA 资源** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Interface` |
| **值：** | `"TCP/IP Socket"`（默认）| `"TCP/IP HiSLIP"` | `"TCP/IP VXI-11"` |

**示例：** `set_param(gcb,"Interface","TCP/IP
VXI-11")`

### **Board index** — 要连接的板卡索引 正整数

要连接的 VISA 资源的板卡索引。对于 VISA-TCP/IP 资源，这是与仪器关联的网络板卡的索引号。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **配置新的 VISA 资源** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `BoardNumber` |
| **值：** | 带引号的正数 |

**示例：** `set_param(gcb,"BoardNumber","5")`

### **IP address** — 要连接的 IP 地址 IP 地址

要连接的 VISA 资源的 IP 地址。对于 VISA-TCP/IP 资源，这是套接字的点分十进制表示法的 TCP/IP 地址。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **配置新的 VISA 资源** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `IPAddress` |
| **值：** | 带引号的点分十进制表示法的 IP 地址 |

**示例：** `set_param(gcb,"IPAddress","127.0.0.1")`

### **Port number** — 用于连接的端口号 `4880`（默认）| 正整数

VISA-TCP/IP 资源连接所使用的端口号，指定为 1 到 65535（含）之间的数字。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **配置新的 VISA 资源** 选项。
- 要启用此参数，**VISA 资源类型** 必须为 `TCP/IP Socket` 或 `TCP/IP HiSLIP`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Port` |
| **值：** | `"4880"`（默认）| 带引号的正数 |

**示例：** `set_param(gcb,"Port","80")`

### **Device ID** — 要连接的设备 ID 正整数

要连接的 VISA-TCP/IP 资源的设备 ID 号。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **配置新的 VISA 资源** 选项。
- 要启用此参数，**VISA 资源类型** 必须为 `TCP/IP HiSLIP` 或 `TCP/IP VXI-11`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DeviceID` |
| **值：** | 带引号的正数 |

**示例：** `set_param(gcb,"DeviceID","1")`

#### 指定资源名称

### **Resource name** — VISA 资源名称 VISA 资源名称

您要连接并通信的计算机上的 VISA 资源。每种 VISA 接口类型都有不同的格式。有关详细信息，请参阅 ResourceName。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **指定资源名称** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ResourceString` |
| **值：** | 带引号的资源名称 |

**示例：** `set_param(gcb,"ResourceString","GPIB0::5::INSTR")`

#### 配置连接

### **EOI Mode** — EOI 模式 `on`（默认）| `off`

在写操作结束时是否置位 EOI（结束或识别）线。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **配置新的 VISA 资源** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `EOIMode` |
| **值：** | `"on"`（默认）| `"off"` |

**示例：** `set_param(gcb,"EOIMode","off")`

### **Byte order** — 字节的顺序 `little-endian`（默认）| `big-endian`

字节排列为更大数值时的顺序。

#### 依赖关系

- 要启用此参数，请从 **选择和配置硬件** 中选择 **配置新的 VISA 资源** 或 **指定资源名称** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ByteOrder` |
| **值：** | `"little-endian"`（默认）| `"big-endian"` |

**示例：** `set_param(gcb,"ByteOrder","big-endian")`

### **Read terminator** — 读取数据的终止符字符 `off`（默认）| `LF` | `CR` | `CR/LF` | 0 到 255

用于读取 ASCII 终止数据的终止符字符，指定为 `off`、`LF`、`CR`、`CR/LF` 或 0 到 255（含）之间的数字。当从远程主机读取且终止符值为 `CR/LF` 时，读取在同时出现 `CR` 和 `LF` 时终止。如果终止符值为 `off`，读操作将忽略终止符字符。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ReadTerminator` |
| **值：** | `"off"`（默认） | `"LF"` | `"CR"` | `"CR/LF"` | 0 到 255（带引号） |

**示例：** `set_param(gcb,"ReadTerminator","CR")`

### **写入终止符** — 用于写入数据的终止符字符 `LF`（默认） | `CR` | `CR/LF` | 0 到 255

用于写入 ASCII 终止数据的终止符字符，指定为
`LF`、`CR`、`CR/LF` 或 0 到 255（含）之间的数字。当以终止符值
`CR/LF` 向远程主机写入时，写入操作通过同时添加 `CR`
和 `LF` 来终止。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `WriteTerminator` |
| **值：** | `"LF"`（默认） | `"CR"` | `"CR/LF"` | 0 到 255（带引号） |

**示例：** `set_param(gcb,"WriteTerminator","CR")`

### **数据位** — 表示一个数据字符的位数 `8`（默认） | `5` | `6` | `7`

通过 VISA 资源传输的数据位数。

#### 依赖关系

- 要启用此参数，请从 **选择和配置
  硬件** 中选择 **从资源列表中选择**
  选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DataBits` |
| **值：** | `"8"`（默认） | `"5"` | `"6"` | `"7"` |

**示例：** `set_param(gcb,"DataBits","5")`

### **奇偶校验** — 奇偶校验位类型 `none`（默认） | `even` | `odd`

添加到 VISA 资源所传输数据的奇偶校验位类型。您可以使用此
参数向数据中添加奇偶校验位（也称为校验位）。向二进制代码字符串中
添加奇偶校验位是一种通过确保 1 位的总数为偶数或奇数来检测数据
传输错误的方法。

奇偶校验位的值由给定比特集中 1 的数量决定，设置
如下。

| 奇偶校验位类型 | 奇偶校验位值 | |
| --- | --- | --- |
| 如果 1 的数量为偶数 | 如果 1 的数量为奇数 |
| `none` | 不设置奇偶校验位 | 不设置奇偶校验位 |
| `even` | 0 | 1 |
| `odd` | 1 | 0 |

#### 依赖关系

- 要启用此参数，请从 **选择和配置
  硬件** 中选择 **从资源列表中选择**
  选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Parity` |
| **值：** | `"none"`（默认） | `"even"` | `"odd"` |

**示例：** `set_param(gcb,"Parity","even")`

### **停止位** — 指示字符结束的位模式 `1`（默认） | 正标量

用于指示字节结束的位数。此参数取决于您为 **数据位** 参数
选择的值。如果您选择数据位
`6`、`7` 或
`8`，默认值为 `1`，另一个
可选值为 `2`。如果您选择数据位
`5`，默认值为 `1`，另一个可选值为 `1.5`。

#### 依赖关系

- 要启用此参数，请从 **选择和配置
  硬件** 中选择 **从资源列表中选择**
  选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `StopBits` |
| **值：** | `"1"`（默认） | 正标量 |

**示例：** `set_param(gcb,"StopBits","2")`

### **Flow control** — 管理数据传输速率的模式 `none`（默认）| `hardware` | `software`

管理 VISA 资源上数据传输速率的过程。选择
`none` 表示不使用流控制，
`hardware` 表示由硬件决定流控制，
`software` 表示由软件决定流
控制。

#### 依赖关系

- 要启用此参数，请从 **Select and configure
  hardware** 中选择 **Select from resource
  list** 选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FlowControl` |
| **值：** | `"none"`（默认）| `"hardware"` | `"software"` |

**示例：** `set_param(gcb,"FlowControl","hardware")`

### **Baud rate** — 通信速度 9600（默认）| 正整数

VISA 资源传输比特的速率，单位为比特每秒。

#### 依赖关系

- 要启用此参数，请从 **Select and configure
  hardware** 中选择 **Select from resource
  list** 选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `BaudRate` |
| **值：** | `"9600"`（默认）| 正整数 |

**示例：** `set_param(gcb,"BaudRate",14400)`

### **Timeout** — 完成操作所允许的时间 10（默认）| 数值

完成读取和写入操作所允许的时间，单位为秒。

#### 依赖关系

- 要启用此参数，请从 **Select and configure hardware** 中选择 **Configure new VISA
  resource** 或 **Specify resource name** 选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TimeOut` |
| **值：** | 10（默认）| 数值 |

**示例：** `set_param(gcb,20)`

#### 验证并测试连接

### **Instrument identification command** — 发送到仪器的 SCPI 命令 `*IDN?`（默认）| SCPI 命令

发送到仪器的仪器识别 SCPI 命令，用于查看其响应。使用此命令测试你是否能够成功与 VISA 资源建立连接。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `TestCommand` |
| **值：** | `"*IDN?"`（默认）| 带引号的 SCPI 命令 |

**示例：** `set_param(gcb,"TestCommand","*IDN?")`

### **Validate and test connection** — VISA 资源连接验证按钮

点击此按钮，将 **Instrument identification command** 中指定的 SCPI 命令发送到你的 VISA 资源，并在 **Response** 中返回一个值。

### **Response** — 仪器查询响应 只读：字符串标量

此参数为只读。

仪器对 **Instrument
identification command** 中指定的 SCPI 命令的响应。此字段在你点击 **Validate and test connection** 后填充。

#### 程序化使用

要以程序化方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Response` |
| **值：** | 只读：带引号的仪器响应 |

**示例：** `get_param(gcb,"Response")`

### Instrument Initialization

#### Initialization commands

### **Initialization commands** — 要发送到仪器的 SCPI 命令 `*RST;*CLS`（默认）| SCPI 命令

发送到仪器的仪器初始化 SCPI 命令。如果有多个命令，请用分号（`;`）分隔每个命令。每个命令会依次发送。这些命令在仿真期间执行一次。点击 **Upload initialization commands and check instrument error status** 按钮将这些命令发送到仪器。

#### 依赖关系

- 要启用此参数，请从 **Send initialization commands** 中选择 **Initialization commands** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SendString` |
| **值**：| `"*RST;*CLS"`（默认）| 引号中的 SCPI 命令 |

**Example:** `set_param(gcb,"SendString","SOURce1:FUNCtion
SQU")`

#### MATLAB Code

### **MATLAB Code** — 要发送到仪器的 MATLAB® 代码 MATLAB 代码

发送到仪器的仪器初始化 MATLAB 脚本。编写此代码时，请使用 `visaObj` 作为表示与仪器连接的 VISA 对象。可以使用 `write` 函数向仪器发送 ASCII 初始化命令。点击 **Upload initialization commands and check instrument error status** 按钮将此代码发送到仪器。

#### 依赖关系

- 要启用此参数，请从 **Send initialization commands** 中选择 **MATLAB Code** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ExecuteFunction` |
| **值**：| 引号中的 MATLAB 代码 |

**Example:** `set_param(gcb,"ExecuteFunction","write(visaObj,'SOURce1:FUNCtion
SQU')")`

#### Test instrument initialization commands

### **Instrument error check command** — 要发送到仪器的 SCPI 命令 `SYSTem:ERRor?`（默认）| SCPI 命令

发送到仪器以查看其响应的仪器错误检查 SCPI 命令。如果指定了任何初始化 SCPI 命令或 MATLAB 代码，则此命令会在它们之后发送。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InitTestCommand` |
| **值**：| `"SYSTem:ERRor?"`（默认）| 引号中的 SCPI 命令 |

**Example:** `set_param(gcb,"InitTestCommand","SYSTem:ERRor?")`

### **Upload initialization commands and check instrument error status** — 初始化和错误检查命令上传按钮

点击此按钮可向仪器发送在 **Initialization commands** 或 **MATLAB Code** 中指定的任何初始化命令，随后发送在 **Instrument error check command** 中指定的错误检查命令。根据仪器状态，仪器会发送响应，并显示在 **Instrument status** 字段中。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

### **Instrument status** — 仪器初始化响应 只读：字符串标量

此参数为只读。

仪器对在 **Initialization commands** 或 **MATLAB Code** 中指定的初始化命令的响应。如果仪器接受这些命令，此字段会显示成功消息。如果仪器处于错误状态，状态会反映该情况。

#### 程序化使用

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `initStatus` |
| **值：** | 只读：带引号的仪器响应 |

**示例：** `get_param(gcb,"initStatus")`

### 发送或查询

#### 发送命令

### **SCPI Command** — 要发送到仪器的 SCPI 命令 SCPI command

作为 SCPI 命令发送到仪器的数据。您发送的 SCPI 命令必须受您的仪器支持。

#### 依赖关系

- 要启用此参数，请从 **Send command type** 中选择 **SCPI command** 选项。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `StaticCommand` |
| **值：** | 带引号的 SCPI 命令 |

**示例：** `set_param(gcb,"StaticCommand","SYST:PON:TIME?")`

### **Binary command** — 要发送到仪器的二进制命令 binary values

作为二进制数据发送到仪器的数据。值必须在 0 到 256 之间。

#### 依赖关系

- 要启用此参数，请从 **Send command type** 中选择 **Binary** 选项。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `StaticBinary` |
| **值：** | 带引号的二进制值 |

**示例：** `set_param(gcb,"StaticBinary","[83 89 83 84 58 80 79 78 58 84 73 77 69 63]")`

### **Binblock data** — 要发送到仪器的 Binblock 命令 binblock values

作为 binblock 发送到仪器的数据。

#### 依赖关系

- 要启用此参数，请从 **Send command type** 中选择 **Binblock** 选项。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `BinBlockCommand` |
| **值：** | 带引号的 binblock 值 |

**示例：** `set_param(gcb,"BinBlockCommand","[83 89 83 84 58 80 79 78 58 84 73 77 69 63]")`

### **Data type** — 每个值的大小和格式 `uint8` (default) | `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `uint64` | `int64`

将数据发送到仪器时使用的数据类型。此参数决定每个值要写入的字节数以及将这些字节解释为 MATLAB 数据类型的方式。

#### 依赖关系

- 要启用此参数，请从 **Send command type** 中选择 **Binary** 或 **Binblock** 选项。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DataType` |
| **值：** | `"uint8"` (default) | `"single"` | `"double"` | `"int8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` |

**示例：** `set_param(gcb,"DataType","double")`

### **Command header** — 随输入端口数据一起发送的 SCPI 命令头 SCPI command

附加在输入端口数据之前发送到仪器的 SCPI 命令头。

#### 依赖关系

- 要启用此参数，请从 **Send command type** 中选择 **Compose command from input data** 选项。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Header` |
| **值：** | 带引号的 SCPI 命令 |

**示例：** `set_param(gcb,"Header","SOUR1:VOLT")`

### **Numeric format** — 数值数据的格式 `Integer, signed (%d)`（默认）| `Integer, unsigned (%u)` | `Floating-point (%f)` | `Characters (%c)` | `Enter numeric format`

输入端口数据的格式。如果选择 `Enter numeric format`，则可以指定所提供选项之外的格式。

#### 依赖关系

- 要启用此参数，请从 **Send command type** 中选择 **Compose command from input
  data** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以编程方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `NumFormat` |
| **值**：| `"Integer, signed (%d)"`（默认）| `"Integer, unsigned (%u)"` | `"Floating-point (%f)"` | `"Characters (%c)"` | `"Enter numeric format"` |

**Example:** `set_param(gcb,"NumFormat","Characters
(%c)")`

### **Enter numeric format** — 数值数据的自定义格式 `%2f`（默认）| numeric formats

输入端口数据的自定义格式。

#### 依赖关系

- 要启用此参数，请从 **Numeric format** 中选择 `Enter numeric
  format` 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以编程方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `CustomNumericFormat` |
| **值**：| `"%2f"`（默认）| numeric format in quotes |

**Example:** `set_param(gcb,"CustomNumericFormat","%2f")`

### **delimiter** — 分隔字符 `,`（默认）

追加到数值格式后的分隔字符，用于创建要发送到仪器的命令字符串。

#### 依赖关系

- 要启用此参数，请从 **Send command type** 中选择 **Compose command from input
  data** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以编程方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `delimiter` |
| **值**：| `","`（默认）| delimiting character in quotes |

**Example:** `set_param(gcb,"delimiter",",")`

#### Receive response

### **Data type** — 每个值的大小和格式 `uint8`（默认）| `single` | `double` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `uint64` | `int64`

从仪器读取数据时所用的数据类型。此参数决定每个值要读取的字节数，以及如何将这些字节解释为
MATLAB 数据类型。

#### 依赖关系

- 要启用此参数，请从 **Data format** 中选择 **Read numeric
  data** 选项。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以编程方式获取模块参数值，
请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ReceiveDatatype` |
| **值**：| `"uint8"`（默认）| `"single"` | `"double"` | `"int8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` |

**Example:** `set_param(gcb,"ReceiveDatatype","double")`

### **Determine data size automatically** — 允许模块自动检测数据大小 on（默认）| off

选择此参数可让模块确定接收数据的大小。如果要手动指定数据大小，请清除此参数，并相应地设置
**Data size** 参数的值。

#### 依赖关系

- 要启用此参数，请从 **Data format** 中选择 **Read string response and
  convert to numeric value** 或 **Binblock** 选项。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `AutoSize` |
| **值：** | `"on"`（默认） | `"off"` |

**示例：** `set_param(gcb,"AutoSize","off")`

### **数据大小** — 读取的值的数量 `[1,1]`（默认） | `[10000,1]`（默认） | 数值数组

手动指定每个仿真时间步应读取的值的数量。将大小定义为多维数值数组。数据大小不包括报头或终止符值。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 从 **数据格式** 中选择 **读取数值数据** 选项。此情况使用 `Size` 程序化参数，默认值为 `[1,1]`。
- 从 **数据格式** 中选择 **读取字符串响应并转换为数值** 或 **Binblock** 选项，并清除 **自动确定数据大小**。此情况使用 `OutputSize` 程序化参数，默认值为 `[10000,1]`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Size` |
| **值：** | `"[1,1]"`（默认） |

**示例：** `set_param(gcb,"Size","[1,2]")`

|  |  |
| --- | --- |
| **参数：** | `OutputSize` |
| **值：** | `"[10000,1]"`（默认） |

**示例：** `set_param(gcb,"OutputSize","[10000,2]")`

### 处理错误

### **发生错误时的操作** — 仪器出错时要执行的操作 `Stop simulation`（默认） | `Continue simulation`

当仪器在仿真期间返回错误时，模块应执行的操作。如果选择 `Stop simulation`，诊断查看器窗口将显示该错误。此错误可能是 `visadev` 错误或仪器错误。如果选择 `Continue simulation`，并且发生读取错误，则状态位设置为 1。如果发生仪器错误，则仪器错误端口将错误消息文本作为字符串输出。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ActionWhenerror` |
| **值：** | `"Stop simulation"`（默认） | `"Continue simulation"` |

**示例：** `set_param(gcb,"ActionWhenerror","Continue
simulation")`

### **检查仪器错误** — 输出错误消息 `off`（默认） | `on`

选择此选项可在每个时间步使用 **错误检查命令** 中指定的 SCPI 命令将任何错误输出到模块的仪器错误端口。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Checkerror` |
| **值：** | `"off"`（默认） | `"on"` |

**示例：** `set_param(gcb,"Checkerror","on")`

### **错误检查命令** — 发送到仪器的 SCPI 命令 `SYSTem:ERRor?`（默认） | SCPI 命令

仪器错误检查 SCPI 命令，您将其发送到仪器以查看其响应。

#### 依赖关系

- 要启用此参数，请将 **检查仪器错误** 参数设置为 `on`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `CheckCommand` |
| **值：** | `"SYSTem:ERRor?"`（默认） | 带引号的 SCPI 命令 |

**示例：** `set_param(gcb,"InitTestCommand","SYSTem:ERRor?")`

## 所属库

Instrument Control Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

与 VISA 资源通信

VISA 模块与 VISA 资源通信。根据配置，您可以使用此模块发送或接收数据，以及查询 VISA 资源。
