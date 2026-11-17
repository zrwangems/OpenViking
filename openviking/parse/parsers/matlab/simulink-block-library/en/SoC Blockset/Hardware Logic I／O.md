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
language: en
---

# Hardware I/O Devices

Hardware I/O Devices

Model the connection between the IO devices on your board and your FPGA
logic

Use these blocks to create models that simulate the connection between
your SoC design and these IO devices.

## Blocks

|  |  |
| --- | --- |
| AD936x Receiver | Receive data from AD936x-based Zynq radio hardware *(Since R2024b)* |
| AD936x Transmitter | Send data to AD936x-based Zynq radio hardware *(Since R2024b)* |
| AD936x Data Read | Read data from AD936x-based Zynq radio hardware *(Since R2024b)* |
| AD936x Data Write | Write data to AD936x-based Zynq radio hardware *(Since R2024b)* |
| HDMI Rx | Convert video stream to YCbCr 4:2:2 pixel stream |
| HDMI Tx | Convert YCbCr 4:2:2 pixel stream to video frame |
| RF Data Converter | Provide RF data path interface to hardware logic |
| ADC To Vector | Convert concatenated 16-bit ADC input samples to vector outputs |
| Vector To DAC | Convert vector inputs to concatenated 16-bit DAC output samples |
| RFDC Bus Creator | Convert control signals into RF Data Converter real-time interface-compatible bus *(Since R2022a)* |
| RFDC Bus Selector | Convert RF Data Converter real-time interface-compatible bus into control signals *(Since R2022a)* |
| OTAVA DTRX2 | Integrate OTAVA DTRX2 mmWave radio card with ZCU208 board *(Since R2023a)* |
| Aurora 64B66B | Provide high-speed serial communication using Xilinx Aurora interface *(Since R2023a)* |

## Tools

|  |  |
| --- | --- |
| HDL IP Importer | Import HDL IP core into SoC model *(Since R2023a)* |

## Topics

### Wireless Applications

- **Introduction To Custom OFDM Using AMD RFSoC**
  Design and verify a transmitter and receiver for a custom OFDM communication system by
  using SoC Blockset™ on AMD® RFSoC device.
- **OFDM Transmit and Receive Using AMD RFSoC Device**
  Simulate and deploy OFDM transmit and receive algorithm using SoC Blockset on Xilinx® RFSoC device.
- **Introduction to 5G NR Signal Detection using AMD RFSoC**
  Deploy primary synchronization signal (PSS) correlation and synchronization signal block (SSB) demodulation using SoC Blockset on Xilinx RFSoC device.
- **5G NR SIB1 Recovery for FR1 and FR2 Using AMD RFSoC Device**
  Deploy 5G NR SIB1 recovery algorithm for FR1 and FR2 using SoC Blockset on Xilinx RFSoC device.
- **5G NR Downlink Signal Measurements Using AMD RFSoC Device**
  Measure SSB signal quality and error vector magnitude (EVM) of the received resource grid using SoC Blockset on Xilinx RFSoC device.
- **DVB-S2 HDL PL Header Recovery Using Analog Devices AD9361/AD9364**
  Deploy Digital Video Broadcasting Satellite Second Generation (DVB-S2) time,
  frequency, and phase synchronization and PL header recovery algorithm using SoC Blockset.
- **DVB-S2 Receive Using AMD RFSoC Device**
  Simulate and deploy DVB-S2 transmit and receive algorithm using SoC Blockset on Xilinx RFSoC device.
- **WLAN Receiver Using AMD RFSoC Device**
  Simulate and deploy WLAN transmit and receive algorithm using SoC Blockset on Xilinx RFSoC device.
- **Pulse-Doppler Radar Using AMD RFSoC Device**
  Build, simulate, and deploy pulse-Doppler radar system using SoC Blockset on Xilinx RFSoC device.
- **GPS Acquisition and Tracking Using AMD RFSoC Device**
  Simulate and deploy global positioning system (GPS) acquisition algorithm on ZCU111
  evaluation kit.
