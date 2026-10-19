from __future__ import annotations

import os
from pathlib import Path

import onnxruntime as ort


MODEL_PATH = Path(
    os.getenv("MODEL_PATH", Path(__file__).with_name("hair_classifier_v1.onnx"))
)
session = ort.InferenceSession(
    str(MODEL_PATH),
    providers=["CPUExecutionProvider"],
)
INPUT_NAME = session.get_inputs()[0].name
OUTPUT_NAME = session.get_outputs()[0].name

print(f"session input object: {session.get_inputs()[0]}") # session input object: NodeArg(name='input', type='tensor(float)', shape=['s77', 3, 200, 200])
print(f"session output object: {session.get_outputs()[0]}") # session output object: NodeArg(name='output', type='tensor(float)', shape=['s77', 1])

# Answer: output