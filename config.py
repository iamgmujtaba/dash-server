import argparse

def parse_opts():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--inp_path', type=str, default='./input/', help='Input videos path')
    parser.add_argument('-o','--out_path', type=str, default='./output/', help='Output videos path')

    parser.add_argument('-a','--audio', type=bool, default=False, help='Extract audio (True/False)')
    parser.add_argument('-f','--frames', type=bool, default=False, help='Extract video frames (True/False)')

    return parser.parse_args()
