# 一筆書きゲーム
import tkinter
import tkinter.messagebox
import pygame as pg

idx = 0
tmr = 0
stage = 1
ix = 0
iy = 0
key = 0

# bgmを再生(mp3音源のみ再生可能)
pg.mixer.init()

def key_down(e):
    global key
    key = e.keysym
    
def key_up(e):
    global key
    key = 0
    
# pg.mixer.music.unpause()
maze = [[], [], [], [], [], [], [], []]

def stage_data():
    global ix, iy
    global maze
    if stage == 1:
        ix = 8
        iy = 6
        maze = [    # ０が床、１が塗ったところ、９が壁
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 9, 0, 9],
        [9, 0, 0, 9, 9, 0, 0, 9, 0, 9],
        [9, 0, 0, 9, 9, 0, 0, 9, 0, 9],
        [9, 0, 0, 0, 9, 0, 0, 9, 0, 9],
        [9, 0, 0, 0, 9, 0, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 
        ]
        pg.mixer.music.load("waterblue.mp3")
        pg.mixer.music.play(-1)
    if stage == 2:
        ix = 8
        iy = 6
        maze = [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 9, 0, 0, 9, 0, 9],
        [9, 0, 0, 9, 9, 9, 0, 0, 0, 9],
        [9, 9, 0, 0, 9, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 9, 0, 0, 0, 9, 0, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],    
        ]
        pg.mixer.music.load("marbletechno1.mp3")
        pg.mixer.music.play(-1)
    if stage == 3:
        ix = 3
        iy = 3
        maze = [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 0, 0, 9, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 9, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 9, 9],
        [9, 9, 0, 0, 0, 0, 0, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],    
        ]
        pg.mixer.music.load("marbletechno2.mp3")
        pg.mixer.music.play(-1)
    if stage == 4:
        ix = 4
        iy = 3
        maze = [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 9, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 9, 0, 0, 0, 9, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 9, 0, 9],  
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],    
        ]
        pg.mixer.music.load("tsukitoiruka.mp3")
        pg.mixer.music.play(-1)
    if stage == 5:
        ix = 1
        iy = 6
        maze = [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 9, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 9, 9, 0, 9],
        [9, 0, 0, 0, 0, 9, 9, 9, 0, 9],
        [9, 0, 0, 9, 0, 0, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],    
        ]
        pg.mixer.music.load("waterblue.mp3")
        pg.mixer.music.play(-1)
    maze[iy][ix] = 1
    
def draw_bg():
    for y in range(8):
        for x in range(10):
            gx = 80 * x
            gy = 80 * y
            if maze[y][x] == 0:
                cvs.create_rectangle(gx, gy, gx + 80, gy + 80, fill = "white", width = 0, tag = "BG")
            if maze[y][x] == 9:
                cvs.create_image(gx + 40, gy + 40, image = wall, tag = "BG")
    cvs.create_text(120, 40, text = "STAGE " + str(stage), fill = "Black", font = ("Times New Roman", 30, "bold"), tag = "BG")
    gx = 80 * ix
    gy = 80 * iy
    cvs.create_rectangle(gx, gy, gx + 80, gy + 80, fill ="sky blue", width = 0, tag = "BG")
    cvs.create_image(gx + 60, gy + 20, image = pen, tag = "PEN")
    
def erase_bg():
    cvs.delete("BG")
    cvs.delete("PEN")
    
def move_pen():
    global idx, tmr, ix, iy, key
    bx = ix
    by = iy
    if (key == "Left" or key == "a" or key == "A") and maze[iy][ix - 1] == 0:
        ix = ix - 1
    if (key == "Right"or key == "d" or key == "D") and maze[iy][ix + 1] == 0:
        ix = ix + 1
    if (key == "Up" or key == "w" or key == "W") and maze[iy - 1][ix] == 0:
        iy = iy - 1
    if (key == "Down" or key == "s" or key == "S") and maze[iy + 1][ix] == 0:
        iy = iy + 1
    if ix != bx or iy != by:
        maze[iy][ix] = 2
        gx = 80 * ix
        gy = 80 * iy
        cvs.create_rectangle(gx, gy, gx + 80, gy + 80, fill = "pink", width = 0, tag = "BG")
        cvs.delete("PEN")
        cvs.create_image(gx + 60, gy + 20, image = pen, tag = "PEN")
        
    if key == "g" or key == "G" or key == "Shift_L":
        key = 0
        ret = tkinter.messagebox.askyesno("ギブアップ", "やり直しますか？")
        root.focus_force()
        if ret == True:
            stage_data()
            erase_bg()
            draw_bg()
            
def count_tile():
    cnt = 0
    for y in range(8):
        for x in range(10):
            if maze[y][x] == 0:
                cnt = cnt + 1
    return cnt

def game_main():
    global idx, tmr, stage
    if idx == 0:    # 初期化
        stage_data()
        draw_bg()
        idx = 1
    if idx == 1:    # ペンの移動とクリア判定
        move_pen()
        if count_tile() == 0:
            txt = "STAGE CLEAR"
            if stage == 5:
                txt = "ALL STAGE CLEAR!"
            cvs.create_text(400, 320, text = txt, fill = "Black", font = ("Times New Roman", 40, "bold"), tag = "BG")
            idx = 2
            tmr = 0
    if idx == 2:    # ステージクリア
        tmr = tmr + 1
        if tmr == 30:
            if stage < 5:
                stage = stage + 1
                stage_data()
                erase_bg()
                draw_bg()
                idx = 1
    root.after(200, game_main)
    
root = tkinter.Tk()
root.title("一筆書き迷路ゲーム")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
cvs = tkinter.Canvas(root, width = 800, height = 640)
cvs.pack()
pen = tkinter.PhotoImage(file = "ペン.png")
wall = tkinter.PhotoImage(file = "壁.png")
game_main()
root.mainloop()