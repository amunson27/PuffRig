# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:04:35 2020
​
@author: oostland
"""
import pandas as pd
import os
import time
import puffStim
#%%
# General parameters
#t = eyeblink.eyeblink()  # I think this can be deleted?
t = puffStim.eyeblink() # create an eyeblink object
t.settrial('numTrial',3)
time.sleep(0.01)
#%%
# Trial-specific paramaters
# First, open csv file with trial-specific paramaters
#filepath = 'S:\\oostland\\Protocols\\Eyeblink_rig' # Possibly stil change
file = 'puffTime.csv'
df = pd.read_csv(file)

#Set the parameters for the initial trial and start session
t.settrial('prePuffDur',250)# currently setting 250 millis of trial prior to first puff
time.sleep(0.01)
t.settrial('puffNum',df.puffNum[0])
time.sleep(0.01)
t.settrial('puffFreq',df.puffFreq[0])
time.sleep(0.01)
t.settrial('interTrialInterval',df.iti[0])
time.sleep(3)
t.startSession()

for ind, trialid in enumerate(df.trialid):
    #poll for when the current trial has finished
    while not t.trial['justFinished']:
        time.sleep(0.03)

    #reset the trial parameters at the completion of each trial
    t.trial['justFinished'] = False
    time.sleep(0.01)
    t.settrial('interTrialInterval', df.iti[trialid]) #ms, lowest ITI from random draw
    time.sleep(0.01)
    t.settrial('puffNum', df.puffNum[trialid]) # number of puffs within this trial
    time.sleep(0.01)
    t.settrial('puffFreq', df.puffFreq[trialid]) # number of puffs within this trial
