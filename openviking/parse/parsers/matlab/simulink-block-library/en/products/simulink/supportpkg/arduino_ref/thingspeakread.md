---
type: simulink-block
title: 'ThingSpeak Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / ThingSpeak'
documentation_page: 'thingspeakread'
documentation_source_path: 'supportpkg/arduino_ref/thingspeakread.html'
language: en
---

# ThingSpeak Read

## Ports

### Output

### **fieldn** — Data read from nth field of ThingSpeak channel [`1` x *N*] vector, where *N* ranges from [`1` to `8`]

The block outputs the data read from the nth field in the ThingSpeak channel at each time step. The number of data channels at the block
output depends on the number of fields that you enter in the **Fields to read** parameter. For example, if you set the **Fields to read** parameter to [`1 4 5`], the
block enables three output ports with port names **field1**, **field4**, and **field5**. If the data received from the channel is null, the
block outputs `0`.

**Data Types:** `single`

### **status** — ThingSpeak server response for each read request scalar

The block outputs the ThingSpeak server response for the read request at each time step. The block
receives the response as an HTTP status code. For more information on HTTP status
codes, see `matlab.net.http.StatusCode`

**Example:** An HTTP status code of `200` indicates that the read
request is successfully completed. Whereas, an HTTP status code of
`204`, indicates that the data received on the data channel is
null.

**Data Types:** `int16`

## Parameters

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

### **Channel access** — Type of access to ThingSpeak channel `Public` (default) | `Private`

Select the type of sharing access for the ThingSpeak channel.

Follow these steps to find the sharing access settings for your ThingSpeak channel.

1. Sign in to ThingSpeak using your MATLAB account.
2. Select **Channels** > **My Channels**.
3. Select the channel to view the sharing status.
4. Click the **Sharing** tab. Use the option selected in the tab
   to set **Channel access**.

   - **Keep channel view private**: Set **Channel
     access** to `Private`. Only you can view
     the channel data.
   - **Share channel view with everyone**: Set
     **Channel access** to `Public`.
     Anyone browsing the ThingSpeak website can view the channel data.
   - **Share channel view only with the following users**: Set
     **Channel access** to `Private`.
     Users who have access to shared channels can only view the channel, but they
     cannot add channels, see alerts, or see license information.

   ThingSpeak Channel Sharing Settings

### **Read API key** — Key to read from private or shared ThingSpeak channel ABCDEFGHIJKLMNO (default) | valid Read API key

Enter the 16-digit read API key of the ThingSpeak channel. This API key is not needed to read data from public or
ThingSpeak channel.

Follow these steps to know the API key for your ThingSpeak channel.

1. Sign in to ThingSpeak using your MATLAB account.
2. Select **Channels** > **My Channels**.
3. Select the channel to get the read API key.
4. Click the **API Keys** tab and Copy the key from the
   **Read API Keys** parameter.

   Write API Key Arduino ThingSpeak
5. Open the ThingSpeak Read block in your model and paste the
   copied API key into the **Read API key** parameter.

#### Dependencies

To enable this parameter, set **Channel access** to
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

### **Sample time** — Time interval at which block reads data from ThingSpeak channel `60` (default) | `-1` | nonnegative integer

Enter the time interval in seconds at which the block reads data from the
ThingSpeak channel. When you set this parameter to `-1`,
Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Support Package for Arduino Hardware / Ethernet Shield

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Read data stored in ThingSpeak channel

The ThingSpeak Read block reads data from the ThingSpeak™ channel.

ThingSpeak is an open-source Internet of
Things (IoT) platform with MATLAB® analytics that allows you to collect and store the sensor data in the cloud and
develop IoT applications. The ThingSpeak IoT platform provides applications that allow you to analyze and visualize your
data in MATLAB and then act on the data. For more information on how to use ThingSpeak, see ThingSpeak
Apps, Plugins, and Tutorials.
