from abc import ABC, abstractmethod

class Mobil(ABC):
    def kecepatan(self):
        pass
    def fasilitas(self):
        pass
    def harga(self):
        pass
    def kekuatan(self):
        pass
    def nama_mobil(self):
        pass

class BMW(Mobil):
    def kecepatan(self):
        return "2000 km"
    def fasilitas(self):
        return "4 sheat"
    def harga(self):
        return "2.000.000.000"
    def kekuatan(self):
        return "super kuat"
    def nama_mobil(self):
        return "BMW"
    
class Avanza(Mobil):
    def kecepatan(self):
        return "1500 km"
    def fasilitas(self):
        return "6 sheat"
    def harga(self):
        return "250.000.000"
    def kekuatan(self):
        return "kuat"
    def nama_mobil(self):
        return "Avanza"
    
class Ferarri(Mobil):
    def kecepatan(self):
        return "4000 km"
    def fasilitas(self):
        return "2 sheat"
    def harga(self):
        return "5.000.000.000"
    def kekuatan(self):
        return "super kuat"
    def nama_mobil(self):
        return "ferarri"
    
def mobil_behavior(mobil:Mobil):
    print(f"nama mobil: {mobil.nama_mobil()}")
    print(f"kecepatan mobil: {mobil.kecepatan()}")
    print(f"fasilitas mobil: { mobil.fasilitas()}")
    print(f"kekuatan: { mobil.kekuatan()}")
    print(f"harga mobil: " + str(mobil.harga()))

bmw = BMW();
avanza = Avanza();
ferarri = Ferarri();

mobil_behavior(bmw);
mobil_behavior(avanza);
mobil_behavior(ferarri);

