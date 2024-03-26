#!/usr/bin/env python3

# MIT License

# Copyright (c) 2023-2024 Achille MARTIN

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Re-usable PID class
# Inspired from: https://github.com/ivmech/ivPID/blob/master/PID.py

class PID:

    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.0, set_point=1.0, dt=0.1, windup_guard=None, output_saturation=None, Kf=None):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.sp = set_point
        self.dt = dt
        self.wg = windup_guard
        self.os = output_saturation
        self.Kf = Kf
        
        self.reset()
    
    def reset(self):
        self.i_err = 0.0
        self.last_err = 0.0
        self.feedback_val = 0.0
  
    def saturate(self, value_to_saturate, saturation_value):
        if (value_to_saturate is not None and saturation_value is not None):
            if (value_to_saturate < -saturation_value):
                value_to_saturate = -saturation_value
            elif (value_to_saturate > saturation_value):
                value_to_saturate = saturation_value
        return value_to_saturate
  
    def compute(self, feedback_val=None):
        err, output, d_err = 0, 0, 0
        if(feedback_val is not None):
            self.feedback_val = feedback_val
            if(self.Kf is not None):
                self.feedback_val = self.Kf * feedback_val
    
        err = self.sp - self.feedback_val
        self.i_err += err * self.dt
        self.i_err = self.saturate(self.i_err, self.wg)
        d_err = (err - self.last_err) / self.dt
    
        output = (self.Kp * err + self.Ki * self.i_err + self.Kd * d_err)
        output = self.saturate(output, self.os)
        
        self.last_err = err
        self.feedback_val = output
    
        return output