- **Monitor and Analyze Applications Targeted to AMD RFSoC Devices**
  Monitor, analyze, and debug ADC, DAC, and valid signals of AXI4-Stream interface of RF
  Data Converter using FPGA data capture.

### Video Applications

- **Edge Detection and Image Overlay**
  Implement an edge detection and image overlay system with HDMI input and
  output.
- **Vertical Video Flipping Using External Memory**
  Flip an incoming video stream vertically by using a random-access external memory
  interface.
- **Contrast Limited Adaptive Histogram Equalization with External Memory**
  This example shows how to implement the contrast-limited adaptive histogram equalization (CLAHE) algorithm for FPGA, including an external memory interface.

## Featured Examples

RF Data Recording and Playback for RFSoC Devices

### RF Data Recording and Playback for RFSoC Devices

Capture real-world RF data from RFSoC devices, and then use this data in MATLAB® and Simulink® for simulation and analysis.

- Open Script

Validate RF Data Converter Configuration

### Validate RF Data Converter Configuration

Validate RF data converter (RFDC) configuration in simulation.

- Open Script

Transmit and Receive Tone Using AMD RFSoC Device - Part 1 System Design

### Transmit and Receive Tone Using AMD RFSoC Device - Part 1 System Design

Design and simulate data path using SoC Blockset on Xilinx RFSoC device.

- Open Script

Transmit and Receive Tone Using AMD RFSoC Device - Part 2 Deployment

### Transmit and Receive Tone Using AMD RFSoC Device - Part 2 Deployment

Implement and verify design using SoC Blockset on Xilinx RFSoC device.

- Open Script

Transmit and Receive Tone Using OTAVA DTRX2 mmWave Radio Card

### Transmit and Receive Tone Using OTAVA DTRX2 mmWave Radio Card

Integrate OTAVA DTRX2 mmWave radio card with Xilinx
Zynq®
UltraScale+™ RFSoC ZCU208 Evaluation Kit using SoC Blockset.

- Open Script

Transmit and Receive Tones Using AD9361 Dual-Channels

### Transmit and Receive Tones Using AD9361 Dual-Channels

Design, simulate, and deploy dual-channel application system with AD9361 RF card using
SoC Blockset on Xilinx
Zynq
UltraScale+ MPSoC ZCU102 Evaluation Kit.

- Open Script

QPSK Transmit and Receive Using Zynq and FMCOMMS2/3/4

### QPSK Transmit and Receive Using Zynq and FMCOMMS2/3/4

Simulate and deploy quadrature phase-shift keying (QPSK) transmit and receive
algorithm using SoC Blockset.

- Open Script

Frequency Hopping Using Xilinx RFSoC Device

### Frequency Hopping Using Xilinx RFSoC Device

Design and implement frequency hopping algorithm using Xilinx RF Data Converter numerically controlled oscillator (NCO) real time
ports.

- Open Script

Detect and Capture Wideband Radar Signal Using AMD RFSoC Device

### Detect and Capture Wideband Radar Signal Using AMD RFSoC Device

Build, simulate, and deploy wideband radar signal detection and capture system using
SoC Blockset on Xilinx RFSoC device.

- Open Script

Import Custom HDL IP into SoC Blockset Design

### Import Custom HDL IP into SoC Blockset Design

Import HDL IP and integrate it into SoC Blockset design.

- Open Script

Minimum Variance Distortionless Response Beamformer Using AMD RFSoC Device

### Minimum Variance Distortionless Response Beamformer Using AMD RFSoC Device

Deploy minimum variance distortionless response algorithm on AMD RFSoC device.

- Open Script

Multi-Tile Synchronization Using AMD RFSoC Device

### Multi-Tile Synchronization Using AMD RFSoC Device

Implement and use multi-tile synchronization using RF Data Converter block on
AMD RFSoC device.

- Open Script

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: .

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

You can also select a web site from the following list

**How to Get Best Site Performance**

Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.

Americas

- América Latina (Español)
- Canada (English)
- United States (English)

Europe

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

Asia Pacific

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

Contact your local office
