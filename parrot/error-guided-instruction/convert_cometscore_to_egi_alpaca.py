##############################
# Function: convert COMET score data to error-guided instruction in alpaca data format
# Author: Wenxiang Jiao
# Last modified: 2023/06/14
##############################

import argparse
import time
import json
from tqdm import tqdm
import random
import numpy as np
import csv, json



# Instrauct language
lang_instruction = {
    'de': {'de': "Deutsch", 'en': "Englisch", 'ja': "Japanisch", 'zh': "Chinesisch"},
    'en': {'de': "German", 'en': "English", 'ja': "Japanese", 'zh': "Chinese"},
    'ja': {'de': "ドイツ語", 'en': "英語", 'ja': "日本語", 'zh': "中国語"},
    'zh': {'de': "德语", 'en': "英语", 'ja': "日语", 'zh': "中文"},
}


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def read_instruct(path, src, tgt, lang_ins):
    source, target = lang_instruction[lang_ins][src], lang_instruction[lang_ins][tgt]
    ins_list = []
    with open(path, 'r', encoding='utf-8') as f:
        for l in f:
            line = l.strip().replace("[SRC]", source).replace("[TGT]", target)
            ins_list.append(line)
    return ins_list


def create_prompt(data_json, ins_list, subset):
    prompts = []
    for seg,seg_info in data_json.items():
        source, targets, severities = seg_info["source"][0], seg_info["hypothesis"], seg_info["severity"]
        source = source.strip()
        for target,severity in zip(targets,severities):
            target, severity = target.strip(), severity.strip().lower()
            p = dict()
            ins_idx = random.randint(0, len(ins_list) - 1)
            instruct, input_suffix = ins_list[ins_idx].split("###")
            p["instruction"] = instruct
            input_suffix = input_suffix.replace("[SEV] ", "").replace("[ERR]", severity)
            p["input"] = "\n\n".join([source, "### Hint: {}".format(input_suffix)])
            p["output"] = target.replace("<v>", " <v>").replace("  <v>", " <v>").replace("</v>", "</v> ").replace("</v>  ", "</v> ")
            prompts.append(p)

    if subset > 0:
        sub_idx = sorted(np.random.choice(range(len(prompts)), size=subset, replace=False))
        prompts_sub = [prompts[i] for i in sub_idx]
        return prompts_sub
    return prompts


def write_json(out_file, data_json, ins_list, subset, seed=0):
    random.seed(seed)
    np.random.seed(seed)
    with open(out_file, 'w', encoding='utf-8') as fo:
        prompts = create_prompt(data_json, ins_list, subset)
        print("Selected number of samples: {}".format(len(prompts)))
        json.dump(prompts, fo, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    """
    python3 ./convert_cometscore_to_egi_alpaca.py -s en -t zh -if ./instruct_e2t.txt -i ./sys_rating_comet.en-zh.json -o data_e2t.en-zh.json
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', '-s', type=str, required=True, help='src language, en, de, ja, zh')
    parser.add_argument('--tgt', '-t', type=str, required=True, help='tgt language, en, de, ja, zh')
    parser.add_argument('--lang-ins', '-li', type=str, default='en', help='instruct language, en, de, ja, zh')
    parser.add_argument('--ins-file','-if', type=str, required=True, help='ins file')
    parser.add_argument('--inp-file','-i', type=str, required=True, help='data.json file')
    parser.add_argument('--out-file','-o', type=str, required=True, help='out file')
    parser.add_argument('--seed', type=int, default=0, help='random seed')
    parser.add_argument('--subset','-sub', type=int, default=0, help='subset of all resulting samples')
    args = parser.parse_args()
    src, tgt = args.src, args.tgt
    lang_ins = args.lang_ins
    ins_file = args.ins_file
    inp_file = args.inp_file
    out_file = args.out_file
    seed = args.seed
    subset = args.subset

    # Start
    ins_list = read_instruct(ins_file, src, tgt, lang_ins)
    print("Number of instructs: {}".format(len(ins_list)))
    data_json = read_json(inp_file)
    print("Total number of sources: {}".format(len(data_json)))
    write_json(out_file, data_json, ins_list, subset, seed)
