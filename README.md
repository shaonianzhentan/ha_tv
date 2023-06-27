# HomeAssistant TV
在电视上语音控制HomeAssistant设备


[![hacs_badge](https://img.shields.io/badge/Home-Assistant-049cdb)](https://www.home-assistant.io/)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
![visit](https://visitor-badge.laobi.icu/badge?page_id=shaonianzhentan.ha_tv&left_text=visit)

[![badge](https://img.shields.io/badge/Conversation-语音小助手-049cdb?logo=homeassistant&style=for-the-badge)](https://github.com/shaonianzhentan/conversation)
[![badge](https://img.shields.io/badge/Windows-家庭助理-blue?logo=windows&style=for-the-badge)](https://www.microsoft.com/zh-cn/store/productId/9n2jp5z9rxx2)
[![badge](https://img.shields.io/badge/wechat-微信控制-6cae6a?logo=wechat&style=for-the-badge)](https://github.com/shaonianzhentan/ha_wechat)
[![badge](https://img.shields.io/badge/android-家庭助理-purple?logo=android&style=for-the-badge)](https://github.com/shaonianzhentan/ha_app)
[![badge](https://img.shields.io/badge/android-家庭助理TV-orange?logo=android&style=for-the-badge)](https://github.com/shaonianzhentan/ha_tv)

[![badge](https://img.shields.io/badge/QQ群-64185969-76beff?logo=tencentqq&style=for-the-badge)](https://qm.qq.com/cgi-bin/qm/qr?k=m4uDQuuAJCnCll6PuQZUnnJ0zEy7zuk2&jump_from=webapi&authKey=WTxRChNkBUDdVsTcYHeO8yb98Uu8WGJC3hxw53Il4PB7RgBTQ6StHa43MwZJtN5w)


## 使用

命令授权
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