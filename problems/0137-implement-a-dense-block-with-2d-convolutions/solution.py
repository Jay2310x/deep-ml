import numpy as np

def dense_net_block(input_data, num_layers, growth_rate, kernels, kernel_size=(3, 3)):
    
    N, H, W, C = input_data.shape
    kh, kw = kernel_size
    
    features = input_data  # running tensor
    
    # symmetric padding (for odd kernel)
    pad_h = (kh - 1) // 2
    pad_w = (kw - 1) // 2
    
    for l in range(num_layers):
        
        # 1️⃣ ReLU activation
        activated = np.maximum(0, features)
        
        kernel = kernels[l]
        
        # 2️⃣ Validate input channels
        if kernel.shape[2] != activated.shape[3]:
            raise ValueError(
                f"Layer {l}: Kernel expects {kernel.shape[2]} channels, "
                f"but got {activated.shape[3]}"
            )
        
        # 3️⃣ Validate growth rate
        if kernel.shape[3] != growth_rate:
            raise ValueError(
                f"Layer {l}: Kernel output channels must equal growth_rate"
            )
        
        # 4️⃣ Zero padding to preserve spatial