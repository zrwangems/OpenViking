---
type: simulink-block
title: 'Read Point Cloud'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'readpointcloudros1'
documentation_source_path: 'ref/readpointcloudros1.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Point Cloud

## 端口

### 输入

### **Msg** — ROS `sensor_msgs/PointCloud2` 消息，非虚拟总线

ROS `sensor_msgs/PointCloud2` 消息，指定为非虚拟总线。您可以使用 Subscribe 模块从 ROS 网络获取消息。

**数据类型：** `bus`

### 输出

### **XYZ** — XYZ 坐标矩阵 | 数组

点云数据中每个点的 *x*、*y* 和 *z* 坐标，返回为 *N*×3 矩阵或 *h*×*w*×3 数组。*N* 是点云中的点数。*h* 和 *w* 是图像的高度和宽度，以 pixels 为单位。若要以数组形式获取 *x*、*y* 和 *z* 坐标，请选择 **Preserve point cloud structure** 参数。

**数据类型：** `single`

### **RGB** — 每个点的 RGB 值 矩阵 | 数组

点云数据中每个点的 RGB 值，输出为 *N*×3 矩阵或 *h*×*w*×3 数组。*N* 是点云中的点数。*h* 和 *w* 是图像的高度和宽度，以 pixels 为单位。RGB 值指定红色、绿色和蓝色颜色强度，范围为 `[0,1]`。若要以数组形式返回 RGB 值，请选择 **Preserve point cloud structure** 参数。

**数据类型：** `double`

### **Intensity** — 每个点的强度值 数组 | 矩阵

点云数据中每个点的强度值，返回为数组或 *h*×*w* 矩阵。*h* 和 *w* 是图像的高度和宽度，以 pixels 为单位。若要以矩阵形式返回强度值，请选择 **Preserve point cloud structure** 参数。

**数据类型：** `single`

### **ErrorCode** — 图像转换的错误代码 标量

图像转换的错误代码，返回为标量。错误代码值包括：

- `0` – 成功转换点云消息。
- `1` – 传入点云的维度超过 **Maximum point cloud size** 参数中设置的限制。
- `2` – 传入消息中的一个可变长度数组被截断。有关增加数组最大长度的详细信息，请参阅 Manage Array Sizes for ROS Messages in Simulink。
- `3` – 点云消息的 `X`、`Y` 或 `Z` 字段缺失。
- `4` – 点云不包含任何 RGB 颜色数据。仅当您启用 **Show RGB output port** 参数时，才会出现此错误。
- `5` – 点云不包含任何强度数据。仅当您启用 **Show Intensity output port** 参数时，才会出现此错误。

对于某些错误代码，该模块会截断数据或在适当情况下用 `NaN` 值填充。

**数据类型：** `uint8`

## 参数

### **Maximum point cloud size** — 最大点云图像大小 `[480 640]`（默认） | 二元素向量

最大点云图像大小，指定为二元素 `[height width]` 向量。

选择 **Configure using ROS** 以使用 ROS 网络上的活动话题自动设置此参数。您必须已连接到 ROS 网络。

### **Preserve point cloud structure** — 点云数据输出形状保留 `off`（默认） | `on`

当选择此参数时，模块会为 **XYZ**、**RGB** 和 **Intensity** 输出保留点云数据输出形状。每个输出对应于原始图像的分辨率。**XYZ** 和 **RGB** 输出变为多维数组，**Intensity** 输出变为矩阵。

### **Show RGB output port** — `RGB` 端口开关 `off`（默认） | `on`

选择此参数以启用 **RGB** 端口。如果启用此参数，消息必须包含 RGB 数据，否则模块将返回错误代码。

### **Show Intensity output port** — `Intensity` 端口开关 `off`（默认） | `on`

选择此参数以启用 **Intensity** 端口。如果启用此参数，消息必须包含强度数据，否则模块将返回错误代码。

### **Show ErrorCode output port** — `ErrorCode` 端口开关 `on`（默认） | `off`

选择此参数以启用 **ErrorCode** 端口并监视错误。

### **Output variable-size signals** — 可变大小信号输出开关 `off`（默认） | `on`

切换是否输出可变大小信号。仅当您预计图像大小会随时间变化时，才使用可变大小信号。有关可变大小信号的详细信息，请参阅 Variable-Size Signal Basics (Simulink)。

## 所属库

ROS Toolbox / ROS

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

从 ROS PointCloud2 消息中提取点云

Read Point Cloud 模块从 ROS `sensor_msgs/PointCloud2` 消息中提取点云。您可以选择在实时 ROS 网络上处于活动状态的话题的 ROS 消息参数，也可以单独指定消息参数。ROS 消息指定为非虚拟总线。使用 Subscribe 模块从 ROS 网络接收消息，并将该消息输入到 Read Point Cloud 模块。

**注意**

从网络读取 ROS 点云消息时，消息的 `Data` 属性可能超过 Simulink® 中设置的最大数组长度。要为模型中的所有消息类型增加最大数组长度，请在 **Simulation** 选项卡下的 **Prepare** 部分中，选择 **ROS Toolbox**  > **Variable Size Messages**。取消选中 **Use default limits for this message type**，然后在 **Maximum length** 列中，根据点云中的点数增加长度。
