import os

re_op = ' > ' # Redirection Operator

class Laser:


    def __init__(self):
        self.terminal_width = os.get_terminal_size().columns


    def gap(self, gaps=0):
        if gaps < 1:
            self.gaps = 1
        else:
            self.gaps = gaps

        while self.gaps > 0:
            print(''.center(self.terminal_width))
            self.gaps -= 1


    def center(self, print_content=''): 
        print('{}'.format(print_content).center(self.terminal_width))


    def get(self, print_content=''): 
        get_output = input('{}{}'.format(print_content, re_op).center(int(self.terminal_width/2)))
        output = get_output.lower()
        return output