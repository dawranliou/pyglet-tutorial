import pyglet

from pyglet.window import key, mouse

window = pyglet.window.Window()
image = pyglet.resource.image('an_image.png')

position = dict(x=0, y=0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        position['x'] += 1
    elif symbol == key.UP:
        position['y'] += 1
    elif symbol == key.LEFT:
        position['x'] -= 1
    elif symbol == key.DOWN:
        position['y'] -= 1

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        position['x'] = x
        position['y'] = y

@window.event
def on_draw():
    window.clear()
    image.blit(position['x'], position['y'])

pyglet.app.run()
