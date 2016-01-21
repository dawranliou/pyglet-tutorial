import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('an_image.png')
image.anchor_x = image.width // 2
image.anchor_y = image.width // 2

@window.event
def on_draw():
    window.clear()
    image.blit(window.width//2, window.height//2)

pyglet.app.run()
