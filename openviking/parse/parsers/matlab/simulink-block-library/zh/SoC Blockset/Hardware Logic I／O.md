---
type: simulink-block
title: 'Hardware I/O Devices'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'hardware-io-devices'
documentation_source_path: 'hardware-io-devices.html'
language: zh-CN
chinese_source: worker-translation
---

# Hardware I/O Devices

Hardware I/O Devices

对板卡上的 IO 设备与 FPGA 逻辑之间的连接进行建模

使用这些模块创建模型，以仿真 SoC 设计与这些 IO 设备之间的连接。

## 模块

|  |  |
| --- | --- |
| AD936x Receiver | 从基于 AD936x 的 Zynq 无线电硬件接收数据 *(自 R2024b 起)* |
| AD936x Transmitter | 向基于 AD936x 的 Zynq 无线电硬件发送数据 *(自 R2024b 起)* |
| AD936x Data Read | 从基于 AD936x 的 Zynq 无线电硬件读取数据 *(自 R2024b 起)* |
| AD936x Data Write | 向基于 AD936x 的 Zynq 无线电硬件写入数据 *(自 R2024b 起)* |
| HDMI Rx | 将视频流转换为 YCbCr 4:2:2 像素流 |
| HDMI Tx | 将 YCbCr 4:2:2 像素流转换为视频帧 |
| RF Data Converter | 为硬件逻辑提供 RF 数据路径接口 |
| ADC To Vector | 将拼接的 16 位 ADC 输入采样转换为向量输出 |
| Vector To DAC | 将向量输入转换为拼接的 16 位 DAC 输出采样 |
| RFDC Bus Creator | 将控制信号转换为 RF Data Converter 实时接口兼容总线 *(自 R2022a 起)* |
| RFDC Bus Selector | 将 RF Data Converter 实时接口兼容总线转换为控制信号 *(自 R2022a 起)* |
| OTAVA DTRX2 | 将 OTAVA DTRX2 毫米波无线电卡与 ZCU208 板集成 *(自 R2023a 起)* |
| Aurora 64B66B | 使用 Xilinx Aurora 接口提供高速串行通信 *(自 R2023a 起)* |

## 工具

|  |  |
| --- | --- |
| HDL IP Importer | 将 HDL IP 核导入 SoC 模型 *(自 R2023a 起)* |

## 主题

### 无线应用

- **Introduction To Custom OFDM Using AMD RFSoC**
  使用 SoC Blockset™ 在 AMD® RFSoC 设备上设计并验证自定义 OFDM 通信系统的发射机和接收机。
- **使用 AMD RFSoC 设备进行 OFDM 发送和接收**
  使用 SoC Blockset 在 Xilinx® RFSoC 设备上仿真并部署 OFDM 发射和接收算法。
- **使用 AMD RFSoC 进行 5G NR 信号检测简介**
  使用 SoC Blockset 在 Xilinx RFSoC 设备上部署主同步信号 (PSS) 相关和同步信号块 (SSB) 解调。
- **使用 AMD RFSoC 设备进行 FR1 和 FR2 的 5G NR SIB1 恢复**
  使用 SoC Blockset 在 Xilinx RFSoC 设备上部署适用于 FR1 和 FR2 的 5G NR SIB1 恢复算法。
- **使用 AMD RFSoC 设备进行 5G NR 下行信号测量**
  使用 SoC Blockset 在 Xilinx RFSoC 设备上测量接收资源网格的 SSB 信号质量和误差向量幅度 (EVM)。
- **DVB-S2 HDL PL Header Recovery Using Analog Devices AD9361/AD9364**
  使用 SoC Blockset 部署数字视频广播卫星第二代 (DVB-S2) 时间、频率和相位同步以及 PL 报头恢复算法。
- **DVB-S2 Receive Using AMD RFSoC Device**
  使用 SoC Blockset 在 Xilinx RFSoC 设备上仿真并部署 DVB-S2 发射和接收算法。
- **WLAN Receiver Using AMD RFSoC Device**
  使用 SoC Blockset 在 Xilinx RFSoC 设备上仿真并部署 WLAN 发射和接收算法。
- **Pulse-Doppler Radar Using AMD RFSoC Device**
  使用 SoC Blockset 在 Xilinx RFSoC 设备上构建、仿真并部署脉冲多普勒雷达系统。
- **使用 AMD RFSoC 设备进行 GPS 捕获和跟踪**
  在 ZCU111 评估套件上仿真并部署全球定位系统 (GPS) 捕获算法。
