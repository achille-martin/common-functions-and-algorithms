#!/usr/bin/env python3

# Understand the resolution of differential equations

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

if __name__ == "__main__": 

  # parameters
  m = 0.5 # kg
  b = 0.09 # kg/s
  f = 0 # N
  duration = 100 # s

  # additional parameters
  fx = 0 # N
  fy = 0 # N
  bx = 0.1 # kg/s
  by = 0.01 # kg/s

  ## SIMPLE MODEL

  # Simple modelling only takes into account a force pushing/pulling the vehicle
  # The equation is:
  # Sum(Forces) = m * a
  # Projected onto x-axis:
  # f(t) = m*d^2x(t)/dt^2

  def simple_model(x, t, m, f):
	  x1 = x[0]
	  x2 = x[1]
	  dx1_dt = x2
	  dx2_dt = f/m
	  dx_dt = [dx1_dt, dx2_dt]
	  return dx_dt

  # initial condition
  x_0 = [0, 5]

  # time points
  t = np.linspace(0, duration)

  # solve ODE
  x = odeint(simple_model, x_0, t, args = (m, f))

  # plot results
  plt.figure("Simple model")
  plt.plot(t, x[:,0])
  plt.xlabel('time(t) in s')
  plt.ylabel('x(t) in m')

  ## ADVANCED MODEL

  # Advanced modelling takes into account a force pushing/pulling the vehicle
  # and viscous force from water
  # The equation is:
  # Sum(Forces) = m * a
  # Projected onto x-axis:
  # f(t) -  b*dx(t)/dt = m*d^2x(t)/dt^2
  # Where b is a constant equal to: 6*pi*0.001*0.5 = 0.009 kg/s (water fluid)

  def advanced_model(x, t, m, f, b):
	  x1 = x[0]
	  x2 = x[1]
	  dx1_dt = x2
	  dx2_dt = f/m - b/m*x2
	  dx_dt = [dx1_dt, dx2_dt]
	  return dx_dt

  # initial condition
  x_0 = [0, 5]

  # time points
  t = np.linspace(0, duration)

  # solve ODE
  x = odeint(advanced_model, x_0, t, args = (m, f, b))

  # plot results
  plt.figure("Advanced model")
  plt.plot(t, x[:,0])
  plt.xlabel('time(t) in s')
  plt.ylabel('x(t) in m')

  ## 2D SYSTEM MODEL

  # 2D system with linear drag and currents
  # Sum(Forces) = m * a
  # Projected onto x-axis:
  # fx(t) -  bx*dx(t)/dt = m*d^2x(t)/dt^2
  # Projected onto y-axis:
  # fy(t) -  by*dx(t)/dt = m*d^2y(t)/dt^2

  def system_2d_model(x, t, m, fx, fy, bx, by):
	  x1 = x[0]
	  x2 = x[1]
	  y1 = x[2]
	  y2 = x[3]
	  dx1_dt = x2
	  dx2_dt = fx/m - bx/m*x2
	  dy1_dt = y2
	  dy2_dt = fy/m - by/m*x2
	  dx_dt = [dx1_dt, dx2_dt, dy1_dt, dy2_dt]
	  return dx_dt

  # initial condition
  x_0 = [0, 5, 0, 2.5]

  # time points
  t = np.linspace(0, duration)

  # solve ODE
  x = odeint(system_2d_model, x_0, t, args = (m, fx, fy, bx, by))

  # plot results
  plt.figure("2D System")
  plt.plot(x[:,0], x[:,2])
  plt.xlabel('x(t) in m')
  plt.ylabel('y(t) in m')

  ## Show the results
  plt.show()

  # TODO: replace odeint with Euler method for 1st and 2nd order
  # The principle is: y1 = y0 + h * y_prime(x0, y0)

