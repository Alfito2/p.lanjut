from abc import ABC, abstractmethod

# class Animal(ABC):
#     def speak(self):
#         pass
#     def foot(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Bark!"
#     def foot(self):
#         return 4

# class Chiken(Animal):
#     def speak(self):
#         return "chik-chik"
#     def foot(self):
#         return 2
    
# # abstrak
# # dog = Dog()
# # chiken = Chiken()


# def animal_behavior(animal:Animal):
#     print(f"The animal says: {animal.speak()}")
#     print(f"The animal has: " + str(animal.foot()) + "legs")

# dog = Dog();
# chiken = Chiken();

# animal_behavior(dog);
# animal_behavior(chiken);

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
    print(f"harga mobil: " + str(mobil.harga()) + "legs")

bmw = BMW();
avanza = Avanza();
ferarri = Ferarri();

mobil_behavior(bmw);
mobil_behavior(avanza);
mobil_behavior(ferarri);

