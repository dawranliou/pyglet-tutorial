import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          x=window.width//2, # origin - left
                          y=window.height//2, # origin - bottom
                          anchor_x='center',
                          anchor_y='center')


def update(dt):
    print(dt)
    label.x += 1
    label.y += 1

@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.clock.schedule(update) # cause a timed event as fast as you can
pyglet.app.run()
