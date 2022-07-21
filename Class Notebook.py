class NoteBook:
    MINUSBPORT = 2
    MAXUSBPORT = 4
    LANPORT = 1
    WIFIMODUL = 1
    PROCESSOR = 1
    MAXRAM = 4
    GARDDISK = 1
    SCREEN = 1
    MOTHERBOARD = 1
    TOUCH = 1
    CAMERA = 1
    KEYBOARD = 1

    def __init__(self, diag, processor, ram, memory, color):
        self.diag = diag
        self.processor = processor
        self.volume_ram = ram
        self.volume_hard = memory
        self.color = color

    def choicenout(self):
        print('Выбиранный ноутбук: ')
        if self.volume_ram >= 16 and self.volume_hard >=256:
            print(f'Ноут с процессором {self.processor}, ОЗУ '
                  f'с объемом {self.volume_ram} Гб и с диском '
                  f'объемом {self.volume_hard} Гби цветом {self.color} '
                  f'является хорошим выбором')
        elif self.volume_ram < 16 and 20 <= self.volume_hard < 256:
            print(f'Ноут с процессором {self.processor}, ОЗУ '
                  f'с объемом {self.volume_ram} Гб и c диском '
                  f'объемом {self.volume_hard} Гб и цветом {self.color} '
                  f'является слабым выбором')
            print(f'нужно увеличить ОЗУ с {self.volume_ram} Гб до 16 Гб')

    def upgraide(self):
        print('Обновим ноут:')
        self.volume_ram += 8
        print(f'Увеличим ОЗУ до {self.volume_ram}')
        self.volume_hard += 64
        print(f'Увеличим объем диска до {self.volume_hard}')
        print(f'Теперь твой ноут с процессором {self.processor}, ОЗУ '
                  f'с объемом {self.volume_ram} Гб и c диском '
                  f'объемом {self.volume_hard} Гб и цветом {self.color} '
                  f' является хорошим выбором')


class Notebookmaterial:
    def materialmetal(self, metal):
        self.metal = metal
        print(f'Ноутбук  {self.metal}')

    def materialplastic(self, plastic):
        self.plastic = plastic
        print(f'Ноутбук {self.plastic}')



class ChoiceNoteMaterial(Notebookmaterial, NoteBook):
    pass



def main():
    nout = NoteBook(14, 'Pent', 32, 256, 'black')
    nout1 = NoteBook(14, 'AMD', 12, 64, 'black')
    nout.choicenout()
    nout1.choicenout()
    nout1.upgraide()

    nout2 = ChoiceNoteMaterial(14, 'Pent', 32, 256, 'black')
    nout2.materialplastic('пластиковый')
    nout2.materialmetal('неизвестно из чего сделан')
    nout2.choicenout()
    nout3 = ChoiceNoteMaterial(18, 'Pent', 2, 26, 'black')
    nout3.upgraide()
    nout3.choicenout()

if __name__ == '__main__':
    main()