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

Below lists the resources of high-quality translation data for instruction tuning. You can access the data through the links.
The previous links are problematic, now they are fixed.

<div align="center">
<table style="text-align:right">
  <tr>
    <th> Data </th>
    <th> Source </th>
    <th> Zh-En </th>
    <th> En-Zh </th>
    <th> De-En </th>
    <th> En-De </th>
    <th> Format </th>
  </tr>
  <tr>
    <td>Translation </td>
    <td> <a href="https://drive.google.com/drive/folders/19_kMgbH1R9VrYf72xCNDxILX5ptPct_a?usp=sharing" >newstest17-20 </a> </td>
    <td> 12.2k </td>
    <td> 12.2k </td>
    <td> 13.3k </td>
    <td> 13.3k </td>
    <td> `TXT` </td>
  </tr>
  <tr>
    <td>MQM-Score </td>
    <td> <a href="https://drive.google.com/drive/folders/1OFmqJVtu_dhVYq-KNb478pmqdfqPNQSA?usp=sharing" >newstest20 </a> </td>
    <td> 20.0k </td>
    <td> n/a </td>
    <td> n/a </td>
    <td> 14.1k </td>
    <td> `JSON` </td>
  </tr>
  <tr>
    <td>MQM-Error </td>
    <td> <a href="https://drive.google.com/drive/folders/18O5hZc9GVX6V5wq9PKb3hzSef0pgzkbO?usp=sharing" >newstest20 </a> </td>
    <td> 124.3k </td>
    <td> n/a </td>
    <td> n/a </td>
    <td> 79.0k </td>
    <td> `TXT` </td>
  </tr>
  <tr>
    <td>COMET-Score </td>
    <td> <a href="https://drive.google.com/drive/folders/1wDiHYuu-vZiBnfGmzEigRpnmx2qFiFwF?usp=sharing" >newstest20 </a> </td>
    <td> n/a </td>
    <td> 19.8k </td>
    <td> 9.4k </td>
    <td> n/a </td>
    <td> `JSON` </td>
  </tr>
  <tr>
    <td>Translation </td>
    <td> <a href="https://drive.google.com/drive/folders/1g7x0jrKlUfkEduy_gS7k7JFn7zPB7o_u?usp=sharing" >wmt20 </a> </td>
    <td> 475.0k </td>
    <td> 475.0k </td>
    <td> n/a </td>
    <td> n/a </td>
    <td> `TXT`: Filtered from 26M </td>
  </tr>
</table>
</div>


---

### ParroT Instructions

```
parrot
├── alpaca
│   └── convert_alpaca_to_hf.py
├── contrastive-instruction
│   ├── convert_cometscore_to_csi_alpaca.py
│   ├── convert_mqmscore_to_csi_alpaca.py
│   └── instruct_t2t.txt
├── error-guided-instruction
│   ├── convert_cometscore_to_egi_alpaca.py
│   ├── convert_mqmerror_to_egi_alpaca.py
│   └── instruct_e2t.txt
└── translation-instruction
    ├── convert_pair_to_alpaca.py
    └── instruct_follow.txt
```

**1. Translation Instruction**

Example usage and output:
```
cd ./parrot/translation-instruction

# Download the Translation data into the folder

python3 convert_pair_to_alpaca.py \
    -s zh -t en \
    -if instruct_follow.txt \
    -sf newstest17-20.en-zh.zh \
    -tf newstest17-20.en-zh.en \
    -of data_ti_alp.zh-en.json
```

```
[
    {
        "instruction": "I'd appreciate it if you could present the English translation for these sentences.",
        "input": "28岁厨师被发现死于旧金山一家商场",
        "output": "28-Year-Old Chef Found Dead at San Francisco Mall"
    },
    ...
]
```

**2. Contrastive Instruction**

Example usage and output for __MQM Zh-En__:
```
cd ./parrot/contrastive-instruction

# Download the MQM-Score data into the folder

python3 convert_mqmscore_to_csi_alpaca.py \
    -s zh -t en \
    -if instruct_t2t.txt \
    -i sys_rating_mqm.zh-en.json \
    -o data_csi_alp.zh-en.json
```

```
[
    {
        "instruction": "Could you supply the English translation for the upcoming sentences?",
        "input": "国有企业和优势民营企业走进赣南革命老区。\n\n### Hint: A superior translation would be",
        "output": "<p>State-owned enterprises and advantageous private enterprises entered the old revolutionary area of Gannan.</p> rather than <p>State-owned enterprises and dominant private enterprises entered the old revolutionary area of southern Jiangxi.</p>"
    },
    ...
]
```

