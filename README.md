<div align="center">
    <img width="25%" alt="ParroT" src="https://github.com/wxjiao/InstructMT/assets/31032829/3a19944b-d42d-45da-919b-320f1410a3a6">
    <h2>
    InstructMT Data & Scripts <a href="https://github.com/wxjiao/ParroT">@ParroT</a>
    </h2>
</div>

A collection of instruction data and scripts for machine translation.

The resulting files mainly fit the format of [ParroT](https://github.com/wxjiao/ParroT) and partially that of [Stanford-Alpaca](https://github.com/tatsu-lab/stanford_alpaca).

## Machine Translation

### Data Resources

<div align="center">
  
| Data |  Source  |  Zh-En | En-Zh | De-En | En-De | Format |
| :------ | :------: | ------: | ------: | ------: | ------: |  :------ |
| Translation |  [newstest17-20](https://drive.google.com/drive/folders/19_kMgbH1R9VrYf72xCNDxILX5ptPct_a?usp=drive_link)  |  12.2k | 12.2k | 13.3k  | 13.3k | `TXT` |
| MQM-Score |  [newstest20](https://drive.google.com/drive/folders/1OFmqJVtu_dhVYq-KNb478pmqdfqPNQSA?usp=drive_link)  | 20.0k  | -/- | -/- | 14.1k | `JSON`: 1 source + 10 system outputs w/ score |
| MQM-Error |  [newstest20](https://drive.google.com/drive/folders/18O5hZc9GVX6V5wq9PKb3hzSef0pgzkbO?usp=drive_link)  | 124.3k | -/- | -/- | 79.0k | `TXT`: 1 source + 1 system output w/ annotation |
| COMET-Score |  [newstest20](https://drive.google.com/drive/folders/1wDiHYuu-vZiBnfGmzEigRpnmx2qFiFwF?usp=drive_link)  | -/- | 19.8k | 9.4k | -/- | `JSON`: 1 source + 14/12 system outputs w/ score |
| Translation |  [WMT20](https://drive.google.com/drive/folders/1g7x0jrKlUfkEduy_gS7k7JFn7zPB7o_u?usp=drive_link)  |  475.0k | 475.0k | -/- | -/- | `TXT`: Filtered from 26M raw data |

</div>


<div align="center">
<table style="text-align:right">
  <tr>
    <th>WMT20 En-De </th>
    <th>Batch (tok*freq*gpu)</th>
    <th>Step</th>
    <th>Lr-sch</th>
    <th>Dp</th>
    <th>V_loss<sup>*</sup></th>
    <th>V_bleu<sup>*</sup></th>
    <th>T-bleu(sac/mul)</th>
    <th>GPU*Hour</th>
  </tr>
  <tr>
    <td>Transformer-big</td>
    <td>460K (3600*16*8)</td>
    <td>30K</td>
    <td>Cosine</td>
    <td>0.1</td>
    <td>3.119</td>
    <td>43.73</td>
    <td>32.4/35.2</td>
    <td>8V100*16.0</td>
  </tr>
  <tr>
    <td rowspan=4>mBART_cc06</td>
    <td rowspan=2>131K (2048*8*8)</td>
    <td>100K</td>
    <td>Polynomial</td>
    <td>0.3</td>
    <td>4.875</td>
    <td>45.11</td>
    <td>32.8/35.6</td>
    <td>8A100*26.0</td>
  </tr>
  <tr>
    <td>100K</td>
    <td>Polynomial</td>
    <td>0.1</td>
    <td>4.809</td>
    <td>44.98</td>
    <td>33.0/35.7</td>
    <td>8A100*26.0</td>
  </tr>
  <tr>
    <td rowspan=2>32K (2048*2*8)</td>
    <td>300K</td>
    <td>Polynomial</td>
    <td>0.3</td>
    <td>4.836</td>
    <td>45.38</td>
    <td>33.3/36.1</td>
    <td>8A100*25.4</td>
  </tr>
  <tr>
    <td>300K</td>
    <td>Polynomial</td>
    <td>0.1</td>
    <td>4.782</td>
    <td>45.42</td>
    <td><b>33.4/36.1</b></td>
    <td>8A100*25.4</td>
  </tr>
</table>
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
