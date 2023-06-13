# InstructMT
A collection of instruction data and scripts for machine translation, using Chinese (zh) and English (en) as the examples.


## Translation Scenarios

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

