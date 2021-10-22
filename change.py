import os
import shutil

torch_path = "/Vol0/user/p.andreev/anaconda3/envs/pynight/lib/python3.8/site-packages/"

l=  ["torch/quantization/quantization_mappings.py",
     "torch/quantization/fake_quantize.py",
     "torch/nn/qat/modules/conv.py",
     "torch/nn/modules/conv.py",
     "torch/nn/intrinsic/modules/fused.py",
     "torch/nn/intrinsic/quantized/modules/conv_relu.py",
     "torch/nn/intrinsic/qat/modules/conv_fused.py",
     "torch/nn/quantized/modules/conv.py",
     "torch/nn/quantized/modules/functional_modules.py",
     "torch/nn/qat/modules/__init__.py",
     "torch/nn/intrinsic/modules/__init__.py",
     "torch/nn/intrinsic/quantized/modules/__init__.py",
     "torch/nn/intrinsic/qat/modules/__init__.py"]

for f in l:
    dest = os.path.join(torch_path, f)
    shutil.copy("./" + f, dest)

    
