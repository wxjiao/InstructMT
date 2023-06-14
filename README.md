<div align="center">
    <img width="25%" alt="ParroT" src="https://github.com/wxjiao/InstructMT/assets/31032829/3a19944b-d42d-45da-919b-320f1410a3a6">
    <h2>
    InstructMT Data & Scripts <a href="https://github.com/wxjiao/ParroT">@ParroT</a>
    </h2>
</div>

A collection of instruction data and scripts for machine translation.

## Machine Translation

### Data Resources

<div align="center">
  
| Data |  Source  |  Zh-En | En-Zh | De-En | En-De | Format |
| :------ | :------: | ------: | ------: | ------: | ------: |  :------ |
| Translation |  [newstest17-20](https://drive.google.com/drive/folders/19_kMgbH1R9VrYf72xCNDxILX5ptPct_a?usp=drive_link)  |  12.2k | 12.2k | 13.3k  | 13.3k | `TXT` |
| MQM-Score |  newstest20  | 20.0k  | -/- | -/- | 14.1k | `JSON`: 1 source + 10 system outputs w/ score |
| MQM-Error |  newstest20  | 124.3k | -/- | -/ | 79.0k | `TXT`: 1 source + 1 system output w/ annotation |
| COMET-Score |  newstest20  |     |  |  |  | |
| Translation |  WMT20  |  475k | 475k | -/- | -/- | `TXT`: Filtered from 26M raw data |

</div>


### Instructions

**Script**: `convert_pair_to_hf.py` 

**Function**: To transform sentence pairs to instructions in HF format 

**Hyperparams**: 
- `-dir`: the direction of instruction prefix files, which support various languages 
- `-tp`: "instruct_fol", "instruct_sep" and "instruct_abo", which correspond to the three scenarios below, respectively
```
python3 convert_pair_to_hf.py \
    -s zh -t en \
    -dir ./ \
    -sf test_rand_50.zh.txt \
    -tf test_rand_50.en.txt \
    -of zhen_hf.fol.json \
    -tp instruct_fol
```

**1.【 Instruction + Source > Target 】**: Input the instruction and source sentence at the same time.

<p align="center">
    <img width="45%" alt="image" src="https://github.com/wxjiao/InstructMT/assets/31032829/b77eb575-6f7f-4ddb-8173-4eede4c9797c">
</p>

**2.【 Instruction > Response > Source > Target 】**: Input the instruction only, then the LLMs should remind the user to input the source sentence.

<p align="center">
    <img width="45%" alt="image" src="https://github.com/wxjiao/InstructMT/assets/31032829/2bad9b55-825a-440b-934b-591042c7b6b2">
</p>

**3.【 Source > Instruction > Target 】**: Translate the last chat record.

<p align="center">
    <img width="45%" alt="image" src="https://github.com/wxjiao/InstructMT/assets/31032829/bd53e282-67d4-4347-ae98-780f14f450ef">
</p>


<details>
## General Scenarios

**Script**: `convert_alp_to_hf.py` 

**Function**: To transform Alpaca data to instructions in HF format. 

</details>
