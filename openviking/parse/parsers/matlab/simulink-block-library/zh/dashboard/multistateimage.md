---
type: simulink-block
title: 'MultiStateImage'
family: dashboard
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'multistateimage'
language: zh-CN
chinese_source: worker-translation
---

# MultiStateImage

## 端口

R2025b 官方文档未提供。

## 参数

### **连接** — 要连接的信号以及显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 Dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® Toolstrip 或“块参数”对话框中的 **连接** 表。有关连接模式以及如何使用 Toolstrip 进行连接的信息，请参阅 Connect Dashboard Blocks to Simulink Model。

要使用 **连接** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接该模块，请在属性检查器的 **参数** 选项卡上单击 **连接**。要更改该模块的连接，请改为单击 **更改**。
3. 选择要连接到的信号线。
4. 在表中，选择要连接到的信号。
5. 单击 **应用**。

您还可以将 Dashboard 模块连接到 Stateflow 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数：** `Binding` |
| **类型：** `Simulink.HMI.SignalSpecification` |
| **默认：** `[]` |

### **缩放模式** — 指定如何缩放图像 `Fill with fixed aspect ratio`（默认） | `Fixed` | `Fill`

指定如何缩放图像。

**Fill with fixed Aspect Ratio** 将图像缩放到模块大小，同时保留其原始宽高比。

**Fixed** 以固定的真实大小显示图像。

**Fill** 调整图像以填充模块。

#### 编程用法

|  |
| --- |
| **模块参数：** `ScaleMode` |
| **类型：** string or character vector |
| **值：** `'Fill with fixed aspect ratio'` | `'Fixed'` | `'Fill'` |
| **默认：** `'Fill with fixed aspect ratio'` |

### **States** — 将值与图像匹配以显示标量和图像

States 将要显示的图像与所连接变量或参数的值进行匹配。每个状态由一个 **State** 和一个图像组成，并在 MultiStateImage 模块的 **States** 表中显示为 **Thumbnail**。

- **State** — 所连接变量或参数的值，该值使 MultiStateImage 模块显示对应图像。
- **Thumbnail** — 当所连接变量或参数的值与对应的 **State** 匹配时要显示的图像。

单击 **+** 按钮以添加另一个状态。

#### 编程用法

要以编程方式为 MultiStateImage 模块配置 `State` 和 `Thumbnail` 参数值，请使用 `States` 参数。将 `States` 参数的值指定为包含以下字段的结构体数组：

- `State` — 状态值。
- `Size` — `1`-by-`2` 向量，按顺序包含图像的宽度和高度（以像素为单位），指定为 `uint64`。
- `Image` — Base64 编码图像数据的字符数组。
- `Thumbnail` — 用于在块对话框中 **States** 表内显示的缩略图图像的 Base64 编码图像数据的字符数组。

对于要为该模块指定的每个状态，在数组中包含一个结构体。在示例中，`myBase64Image` 和 `myBase64Thumbnail` 变量包含用于模块图像和缩略图的 Base64 图像数据的字符向量。

    state1.State = 1;
    state1.Size = [uint64(400) uint64(400)];
    state1.Image = myBase64Image;
    state1.Thumbnail = myBase64Thumbnail;
    state2.State = 2;
    state2.Size = uint64(400) uint64(400)];
    state2.Image = myBase64Image2;
    state2.Thumbnail = myBase64Thumbnail2;
    msiStates = [state1 state2];

|  |
| --- |
| **模块参数：** `States` |
| **类型：** structure array |

当所连接信号的值不对应任何指定状态时，该模块显示默认图像。将 `DefaultImage` 参数指定为包含以下字段的结构体：

- `Size` — `1`-by-`2` 向量，按顺序包含图像的宽度和高度（以像素为单位），指定为 `uint64`。
- `Image` — Base64 编码图像数据的字符数组。
- `Thumbnail` — 用于在块对话框中 **States** 表内显示的缩略图图像的 Base64 编码图像数据的字符数组。

|  |
| --- |
| **模块参数：** `DefaultImage` |
| **类型：** structure |

### **标签** — 模块标签位置 `Top`（默认） | `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签为所连接元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数：** `LabelPosition` |
| **类型：** character vector |
| **值：** `'Top'` | `'Bottom'` | `'Hide'` |
| **默认：** `'Top'` |

## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2016b 中引入**

## 描述

显示反映输入值的图像

MultiStateImage 模块显示图像以指示输入信号的值。您可以将 MultiStateImage 模块与其他 Dashboard 模块一起使用，为您的模型构建由控件和指示器组成的交互式仪表板。您可以指定输入值和图像的配对，以在仿真期间提供所需信息。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 Dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请将鼠标悬停在要连接的模块上，并单击连接按钮。要在已连接的模块上进入连接模式，请选择该模块，将鼠标悬停在出现的省略号 (…) 上，然后在展开的操作菜单中，单击连接按钮。

要将显示模块连接到模型中的信号，或更改显示模块的连接，请进入连接模式。选择要连接到的信号线。在出现的列表中，选择要连接到的信号。然后，将鼠标悬停在 Dashboard 模块上，并单击完成连接按钮。要查看 Dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 Dashboard 模块的详细信息，请参阅 Connect Dashboard Blocks to Simulink Model。

您还可以将 Dashboard 模块连接到 Stateflow® 图。有关详细信息，请参阅 Connect Dashboard Blocks to Stateflow (Stateflow)。

此动画显示如何将 MultiStateImage 模块连接到您的模型。

未连接的 MultiStateImage 模块连接到 Pulse Generator 模块发送到 Display 模块的信号。