- **Monitor and Analyze Applications Targeted to AMD RFSoC Devices**
  使用 FPGA 数据捕获来监测、分析和调试 RF Data Converter 的 AXI4-Stream 接口的 ADC、DAC 和有效信号。

### 视频应用

- **边缘检测与图像叠加**
  实现一个具有 HDMI 输入和输出的边缘检测与图像叠加系统。
- **使用外部存储器进行垂直视频翻转**
  通过使用随机访问外部存储器接口，对输入视频流进行垂直翻转。
- **使用外部存储器的对比度受限自适应直方图均衡化**
  此示例展示如何为 FPGA 实现对比度受限自适应直方图均衡化（CLAHE）算法，包括外部存储器接口。

## 精选示例

用于 RFSoC 设备的 RF 数据记录与回放

### 用于 RFSoC 设备的 RF 数据记录与回放

从 RFSoC 设备捕获真实世界的 RF 数据，然后在 MATLAB® 和 Simulink® 中使用此数据进行仿真和分析。

- 打开脚本

验证 RF 数据转换器配置

### 验证 RF 数据转换器配置

在仿真中验证 RF 数据转换器（RFDC）配置。

- 打开脚本

使用 AMD RFSoC 设备发送和接收单音 - 第 1 部分 系统设计

### 使用 AMD RFSoC 设备发送和接收单音 - 第 1 部分 系统设计

在 Xilinx RFSoC 设备上使用 SoC Blockset 设计和仿真数据路径。

- 打开脚本

使用 AMD RFSoC 设备发送和接收单音 - 第 2 部分 部署

### 使用 AMD RFSoC 设备发送和接收单音 - 第 2 部分 部署

在 Xilinx RFSoC 设备上使用 SoC Blockset 实现并验证设计。

- 打开脚本

使用 OTAVA DTRX2 毫米波无线电卡发送和接收单音

### 使用 OTAVA DTRX2 毫米波无线电卡发送和接收单音

使用 SoC Blockset 将 OTAVA DTRX2 毫米波无线电卡与 Xilinx
Zynq®
UltraScale+™ RFSoC ZCU208 评估套件集成。

- 打开脚本

使用 AD9361 双通道发送和接收单音

### 使用 AD9361 双通道发送和接收单音

在 Xilinx
Zynq
UltraScale+ MPSoC ZCU102 评估套件上使用 SoC Blockset 设计、仿真和部署带有 AD9361 RF 卡的双通道应用系统。

- 打开脚本

使用 Zynq 和 FMCOMMS2/3/4 进行 QPSK 发送和接收

### 使用 Zynq 和 FMCOMMS2/3/4 进行 QPSK 发送和接收

使用 SoC Blockset 仿真和部署正交相移键控（QPSK）发送和接收算法。

- 打开脚本

使用 Xilinx RFSoC 设备进行跳频

### 使用 Xilinx RFSoC 设备进行跳频

使用 Xilinx RF 数据转换器数控振荡器（NCO）实时端口设计和实现跳频算法。

- 打开脚本

使用 AMD RFSoC 设备检测和捕获宽带雷达信号

### 使用 AMD RFSoC 设备检测和捕获宽带雷达信号

在 Xilinx RFSoC 设备上使用 SoC Blockset 构建、仿真和部署宽带雷达信号检测与捕获系统。

- 打开脚本

将自定义 HDL IP 导入 SoC Blockset 设计

### 将自定义 HDL IP 导入 SoC Blockset 设计

导入 HDL IP 并将其集成到 SoC Blockset 设计中。

- 打开脚本

使用 AMD RFSoC 设备的最小方差无失真响应波束形成器

### 使用 AMD RFSoC 设备的最小方差无失真响应波束形成器

在 AMD RFSoC 设备上部署最小方差无失真响应算法。

- 打开脚本

使用 AMD RFSoC 设备的多片同步

### 使用 AMD RFSoC 设备的多片同步

在 AMD RFSoC 设备上使用 RF Data Converter 模块实现并使用多片同步。

- 打开脚本

## MATLAB 命令

您点击了一个对应于某个 MATLAB 命令的链接：

在 MATLAB Command Window 中输入该命令以运行它。
Web 浏览器不支持 MATLAB 命令。

Close

MathWorks
MathWorks

Select a Web Site

选择一个网站，以获取可用的翻译内容并查看本地活动和优惠。根据您的位置，我们建议您选择：

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择一个网站

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

亚太地区

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
