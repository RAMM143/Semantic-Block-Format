# sbf.py - The Semantic Block Format Core Library
# Copyright (c) 2026 Madhan Mohan. Licensed under Apache 2.0.

import torch
import os
import json
import time

class NeuralShell:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        self.base_arch = model.config.architectures[0]

    def extract_block(self, layer_start, layer_end, block_name, domain_tag):
        """Extracts a localized neural block into .SBF format"""
        print(f"📦 Packaging {block_name} (Layers {layer_start}-{layer_end})...")
        
        sbf_payload = {
            "meta": {
                "version": "0.1",
                "arch": self.base_arch,
                "layers": list(range(layer_start, layer_end)),
                "domain": domain_tag,
                "timestamp": time.time()
            },
            "weights": {}
        }

        # Extract weights preserving quantization state
        for i in range(layer_start, layer_end):
            for name, param in self.model.model.layers[i].named_parameters():
                # Clone to CPU to avoid VRAM spikes
                sbf_payload["weights"][f"layers.{i}.{name}"] = param.clone().cpu()

        # Save to disk
        filename = f"{block_name}.sbf"
        torch.save(sbf_payload, filename)
        print(f"✅ Created artifact: {filename} ({os.path.getsize(filename)/1024/1024:.2f} MB)")
        return filename

    def inject_block(self, sbf_path):
        """Performs Direct State Overwrite (DSO) injection"""
        print(f"⚡ Injecting {sbf_path}...")
        start_t = time.time()
        
        # Load Artifact
        packet = torch.load(sbf_path)
        layers = packet["meta"]["layers"]
        
        # Injection Loop
        with torch.no_grad():
            for i in layers:
                for name, param in self.model.model.layers[i].named_parameters():
                    key = f"layers.{i}.{name}"
                    if key in packet["weights"]:
                        # Direct VRAM Overwrite
                        param.data.copy_(packet["weights"][key].to(param.device))
        
        latency = time.time() - start_t
        print(f"🚀 Injection Complete: {latency:.4f}s")
