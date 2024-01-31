# Simple version of the "Simon" game using tkinter.
#
# This is a very basic implementation that probably has some bugs!
#
# It is not as fully event-driven as I would like, relying instead
# on using time.sleep() to time certain UI events.
#
import tkinter
import random                   # for randint()
import time                     # for sleep()

class simon(tkinter.Tk):
    '''Application class for Simon, derived from the base tkinter 
    application class, which is called 'Tk'.'''
    
    # Define standard colors used.
    BRIGHTRED    = 'red'
    RED          = '#9b0000'
    BRIGHTGREEN  = '#00ff00'
    GREEN        = '#009b00'
    BRIGHTBLUE   = 'blue'
    BLUE         = '#00009b'
    BRIGHTYELLOW = 'yellow'
    YELLOW       = 'yellow3'
    DARKGRAY     = '#282828'

    # game states
    DEMO = 1         # Game is showing the new pattern.
    PLAY = 2         # Player is mimicking the pattern.
    LOST = 3         # Player lost.

    DELAY = 500      # timer delay in milliseconds.

    SIZE = 640       # Total window width and height.
    ROWS = 2         # How many rows of buttons.
    COLS = 2         # How many columns of buttons.
    BUTTONS = ROWS * COLS # Total number of buttons.
    GAP = 10         # Number of pixels between buttons.
    
    # There are as many colors as there are buttons!
    COLORS = [BLUE, RED, YELLOW, GREEN]
    FLASHCOLORS = [BRIGHTBLUE, BRIGHTRED, BRIGHTYELLOW, BRIGHTGREEN]

    assert BUTTONS <= len(COLORS)

    def __init__(self):
        '''Initialize the Simon application.'''
        super().__init__(None) # initialize the base class.
        self.score = 0        # total score.
        self.newgame()
        
        # Create the canvas.
        self.canvas = tkinter.Canvas(self,
                                     width = self.SIZE,
                                     height = self.SIZE,
                                     bg = 'white')
        self.canvas.pack()
        
        self.btn_ids = []       # list of rectangle object ids

        # Compute dimensions of the four big rectangles.
        xr = (self.SIZE - self.GAP * (self.COLS + 1)) // self.COLS
        yr = (self.SIZE - self.GAP * (self.ROWS + 1)) // self.ROWS

        # Create the rectangles, computing their sizes and positions.
        for i, color in enumerate(self.COLORS):
            # Compute the row and column of the rectangle.
            row = i % self.ROWS
            col = i // self.ROWS
            x0 = self.GAP * (col + 1) + xr * col
            x1 = x0 + xr
            y0 = self.GAP * (row + 1) + yr * row
            y1 = y0 + yr
            # Rectangle is created by specifying the upper corner and lower
            # corner.
            id = self.canvas.create_oval(x0, y0, x1, y1, fill = color)
            self.btn_ids.append(id) # save the ID of the rectangle.

        self.title('Simon, score: {}'.format(self.score))
        lbl = tkinter.Label(self, text = 'This is basically a simon says game where you need to press the buttons in the order given')
        lbl.pack()
        # Start the timer handler.
        self.auto = self.after(self.DELAY, self.on_timer) 

        # Register a handler for the left mouse button.
        # This means that if the user clicks over the canvas, this
        # function will be called.
        self.canvas.bind("<Button-1>", lambda event: self.on_click(event))
        self.canvas.bind('<Button-3>', lambda ko: self.end(ko))
        
    def end(self, ko):
        exit()

    def newgame(self):
        '''Reset some fields in preparation for a new sequence.'''
        self.pattern = []     # stores the pattern of colors
        self.player_index = 0 # index of user's last successful click.
        self.state = self.DEMO
        
    def on_click(self, event):
        '''Handle a left click from the mouse.'''
        if self.state != self.PLAY:
            return
        # Convert event coordinate to canvas coordinate.
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        # Find the closes rectangle.
        id = self.canvas.find_closest(x, y)[0]
        x0, y0, x1, y1 = self.canvas.coords(id)
        # Collision test - check whether the mouse click lies inside one
        # of the buttons.
        r = (x1-x0)/2
        x00 = (x1+x0)/2
        y00 = (y1+y0)/2
        f = ((x00-x)**2+(y00-y)**2)**0.5
        if f >= r:
            return              # skip the rest if not in button.
        i_button = self.btn_ids.index(id)
        if self.pattern[self.player_index] == i_button:
            # Clicked the correct button.
            self.flash(i_button)
            self.player_index += 1
            if len(self.pattern) == self.player_index:
                # Finished the pattern so far.
                self.state = self.DEMO
                self.player_index = 0
                self.score += len(self.pattern)
                self.title('Simon, score: {}'.format(self.score))
                print("SCORE: ", self.score)
                time.sleep(1.0)
        else:
            # Clicked the wrong button.
            print("YOU LOSE")
            self.state = self.LOST
            self.gameover()
            self.newgame()
        
    def gameover(self):
        '''Give the user a visual indication they lost, by flashing
        all four buttons dark grey.'''
        # Turn all 4 buttons dark grey.
        for id in self.btn_ids:
            self.canvas.itemconfig(id, fill = self.DARKGRAY)
        self.canvas.update()
        time.sleep(1.0)
        # Switch the buttons back to their normal colors.
        for id, color in zip(self.btn_ids, self.COLORS):
            self.canvas.itemconfig(id, fill = color)
        self.canvas.update()
        self.score = 0
        time.sleep(1.0)
                

    def on_timer(self):
        '''This method is used to handle a timer event. It is called 
        in the main event loop when a timer event fires.
        '''
        if self.state == self.DEMO:
            # Add a new element to the pattern.
            self.pattern.append(random.randint(0, self.BUTTONS - 1))
            # Now flash the pattern.
            for p in self.pattern:
                self.flash(p)
            # Transition to PLAY state, where we wait for button presses.
            self.state = self.PLAY
        # Start the next timer. The event loop will call on_timer after
        # DELAY milliseconds pass.
        self.auto = self.after(self.DELAY, self.on_timer)
    
    def flash(self, i):
        '''Flash one of the four buttons.'''
        if i < 0 or i >= self.BUTTONS:
            raise ValueError("Button index out of range.")
        id = self.btn_ids[i]
        # Draw the button in the highlighted color.
        self.canvas.itemconfig(id, fill = self.FLASHCOLORS[i])
        self.canvas.update()
        time.sleep(0.5)
        # Revert to the standard color.
        self.canvas.itemconfig(id, fill = self.COLORS[i])
        self.canvas.update()
        time.sleep(0.5)
        
if __name__ == '__main__':
    app = simon()
    app.mainloop()
