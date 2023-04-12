import pandas as pd

import warnings
import pdb
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 150)

#path = os.path.join(os.getcwd(), 'dataset/')
path = "C:/Users/HiroshiHarada/DeepLearning/BoatRace/Acquisition_Data/boat-racer_csv/"

df = pd.read_csv(path + 'fan0410.csv', encoding="ANSI")

pdb.set_trace()



