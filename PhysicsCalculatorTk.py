import tkinter as tk



def force_window():
        new_window = tk.Toplevel(window)
        new_window.title("Force Calculator")
        new_window.geometry("300x200")


        tk.Label(new_window, text="Mass").pack()
        mass_entry = tk.Entry(new_window)
        mass_entry.pack()

        tk.Label(new_window, text="Acceleration").pack()
        acceleration_entry = tk.Entry(new_window)
        acceleration_entry.pack()


        result_label = tk.Label(new_window, text="Result")
        result_label.pack()

        def calculate():
            mass = float(mass_entry.get())
            acceleration = float(acceleration_entry.get())

            Force = mass * acceleration
            result_label.config(text=f"Force = {Force}N")

        tk.Button(new_window,
                      text="Calculate",
                      command=calculate).pack()

window = tk.Tk()
window.title("Physics Calculator")
window.geometry("400x800")

force_button = tk.Button(
        window,
        text="Force",
        command=force_window,
        width=20,
        height=3

    )


force_button.pack(pady=10)


def speed_window():
    new_window = tk.Toplevel(window)
    new_window.title("Speed Calculator")
    new_window.geometry("300x200")


    speed = tk.Label(new_window, text="Distance").pack()
    distance_entry = tk.Entry(new_window)
    distance_entry.pack()

    speed = tk.Label(new_window, text="Time").pack()
    time_entry = tk.Entry(new_window)
    time_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        distance = float(distance_entry.get())
        time = float(time_entry.get())

        speed = distance / time
        result_label.config(text=f"Speed = {speed}KM/h")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

speed_button = tk.Button(
            window,
            text="Speed",
            command=speed_window,
            width=20,
            height=3)
speed_button.pack(pady=10)



def density_window():
    new_window = tk.Toplevel(window)
    new_window.title("Density Calculator")
    new_window.geometry("300x200")


    mass = tk.Label(new_window, text="Mass").pack()
    mass_entry = tk.Entry(new_window)
    mass_entry.pack()


    volume = tk.Label(new_window, text="Volume").pack()
    volume_entry = tk.Entry(new_window)
    volume_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        mass = float(mass_entry.get())
        volume = float(volume_entry.get())


        density = mass / volume
        result_label.config(text=f"Density = {density}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

weight_button = tk.Button(
            window,
            text="Density",
            command=density_window,
            width=20,
            height=3)
weight_button.pack(pady=10)

def weight_window():
    new_window = tk.Toplevel(window)
    new_window.title("Weight Calculator")
    new_window.geometry("300x200")


    weight = tk.Label(new_window, text="Mass").pack()
    mass_entry = tk.Entry(new_window)
    mass_entry.pack()




    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        mass = float(mass_entry.get())
        gravity = float(9.8)

        weight = mass * gravity
        result_label.config(text=f"Weight = {weight}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

weight_button = tk.Button(
            window,
            text="Weight",
            command=weight_window,
            width=20,
            height=3)
weight_button.pack(pady=10)




def momentum_window():
    new_window = tk.Toplevel(window)
    new_window.title("Momentum Calculator")
    new_window.geometry("300x200")


    mass = tk.Label(new_window, text="Mass").pack()
    mass_entry = tk.Entry(new_window)
    mass_entry.pack()


    velocity = tk.Label(new_window, text="Velocity").pack()
    velocity_entry = tk.Entry(new_window)
    velocity_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        mass = float(mass_entry.get())
        velocity = float(velocity_entry.get())

        momentum = mass * velocity
        result_label.config(text=f"Momentum = {momentum}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

momentum_button = tk.Button(
            window,
            text="Momentum",
            command=momentum_window,
            width=20,
            height=3)
momentum_button.pack(pady=10)

def kineticenergy_window():
    new_window = tk.Toplevel(window)
    new_window.title("Kinetic Energy Calculator")
    new_window.geometry("300x200")


    mass = tk.Label(new_window, text="Mass").pack()
    mass_entry = tk.Entry(new_window)
    mass_entry.pack()


    velocity = tk.Label(new_window, text="Velocity").pack()
    velocity_entry = tk.Entry(new_window)
    velocity_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        mass = float(mass_entry.get())
        velocity = float(velocity_entry.get())

        kineticenergy = 1/2*mass * velocity**2
        result_label.config(text=f"Kinetic Energy = {kineticenergy}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

kineticenergy = tk.Button(
            window,
            text="Kinetic energy",
            command=kineticenergy_window,
            width=20,
            height=3)
kineticenergy.pack(pady=10)

def potentialenergy_window():
    new_window = tk.Toplevel(window)
    new_window.title("Potential energy Calculator")
    new_window.geometry("300x200")


    mass = tk.Label(new_window, text="Mass").pack()
    mass_entry = tk.Entry(new_window)
    mass_entry.pack()


    height = tk.Label(new_window, text="Height").pack()
    height_entry = tk.Entry(new_window)
    height_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        mass = float(mass_entry.get())
        height = float(height_entry.get())

        potentialenergy = mass * 9.8 *  height
        result_label.config(text=f"Potential Energy = {potentialenergy}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

potentialenergy = tk.Button(
            window,
            text="Potential energy",
            command=potentialenergy_window,
            width=20,
            height=3)
potentialenergy.pack(pady=10)

def pressure_window():
    new_window = tk.Toplevel(window)
    new_window.title("Pressure Calculator")
    new_window.geometry("300x200")


    force = tk.Label(new_window, text="Force").pack()
    force_entry = tk.Entry(new_window)
    force_entry.pack()


    area = tk.Label(new_window, text="Area").pack()
    area_entry = tk.Entry(new_window)
    area_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        force = float(force_entry.get())
        area = float(area_entry.get())

        pressure = force / area
        result_label.config(text=f"Pressure = {pressure}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

pressure = tk.Button(
            window,
            text="Pressure",
            command=pressure_window,
            width=20,
            height=3)
pressure.pack(pady=10)

def work_window():
    new_window = tk.Toplevel(window)
    new_window.title("Work Calculator")
    new_window.geometry("300x200")


    force = tk.Label(new_window, text="Force").pack()
    force_entry = tk.Entry(new_window)
    force_entry.pack()


    distance = tk.Label(new_window, text="Area").pack()
    distance_entry = tk.Entry(new_window)
    distance_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        force = float(force_entry.get())
        distance = float(distance_entry.get())

        work = force * distance
        result_label.config(text=f"Work Done = {work}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

work = tk.Button(
            window,
            text="Work Done",
            command=work_window,
            width=20,
            height=3)
work.pack(pady=10)

def power_window():
    new_window = tk.Toplevel(window)
    new_window.title("Power Calculator")
    new_window.geometry("300x200")


    work = tk.Label(new_window, text="Work").pack()
    work_entry = tk.Entry(new_window)
    work_entry.pack()


    time = tk.Label(new_window, text="Time").pack()
    time_entry = tk.Entry(new_window)
    time_entry.pack()


    result_label = tk.Label(new_window, text="Result")
    result_label.pack()

    def calculate():
        work = float(work_entry.get())
        time = float(time_entry.get())

        power = work / time
        result_label.config(text=f"Power = {power}")

    tk.Button(new_window,
                  text="Calculate",
                  command=calculate).pack()

power = tk.Button(
            window,
            text="Power",
            command=power_window,
            width=20,
            height=3)
power.pack(pady=10)

window.mainloop()