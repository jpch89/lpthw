# -*- coding: utf-8 -*-
# @Author: jpch89
# @Email:  jpch89@outlook.com
# @Time:   2018/7/23 10:59

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print('This scene is not yet configured.')
        print('Subclass it and implement enter().')
        exit(1)

# Engine类
class Engine(object):
    # 初始化的时候接收一个地图对象
    def __init__(self, scene_map):
        self.scene_map = scene_map
    # 开始游戏
    def play(self):
        # 地图对象调用开场函数，赋值给当前场景
        # 地图对象的开场函数调用了下一场景函数，参数是初始场景
        # 返回值是初始场景类生成的初始场景对象CentralCorridor()
        current_scene = self.scene_map.opening_scene()
        # 最后一个场景是完结场景
        last_scene = self.scene_map.next_scene('finished')
        # 当前场景不是完结场景时
        while current_scene != last_scene:
            # 下一个场景名的值是当前场景调用enter()函数
            # 每个场景类都有enter()函数
            # enter()函数给出了一些场景提示和选择
            # 根据用户的选择，返回不同的字符串
            # 返回的字符串可能是当前场景，可能是'death'，也可能是下一场景
            next_scene_name = current_scene.enter()
            # 把下一场景名称的字符串给Map类的next_scene
            # 返回的是根据字符串在字典里面查到的对象
            # 然后重新进入循环
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        # 假如已经是'finished'场景
        # 那么还需要进入场景一次
        # 提示成功信息
        # 至此Engine.play()完成，游戏结束
        current_scene.enter()


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and
        destroyed your entire crew. You are the last surviving
        member and your last mission is to get the neutron destruct
        bomb from the Weapons Armory, put it in the bridge, and
        blow the ship up after getting into an escape pod.
        
        You're running down the central corridor to the Weapons
        Armory when a Gothon jumps out, red scaly skin, dark grimy
        teeth, and evil clown costume flowing around his hate
        filled body. He's blocking the door to the Armory and 
        about to pull a weapon to blast you.
        """))

        action = input('> ')

        if action == 'shoot!':
            print(dedent("""
            Quick on the draw you yank out your blaster and fire 
            it at the Gothon. His clown costume is flowing and 
            moving around his body, which throws off your aim.
            Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother 
            bought him, which makes him fly into an insane rage 
            and blast you repeatedly in the face until you are 
            dead. Then he eats you.
            """))
            return 'death'

        elif action == 'dodge!':
            print(dedent("""
            Like a world class boxer you dodge, weave, slip and 
            slide right as the Gothon's blaster cranks a laser
            past your head. In the middle of your artful dodge
            your foot slips and you bang your head on the metal 
            wall and pass out. You wake up shortly after only to 
            die as the Gothon stomps on your head and eats you.
            """))
            return 'death'

        elif action == 'tell a joke':
            print(dedent("""
            Lucky for you they made you learn Gothon insults in 
            the academy. You tell the one Gothon joke you know:
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, 
            fur fvgf nebhaq gur ubhfr. The Gothon stops, tries 
            not to laugh, then busts out laughping and can't move.
            While he's laughping you run up and shoot him square in 
            the head putting him down, then jump through the 
            Weapon Armory door.
            """))
            return 'laser_weapon_armory'

        else:
            print('DOES NOT COMPUTE!')
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, crouch and scan 
        the room for more Gothons that might be hiding. It's dead 
        quiet, too quiet. You stand up and run to the far side of 
        the room and find the neutron bomb in its container.
        There's a keypad lock on the box and you need the code to 
        get the bomb out. If you get the code wrong 10 times then 
        the lock closes forever and you can't get the bomb. The 
        code is 3 digits.
        """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEDD!")
            guess += 1
            guess = input("[keypad]> ")
            if guess == code:
                break

        if guess == code:
            print(dedent("""
            The container clicks open and the seal breaks, letting 
            gas out. You grab the neutron bomb and run as fast as 
            you can to the bridge where you must place it in the 
            right spot.
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a 
            sickening melting sound as the mechanism is fused
            together. You decide to sit there, and finally the 
            Gothons blow up the ship from their ship and you die.
            """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the neutron destruct bomb
        under your arm and surprise 5 Gothons who are trying to 
        take control of the ship. Each of them has an even uglier
        clown costume than the last. They haven't pulled their 
        weapons out yet, as they see the active bomb under your 
        arm and don't want to set it off.
        """))

        action = input('> ')

        if action == 'throw the bomb':
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons
            and make a leap for the door. Right as you drop it a 
            Gothon shoots you right in the back killing you. As
            you die you see another Gothon frantically try to 
            disarm the bomb. You die knowing they will probably
            blow up when it goes off.
            """))
            return 'death'

        elif action == 'slowly place the bomb':
            print(dedent("""
            You point your blaster at the bomb under your arm and 
            the Gothons put their hands up and start to sweat.
            You inch backward to the door, open it, and then 
            carefully place the bomb on the floor, pointing your 
            blaster at it. You then jump back through the door, 
            punch the close button and blast the lock so the 
            Gothons can't get out. Now that the bomb is placed
            you run to the escape pod to get off this tin can.
            """))
            return 'escape_pod'
        else:
            print('DOES NOT COMPUTE!')
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush through the ship desperately trying to make it to 
        the escape pod before the whole ship explodes. It seems
        like hardly any Gothons are on the ship, so your run is 
        clear of interference. You get to the chamber with the 
        escape pods, and now need to pick one to take. Some of 
        them could be damaged but you don't have time to look.
        There's 5 pods, which one do you take?
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button.
            The pod escapes out into the void of space, then 
            implode as the hull ruptures, crushing your body 
            into jam jelly.
            """))
            return 'death'
        else:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button.
            The pod easily slides out into space heading to 
            the planet below. As it flies to the planet, you look 
            back and see your ship implode then explode like a
            bright star, taking out the Gothon ship at the same 
            time. You won!
            """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    # 场景是一个字典
    # 键是场景名称，值是场景类生成的场景对象
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        # 初始化场景
        # 这里接收的是'central_corridor'字符串
        self.start_scene = start_scene

    # 下一个场景，要传入下一个场景的名称
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        # 返回字典里的值
        # 该值是一个场景对象
        return val

    # 开场
    def opening_scene(self):
        return self.next_scene(self.start_scene)

# 新建Map对象，初始场景为central_corridor
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()