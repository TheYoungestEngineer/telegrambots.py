import arcade
import random
import time
class Animate(arcade.Sprite):
    i = 0

    time = 0

    def update_animation(self, delta_time):

        self.time += delta_time

        if self.time >= 0.3:

            self.time = 0

            if self.i == len(self.textures) - 1:

                self.i = 0

            else:

                self.i += 1

            self.set_texture(self.i)
class Greenline2(arcade.Sprite):
    def __init__(self):
        super(Greenline2, self).__init__('contra/Image20240106115241.png', angle=90)
        self.alpha=0
class Sniper (arcade.Sprite):
    def __init__(self):
        super(Sniper, self).__init__('contra/sniper/sniper_angle.png',1)
        self.append_texture(arcade.load_texture('contra/sniper/sniper_forward.png'))
        self.append_texture(arcade.load_texture('contra/sniper/sniper_angle.png' , flipped_horizontally=True))
        self.append_texture(arcade.load_texture('contra/sniper/sniper_forward.png', flipped_horizontally=True))
        self.side=0
        self.randomstop1=random.randint(50,750)
        self.randomstop2 = random.randint(50, 750)
        self.firetime = time.time()
    def update(self):
        if time.time()-self.firetime>1:
            self.enebullet=EneBullet()
            self.enebullet.center_x=self.center_x+10
            self.enebullet.center_y = self.center_y+10
            halon.eneemmo.append(self.enebullet)
            self.firetime=time.time()
            if self.center_x >= halon.runman.center_x:
                self.enebullet.change_x=-10

            else:
                self.enebullet.change_x = 10
            if self.change_x!=0:
                self.enebullet.center_x=10000



        self.center_x+=self.change_x
        if self.side == 1:
            if self.center_x >= self.randomstop1:
                self.change_x = 0
        else:
            if self.center_x <= self.randomstop2:
                self.change_x = 0
        if self.center_x>=halon.runman.center_x:
            self.set_texture(1)

        else:

                self.set_texture(3)
class Runene(Animate):
    def __init__(self):
        super(Runene, self).__init__('contra/runman/frame-01.gif',2)
        self.runman=[]
        self.runman1=[]
        for i in range(1,10):
            self.runman.append(arcade.load_texture(f'contra/runman/frame-0{i}.gif'))
        for i in range(1,10):
            self.runman1.append(arcade.load_texture(f'contra/runman/frame-0{i}.gif', flipped_horizontally=True))
        self.textures=self.runman

    def update(self):
        self.center_x+=self.change_x
        if arcade.check_for_collision(self,halon.runman):
            halon.pain.play(volume=0.6)
            halon.hp-=20
            self.kill()

class Bullet(arcade.Sprite):
    def __init__(self):
        super(Bullet, self).__init__('contra/bullet.png',0.05)
    def update(self):
        self.center_x+=self.change_x
        self.angle+=2
        for element in halon.runenelist:
            if arcade.check_for_collision(self,element):
                self.kill()
                element.hp-=1
                if element.hp==0:
                    halon.elim+=1
                    element.kill()
        if arcade.check_for_collision(halon.line_boss,self):
            self.kill()
            halon.boss_hp-=2
        if halon.boss_hp<=0:
            halon.line_boss.kill()
            halon.lvl=14
class EneBullet(arcade.Sprite):
    def __init__(self):
        super(EneBullet, self).__init__('contra/bullet.png', 0.05)
    def update(self):
        self.center_x+=self.change_x
        if arcade.check_for_collision(self,halon.runman) and halon.runman.textures!=halon.runman.ranm4 and arcade.check_for_collision(self,halon.runman) and halon.runman.textures!=halon.runman.ranm3:
            halon.hp-=25
            self.kill()

class GreenLine(arcade.Sprite):
    def __init__(self):
        super(GreenLine, self).__init__('contra/line.png')
        self.alpha=0
    def update(self):
        if arcade.check_for_collision(self, halon.runman) and self.center_y<=halon.runman.center_y and halon.runmcol==False and self.lvl==halon.lvl:
            print ('col')
            halon.runman.bottom=self.top
            halon.lim=self.center_y+300
            halon.stop=0



class Runman(Animate):
    def __init__(self):
        super(Runman, self).__init__('contra/go_bill/0.gif',2)
        self.ranmlist=[]
        self.ranmlist2=[]
        self.ranm3=[]
        self.ranm4=[]
        for i in range(0,6):
            self.ranmlist.append(arcade.load_texture(f'contra/go_bill/{i}.gif'))
        for i in range(0,6):
            self.ranm3.append(arcade.load_texture('contra/bill_textures/BillLayingDown.png'))
        for i in range(0,6):
            self.ranm4.append(arcade.load_texture('contra/bill_textures/BillLayingDown.png',flipped_horizontally=True))

        for i in range(0,6):
            self.ranmlist2.append(arcade.load_texture(f'contra/go_bill/{i}.gif',flipped_horizontally=True))

        self.textures = self.ranmlist

