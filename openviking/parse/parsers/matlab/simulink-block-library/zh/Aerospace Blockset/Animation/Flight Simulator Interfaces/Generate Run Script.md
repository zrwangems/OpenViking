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

在 R2025b 中未记录。

## 参数

### **选择目标架构** — 要运行脚本的目标平台 `Default` (默认) | `Win64` | `Linux` | `Mac`

从列表中选择要在其上执行运行脚本的目标平台。该平台可以不同于创建运行脚本的平台。如果要生成在创建运行脚本的平台上运行的运行脚本，请选择 `Default`。

- `Win64`
- `Linux`
- `Mac`

#### 程序化使用

|  |
| --- |
| **模块参数**: `Architecture` |
| **类型**: character vector |
| **值：** `'Win64' | 'Linux' | 'Mac'` |
| **默认**: `'Default'` |

### **选择 FlightGear 数据流** — FlightGear 数据流 `Send` (默认) | `Receive` | `Send-Receive`

从列表中选择数据流的方向：

- `Send`

  创建运行脚本以设置将 `net_fdm` 控制模型从 Simulink 发送到 FlightGear。
- `Receive`

  创建运行脚本以设置将 `net_ctrl` 控制模型从 FlightGear 接收到 Simulink。
- `Send-Receive`

  创建运行脚本以设置 FlightGear 接收和广播往返于 Simulink 的数据。

  **注意**

  选择 `Send-Receive` 选项并不意味着您会收到与发送相同的数据（例如，您可能看不到操纵面位置数据）。使用此选项，您主要会看到用户输入（例如通过操纵杆输入的数据）和环境数据。

#### 程序化使用

|  |
| --- |
| **模块参数**: `dataFlow` |
| **类型**: character vector |
| **值：** `'Receive' | 'Send-Receive'` |
| **默认**: `'Send'` |

### **FlightGear 几何模型名称** — 包含 FlightGear 几何模型的文件夹 HL20 (默认)

指定您希望在 *`FlightGear`*`\data\Aircraft` 文件夹中使用的模型几何体所在的文件夹名称。

#### 程序化使用

|  |
| --- |
| **模块参数**: `GeometryModelName` |
| **类型**: character vector |
| **值：**`'HL20'` |
| **默认**: `'HL20'` |

### **机场 ID** — 支持的机场的 ID KSFO (默认)

支持的机场的 ID，从 FlightGear 界面中 **Location** 下可用的受支持机场列表中选择。

#### 程序化使用

|  |
| --- |
| **模块参数**: `'AirportId'` |
| **类型**: character vector |
| **值：**`'KSFO'` |
| **默认**: `'KSFO'` |

### **跑道 ID** — 支持的跑道的 ID 10L (默认)

指定跑道 ID。

#### 程序化使用

|  |
| --- |
| **模块参数**: `RunwayId` |
| **类型**: character vector |
| **值：**`'10L'` |
| **默认**: `'10L'` |

### **初始高度 (ft)\*** — 飞机的初始高度 7224 | numeric

飞机的初始高度，以英尺为单位。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InitialAltitude` |
| **类型**: character vector |
| **值：**`'7224'` |
| **默认**: `'7224'` |

### **初始航向 (deg)\*** — 飞机的初始航向 113 | numeric

飞机的初始航向，以度为单位。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InitialHeading` |
| **类型**: character vector |
| **值：**`'113'` |
| **默认**: `'113'` |

### **偏移距离 (miles)\*** — 偏移距离 4.72 | numeric

飞机距机场的偏移距离，以英里为单位。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OffsetDistance` |
| **类型**: character vector |
| **值：**`'4.72'` |
| **默认**: `'4.72'` |

### **偏移方位角 (deg)\*** — 飞机偏移方位角 0 | numeric

飞机的偏移方位角，以度为单位。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OffsetAzimuth` |
| **类型**: character vector |
| **值：**`'0'` |
| **默认**: `'0'` |

### **在仿真期间安装 FlightGear 场景 (需要 Internet 连接)** — 安装 FlightGear 场景 `off` (默认) | `on`

