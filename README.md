# 🧠 Semantic Block Format (.SBF)
**A Protocol for Dynamic, Sub-Second Knowledge Injection in Quantized LLMs.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Paper](https://zenodo.org/records/18870663?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6Ijg2MjU5ZWU2LTQ3OTMtNDlmNC1hZDk3LWRhYzljNGFkYjZmMCIsImRhdGEiOnt9LCJyYW5kb20iOiIzNjE5M2ZhNzE4ZTBiNjZjZjc5OTY4YjFlMzVhZTQyOCJ9.bWK5s3jWoKsZoWiD8wA71-1GvUraU2CXgBrPeLfVXjuae2NRI3x6w9MfC_rf2QHsDmTkMxEv8wA4uwONZl84tA)

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
