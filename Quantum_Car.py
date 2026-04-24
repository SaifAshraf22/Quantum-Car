class Engine:
    def __init__(self):
        self.speed = 0

    def increase(self):
        self.speed += 1

    def decrease(self):
        if self.speed > 0:
            self.speed -= 1

    def set_speed(self, car_speed):
        while self.speed < car_speed:
            self.increase()
        while self.speed > car_speed:
            self.decrease()

    def __str__(self):
        return "Engine"


class GasolineEngine(Engine):
    def __str__(self):
        return "Gasoline Engine"


class ElectronicEngine(Engine):
    def __str__(self):
        return "Electronic Engine"

class MixedHybridEngine(Engine):
    def __init__(self):
        super().__init__()
        self.gas = GasolineEngine()
        self.electric = ElectronicEngine()
        self.active_engine = None

    def set_speed(self, car_speed):
        if car_speed < 50:
            self.active_engine = self.electric
        else:
            self.active_engine = self.gas

        self.active_engine.set_speed(car_speed)
        self.speed = car_speed 

    def __str__(self):
        if self.active_engine:
            return f"Hybrid using {self.active_engine}"
        return "Hybrid Engine"


class Car:
    def __init__(self, engine):
        self.engine = engine
        self.speed = 0

    def start(self):
        self.speed = 0
        self.engine.set_speed(self.speed)
        print("Car started with", self.engine)

    def stop(self):
        self.speed = 0
        self.engine.set_speed(self.speed)
        print("Car stopped")

    def accelerate(self):
        if self.speed < 200:
            self.speed += 20
            if self.speed > 200:
                self.speed = 200

            self.engine.set_speed(self.speed)
            print(f"Speed: {self.speed} | Engine: {self.engine}")

    def brake(self):
        if self.speed > 0:
            self.speed -= 20
            if self.speed < 0:
                self.speed = 0

            self.engine.set_speed(self.speed)
            print(f"Speed: {self.speed} | Engine: {self.engine}")

    def change_engine(self, new_engine):
        self.engine = new_engine
        self.engine.set_speed(self.speed)
        print("Engine changed to", self.engine)


class CarFactory:
    @staticmethod
    def create_car(engine_type):
        if engine_type == "gas":
            return Car(GasolineEngine())
        elif engine_type == "electric":
            return Car(ElectronicEngine())
        elif engine_type == "hybrid":
            return Car(MixedHybridEngine())
        else:
            print("Invalid engine type")
            return None



if __name__ == "__main__":
    factory = CarFactory()

    gas_car = factory.create_car("gas")
    electric_car = factory.create_car("electric")
    hybrid_car = factory.create_car("hybrid")

    print("\n Gas Car")
    gas_car.start()
    gas_car.accelerate()
    gas_car.accelerate()
    gas_car.brake()
    gas_car.stop()

    print("\n Electric Car")
    electric_car.start()
    electric_car.accelerate()
    electric_car.stop()

    print("\n Hybrid Car")
    hybrid_car.start()
    hybrid_car.accelerate() 
    hybrid_car.accelerate()
    hybrid_car.accelerate()
    hybrid_car.brake()
    hybrid_car.stop()

    print("\n Change Engine")
    gas_car.change_engine(ElectronicEngine())
    gas_car.accelerate()