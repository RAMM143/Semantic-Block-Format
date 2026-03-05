# 🧠 Semantic Block Format (.SBF)
**A Protocol for Dynamic, Sub-Second Knowledge Injection in Quantized LLMs.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18870663.svg)](https://doi.org/10.5281/zenodo.18870663)

## ⚡ What is it?
.SBF is a "Neural Container" format. It allows you to extract specific skills (Geography, Math, Coding) from massive LLMs and save them as lightweight modules (~400MB). 
These modules can be **injected into a running AI model in < 0.4 seconds** without reloading the model.

## 🚀 Quick Start
```python
import sbf
from unsloth import FastLanguageModel

# 1. Load the Shell
model, tokenizer = FastLanguageModel.from_pretrained("llama-3-8b-bnb-4bit", load_in_4bit=True)
shell = sbf.NeuralShell(model, tokenizer)

# 2. Inject a Skill (Hot-Swap)
shell.inject_block("geography_v1.sbf")
# Output: 🚀 Injection Complete: 0.3907s

#📜 Citation
#If you use .SBF, please cite our whitepaper.
