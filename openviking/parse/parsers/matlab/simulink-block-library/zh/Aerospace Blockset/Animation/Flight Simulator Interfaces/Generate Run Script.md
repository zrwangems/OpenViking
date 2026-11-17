---
type: simulink-block
title: 'Generate Run Script'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'generaterunscript'
documentation_source_path: 'generaterunscript.html'
language: zh-CN
chinese_source: worker-translation
---

# Generate Run Script

## 端口

R2025b 中未记录。

## 参数

### **Select target architecture** — 运行脚本的目标平台 `Default`（默认）| `Win64` | `Linux` | `Mac`

从列表中选择要执行运行脚本的目标平台。该平台可以与创建运行脚本的平台不同。如果希望生成在创建运行脚本的平台上运行的运行脚本，请选择 `Default`。

- `Win64`
- `Linux`
- `Mac`

#### 编程使用

|  |
| --- |
| **模块参数**：`Architecture` |
| **类型**：字符向量 |
| **值**：`'Win64' | 'Linux' | 'Mac'` |
| **默认值**：`'Default'` |

### **Select FlightGear data flow** — FlightGear 数据流 `Send`（默认）| `Receive` | `Send-Receive`

从列表中选择数据流的方向：

- `Send`

  创建运行脚本，以设置将 `net_fdm` 控制模型从 Simulink 发送到 FlightGear。
- `Receive`

  创建运行脚本，以设置从 FlightGear 接收 `net_ctrl` 控制模型到 Simulink。
- `Send-Receive`

  创建运行脚本，以设置 FlightGear 接收并广播与 Simulink 之间的数据。

  **注意**

  选择 `Send-Receive` 选项并不意味着您接收与发送相同的数据（例如，您可能看不到控制面位置数据）。使用此选项时，您主要看到的是用户输入（例如通过操纵杆输入的数据）和环境数据。

#### 编程使用

|  |
| --- |
| **模块参数**：`dataFlow` |
| **类型**：字符向量 |
| **值**：`'Receive' | 'Send-Receive'` |
| **默认值**：`'Send'` |

### **FlightGear geometry model name** — 包含 FlightGear 几何模型的文件夹 HL20（默认）

指定包含所需模型几何模型的文件夹名称，该文件夹位于 *`FlightGear`*`\data\Aircraft` 文件夹中。

#### 编程使用

|  |
| --- |
| **模块参数**：`GeometryModelName` |
| **类型**：字符向量 |
| **值**：`'HL20'` |
| **默认值**：`'HL20'` |

### **Airport ID** — 支持的机场 ID KSFO（默认）

支持的机场 ID，从 FlightGear 界面中 **Location** 下可用支持机场列表中选择。

#### 编程使用

|  |
| --- |
| **模块参数**：`'AirportId'` |
| **类型**：字符向量 |
| **值**：`'KSFO'` |
| **默认值**：`'KSFO'` |

### **Runway ID** — 支持的跑道 ID 10L（默认）

指定跑道 ID。

#### 编程使用

|  |
| --- |
| **模块参数**：`RunwayId` |
| **类型**：字符向量 |
| **值**：`'10L'` |
| **默认值**：`'10L'` |

### **Initial altitude (ft)\*** — 飞机初始高度 7224 | 数值

飞机的初始高度，以英尺为单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialAltitude` |
| **类型**：字符向量 |
| **值**：`'7224'` |
| **默认值**：`'7224'` |

### **Initial heading (deg)\*** — 飞机初始航向 113 | 数值

飞机的初始航向，以度为单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialHeading` |
| **类型**：字符向量 |
| **值**：`'113'` |
| **默认值**：`'113'` |

### **Offset distance (miles)\*** — 偏移距离 4.72 | 数值

飞机距机场的偏移距离，以英里为单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`OffsetDistance` |
| **类型**：字符向量 |
| **值**：`'4.72'` |
| **默认值**：`'4.72'` |

### **Offset azimuth (deg)\*** — 飞机偏移方位角 0 | 数值

飞机的偏移方位角，以度为单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`OffsetAzimuth` |
| **类型**：字符向量 |
| **值**：`'0'` |
| **默认值**：`'0'` |

