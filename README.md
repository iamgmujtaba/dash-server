# Configure DASH Server on Windows 10/11
Dynamic Adaptive Streaming over HTTP (DASH), also known as MPEG-DASH, is an adaptive bitrate streaming technique that enables high-quality streaming of media content over the Internet delivered from conventional HTTP web servers. Like Apple's HTTP Live Streaming (HLS) solution, MPEG-DASH works by breaking the content into a sequence of small segments, which are served over HTTP. Each segment contains a short interval of playback time of content that is potentially many hours in duration, such as a movie or the live broadcast of a sports event. The content is made available at a variety of different bit rates, i.e., alternative segments encoded at different bit rates covering aligned short intervals of playback time [ref](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP). Now, we will move forward towards the steps followed in the process: 

## Step 1: Creation of the Web Server
Microsoft provides Internet Information Services (IIS) that can be used as a webserver. To configure, follow the below steps.
1. Select and open Windows features (WindowsKey+S (Search box) then type **Turn Windows features on or off**).
2. Find Internet Information Services and Tick the box (Wait for the process to configure and then **Close**).
3. Test it by opening Chrome and navigating to your local internet address, **127.0.0.1**.
4. The default page should appear (If not reboot your system).

<img src="https://github.com/iamgmujtaba/dash-server/blob/master/figures/iis_home.jpg" width="550" height="200">

## Step 2: Change Default Physical Path
If you don't want to change the default path, you can skip this step. All the files can be located at the default path **C:\inetpub\wwwroot\\**

Open IIS Manager (WindowsKey+S then type IIS). The **Default Site** stores its files in a particular directory. To expose this information, right-click on it, choose **Manage Website** then **Advanced Settings**. This will open a pop-up window with all of the Default Sites information such as files or Document Root as it is normally known, enabled protocols, and even bindings. If you click on **Physical Path** a button appears on its extreme right where you can choose a different document root.

<img src="https://github.com/iamgmujtaba/dash-server/blob/master/figures/iis_path.jpg" width="550" height="200">

## Step 3: Enabling Cross-origin resource sharing (CORS)
To test streams, you need to allow other websites to access files on your web server. However, due to security concerns, not all modern browsers allow this by default. To allow this, you need to explicitly tell the browser that you agree to a website to read data from your server. This is called cross-source resource sharing (CORS). To enable CORS to follow the below steps:
1. Open the webserver (WindowsKey+S then type **IIS**).
2. Select **Default Web Site** and Right Click or Double click **HTTP Response Headers**.
3. Select **Open Feature** from the Action. Then, click Add and Type in **Access-Control-Allow-Origin** for Name and type "*" for Value.
4. Click OK to add the header to add another value: type in **Access-Control-Allow-Headers** for Name; type in **Range** for Value.

<img src="https://github.com/iamgmujtaba/dash-server/blob/master/figures/hrs_page.jpg" width="550" height="200">

## Step 4: Adding the HLS MIME Type
HLS requires statements to learn how to analyze video and audio files. HLS manifest file ends in **.mpd**. Windows IIS does not know about this extension. So, for IIS to correctly send the file to the player, you need to add this extension to IIS.
Under connections click your server and double Click MIME Types
1. Type **.m3u8** for File name extension; type **application/dash+xml** for MIME-type
2. Press okay.

<!-- <img src="https://github.com/iamgmujtaba/hls-server/blob/master/figures/mime.jpg" width="550" height="200"> -->

## Step 5: FFmpeg Installation
You can skip Step 5 and Step 6, by downloading the processed video from <!-- [google drive](https://drive.google.com/drive/folders/1JS9lwJWr9pOibl9ZpOB6uAinh-PseZXG).  --> After downloading the video place it into the default IIS physical path (i.e., C:\inetpub\wwwroot\) or the modified path.
1. Download FFmpeg from [here](https://www.ffmpeg.org/download.html#build-windows).
2. Extract the downloaded FFmpeg zip file to **C:\ffmpeg**.
3. Navigate to the **bin** folder under C:\ffmpeg and copy the address using Ctrl+C.
4. Open up the System information window and click on **Advanced System Settings**. Then click on **Environment Variables**.
5. Select the **Path** variable under System variables. 
6. Click **Edit**. then click **New**.
8. Type Ctrl+V to paste in the address where you extracted FFmpeg earlier. Then press OK,
### Check Installation
Open cmd and type **ffmpeg** in the command prompt. If you see a lot of text in the cmd, your FFmpeg is installed successfully.

## Step 6: Prepare Workspace
1. Download sample video [BigBuckBunny](https://download.blender.org/demo/movies/BBB/bbb_sunflower_1080p_30fps_normal.mp4).
2. Rename the downloaded file to **input.mp4**
3. Run the following command in the cmd in the same directory.
<!-- 
```shell
ffmpeg -i input.mp4 -force_key_frames "expr:gte(t,n_forced*10)" -strict -2 -c:a aac -c:v libx264 -f segment -segment_list_type m3u8 -segment_list_size 0 -segment_time 10.0 -segment_time_delta 0.1 -segment_list out.m3u8 out%02d.ts
``` -->
5. Once the process is completed, copy all the files excluding **input.mp4** into the default IIS physical path (i.e., C:\inetpub\wwwroot\) or the modified path. 

## Step 7: Final Testing
### Check your IP Address
Open cmd and type **ipconfig**. Get IPv4 Address. It would be 192.XXX.XXX.XXX.
### Play Video on DASH Player

<!-- #### iPhone/iPad (Safari Web Browser)
If you have iPhone, open safari and type like this **192.XXX.XXX.XXX/bbb/out.m3u8**. **bbb** is the directory of the processed BigBuckBunny video and **out.m3u8** is the HLS text file we created using the above script. Please note the iPhone should be connected to the same WiFi network.
#### VLC
If you do not have iPhone, install [VLC](https://www.videolan.org/vlc/download-windows.html). Open **Network Stream** by using **Ctrl+N**. Type the URL like this **http://192.XXX.XXX.XXX/bbb/out.m3u8**. And then press play. 
If you can watch the video, it means you have configured HLS on your window machine.
#### Ubuntu or Jetson Devices
If you want to use a native HLS web player, clone [hls.js](https://github.com/video-dev/hls.js/) from GitHub and follow the [installation](https://github.com/video-dev/hls.js/#getting-started-with-development) instructions. -->

Raise an issue if you are facing any problem :)
