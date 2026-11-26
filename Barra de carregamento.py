from tqdm import tqdm
import time

for i in tqdm(range(100), desc='Carregando dados'):
    time.sleep(0.05)
