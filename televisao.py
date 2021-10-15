class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True 

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminiui_canal(self):
        if self.ligada:
            self.canal -= 1
    
televisao = Televisao()

print('A TV está ligada? {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
televisao.aumenta_canal()

print('A TV está ligada? {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
televisao.aumenta_canal()
televisao.aumenta_canal()

print('A TV está ligada? {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.power()
televisao.diminiui_canal()
