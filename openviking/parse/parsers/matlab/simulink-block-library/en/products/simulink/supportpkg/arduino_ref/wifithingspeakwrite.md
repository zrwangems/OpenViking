---
type: simulink-block
title: 'WiFi ThingSpeak Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Wi-Fi'
documentation_page: 'wifithingspeakwrite'
documentation_source_path: 'supportpkg/arduino_ref/wifithingspeakwrite.html'
language: en
---

# WiFi ThingSpeak Write

## Ports

### Input

### **fieldn** — Data published to nth field of ThingSpeak channel [`1` x *N*] vector, where *N* ranges from [`1` to `8`]

The block publishes the data read to the nth field in the ThingSpeak channel at each time step. The number of data channels at the block
input depends on the number of fields that you enter in the **Fields to write** parameter. For example, if you set the **Fields to write** parameter to [`1 4 5`], the
block enables three input ports with port names **field1**, **field4**, and **field5**.

#### Dependencies

- To enable this port, on the **Optional** tab, select
  **Send location information** and set the **Location
  source** parameter to `Input port`.

**Data Types:** `single`

### **location** — Send location data three-element numeric vector

The block sends the location data as a three-element numeric vector of the form
[*latitude*, *longitude*,
*altitude*].

#### Dependencies

- To enable this port, on the **Optional** tab, select
  **Send location information** and set the **Location
  source** parameter to `Input port`.

**Data Types:** `single` | `double`

## Parameters

### Main

### **Channel ID** — ThingSpeak channel ID `12397` (default) | positive integer

Enter the unique identification number of the ThingSpeak channel from which the block reads data.

Follow these steps to find the ThingSpeak channel identification number.

1. Sign in to ThingSpeak using your MATLAB account.
2. Select **Channels** > **My Channels**.
3. Select the channel from which to read data.
4. Click the **Channel Settings** tab and copy the channel ID
   from the **Channel ID** parameter.

   ThingSpeak Channel Settings
5. Open the ThingSpeak Read block in your model and paste the
   copied ID to the **Channel ID** parameter.

### **Write API key** — Write API key of ThingSpeak channel no default (default) | character vector

Enter the 16-digit write API key of the ThingSpeak channel.

Follow these steps to know the API key for your ThingSpeak channel.

1. Sign in to ThingSpeak using your MATLAB account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the write API key.
4. Click the **API Keys** tab and copy the key from the
   **Read API Keys** parameter.Arduino ThingSpeak Write API Key
5. Open the ThingSpeak Read block in your model and paste the
   copied API key into the **Read API key** parameter.

### **Fields to write** — Field(s) of ThingSpeak channels to write data `1` (default) | [`1` x *N*] vector, where *N* ranges from [`1` to `8`]

Enter the field(s) of the ThingSpeak channel to which the block writes the data. For example, if you set this
parameter to [`1 2 3`], the block writes data to three fields and has
three input ports `field1`, `field2`, and
`field3`. If you set this parameter to `1`, the
block writes data to only one field and has one input port
`field1`.

### **Update interval (seconds)** — Data update interval `60` (default) | nonnegative integer

Specify the time interval at which the input data is updated on the ThingSpeak channel.

### **Print diagnostic messages** — Save ThingSpeak server response to log file off (default) | on

Select this parameter to save the response from the ThingSpeak server to a log file for each write request. The name of the log file
has the format `<model_name>.log`.

### Optional

### **Send location information** — Send location information off (default) | on

Select this parameter to send the location information to the ThingSpeak channel.

### **Location source** — Source of location data `Block dialog` (default) | `Input port`

Select the source of the location data to one of the following:

- `Block dialog` — Specify the location using the
  **Location (latitude, longitude, altitude)**
  parameter.
- `Input port` — Specify the location using the
  **location** input port.

Use decimal degrees notation to specify *latitude* and
*longitude* and use meters to specify *altitude*.
For example:

- The lowest human-sized point underground, the TauTona Mine in Carletonville,
  South Africa, is [`-26.416111,27.4275,-3900`].
- The highest point measured from sea level, the summit of Mount Everest in
  Nepal, is [`27.988056,86.925278,8848`].

### **Location (latitude, longitude, altitude)** — Location information [`42.29971`, `-71.350719`, `69.29`] (default) | three-element numeric vector

Enter the location information as a three-element numeric vector of the form
[*latitude*, *longitude*,
*altitude*] to send location information to the ThingSpeak channel.

#### Dependencies

- To enable this parameter, set **Location source** to
  `Block dialog`.

## Libraries

Simulink Support Package for Arduino Hardware / WiFi

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Publish data to Internet of Things using ThingSpeak on wireless network

Use the ThingSpeak Write block to publish input data from your Arduino® board on a wireless network to Internet of Things (IoT) using ThingSpeak™.

ThingSpeak is an open-source
IoT platform with MATLAB® analytics that allows you to collect and store the sensor data in the cloud and
develop IoT applications. The ThingSpeak IoT platform provides applications that allow you to analyze and visualize your
data in MATLAB and then act on the data. For more information on how to use ThingSpeak, see ThingSpeak
Apps, Plugins, and Tutorials.

### Supported Hardware

This table lists the properties of the hardware that the Arduino board supports for the WiFi ThingSpeak Write block.

| Target Hardware | Receive Limit (Number of Bytes) |
| --- | --- |
| Wi-Fi® Shield | 64 bytes |
| Arduino MKR1000, Arduino MKR Wi-Fi 1010, Arduino Nano 33 IoT, Arduino compatible ESP32 – WROOM, Arduino compatible ESP32 – WROVER | 1400 bytes |

**Note**

Using ESP8266 chip for Wi-Fi connectivity does not support deploying WiFi ThingSpeak Write
block on an Arduino board.
