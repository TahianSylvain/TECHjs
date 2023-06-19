"""
import os
import pathlib
import co
import numpy as np
import tensorflow as tf


def main() -> co.Serial:
    path = "/conducto/data/pipeline"
    root = co.Serial(image=get_image())
    # Get data from keras for testing and training
    root["Get Data"] = co.Exec(run_whole_thing, f"{path}/raw")
    return root


def run_whole_thing(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    # Set seed for experiment reproducibility
    seed = 55
    tf.random.set_seed(seed)
    np.random.seed(seed)
    data_dir = pathlib.Path("data/mini_speech_commands")
    if not data_dir.exists():
        # Get the ﬁles from external source and put them in an accessible directory
        tf.keras.utils.get_ﬁle(
            'mini_speech_commands.zip',
            origin="http://storage.googleapis.com/download.tensorﬂow.org/data/mini_speech_commands.zip",
            extract=True
        )


# Convert the binary audio ﬁle to a tensor
def decode_audio(audio_binary):
    audio, _ = tf.audio.decode_wav(audio_binary)
    return tf.squeeze(audio, axis=-1)


def get_label(ﬁle_path):
    parts = tf.strings.split(ﬁle_path, os.path.sep)
    return parts[-2]


# Create a tuple that has the labeled audio ﬁles
def get_waveform_and_label(ﬁle_path):
    label = get_label(ﬁle_path)
    audio_binary = tf.io.read_ﬁle(ﬁle_path)
    waveform = decode_audio(audio_binary)
    return waveform, label


# Convert audio ﬁles to images
def get_spectrogram(waveform):
    # Padding for ﬁles with less than 16000 samples
    zero_padding = tf.zeros([16000] - tf.shape(waveform), dtype=tf.ﬂoat32)
    # Concatenate audio with padding so that all audio clips will be of the same length
    waveform = tf.cast(waveform, tf.ﬂoat32)
    equal_length = tf.concat([waveform, zero_padding], 0)
    spectrogram = tf.signal.stft(
        equal_length, frame_length=255, frame_step=128
    )
    spectrogram = tf.abs(spectrogram)
    return spectrogram


# Label the images created from the audio ﬁles and return a tuple
def get_spectrogram_and_label_id(audio, label):
    spectrogram = get_spectrogram(audio)
    spectrogram = tf.expand_dims(spectrogram, -1)
    label_id = tf.argmax(label == commands)
    return spectrogram, label_id


# Preprocess any audio ﬁles
def preprocess_dataset(ﬁles, autotune, commands):
    # Creates the dataset
    ﬁles_ds = tf.data.Dataset.from_tensor_slices(ﬁles)
    # Matches audio ﬁles with correct labels
    output_ds = ﬁles_ds.map(
        get_waveform_and_label,
        num_parallel_calls=autotune
    )
    # Matches audio ﬁle images to the correct labels
    output_ds = output_ds.map(
        get_spectrogram_and_label_id, num_parallel_calls=autotune)
    return output_ds


def get_image():
    return co.Image(
        "python:3.8-slim",
        copy_dir=".",
        reqs_py=["conducto", "tensorﬂow", "keras"],
    )


if __name__ == "__main__":
    co.main(default=main)
"""