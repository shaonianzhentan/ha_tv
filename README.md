# ha_tv
在电视上语音控制HomeAssistant设备

```bash
adb shell appops set com.jiluxinqing.tv SYSTEM_ALERT_WINDOW allow
```

```yaml
type: notify
data:
  title: 标题
  message: 内容
```

```yaml
type: play_media
data:
  media_type: tts
  media_id: 测试内容
```

```yaml
type: play_media
data:
  media_type: web
  data: https://tv.cctv.com/live/cctv1/
```

- https://tv.cctv.com/live/cctv1/
- https://tv.cctv.com/live/cctv2/
- https://tv.cctv.com/live/cctv3/
- https://tv.cctv.com/live/cctv4/
- https://tv.cctv.com/live/cctv5/
- https://tv.cctv.com/live/cctv5plus/
- https://tv.cctv.com/live/cctv6/
- https://tv.cctv.com/live/cctv7/
- https://tv.cctv.com/live/cctv8/
- https://tv.cctv.com/live/cctvjilu/
- https://tv.cctv.com/live/cctv10/
- https://tv.cctv.com/live/cctv11/
- https://tv.cctv.com/live/cctv12/
- https://tv.cctv.com/live/cctv13/
- https://tv.cctv.com/live/cctvchild/
- https://tv.cctv.com/live/cctv15/
- https://tv.cctv.com/live/cctv16/
- https://tv.cctv.com/live/cctv17/
- https://tv.cctv.com/live/cctveurope/
- https://tv.cctv.com/live/cctvamerica/