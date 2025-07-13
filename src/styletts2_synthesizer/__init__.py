"""
StyleTTS2 Synthesizer Package
"""
import os
__version__ = "0.1.0"

os.environ['PHONEMIZER_ESPEAK_LIBRARY'] = r'C:/Program Files/eSpeak NG/libespeak-ng.dll'
os.environ['ESPEAK_DATA_PATH'] = r'C:/Program Files/eSpeak NG/espeak-ng-data'

# Import everything from your modules
try:
    from .clsynthesize import clsynthesize
    from .compute import *
    from .gruut_phonemize import *
    from .ljspeechimportable import *
    from .losses import *
    from .meldataset import *
    from .models import *
    from .optimizers import *
    from .styletts2importable import *
    from .text_utils import *
    from .utils import *
except ImportError as e:
    print(f"Warning: Could not import some modules: {e}")

