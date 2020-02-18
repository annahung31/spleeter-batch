Original Spleeter is from here: https://github.com/deezer/spleeter 

In this repo, I write `processing.py` to Run spleeter to process a batch of audios.

## Run on GPU for big amount of data
To run on GPU and process files using multiprocessing, you can directly run
```
python processing.py --CUDA 0 --WMF True --fp /files/you/want/to/process --op /where/you/want/to/save
```
For more information about spleeter, please refer to original repo.



# Brief infos from original repo
## About
**Spleeter** is the [Deezer](https://www.deezer.com/) source separation library with pretrained models
written in [Python](https://www.python.org/) and uses [Tensorflow](https://tensorflow.org/). It makes it easy
to train source separation model (assuming you have a dataset of isolated sources), and provides
already trained state of the art model for performing various flavour of separation :

* Vocals (singing voice) / accompaniment separation ([2 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-2stems-model))
* Vocals / drums / bass / other separation ([4 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-4stems-model))
* Vocals / drums / bass / piano / other separation ([5 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-5stems-model))

2 stems and 4 stems models have state of the art performances on the [musdb](https://sigsep.github.io/datasets/musdb.html) dataset. **Spleeter** is also very fast as it can perform separation of audio files to 4 stems 100x faster than real-time when run on a GPU. 


## Quick start 

Want to try it out ? Just clone the repository and install a
[Conda](https://github.com/deezer/spleeter/wiki/1.-Installation#using-conda)
environment to start separating audio file as follows:

```bash
git clone https://github.com/Deezer/spleeter
conda install -c conda-forge spleeter
spleeter separate -i spleeter/audio_example.mp3 -p spleeter:2stems -o output
```
You should get two separated audio files (`vocals.wav` and `accompaniment.wav`)
in the `output/audio_example` folder.

For a more detailed documentation, please check the [repository wiki](https://github.com/deezer/spleeter/wiki)

Want to try it out but don't want to install anything ? we've setup a [Google Colab](https://colab.research.google.com/github/deezer/spleeter/blob/master/spleeter.ipynb)



## License
The code of **Spleeter** is MIT-licensed.