选中此复选框可指示 FlightGear 在仿真器运行时自动安装所需场景。选中此复选框需要稳定的 Internet 连接。对于 Windows® 系统，在启用此选项的情况下启动 FlightGear 时，您可能会遇到错误消息。有关详细信息，请参阅安装其他 FlightGear 场景。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InstallScenery` |
| **类型**: character vector |
| **值：**`'off' | 'on'` |
| **默认**: `'off'` |

### **禁用 FlightGear 着色器选项** — 禁用 FlightGear 着色器 `off` (默认) | `on`

选中此复选框可禁用 FlightGear 着色器选项。您的计算机内置显卡（例如 NVIDIA® 卡）可能会与 FlightGear 着色器冲突。如果您遇到此冲突，请考虑选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `DisableShaders` |
| **类型**: character vector |
| **值：**`'off' | 'on'` |
| **默认**: `'off'` |

### **目标/源 IP 地址** — 运行 MATLAB 的计算机的网络 IP 地址 127.0.0.1

运行 MATLAB 的计算机的网络 IP 地址。此值为只读。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OriginAddress` |
| **类型**: character vector |
| **值：**`'127.0.0.1'` |
| **默认**: `'127.0.0.1'` |

### **目标端口** — FlightGear 计算机的目标端口 5502

网络飞行动力学模型 (fdm) 端口。有关详细信息，请参阅 Send net\_fdm Packet to FlightGear 模块参考。

#### 程序化使用

|  |
| --- |
| **模块参数**: `DestinationPort` |
| **类型**: character vector |
| **值：**`'5502'` |
| **默认**: `'5502'` |

### **源端口** — FlightGear 计算机的源端口 5505

网络控制 (`ctrl`) 端口。有关详细信息，请参阅 Receive net\_ctrl Packet from FlightGear 模块。

#### 程序化使用

|  |
| --- |
| **模块参数**: `OriginPort` |
| **类型**: character vector |
| **值：**`'5505'` |
| **默认**: `'5505'` |

### **网络 IP 地址** — FlightGear 计算机的网络 IP 地址 127.0.0.1

运行 MATLAB 软件的计算机的网络 IP 地址。

#### 程序化使用

|  |
| --- |
| **模块参数**: `LocalAddress` |
| **类型**: character vector |
| **值：**`'127.0.0.1'` |
| **默认**: `'127.0.0.1'` |

### **输出文件名** — 输出文件 `runfg.bat`

输出文件名。该文件名是用于使用这些初始参数启动 FlightGear 的命令的名称。

**注意**

运行脚本文件名必须由 ASCII 字符组成。

请使用以下文件扩展名：

| 平台 | 扩展名 |
| --- | --- |
| Windows | `.bat` |
| Linux® 和 macOS | `.sh` |

#### 程序化使用

|  |
| --- |
| **模块参数**: `OutputFileName` |
| **类型**: character vector |
| **值：**`'runfg.bat'` |
| **默认**: `'runfg.bat'` |

### **FlightGear 基础目录** — FlightGear 基础目录 `C:\Program Files\FlightGear`

指定 FlightGear 安装文件夹的名称。

**注意**

FlightGear 必须安装在由 ASCII 字符组成的文件夹路径名中。

#### 程序化使用

|  |
| --- |
| **模块参数**: `FlightGearBaseDirectory` |
| **类型**: character vector |
| **值：**`'C:\Program Files\FlightGear'` |
| **默认**: `'C:\Program Files\FlightGear'` |

### **生成脚本** — 生成脚本按钮 按钮

单击 **生成脚本** 生成 FlightGear 的运行脚本。在对话框中输入正确的参数信息之前，请勿单击此按钮。

## 所属库

Aerospace Blockset / Animation / Flight Simulator Interfaces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**R2006a 之前引入**

## 描述

在当前平台上生成 FlightGear 运行脚本

Generate Run Script 模块在当前平台上生成自定义的 FlightGear 运行脚本。

要生成运行脚本，请在参数字段中填写所需信息，然后单击 **生成脚本**。

在对话框中，带星号 (\*) 标记的字段将作为 MATLAB® 表达式求值。其他字段则视为字面文本。
