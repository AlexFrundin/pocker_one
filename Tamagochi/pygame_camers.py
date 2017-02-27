from pygame_fieldgame import *
from pygame import *
WIN_W=800
WIN_H=740
class  Camera(object):
    def __init__(self, camera_func,width, height):
        self.camera_func=camera_func
        self.state=Rect(0,0,width,height)

    def apply(self,target):
        return target.rect.move(self.state.topleft)

    def update(self,target):
        self.state=self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ =target_rect
    _, _, w, h = camera
    l, t=-l+WIN_W/2, -t + WIM_H/2

    l=min(0,l)
    l=max(-(camera.width-WIN_W), l)
    t=max(-(camera.height-WIN_H), t)
    t=min(0,t)
    return Rect(l,t,w,h)
