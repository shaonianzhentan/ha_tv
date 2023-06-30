const HA_JS = {
    ha:{
         sleep: (ms)=> new Promise((resolve)=> setTimeout(resolve, ms))
    },
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
    init: function(){
        
    },
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
    left: function () {
      this.select((list, index) => {
        index -= 1
        if (index < 0) index = list.length - 1
        return index
      })
    },
    right: function () {
      this.select((list, index) => {
        index += 1
        if (index >= list.length) index = 0
        return index
      })
    }
  },
  'v.qq.com': {
    style: `
    #ssi-header,
    .ft_cell_feedback{
        display: none !important;
    }
    #player-container{
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 11111;
    }
    `,
    init: async function(){
        document.querySelector('.txp_btn_fullscreen')?.click()
    },
    login: async function(){
        const { sleep } = HA_JS.ha
        if(!document.querySelector('.user_nickname')?.textContent){
            document.querySelector('.btn_pop_link').click()
            await sleep(3000)
            document.querySelector('.selected').click()
            await sleep(3000)
            document.querySelector('.btn_qq')?.focus()
        }
    },
    enter: function(event){
        document.querySelector('.txp_btn_fullscreen')?.click()
        event.preventDefault()
    }
  }
}
if (location.hostname in HA_JS) {
  const js = HA_JS[location.hostname]
  js.init()
  const style = document.createElement('style')
  style.textContent = js.style
  document.body.appendChild(style)
  // 遥控器
  window.addEventListener('keyup', function (event) {
    console.log(event.key)
    switch (event.key) {
      case 'ArrowUp':
        js.up && js.up(event);
        break;
      case 'ArrowDown':
        js.down && js.down(event);
        break;
      case 'ArrowLeft':
        js.left && js.left(event);
        break;
      case 'ArrowRight':
        js.right && js.right(event);
        break;
      case 'Enter':
        js.enter && js.enter(event);
        break;
      case 'Backspace':
        break;
    }
  }, false)
}