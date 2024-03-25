#!/usr/bin/env python3

# Demonstrate PID tuning with simple physics system

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pid_utility import PID

class Vehicle:
    def __init__(self, initial_pos=0, initial_vel=0, mass=1):
        self.m = mass
        self.x = initial_pos
        self.vx = initial_vel

    def physics_model(self, x_out, t, m, f, b):
        x1 = x_out[0]
        x2 = x_out[1]
        dx1_dt = x2
        dx2_dt = f/m - b/m*x2
        dx_dt = [dx1_dt, dx2_dt]
        return dx_dt

    def move(self, f=0, b=0, dt=1):
        # Force analysis: Sum(f_on_vehicle) = m_vehicle * a_vehicle
        # f_push(t) -  b*dx(t)/dt = m*d^2x(t)/dt^2
        # Where b is a constant equal to: 6*pi*0.001*0.5 = 0.009 kg/s (water fluid)
        
        # initial condition
        x_0 = [self.x, self.vx]
    
        # current time and next time step
        t = np.array([0.0, dt])
    
        # solve ODE
        sol = odeint(self.physics_model, x_0, t, args = (self.m, f, b))
        self.x = sol[1, 0]
        self.vx = sol[1, 1]

if __name__ == "__main__":
    
    # Create an instance of the vehicle
    # Set initial position and vel, and mass
    
    start_pos = 500
    start_vel = 0
    mass_vehicle = 1
    my_vehicle = Vehicle(start_pos, start_vel, mass_vehicle)
    
    # Define physics of the environment
    b = 0.09
    
    # Create an instance of the controller
    # Set parameters and position target
    
    target_pos = 0
    my_pid = PID(0.01, 0.0, 0.1, set_point=target_pos, dt=1.0, output_saturation=1, Kf=1)
    x_vehicle_arr = []
    vx_vehicle_arr = []
    input_arr = []
    x_vehicle = my_vehicle.x
    x_vehicle_arr.append(x_vehicle)
    vx_vehicle_arr.append(my_vehicle.vx)
    
    # Perform the control to the target_pos
    
    nb_steps = 100
    for i in range(nb_steps):
        x_input = my_pid.compute(x_vehicle)
        my_vehicle.move(x_input, b, my_pid.dt)
        x_vehicle = my_vehicle.x
        input_arr.append(x_input)
        x_vehicle_arr.append(x_vehicle)
        vx_vehicle_arr.append(my_vehicle.vx)
    input_arr.append(my_pid.compute(x_vehicle))
      
    # Show results
    time_arr = np.arange(0, (nb_steps+1)*my_pid.dt, my_pid.dt)
    
    fig, axs = plt.subplots(3)
    fig.suptitle("Vehicle motion and command")
    axs[0].set(xlabel="", ylabel="x(t) in m")
    axs[0].plot(time_arr, x_vehicle_arr)
    axs[0].grid(True)
    axs[1].set(xlabel="", ylabel="v(t) in m/s")
    axs[1].plot(time_arr, vx_vehicle_arr)
    axs[1].grid(True)
    axs[2].set(xlabel="time(t) in s", ylabel="u(t) in N")
    axs[2].plot(time_arr, input_arr)
    axs[2].grid(True)
    
    plt.show()
    
    # Tune PID Controller
    # Take inspiration from: https://pidexplained.com/how-to-tune-a-pid-controller/
    # Ziegler-Nichols method for 2nd order or for any order: https://faculty.mercer.edu/jenkins_he/documents/TuningforPIDControllers.pdf
    
    # Start by setting only Kp very low
    # Make Kp vary until your system starts to become unstable (or to overshoot a lot)
    # Write down the Kp_limit and set Kp to 0.5*Kp_limit
    
    # If the system is too slow or there is a steady-state error, add a Ki and set it very low
    # Make Ki vary until your system starts to become unstable
    # Write down the Ki_limit and set Ki to 0.5*Ki_limit
    
    # If the system overshoots, add a Kd and set it very low
    # Make Kd vary until your system starts to become unstable
    # Write down the Kd_limit and set Kd to 0.5*Kd_limit

