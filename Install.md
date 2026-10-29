# Installation instructions

## Python and Jupyter based projects

From the repository root:

```
python3 -m venv audio-venv
source audio-venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

`requirements.txt` installs the notebook dependencies and the shared `audiodsp` helper package (from the `audiodsp/` folder, in editable mode), so every notebook can `import audiodsp` regardless of which project folder it runs from.

### Keep notebook outputs out of git

Notebook outputs (plots and embedded audio) make a notebook several megabytes and make diffs unreadable. Install the `nbstripout` git filter once per clone, with the venv active:

```
nbstripout --install
```

After this, outputs are stripped from notebooks when they are committed. Your local copy keeps its outputs.

### Optional: live audio

The last cell of `projects/04_Real_time_Audio_Processing/realtime_processing.ipynb` can process a live microphone input. It needs the `sounddevice` package and, on Linux, the PortAudio library:

```
pip install sounddevice
sudo apt install libportaudio2
```

Containers and remote machines usually have no audio device. All other cells run without it.

## Teensy based projects

There are no Teensy projects yet.
