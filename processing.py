
# Use audio loader explicitly for loading audio waveform :
from spleeter.separator import Separator
import ipdb
import glob
import time
import random
import warnings
import argparse
import sys
import traceback
warnings.filterwarnings('ignore')

import os

# os.environ["CUDA_VISIBLE_DEVICES"] = ""

def check_exist(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)


def check_done_or_not(filepath, output_path):
    new_filepath = os.path.join(output_path, filepath.split('/')[-1])[:-4]

    if os.path.exists(new_filepath):
        PROCESS = False
    else:
        PROCESS = True

    return PROCESS
    
def main(file_path, output_dir, use_MWF):
    st = time.time()
    separator = Separator('spleeter:4stems', MWF=use_MWF)  
    # List of input to process.
    audio_descriptors = glob.glob(os.path.join(file_path, '*.mp3'))
    print('total {} songs to process'.format(len(audio_descriptors)))
    random.shuffle(audio_descriptors)
    # Batch separation export.
    count = 0
    for i in audio_descriptors:
        print('='*100)
        print(i)
        PROCESS = check_done_or_not(i, output_dir)
        print('PROCESS:', PROCESS)
        if PROCESS:
            try:
                separator.separate_to_file(i, output_dir, synchronous=True)
            except Exception as e:
            #    print(e)
                error_class = e.__class__.__name__ #取得錯誤類型
                detail = e.args[0] #取得詳細內容
                cl, exc, tb = sys.exc_info() #取得Call Stack
                lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
                fileName = lastCallStack[0] #取得發生的檔案名稱
                lineNum = lastCallStack[1] #取得發生的行號
                funcName = lastCallStack[2] #取得發生的函數名稱
                errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
                print(errMsg)
            count += 1
        else:
            print('Already processed:', i)
        
        
    ed = time.time()

    # Wait for batch to finish.
    separator.join()
    print('total spend {}s for {} song. average: {}s'.format(ed - st, count, (ed-st)/count))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='spleeter')
    parser.add_argument('--CUDA', default = '0', help='GPU')
    parser.add_argument('--MWF', default = True, help='<<True>> for better but slower model')
    parser.add_argument('--fp', default = '/volume/youtube-audios/mp3/')
    parser.add_argument('--op', default = '/volume/youtube-audios/mp3_sep/')
    args = parser.parse_args()


    os.environ["CUDA_VISIBLE_DEVICES"] = args.CUDA
    file_path = args.fp
    output_dir = args.op
    use_MWF = args.MWF
    check_exist(output_dir)
    main(file_path, output_dir, use_MWF)