Example usage and output for __COMET En-Zh__:
```
cd ./parrot/contrastive-instruction

# Download the COMET-Score data into the folder

python3 convert_cometscore_to_csi_alpaca.py \
    -s en -t zh \
    -if instruct_t2t.txt \
    -i sys_rating_comet.en-zh.json \
    -o data_csi_alp.en-zh.json
```

```
[
    {
        "instruction": "Could you supply the Chinese translation for the upcoming sentences?",
        "input": "Michael Jackson wore tape on his nose to get front pages, former bodyguard claims\n\n### Hint: A superior translation would be",
        "output": "<p>前保镖声称迈克尔·杰克逊为登上头条新闻在鼻子上贴上胶带</p> rather than <p>前保镖称迈克尔·杰克逊为上头版在鼻子上贴胶带</p>"
    },
    ...
]
```


**3. Error-Guided Instruction**

Example usage and output for __MQM En-Zh__:
```
cd ./parrot/error-guided-instruction

# Download the MQM-Error data into the folder

python3 convert_mqmerror_to_egi_alpaca.py \
    -s zh -t en \
    -if instruct_e2t.txt \
    -i mqm_newstest2020_zhen.txt \
    -o data_egi_alp.zh-en.json
```

```
[
    {
        "instruction": "Could you supply the English translation for the upcoming sentences?",
        "input": "国有企业和优势民营企业走进赣南革命老区。\n\n### Hint: A rendition having minor fluency/grammar errors is possible",
        "output": "State-owned enterprises and dominant private enterprises entered the old revolutionary area of southern Jiangxi <v>State-owned enterprises and dominant private enterprises entered the old revolutionary area of southern Jiangxi.</v> "
    },
    ...
]
```

Example usage and output for __COMET En-Zh__:
```
cd ./parrot/error-guided-instruction

# Download the COMET-Score data into the folder

python3 convert_cometscore_to_egi_alpaca.py \
    -s en -t zh \
    -if instruct_e2t.txt \
    -i sys_rating_comet.en-zh.json \
    -o data_egi_alp.en-zh.json
```

```
[
    {
        "instruction": "Could you supply the Chinese translation for the upcoming sentences?",
        "input": "Michael Jackson wore tape on his nose to get front pages, former bodyguard claims\n\n### Hint: A rendition having no errors is possible",
        "output": "前保镖声称迈克尔·杰克逊为登上头条新闻在鼻子上贴上胶带"
    },
    ...
]
```

**\* Alpaca Format**

The above three instruction types can be used for [Stanford-Alpaca](https://github.com/tatsu-lab/stanford_alpaca) directly. 

Or you can transform them to fit the format of [ParroT](https://github.com/wxjiao/ParroT) as follows:
```
cd ./parrot/translation-instruction

python3 ../alpaca/convert_alpaca_to_hf.py \
    -i data_ti_alp.zh-en.json \
    -o data_ti_hf.zh-en.json
``` 

```
# Each dict is saved as one line but we show it in multiple lines for better appearance
{
    "text": "28-Year-Old Chef Found Dead at San Francisco Mall</s>",
    "prefix": "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\nI'd appreciate it if you could present the English translation for these sentences.\n\n### Input:\n28岁厨师被发现死于旧金山一家商场\n\n### Response:"
}
```


<!---
### Instruction Variants (To Be Optimized)

<details>
    
**1. Translation Instruction**

**【 Instruction + Source > Target 】**: Input the instruction and source sentence at the same time.

<p align="center">
    <img width="45%" alt="image" src="https://github.com/wxjiao/InstructMT/assets/31032829/b77eb575-6f7f-4ddb-8173-4eede4c9797c">
</p>

**【 Instruction > Response > Source > Target 】**: Input the instruction only, then the LLMs should remind the user to input the source sentence.

<p align="center">
    <img width="45%" alt="image" src="https://github.com/wxjiao/InstructMT/assets/31032829/2bad9b55-825a-440b-934b-591042c7b6b2">
</p>

**【 Source > Instruction > Target 】**: Translate the last chat record.

<p align="center">
    <img width="45%" alt="image" src="https://github.com/wxjiao/InstructMT/assets/31032829/bd53e282-67d4-4347-ae98-780f14f450ef">
</p>

</details>
--->




## Public Impact

### Citation
Please kindly cite our paper if you find the data resources here helpful:

```ruby
@inproceedings{jiao2023parrot,
  title={ParroT: Translating During Chat Using Large Language Models}, 
  author={Wenxiang Jiao and Jen-tse Huang and Wenxuan Wang and Xing Wang and Shuming Shi and Zhaopeng Tu},
  booktitle = {ArXiv},
  year      = {2023}
}
```
