from io import BytesIO
import subprocess


def strip_exif(fp):
    args = ('exiftool', '-all=', '-')
    proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate(input=fp.read())

    return BytesIO(out)
