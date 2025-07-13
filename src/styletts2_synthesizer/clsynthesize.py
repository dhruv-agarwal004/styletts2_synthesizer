
import torch
import nltk
nltk.download('punkt_tab')
import os
from txtsplit import txtsplit
import numpy as np
import pickle
import sys
from tqdm import tqdm
from scipy.io import wavfile
from .styletts2importable import LFinference, compute_style

import phonemizer
global_phonemizer = phonemizer.backend.EspeakBackend(language='en-us', preserve_punctuation=True,  with_stress=True)

def clsynthesize(text, voice, output, vcsteps, embscale, alpha, beta,speed):
    import warnings
    if text.strip() == "":
        raise ValueError("You must enter some text")
    if len(text) > 50000:
        raise ValueError("Text must be <50k characters")
    if embscale > 1.3 and len(text) < 20:
        warnings.warn("WARNING: You entered short text, you may get static!", UserWarning)
    print("*** saying ***")
    print(text)
    print("*** end ***")
    texts = txtsplit(text)
    audios = []
    vs = compute_style(voice)
    s_prev= None
    for t in tqdm(texts):
        try:
            audio,s_prev= LFinference(text=t, s_prev=s_prev, ref_s=vs, alpha=alpha, beta=beta, diffusion_steps=vcsteps, embedding_scale=embscale,speed_multiplier=speed)
            print('audio is ', audio)
            print('s_prev is ', s_prev)
            audios.append(audio)
        except Exception as e:
            print(f"Error during synthesis of segment: {t}\n{e}")
            continue
    if not audios:
        raise RuntimeError("No audio was generated.")
    final_audio = np.concatenate(audios)
    wavfile.write(output, 24000, final_audio)
    return (24000, final_audio)

