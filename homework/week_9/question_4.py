import onnxruntime as ort

from lambda_function import download_image, prepare_image


from smoke_test import SAMPLE_URL

session = ort.InferenceSession(
    "hair_classifier_v1.onnx",
    providers=["CPUExecutionProvider"],
)
output = session.run(
    ["output"],
    {"input": prepare_image(download_image(SAMPLE_URL))},
)[0]


# {'straight_probability': 0.727697, 'straight': True}

# Answer: 0.728