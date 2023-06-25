# HomeAssistant TV
在电视上语音控制HomeAssistant设备

```bash
adb shell appops set com.jiluxinqing.tv SYSTEM_ALERT_WINDOW allow
```

## 服务

> 通知服务

显示位置：`top`、`left`、`right`、`bottom`、`center`、`leftTop`、`leftBottom`、`rightTop`、`rightButton`

```yaml
service: notify.ha_tv
data:
  title: 可选标题
  message: 消息内容
  data:
    duration: 10000
    placement: rightTop
```

> 播放视频

```yaml
service: media_player.play_media
data:
  media_content_type: web
  media_content_id: https://tv.cctv.com/live/cctv1/
  entity_id: media_player.jia_ting_zhu_li_tvying_yong
```

## 事件

类型：`ha_tv`
```yaml
type: notify
data:
  title: 标题
  message: 内容
  duration: 10000
  placement: rightTop
```

```yaml
type: play_media
data:
  media_type: web
  media_id: https://tv.cctv.com/live/cctv1/
```

```yaml
type: play_media
data:
  media_type: tts
  media_id: 你在干嘛呢？我在干饭啊
```

## 视频网站
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