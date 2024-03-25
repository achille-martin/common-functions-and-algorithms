#!/usr/bin/env python3

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

