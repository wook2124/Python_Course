class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(self):
    print(self.doors)
    print("What is method.")

porche = Car()
porche.instance = "This is First instance"
porche.start(porche)