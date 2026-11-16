---
type: simulink-block
title: 'MultiStateImage'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Dashboard'
documentation_page: 'multistateimage'
documentation_source_path: 'slref/multistateimage.html'
language: zh-CN
chinese_source: worker-translation
---

# MultiStateImage

## 端口

在 R2025b 中未记录。

## 参数

### **连接** — 要连接的信号和显示信号连接选项

Dashboard 模块不使用端口连接到模型元素。要将 dashboard 模块连接到模型中的参数值，请使用连接模式、Simulink® Toolstrip 或 **Block Parameters** 对话框中的 **连接** 表。有关连接模式以及如何使用 toolstrip 进行连接的信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

要使用 **连接** 表连接显示模块或更改显示模块的连接：

1. 选择该模块。
2. 要连接模块，请在属性检查器中，在 **参数** 选项卡上，单击 **Connect**。要更改模块的连接，请改为单击 **Change**。
3. 选择要连接到的信号线。
4. 在表中，选择要连接到的信号。
5. 单击 **Apply**。

您还可以将 dashboard 模块连接到 Stateflow 图表。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

#### 编程用法

|  |
| --- |
| **模块参数:** `Binding` |
| **类型:** `Simulink.HMI.SignalSpecification` |
| **默认值:** `[]` |

### **缩放模式** — 指定如何缩放图像 `Fill with fixed aspect ratio`（默认）| `Fixed` | `Fill`

指定如何缩放图像。

**Fill with fixed Aspect Ratio** 在保留原始宽高比的同时将图像缩放到模块大小。

**Fixed** 以固定的真实大小显示图像。

**Fill** 调整图像以填充模块。

#### 编程用法

|  |
| --- |
| **模块参数:** `ScaleMode` |
| **类型:** string 或 character vector |
| **值:** `'Fill with fixed aspect ratio'` | `'Fixed'` | `'Fill'` |
| **默认值:** `'Fill with fixed aspect ratio'` |

### **状态** — 将值与图像匹配以显示标量和图像

状态将图像与要显示的值（连接的变量或参数的值）匹配。每个状态包含一个 **State** 和一个图像，并在 MultiStateImage 模块的 **States** 表中显示为 **Thumbnail**。

- **State** — 使 MultiStateImage 模块显示对应图像的已连接变量或参数值。
- **Thumbnail** — 当已连接变量或参数值与对应 **State** 匹配时要显示的图像。

单击 **+** 按钮以添加另一个状态。

#### 编程用法

要以编程方式为 MultiStateImage 模块配置 `State` 和 `Thumbnail` 参数值，请使用 `States` 参数。将 `States` 参数的值指定为结构体数组，其中字段包括：

- `State` — 状态值。
- `Size` — `1`-by-`2` 向量，按顺序包含图像的宽度和高度，单位为 pixels，指定为 `uint64`。
- `Image` — Base64 编码图像数据的字符数组。
- `Thumbnail` — Base64 编码图像数据的字符数组，用于在模块对话框的 **States** 表中显示的缩略图图像。

对于要为模块指定的每个状态，在数组中包含一个结构体。在示例中，`myBase64Image` 和 `myBase64Thumbnail` 变量包含模块图像和缩略图的 Base64 图像数据的字符向量。

```
state1.State = 1;
state1.Size = [uint64(400) uint64(400)];
state1.Image = myBase64Image;
state1.Thumbnail = myBase64Thumbnail;
state2.State = 2;
state2.Size = uint64(400) uint64(400)];
state2.Image = myBase64Image2;
state2.Thumbnail = myBase64Thumbnail2;
msiStates = [state1 state2];
```

|  |
| --- |
| **模块参数:** `States` |
| **类型:** structure array |

当连接信号值不对应任何指定状态时，模块显示默认图像。将 `DefaultImage` 参数指定为包含以下字段的结构体：

- `Size` — `1`-by-`2` 向量，按顺序包含图像的宽度和高度，单位为 pixels，指定为 `uint64`。
- `Image` — Base64 编码图像数据的字符数组。
- `Thumbnail` — Base64 编码图像数据的字符数组，用于在模块对话框的 **States** 表中显示的缩略图图像。

|  |
| --- |
| **模块参数:** `DefaultImage` |
| **类型:** structure |

### **标签** — 模块标签位置 `Top`（默认）| `Bottom` | `Hide`

模块标签的位置。当模块连接到模型中的元素时，标签是所连接元素的名称。

#### 编程用法

|  |
| --- |
| **模块参数:** `LabelPosition` |
| **类型:** character vector |
| **值:** `'Top'` | `'Bottom'` | `'Hide'` |
| **默认值:** `'Top'` |

## 所属库

Simulink / Dashboard

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Dashboard 模块在代码生成时会被忽略。

## 版本历史

**在 R2016b 中引入**

## 描述

显示反映输入值的图像

MultiStateImage 模块显示图像以指示输入信号的值。您可以将 MultiStateImage 模块与其他 Dashboard 模块一起使用，为模型构建包含控件和指示器的交互式仪表板。您可以指定输入值和图像对，以在仿真期间提供所需信息。

### 连接 Dashboard 模块

Dashboard 模块不使用端口连接到模型元素。要连接 dashboard 模块，请使用连接模式。要在未连接的模块上进入连接模式，请暂停在要连接的模块上，然后单击 Connect 按钮。要在已连接的模块上进入连接模式，请选择该模块，暂停在出现的省略号 (…) 上，然后在展开的操作菜单中单击 Connect 按钮。

要将显示模块连接到模型中的信号，或更改显示模块的连接，请进入连接模式。选择要连接到的信号线。从出现的列表中，选择要连接到的信号。然后，暂停在 dashboard 模块上，并单击 Done Connecting 按钮。要查看 dashboard 模块显示所连接模块的值，请运行仿真。

有关连接 dashboard 模块的详细信息，请参阅将 Dashboard 模块连接到 Simulink 模型。

您还可以将 dashboard 模块连接到 Stateflow® 图表。有关详细信息，请参阅将 Dashboard 模块连接到 Stateflow (Stateflow)。

此动画展示如何将 MultiStateImage 模块连接到模型。

未连接的 MultiStateImage 模块连接到 Pulse Generator 模块发送到 Display 模块的信号。
