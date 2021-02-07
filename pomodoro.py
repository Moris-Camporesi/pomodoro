import time, winsound


class pomodoro_timer:

    def __init__(self):
        self.studytime_def = 50
        self.breaktime_def = 10
        self.running = True
        # first_step = self.messaging()
        

        # # if first_step == "START":
        #     print("\nAlright let's start!")
        #     self.start()
        
        # if first_step == "EDIT":
        #     self.timer_settings()

        # if first_step == "SETTINGS":
        #     self.misc_settings()

    def __str__(self):
        return "Current timer-version '0.03'."

    def __repr__(self):
        return "This is the current pomodoro-build"

    def messaging(self):
        inpt = input(f"Do you want to START a timer,\nEDIT a timer or\ngo to the SETTINGS?\n\nThe default timer is {self.studytime_def}/{self.breaktime_def}.\n")
        return inpt


    def timer(self, study_t = 50, break_t = 10):
        
        def studying(timer):
            t = timer * 60
            while t: 
                mins, secs = divmod(t, 60) 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                print(timer, end="\r") 
                time.sleep(1) 
                t -= 1
            self.sound()
            print("It's time for a break!") 
        def study_break(timer):
            t = timer * 60
            while t: 
                mins, secs = divmod(t, 60) 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                print(timer, end="\r") 
                time.sleep(1) 
                t -= 1
            self.sound()
            print("It's time for to work!") 
        
        while self.running:
            studying(study_t)
            study_break(break_t)

    def start(self):
        self.timer()
    
    def pause(self):
        pass

    def stop(self):
        exit

    def sound(self):
        winsound.Beep(400, 200)
        winsound.Beep(400, 200)
        winsound.Beep(1800, 800)

    def timer_settings(self):
        studytime = int(input("How long should the work period be? "))
        breaktime = int(input("How long should the break period be? "))
        decis = input("Do you want to start the new timer? [YES/NO]\n")
        if decis == "YES" or "Y":
            self.timer(studytime,breaktime)
        else:
            pass #implement setting here

    def misc_settings(self):
        pass


# a = pomodoro()
# print("Hello Sabrina")
