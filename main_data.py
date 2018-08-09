"""This module gives the analysis of the route from home to office"""
import os
import math
import pandas as pd


def find_peaks(acc_):
    """Find peaks in the series"""
    peaks = 0
    for i in range(1, len(acc_)-1):
        if (acc_[i - 1] < acc_[i] and acc_[i] > acc_[i + 1]):
            peaks += 1
    return peaks


DISTANCE = 900

DATA = pd.read_csv('1B_7th.csv', sep=';', header=1)

HEADER = DATA.columns.values.tolist()
DATA = DATA.set_index(HEADER[-2])

DATA.index = pd.to_datetime(DATA.index, unit='ms')

ACCX = DATA[HEADER[6]]
ACCY = DATA[HEADER[7]]
ACCZ = DATA[HEADER[8]]
ACC = ACCX ** 2 + ACCY ** 2 + ACCZ ** 2
ACC = ACC.apply(math.sqrt)  # magnitude of Acceleration
ACC = (ACC - ACC.mean())/ACC.std()  # Normalize Acceleration

TIME_SEC = (DATA.index[-1] - DATA.index[0]).total_seconds()

NO_OF_STEPS = find_peaks(-1 * ACC) + find_peaks(ACC)
STEPS_PER_MIN = NO_OF_STEPS / (TIME_SEC / 60)
AVERAGE_STRIDE_LENGTH = DISTANCE / NO_OF_STEPS
TIME = TIME_SEC / 60
VELOCITY = (DISTANCE/1000)/((TIME_SEC / 60)/60)
os.system('clear')

print("The distance from PG to 1B office is %d m" % DISTANCE)
print("Total steps taken to reach the destination are %d" % NO_OF_STEPS)
print("The number of steps taken per min are %d" % STEPS_PER_MIN)
print("Average stride length is %.2f m" % AVERAGE_STRIDE_LENGTH)
print("Average velocity is %.2f km/hr" % VELOCITY)
print("Total time to reach destination is %.2f min" % TIME)
