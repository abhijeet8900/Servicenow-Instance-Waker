import os
import winsound 

def fail_noise():
    winsound.PlaySound('failed_tone.wav', winsound.SND_FILENAME)  



def success_noise():
    winsound.PlaySound('completed_tone.wav', winsound.SND_FILENAME)  