class Halon(arcade.Window):
    def __init__(self,x,y,name):
        super(Halon, self).__init__(x ,y ,name )

    COORDS = [
        [
            [240, 210],
            [300, 210]
        ],
        [
            [-100, 0]
        ],
        [
            [637, 210],
            [667, 210],
            [730, 405],
            [750, 405],
        ],
        [
            [0, 405],
            [53, 405],
            [83, 315],
            [180, 315],
            [260, 315],
            [360, 315],
        ],
        [
            [-100, 0],
        ],
        [
            [750, 210],
        ],
        [
            [0, 210],
            [340, 210],
            [360, 210],
            [0, 315],
            [100, 315],
            [200, 315],
            [295, 315],
            [420, 400],
            [520, 400],
            [620, 400],
            [720, 400],
            [750, 400],
            [570, 315],
            [670, 315],
            [770, 315],

        ],
        [
            [0, 400],
            [0, 315],
            [100, 315],
            [200, 315],
            [250, 315],
        ],
        [
            [-100, 0],
        ],
        [
            [-100, 0],
        ],
        [
            [240, 230],
            [240, 230],
            [340, 230],
            [390, 230],
        ],
        [
            [210, 230],
        ],
        [
            [450, 200],
            [550, 200],
            [450, 320],
            [520, 320],
        ],
        [
            [-100, 0],
        ]
    ]
    reloadtimer=3
    limit=[3,5,7,13,15,17,20,22,24,27,29,31,37,39,45]
    elim=0
    lim=100
    line_boss=Greenline2()
    line_boss.center_x=646
    line_boss.center_y=101
    sniper=Sniper()
    sniper.center_x=400
    sniper.center_y=70
    sniper.change_x=-5
    reload=3
    emmo=10
    eneemmo=arcade.SpriteList()
    sniperhp=15
    enehp=5
    emmocolor=arcade.color.WHITE
    hpcolor=arcade.color.GREEN
    hp=100
    grav=-3
    runmcol=False
    br_y=212
    bottombr=70
    topbr=300
    stop=0
    reloadtimercenterx=1000
    sptime=5
    snipertime=10
    runman=Runman()
    runman.center_x=400
    runman.center_y=200
    runenelist=arcade.SpriteList()
    boss_hp=100
    starttime=time.time()
    starttime2 = time.time()
    sniperspawntime=time.time()
    speed=2
    pain=arcade.load_sound('contra/sounds/pain.wav')
    mainmusic=arcade.load_sound('contra/sounds/main_theme.mp3')
    mainmusic.play(volume=0,loop=True)
    jumpsound=arcade.load_sound('contra/sounds/jump.wav')
    linelist=arcade.SpriteList()
    vsepulli=arcade.SpriteList()
    enespeed=2
    sptimelist=[-10,1000]
    for num,minilist in enumerate (COORDS):
        for cord in minilist:
            line1 = GreenLine()
            line1.center_x = cord[0]
            line1.center_y = cord[1]
            line1.lvl=num
            linelist.append(line1)
            print(line1.lvl)
    greenlines=[]
    for i in range (10):
        line1 = GreenLine()
        line1.center_x = i*100
        line1.center_y = 40
        linelist.append(line1)
        line1.lvl=0
        greenlines.append(line1)
    bgs=[]
    for i in range (1,16):

        bgs.append(arcade.load_texture(f'contra/background/Map{i}.png'))
    print(bgs)
    lvl=0
    def HpColorChange(self):
        if self.hp<=100 and self.hp>=75:
            self.hpcolor=arcade.color.GREEN
        if self.hp<=75 and self.hp>50:
            self.hpcolor=arcade.color.YELLOW
        if self.hp<=50 and self.hp>25 :
            self.hpcolor = arcade.color.ORANGE
        if self.hp<=25 and self.hp>0:
            self.hpcolor = arcade.color.RED
        if self.hp<=0:
            halon.close()
    def EmmoColor(self):
        if self.emmo!="reloading":
            if self.emmo<=5 and self.emmo>=0:
                self.emmocolor=arcade.color.YELLOW
            if self.emmo==0 and self.emmo!='reloading':
                self.emmocolor=arcade.color.RED
    def Reload_Timer(self):
        if self.emmo==0:
            self.reloadtimercenterx=400
            self.reloadtime=time.time()
            self.emmo='reloading'
            self.sec=0.02
        if self.emmo=='reloading':
            self.reloadtimer=f'{int((3-self.sec))}'
            self.sec+=0.02

            if time.time() - self.reloadtime>3:
                self.emmo=10
                self.emmocolor=arcade.color.WHITE
                self.reloadtimercenterx=10000



    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(400,300,800,600, self.bgs[self.lvl])
        arcade.draw_text(f'HP={self.hp}',20,570,self.hpcolor,font_name='import',font_size=20)
        arcade.draw_text(f'EMMO 10/{self.emmo}',20,20,self.emmocolor,font_size=20,font_name='import')
        arcade.draw_text(f'KILLS={self.elim}',650,570,arcade.color.RED,font_size=20,font_name='import')
        arcade.draw_text(self.reloadtimer,self.reloadtimercenterx,300,arcade.color.WHITE,font_size=30,font_name='import')
        self.runman.draw()
        self.linelist.draw()
        self.vsepulli.draw()
        self.eneemmo.draw()
        self.runenelist.draw()
        self.line_boss.draw()
    def add_ene2(self,speed,snipertime,sniperhp):
        if time.time()-self.starttime2>snipertime:
            self.sniper=Sniper()
            self.sniper.hp=sniperhp
            self.eneside=random.randint(1,2)
            self.runenelist.append(self.sniper)
            self.starttime2=time.time()
            if self.eneside==1:
                self.sniper.center_x=-10
                self.sniper.center_y = 70
                self.sniper.change_x = speed
                self.sniper.side=1
                self.sniper.set_texture(2)

            else:
                self.sniper.center_x=1000
                self.sniper.center_y=70
                self.sniper.change_x = -speed
                self.sniper.side=2



    def add_ene(self,speed,sptime,enehp):
        if time.time()-self.starttime>sptime:
            self.ene1=Runene()
            self.eneside=random.randint(1,2)
            self.ene1.hp=enehp

            if self.eneside==1:
                self.ene1.center_x=-10
                self.ene1.center_y=70
                self.ene1.change_x=speed
                self.ene1.textures = self.ene1.runman1
            else:
                self.ene1.center_x = 1000
                self.ene1.center_y = 70
                self.ene1.change_x=-speed
            self.runenelist.append(self.ene1)
            self.starttime=time.time()
    def update(self, delta_time: float):
        self.eneemmo.update()
        self.runenelist.update()
        self.vsepulli.update()
        self.linelist.update()
        print(self.stop)
        self.Reload_Timer()
        self.runenelist.update_animation(delta_time)
        self.runman.change_y=self.grav
        self.runman.center_x+=self.runman.change_x
        self.runman.center_y+=self.runman.change_y
        if self.runman.change_x!=0:
            self.runman.update_animation(delta_time)
        if self.runman.center_x>=820 and self.limit[self.lvl]<=self.elim:
            self.runman.center_x=10
            self.hp+=random.randint(10,50)
            for i in self.greenlines:
                i.lvl+=1
            self.lvl+=1
        if self.lvl == 13 and self.runman.center_x >= 646:
            self.runman.center_x = 646
        if self.limit[self.lvl]>self.elim and self.runman.center_x>=800:
            self.runman.center_x=800
        if self.hp >= 100:
            self.hp = 100
        if self.runman.center_x<=10:
            self.runman.center_x=10
        if self.runman.top>=self.lim:
            self.grav=-3
            print(self.grav)

        self.add_ene(speed=self.enespeed,sptime=10,enehp=self.enehp)
        self.add_ene2(speed=10,snipertime=20,sniperhp=10)
        self.HpColorChange()
        self.EmmoColor()
        if self.lvl==14:
            self.runenelist.clear()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)
        if self.emmo>0:
            self.emmo-=1
            if self.runman.textures == self.runman.ranmlist:

                self.pulka=Bullet()
                self.pulka.center_x=self.runman.center_x+3
                self.pulka.center_y=self.runman.center_y +10
                self.pulka.change_x=5
                self.vsepulli.append(self.pulka)
            if self.runman.textures==self.runman.ranmlist2:
                self.pulka=Bullet()
                self.pulka.center_x = self.runman.center_x - 3
                self.pulka.center_y = self.runman.center_y
                self.pulka.change_x = -5
                self.vsepulli.append(self.pulka)
            if self.runman.textures==self.runman.ranm3:
                self.pulka = Bullet()
                self.pulka.center_x = self.runman.center_x + 5
                self.pulka.center_y = self.runman.center_y - 20
                self.pulka.change_x = 5
                self.vsepulli.append(self.pulka)
            if self.runman.textures==self.runman.ranm4:
                self.pulka = Bullet()
                self.pulka.center_x = self.runman.center_x - 5
                self.pulka.center_y = self.runman.center_y - 20
                self.pulka.change_x = -5
                self.vsepulli.append(self.pulka)






    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.D:
            self.runman.change_x=1
            self.runman.textures = self.runman.ranmlist
        if symbol==arcade.key.A:
            self.runman.change_x = -1
            self.runman.textures = self.runman.ranmlist2
        if symbol==arcade.key.S:
            self.lieing=2
            if self.runman.textures==self.runman.ranmlist:
                self.runman.textures=self.runman.ranm3
            if self.runman.textures==self.runman.ranmlist2:
                self.runman.textures=self.runman.ranm4




        if self.stop==0:
            if symbol==arcade.key.SPACE:

                self.jumpsound.play(volume=0.6)
                self.runman.center_y+=3
                self.grav=10
                self.lim+=70
                self.runmcol=False
                self.stop = 1
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol==arcade.key.D:
            self.runman.change_x=0
        if symbol==arcade.key.A:
            self.runman.change_x=0
        if symbol==arcade.key.SPACE:
            self.runmcol=False
        if symbol==arcade.key.S:
            if self.runman.textures==self.runman.ranmlist:
                self.runman.textures = self.runman.ranmlist
            if self.runman.textures == self.runman.ranmlist2:
                self.runman.textures = self.runman.ranmlist







































































































































halon=Halon(x=800,y=600,name='CONTRA')
arcade.run()