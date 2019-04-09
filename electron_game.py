# I was thinking about it and it seems like any game with only 1 turn has significantly less utility than a game with 2 turns for quantum strategies. You can only instate a quantum state, but you cannot convert that back into a pure state, inevitably leaving a certain amount up to chance. -Brandon

import sys
import numpy as np
import copy as cp
import random as rd
import math as mt

###### Global Variables #####

# State
#The state of the electron spin. Starts at (1, 0)
State = np.array([1, 0])

# Exchange
#The Exchange matrix. When applied to the State, flips the 1s and 0s
Exchange = np.array([[0, 1], [1, 0]])

# SuperIdentity
#A Matrix that creates a superimposition of probabilities when applied to the State.
#When applied twice to the State, returns the State.
SuperIdentity = np.array([[(1 / mt.sqrt(2)), (1 / mt.sqrt(2))], [(1 / mt.sqrt(2)), - (1 / mt.sqrt(2))]])

# SuperNaught
#A Matrix that creates a superimposition of probabilities when applied to the State.
#When applied twice to the State, returns the inverse of the State.
SuperNaught = np.array([[(1 / mt.sqrt(2)), - (1 / mt.sqrt(2))], [(1 / mt.sqrt(2)), (1 / mt.sqrt(2))]])

##### Transformations #####
# No Flip
#Doesn't change the state of the electron
def N(st):
    return st

# Flip
#Flips the electron
def F(st):
    return np.matmul(Exchange, st)

# Superimpose(Identity)
#Instates a superimposition of states; when performed twice, returns the original state
def SI(st):
    return np.matmul(SuperIdentity, st)

# Superimpose(Naught)
#Instates a superimposition of states; when performed twice, returns the reverse of the original state
#Not necessarily used in this game, but potentially useful to have on hand for other games
def SN(st):
    return np.matmul(SuperNaught, st)

# There are an infinitum of possible quantum transformations, although the two mentioned here are the simplest.

##### Game #####

# qGamble
#Takes 3 Functions representing the two choices made by Q and the 1 choice made by P.
#Always performs on a [1, 0] ndarray, represending the original electron state.
def qGamble(Q1, P1, Q2):
    newState = Q2(P1(Q1(State)))
    for i in range(len(newState)):
        #np.round is used to correct rounding errors when quantum strategies have been used.
        if np.round(newState[i], 5) == 0:
            newState[i] = int(0)
        elif np.round(newState[i], 5) == 1:
            newState[i] = int(1)
        elif np.round(newState[i - 1], 5) == 1:
            newState[i] = int(0)
        elif np.round(newState[i - 1], 5) == 0:
            newState[i] = int(1)
        #The below statement handles a collapse of multiple simultaneous states.
        #Currently this works appropriately, but it needs to be revised for:
        #1. models encompassing more than 2 states (such as rock paper scissors)
        #2. a more steadfast interaction between the simultaneity of the states.
        else:
            r = rd.randint(1, 10)
            p = (newState[i] ** 2) * 10
            if r > p:
                newState[i] = 0
            elif r <= p:
                newState[i] = 1
            else:
                print("error returning from superimposed state")
                return 0
    return newState


# score
#Takes a state as an argument. Returns 1 if Q wins, and 0 if Picard wins.
def score(st):
    if st == np.array([1, 0]):
        return 1
    elif st == np.array([0, 1]):
        return 0
    else:
        print("score error")
        return 0


##### Strategy #####

# If someone has an idea in mind or wants to take a shot at this

