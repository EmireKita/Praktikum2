import random

class GuessTheAnimal:
    def __init__(self):
        self.animals = {
            "gajah": "Saya adalah mamalia terbesar di darat. Saya memiliki belalai yang panjang.",
            "jerapah": "Saya memiliki leher yang sangat panjang dan saya suka makan daun dari pohon tinggi.",
            "ikan paus": "Saya adalah mamalia yang hidup di laut dan saya adalah yang terbesar di dunia.",
            "harimau": "Saya adalah kucing besar dengan garis-garis hitam di tubuh saya.",
            "kangguru": "Saya berasal dari Australia dan saya melompat dengan kaki belakang yang kuat.",
            "koala": "Saya adalah hewan marsupial dari Australia dan saya suka makan daun eukaliptus.",
            "panda": "Saya berasal dari Cina dan saya suka makan bambu.",
            "burung hantu": "Saya adalah burung malam yang bisa memutar kepala saya hampir 360 derajat."
        }
        self.animal, self.hint = random.choice(list(self.animals.items()))

    def play(self):
        print("Selamat datang di permainan Tebak Hewan!")
        print("Berikut adalah petunjuknya: ")
        print(self.hint)

        for attempt in range(3):
            guess = input("Tebakan Anda: ").lower()
            if guess == self.animal:
                print("Selamat! Tebakan Anda benar!")
                return
            else:
                print("Tebakan Anda salah. Coba lagi.")

        print(f"Maaf, Anda kalah. Hewan yang dimaksud adalah: {self.animal.capitalize()}")

if __name__ == "__main__":
    game = GuessTheAnimal()
    game.play()
