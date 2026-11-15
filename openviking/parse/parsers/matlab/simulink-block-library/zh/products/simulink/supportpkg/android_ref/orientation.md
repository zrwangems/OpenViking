---
type: simulink-block
title: 'Orientation'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Sensors'
documentation_page: 'orientation'
documentation_source_path: 'supportpkg/android_ref/orientation.html'
language: zh-CN
chinese_source: worker-translation
---

# Orientation

## 端口

### 输出

### **Port\_1** — Android 设备旋转向量

该模块将旋转输出为 1×3 向量。向量元素表示沿 Android 设备的 X、Y 和 Z 轴的旋转，单位为 degrees。

**数据类型：** `single`

## 参数

### **Sample time** — 模块读取数据的频率 `0.1`（默认）| `-1` | 任意正整数

指定模块读取旋转的频率。将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 读取 Android 设备的 Orientation

此 Simulink 模型包含一个 Orientation 模块和一个 Data Display 模块。Orientation 模块根据 Android 设备上的内置加速度计和磁力计传感器计算 Pitch、Roll 和 Azimuth。该模块将旋转输出为 1×3 向量。Data Display 模块接受该向量并在 Android 设备上显示这些值。

要运行模型：

1. 使用 USB 线缆将 Android 设备连接到计算机。
2. 按照 Install Support for Android Devices 中所述，安装 Simulink Support Package for Android Devices。
3. 在工具条的 **Modeling** 选项卡中，选择 **Model Settings**。
4. 在 Configuration Parameters 对话框中，选择 **Hardware Implementation**。
5. 将 **Hardware board** 参数设置为 `Android Device`。此选择会自动使用 Android 的默认值填充 **Hardware board settings** 中的参数。
6. 在 **Target hardware resources** 下的 **Groups** 列表中，选择 **Device options**。
7. 在 **Device** 列表中，选择您的 Android 设备。如果您的设备未列出，请点击 **Refresh**。

   **注意**

   如果点击 **Refresh** 按钮后您的设备仍未列出，请确保您已在设备上启用 **USB debugging** 选项。要启用 **USB debugging**，请在 MATLAB® 命令窗口中输入 `androidhwsetup`，并按照屏幕上的说明操作。
8. 点击 **Apply** 保存更改。点击 **OK**。
9. 在 Simulink 编辑器工具栏上，点击 Build Model 按钮。模型会加载并开始在设备上运行。方向会显示在设备屏幕上。移动您的 Android 设备，并观察屏幕上显示的这些值的变化。

## 所属库

Simulink Support Package for Android Devices / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

测量设备沿 X、Y 和 Z 轴的旋转

Orientation 模块读取 Android™ 设备的旋转。该旋转使用三个角度量测量：Pitch（绕 X 轴）、Roll（绕 Y 轴）和 Azimuth（绕 Z 轴）。该模块以 1×3 向量形式输出这些角度，单位为 degrees。

在没有硬件的情况下进行仿真时，此模块输出零。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation。

此图显示了典型 Android 手机的 X、Y 和 Z 轴。每个轴都有一个指向正方向的箭头。

**注意**

- 即使移动设备，坐标系也保持不变。
- 对于具有不同自然方向的设备，坐标系也不同。例如，大多数 Android 手机的自然方向是竖屏，而大多数 Android 平板电脑的自然方向是横屏。因此，Android 平板电脑的坐标系与此图所示的坐标系不同。
