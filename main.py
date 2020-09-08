# from indeed import get_jobs as get_indeed_jobs
# from so import get_jobs as get_so_jobs
# from save import save_to_file
#
# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jobs = so_jobs + indeed_jobs
# save_to_file(jobs)


class Car:
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "Black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"{self.color} Car with {self.wheels} wheels"


class Convertible(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        print("Taking off")

    def __str__(self):
        return f"{self.color} Car with no roof"


porche = Convertible(color="Red", price="$50")
porche.take_off()

ferrari = Car()
ferrari.color = "Yellow"

mini = Car()
mini.color = "White"

print(porche)
