# -*-coding:utf-8 -*

command: ". todoist/run.sh"

refreshFrequency: 1000#*60#*5#*2#*2#*3#*12

style: """
  top: 245px
  right: 0px
  width: 240px
  height: 600px
  margin-left: -(@width / 2)
  overflow: hidden
  .content
    color: #F2F2F2
    margin-left: 7px
    font-size: 16px
    font-family: Avenir-Light
    text-align: left
  .title
    color: #F2F2F2
    font-size: 24px
    font-family: Avenir-Book
    text-align: center
  bg-blur = 10px
  .bg-slice
    position: absolute
    top: -(bg-blur)
    left: -(bg-blur)
    width: 100% + 2*bg-blur
    height: 100% + 2*bg-blur
    -webkit-filter: blur(bg-blur)
  .mini
    font-size: 2px
    line-height: 0%;
"""

render: (output) -> """
  <canvas class='bg-slice'></canvas>
  <div class='title'>Todoist Inbox</div>
  <div class='content'>#{output}</div>
"""

afterRender: (domEl) ->
  uebersicht.makeBgSlice(el) for el in $(domEl).find '.bg-slice'