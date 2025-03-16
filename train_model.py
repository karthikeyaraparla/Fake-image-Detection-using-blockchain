import tensorflow as tf
from detect_fake import create_model

def main():
    # Create model
    model = create_model()
    
    # Initialize with some weights
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Save the model weights
    model.save_weights('deepfake_model.weights.h5')
    print("Model weights saved to deepfake_model.weights.h5")

if __name__ == "__main__":
    main() 