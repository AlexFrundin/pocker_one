class Game_Field:
    def __init__(self):
        self._field=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]

        #def __repr__(self):
            #return 5*'-'.join('|'.join([[cell for cell in row] + '\n' for row in self._field]))

        def set_sign(self,x,y,sign):
            self._field[x][y]=sign

        def check_rows(self):
            for row in self._field:
                if row==['X','X','X'] or row == ['0','0','0']:
                    return True