### **Install FlightGear scenery during simulation (requires Internet connection)** — 在仿真期间安装 FlightGear 场景 `off`（默认）| `on`

选中此复选框可指示 FlightGear 在仿真器运行时自动安装所需场景。选中此复选框需要稳定的 Internet 连接。对于 Windows® 系统，在启用此选项的情况下启动 FlightGear 时，您可能会遇到错误消息。有关详细信息，请参阅 Install Additional FlightGear Scenery。

#### 编程使用

|  |
| --- |
| **模块参数**：`InstallScenery` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Disable FlightGear shader options** — 禁用 FlightGear 着色器 `off`（默认）| `on`

选中此复选框可禁用 FlightGear 着色器选项。您的计算机内置显卡（例如 NVIDIA® 显卡）可能与 FlightGear 着色器冲突。如果您遇到此冲突，请考虑选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`DisableShaders` |
| **类型**：字符向量 |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Destination/Origin IP address** — 运行 MATLAB 的机器的网络 IP 地址 127.0.0.1

运行 MATLAB 的机器的网络 IP 地址。此值为只读。

#### 编程使用

|  |
| --- |
| **模块参数**：`OriginAddress` |
| **类型**：字符向量 |
| **值**：`'127.0.0.1'` |
| **默认值**：`'127.0.0.1'` |

### **Destination port** — FlightGear 机器的目标端口 5502

网络飞行动力学模型（fdm）端口。有关详细信息，请参阅 Send net\_fdm Packet to FlightGear 模块参考。

#### 编程使用

|  |
| --- |
| **模块参数**：`DestinationPort` |
| **类型**：字符向量 |
| **值**：`'5502'` |
| **默认值**：`'5502'` |

### **Origin port** — FlightGear 机器的源端口 5505

网络控制（`ctrl`）端口。有关详细信息，请参阅 Receive net\_ctrl Packet from FlightGear 模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`OriginPort` |
| **类型**：字符向量 |
| **值**：`'5505'` |
| **默认值**：`'5505'` |

### **Network IP address** — FlightGear 机器的网络 IP 地址 127.0.0.1

运行 MATLAB 软件的机器的网络 IP 地址。

#### 编程使用

|  |
| --- |
| **模块参数**：`LocalAddress` |
| **类型**：字符向量 |
| **值**：`'127.0.0.1'` |
| **默认值**：`'127.0.0.1'` |

### **Output file name** — 输出文件 `runfg.bat`

输出文件名。该文件名是您使用这些初始参数启动 FlightGear 时所使用的命令名称。

**注意**

运行脚本文件名必须由 ASCII 字符组成。

使用以下文件扩展名：

| 平台 | 扩展名 |
| --- | --- |
| Windows | `.bat` |
| Linux® 和 macOS | `.sh` |

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputFileName` |
| **类型**：字符向量 |
| **值**：`'runfg.bat'` |
| **默认值**：`'runfg.bat'` |

### **FlightGear base directory** — FlightGear 基础目录 `C:\Program Files\FlightGear`

指定 FlightGear 安装文件夹的名称。

**注意**

FlightGear 必须安装在由 ASCII 字符组成的文件夹路径名中。

#### 编程使用

|  |
| --- |
| **模块参数**：`FlightGearBaseDirectory` |
| **类型**：字符向量 |
| **值**：`'C:\Program Files\FlightGear'` |
| **默认值**：`'C:\Program Files\FlightGear'` |

### **Generate Script** — Generate Script 按钮 按钮

点击 **Generate Script** 为 FlightGear 生成运行脚本。在对话框中输入正确的参数信息之前，请勿点击此按钮。

## 所属库

Aerospace Blockset / Animation / Flight Simulator Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前推出**

## 描述

在当前平台上生成 FlightGear 运行脚本

Generate Run Script 模块在当前平台上生成自定义的 FlightGear 运行脚本。

要生成运行脚本，请在 Parameters 字段中填写所需信息，然后点击 **Generate Script**。

在对话框中，标有星号（\*）的字段将作为 MATLAB® 表达式进行求值。其他字段则被视为字面文本。
