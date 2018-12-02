# -*-coding:utf-8 -*

command: "cd Inbox-for-Todoist/inbox_for_todoist.widget; sh run.sh"

refreshFrequency: 1000*60#*5#*2#*2#*3#*12
the_height_i_want: ~"calc(100% - 100px)"


style: """
  background-color: white
  width: 240px
  margin-top : 250px
  margin-bottom 400px
  height: calc(100vh - 420px)
  overflow: hidden
  .content
    color: #F2F2F2
    margin-left: 7px
    font-size: 16px
    font-family: Avenir-Light
    text-align: left
    .priority1
      color: rgba(215, 65, 64, 1.0)
    .priority2
      color: rgba(255, 152, 76, 1.0)
    .priority3
      color: rgba(255, 210, 105, 1.0)
    .priority4
      color: rgba(#F2F2F2, 1.0)
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
