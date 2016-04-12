#!/usr/bin/env python
import cmd
import pyautogui
import time
from const import INITPOS
from const import mainButtonPos as MAIN
from const import supplyButtonPos as SUPPLY
from const import battleButtonPos as BATTLE
from const import expeditonButtonPos as EXP
from const import sortleButtonPos as SORTLE
from const import organizeButtonPos as ORG
from const import SideBarButtonPos as SIDE
from const import advanceButtonPos as ADV
from const import topBarButtonPos as TOP
from const import questButtonPos as QUEST
from const import dockingButtonPos as DOCK

class KanShell(cmd.Cmd):
    prevPos = pyautogui.position()
    prompt = 'poi> '

    def precmd(self, line):
        self.prevPos = pyautogui.position()
        return line

    def cmdloop(self):
        try:
            cmd.Cmd.cmdloop(self)
        except KeyboardInterrupt as e:
            print()
            self.cmdloop()

    def do_ma(self, args):
        ''' 出擊 '''
        try:
            areaNum, mapNum = parseMap(args)
        except ValueError:
            return
        self.mapSelect(areaNum, mapNum)

    def mapSelect(self, areaNum, mapNum):
        self.click(*MAIN.SORTLE, sleeptime=.2)
        self.click(*SORTLE.SORTLE, sleeptime=1)
        self.click(*ADV.AREA[areaNum - 1])
        if mapNum > 4:
            self.click(*ADV.EO)
        self.click(*ADV.MAP[mapNum - 1], sleeptime=.2)
        self.click(*ADV.SELECT, sleeptime=.2)
        self.click(*ADV.START, sleeptime=.2)

    def do_ma1(self, args):
        '''1-1 刷閃'''
        self.mapSelect(1, 1)

    def do_ma2(self, args):
        ''' 4-2 東方'''
        self.mapSelect(4, 2)

    def do_ma3(self, args):
        ''' 2-3 撈油'''
        self.mapSelect(2, 3)

    def do_ma4(self, args):
        ''' 5-4 刷戰果'''
        self.mapSelect(5, 4)

    def do_ma5(self, args):
        ''' 1-5 刷閃'''
        self.mapSelect(1, 5)

    def do_view(self, args):
        '''切到編成視窗'''
        try:
            fleetNum = parseInt(args)[0]
        except IndexError:
            fleetNum = 1
        self.click(*MAIN.ORGANIZE, sleeptime=1)
        self.click(*ORG.FLEETS[fleetNum - 1])

    def do_v(self, args):
        return self.do_view(args)

    def do_vf(self, args):
        '''在編成視窗中切換艦隊'''
        try:
            fleetNum = parseInt(args)[0]
        except IndexError:
            fleetNum = 1
        self.click(*ORG.FLEETS[fleetNum - 1])


    def do_supply(self, args):
        '''補給'''
        fleets = parseInt(args)
        if not fleets:
            fleets = (1,)

        self.click(*MAIN.SUPPLY, sleeptime=.2)
        for fleetNum in fleets:
            fleetNum -= 1
            self.click(*SUPPLY.FLEETS[fleetNum])
            self.click(*SUPPLY.SUPPLYALL, sleeptime=.5)
        self.click()

    def do_s(self, args):
        return self.do_supply(args)

    def do_ms(self, args):
        '''刷閃補給(只補第一艦隊前兩隻)'''
        try:
            fleetNum = parseInt(args)[0] - 1
        except:
            fleetNum = 0
        self.click(*MAIN.SUPPLY, sleeptime=.2)
        self.click(*SUPPLY.FLEETS[fleetNum])
        self.click(*SUPPLY.SELECT[0])
        self.click(*SUPPLY.SELECT[1])
        self.click(*SUPPLY.START)
        self.do_view("1")

    def do_refit(self, args):
        '''改修'''
        self.click(*MAIN.REFIT, sleeptime=1)

    def do_r(self, args):
        return self.do_refit(args)
    
    def do_docking(self, args):
        '''入渠'''
        self.click(*MAIN.DOCKING, sleeptime=1)
        try:
            dockNum = parseInt(args)[0] - 1
        except IndexError:
            return
        self.click(*DOCK.DOCKS[dockNum])

    def do_d(self, args):
        return self.do_docking(args)

    def do_clickOrganize(self, args):
        '''點擊側邊欄的「編成」'''
        self.click(*SIDE.ORGANIZE, sleeptime=1.1)
    
    def do_co(self, args):
        return self.do_clickOrganize(args)

    def do_clickSupply(self, args):
        '''點擊側邊欄的「補給」'''
        self.click(*SIDE.SUPPLY, sleeptime=1.1)

    def do_cs(self, args):
        return self.do_clickSupply(args)

    def do_clickRefit(self, args):
        '''點擊側邊欄的「改修」'''
        self.click(*SIDE.REFIT, sleeptime=1)

    def do_cr(self, args):
        return self.do_clickRefit(args)

    def do_clickDocking(self, args):
        '''點擊側邊欄的「入渠」'''
        self.click(*SIDE.DOCKING, sleeptime=1)

        try:
            dockNum = parseInt(args)[0] - 1
        except IndexError:
            return
        self.click(*DOCK.DOCKS[dockNum])

    def do_cd(self, args):
        return self.do_clickDocking(args)

    def do_clickFactory(self, args):
        '''點擊側邊欄的「工廠」'''
        self.click(*SIDE.FACTORY, sleeptime=1.1)

    def do_cf(self, args):
        return self.do_clickFactory(args)

    def do_advance(self, args):
        '''進擊'''
        self.click(*BATTLE.ADVANCE)

    def do_a(self, args):
        self.do_advance(args)

    def do_retreat(self, args):
        '''回家/夜戰'''
        self.click(*BATTLE.RETREAT)

    def do_r(self, args):
        self.do_retreat(args)

    def do_form(self, args):
        '''陣形選擇
            單縱(預設) : 1
            複縱: 2
            輪形: 3
            梯形: 4
            單横: 5'''
        try:
            formNum = parseInt(args)[0] - 1
        except IndexError:
            formNum = 0
        self.click(*BATTLE.FORMATION[formNum])

    def do_f(self, args):
        self.do_form(args)
    
    def do_f5(self, args):
        '''單横的 alias'''
        return self.do_form("5")

    def do_expedition(self, args):
        '''遠征
        
        格式： expedition <遠征ID> <艦隊>
        
        預設為第二艦隊
        自動跳回母港'''
        try:
            expId, fleetNum = parseInt(args)
        except ValueError:
            expId, fleetNum = parseInt(args)[0], 2

        areaNum, expPos = divmod(expId - 1, 8)
        self.click(*MAIN.SORTLE, sleeptime=.2)  # 出擊
        self.click(*SORTLE.EXPEDITION, sleeptime=1.1)
        self.click(*EXP.AREA[areaNum])
        self.click(*EXP.EXPPOS[expPos], sleeptime=.1)
        self.click(*EXP.SELECT, sleeptime=.2)
        self.click(*EXP.FLEETS[fleetNum - 1])
        self.click(*EXP.START, sleeptime=4)
        self.click()


    def do_e(self, args):
        self.do_expedition(args)

    def do_quest(self, args):
        '''選擇任務頁數，沒寫時只點擊任務按鈕'''
        try:
            pageNum = parseInt(args)[0] - 1
        except IndexError:
            self.click(*TOP.QUEST, sleeptime=1)
            self.click()
            return
        self.click(*QUEST.PAGE[pageNum])

    def do_q(self, args):
        return self.do_quest(args)
    
    def do_questSelect(self, args):
        '''點擊任務, 沒給數字時點擊任務獎勵的確認視窗'''
        quests =  parseInt(args)
        if not quests:
            self.click(*QUEST.CLOSE)
            return
        for questNum in quests:
            questNum -= 1
            self.click(*QUEST.OFFSET[questNum], sleeptime=.5)

    def do_qs(self, args):
        return self.do_questSelect(args)

    def do_moveTo(self, args):
        '''移動滑鼠'''
        try:
            self.move(parseInt(args)[:2])
        except ValueError:
            self.move()

    def do_t(self, args):
        return self.do_moveTo(args)

    def do_click(self, args):
        '''點擊(預設為母港按鈕)'''
        try:
            self.click(parseInt(args)[:2])
        except ValueError:
            self.click()

    def do_c(self, args):
        return self.do_click(args)


    def do_exit(self, args):
        return True

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def move(self, x=MAIN.PORT, y=None):
        if isinstance(x, tuple):
            x, y = x
        pyautogui.moveTo(getPos(x, y))

    def click(self, x=MAIN.PORT, y=None, sleeptime=0):
        self.move(x, y)
        pyautogui.click()
        if sleeptime:
            time.sleep(sleeptime)

def getPos(point, y=None):
    if y is not None:
        point = (point, y)
    return tuple(sum(i) for i in zip(INITPOS, point))


def parseInt(args):
    return tuple(map(int, args.split()))

def parseMap(args):
    return tuple(map(int, args.split('-')))

