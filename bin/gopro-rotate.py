#!/usr/bin/env python3

import argparse
import os.path

from gopro_overlay.ffmpeg import rotate_file
# from gopro_overlay.parsing import parse_time


#def as_seconds(timey):
#    parsed_time = parse_time(timey)
#    return (parsed_time.hour * 3600) + (parsed_time.minute * 60) + parsed_time.second + (
#            parsed_time.microsecond / 100000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="rotate GoPro File")

    parser.add_argument("input", help="A single MP4 file ")

    parser.add_argument("--degrees", help="degrees to rotate")

    parser.add_argument("output", help="Output MP4 file")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise IOError(f"File not found {args.input}")

    if args.degrees:
        rotation = int(args.degrees)
    else:
        parser.print_help()
        exit(1)

    if rotation < 1 or rotation > 359:
        raise ValueError("Rotation should be between 1 and 359 degrees")
        parser.print_help()
        exit(1)

    rotate_file(args.input, args.output, rotation)
