const HA_JS = {
  'tv.cctv.com': {
    style: `
      #player{
        width: 100% !important;
        height: 100% !important;
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
      }
      .zhibo_201014,
      .gwA18043_ind01{
        display: none !important;
      }
    `,
    select: function (callback) {
      const list = []
      document.querySelectorAll('#jiemudan dl').forEach(ele => {
        const a = ele.querySelector('dt a')
        list.push(a.href)
      })
      let index = list.findIndex(link => location.href.includes(link))
      index = callback(list, index)
      location.href = list[index]
    },
    up: function () {
      this.select((list, index) => {
        index -= 1
        if (index < 0) index = list.length - 1
        return index
      })
    },
    down: function () {
      this.select((list, index) => {
        index += 1
        if (index >= list.length) index = 0
        return index
      })
    }
  },
  'live.douyin.com': `
  `
}
if (location.hostname in HA_JS) {
  const js = HA_JS[location.hostname]
  const style = document.createElement('style')
  style.textContent = js.style
  document.body.appendChild(style)
  // 遥控器
  window.addEventListener('keyup', function (event) {
    console.log(event.key)
    switch (event.key) {
      case 'ArrowUp':
        js.up();
        break;
      case 'ArrowDown':
        js.down();
        break;
      case 'ArrowLeft':
        break;
      case 'ArrowRight':
        break;
      case 'Enter':
        break;
      case 'Backspace':
        break;
    }
  }, false)
}