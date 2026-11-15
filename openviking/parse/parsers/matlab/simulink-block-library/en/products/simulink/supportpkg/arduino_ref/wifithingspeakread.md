---
type: simulink-block
title: 'WiFi ThingSpeak Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifithingspeakread'
documentation_source_path: 'supportpkg/arduino_ref/wifithingspeakread.html'
language: en
---

# WiFi ThingSpeak Read

## Ports

### Output

### **fieldn** — Data read from nth field of ThingSpeak channel [`1` x *N*] vector, where *N* ranges from [`1` to `8`]

The block outputs the data read from the nth field in the ThingSpeak channel at each time step. The number of data channels at the block
output depends on the number of fields that you enter in the **Fields to read** parameter. For example, if you set the **Fields to read** parameter to [`1 4 5`], the
block enables three output ports with port names **field1**, **field4**, and **field5**. If the data received from the channel is null, the
block outputs `0`.

**Data Types:** `single`

### **status** — ThingSpeak server response for each read request scalar

The block outputs the ThingSpeak server response for the read request at each time step. The response is
received as an HTTP status code. An HTTP status code of `200`
indicates that the read request is successfully completed. For more information on
HTTP status codes, see `matlab.net.http.StatusCode`.

If the data received is null, the port outputs `0`.

**Example:** An HTTP status code of `200` indicates that the read
request is successfully completed. Whereas, an HTTP status code of
`204`, indicates that the data received on the data channel is
null.

**Data Types:** `single`

## Parameters

### **Channel ID** — Channel ID from which block reads data `12397` (default) | any positive integer

Specify the channel ID from which the block reads data.

If you do not know the channel ID of your channel:

1. Sign In
   to ThingSpeak using your MathWorks® Account.
2. Select **Channels** > **My Channels**.
3. Select the channel from which to read data.
4. Click the **Channel Settings** tab.
5. Copy the channel ID from the **Channel ID** parameter.
6. Open the ThingSpeak Read block in your model and paste the copied
   ID to the **Channel ID** parameter.

### **Channel access** — Sharing settings of channel `Public` (default) | `Private`

Specify if your channel is private or public.

If you do not know the sharing settings of your channel:

1. Sign In
   to ThingSpeak using your MathWorks Account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the sharing status.
4. Click the **Sharing** tab. Use the option selected in the tab
   to set **Channel Access**.

   - **Keep channel view private**: Set **Channel
     Access** to `Private`. Only you can view the
     channel data.
   - **Share channel view with everyone**: Set **Channel
     Access** to `Public`. Anyone browsing the
     ThingSpeak website can view the channel data.
   - **Share channel view only with the following users**: Set
     **Channel Access** to `Private`.
     Users who have access to shared channels can see only the private view of a
     channel; they cannot add channels, see alerts, or see license
     information.

### **Read API key** — Key to read data from a private or shared channel `ABCDEFGHIJK` (default) | any valid Read API Key

When you read data from your channel using the ThingSpeak API or MATLAB® code, you need an appropriate read permission. The 16-digit API key allows
you to read data from a private or a shared channel. You do not need an API key to read
from a public ThingSpeak channel.

If you do not know the read API key of your channel:

1. Sign In
   to ThingSpeak using your The MathWorks® Account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the read API key.
4. Click the **API Keys** tab.
5. Copy the key from the **Read API Keys** parameter.
6. Open the ThingSpeak Read block in your model and paste the copied
   API key into the **Read API Key** parameter.

#### Dependencies

- To enable this parameter, set **Channel access** to
  `Private`.

### **Fields to read** — Field(s) of ThingSpeak channels to read data `1` (default) | [`1` x *N*] vector, where *N* ranges from [`1` to `8`]

Enter the field(s) of the ThingSpeak channel from which the block reads the data. For example, if you set this
parameter to [`1 2 3`], the block reads data from three fields and has
three output ports `field1`, `field2`, and
`field3`. If you set this parameter to `1`, the
block reads data from only one field and has one output port
`field1`.

### **Print diagnostic messages** — Save ThingSpeak server response to log file off (default) | on

Select this parameter to save the response from the ThingSpeak server to a log file for each read request. The name of the log file has
the format `<model_name>.log`.

### **Sample time** — Interval at which block reads data from ThingSpeak channel `60` (default) | `-1` | any nonnegative value

Specify how often this block reads data from the ThingSpeak channel.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Read data stored in a ThingSpeak channel on wireless network

Use the WiFi ThingSpeak Read block to retrieve data from the Internet of
Things website by using ThingSpeak™ on a wireless network to download the data to your Arduino® board.

ThingSpeak is an application platform that you can use for the Internet of Things. You can
build an application around data that is collected by sensors. ThingSpeak includes real-time data collection, data processing, visualizations, apps, and
plugins.

You can see the ThingSpeak server response to a data download request by selecting the Print diagnostic
messages option. This option has no effect when you use External mode, Serial Transmit, or
Serial Receive blocks that use port 0.

For more information on how to use ThingSpeak, see ThingSpeak
Apps, Plugins, and Tutorials.

### Supported Hardware

This table lists the properties of the hardware that the Arduino board supports for the WiFi ThingSpeak Read block.

| Target Hardware | Receive Limit (Number of Bytes) |
| --- | --- |
| Wi-Fi® Shield | 64 bytes |
| Arduino MKR1000, Arduino MKR Wi-Fi 1010, Arduino Nano 33 IoT, Arduino compatible ESP32 – WROOM, Arduino compatible ESP32 – WROVER | 1400 bytes |

**Note**

Using ESP8266 chip for Wi-Fi connectivity does not support deploying WiFi ThingSpeak Read
block on an Arduino board.
