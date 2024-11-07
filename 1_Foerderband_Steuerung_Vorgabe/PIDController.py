# Copyright 2020 Hochschule Luzern - Informatik
# Author: Simon van Hemert <simon.vanhemert@hslu.ch>
# Author: Peter Sollberger <peter.sollberger@hslu.ch>

class PIDController:
    """
    Implements a PID controller.
    """
    def __init__(self):
        # Initialize variables
        self.refposition = 415               # Reference position in mm
        self.errorLinear = self.refposition  # Initial error
        self.errorIntegral = 0

        # PID constants:
        self.kp = 0.5
        self.Tn = 10
        self.Tv = 0.001

    def reset(self):
        """
        Restore controller with initial values.
        """
        self.errorLinear = self.refposition
        self.errorIntegral = 0

    def calculateTargetValue(self, actualValue):
        """
        Calculate next target values with the help of a PID controller.
        """
        # TODO:
        #  1. Speichern Sie den vorherigen Fehler in der Variablen
        #     'errorLinearOld', berechnen Sie den neuen Fehler und
        #     speichern Sie diesen in self.errorLinear
        #  2. Berechnen Sie
        #     - den aktuellen Positions-Fehler 'self.errorLinear'
        #     - das aktuelle Fehler-Integral 'errorIntegral'; denken
        #       Sie dabei an windup
        #     - das aktuelle Fehler-Derivative 'errorDerivative'
        #  3. Berechnen Sie aus den Fehlern die P, I und D-Anteile;
        #     Sie können diese Werte in den Variablen p_part, i_part
        #     und d_part abspeichern oder die Berechnungen direkt in die
        #     Liste der PIDactions schreiben

        p_part = 0  # TODO: Berechnen Sie den P-Anteil
        i_part = 0  # TODO: Berechnen Sie den I-Anteil
        d_part = 0  # TODO: Berechnen Sie den D-Anteil

        # Save the three parts of the controller in a vector
        PIDactions = [p_part, i_part, d_part]
        # The output speed is the sum of the parts, 1023 equals 5V = max output
        targetValue = sum(PIDactions)

        return int(targetValue), PIDactions
