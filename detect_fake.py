import tensorflow as tf
import numpy as np
import cv2
import hashlib

def create_model():
    """Create the model architecture"""
    model = tf.keras.Sequential([
        # First block
        tf.keras.layers.Conv2D(8, (3, 3), padding='same', activation='relu', input_shape=(256, 256, 3)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(2, 2),
        
        # Second block
        tf.keras.layers.Conv2D(16, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(2, 2),
        
        # Third block
        tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(2, 2),
        
        # Fourth block
        tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(2, 2),
        
        # Classifier
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

def get_image_hash(image_path):
    """Generate SHA-256 hash for an image"""
    with open(image_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def preprocess_image(image_path):
    """Preprocess image for the model"""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not load image at {image_path}")
    img = cv2.resize(img, (256, 256))
    img = img.astype('float32') / 255.0
    return np.expand_dims(img, axis=0)

def predict_fake(image_path):
    """Run image through deepfake detection model"""
    try:
        # Load and create model
        model = create_model()
        model.load_weights('deepfake_model.weights.h5')
        
        # Preprocess image
        img = preprocess_image(image_path)
        
        # Make prediction
        prediction = model.predict(img, verbose=0)[0][0]
        confidence = abs(0.5 - prediction) * 2  # Convert to confidence score
        return prediction > 0.5, confidence  # Returns (is_fake, confidence)
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return None, 0.0

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python detect_fake.py <image_path>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    is_fake, confidence = predict_fake(image_path)
    
    if is_fake is None:
        print("Error processing the image.")
    else:
        print(f"Image: {image_path}")
        print(f"Prediction: {'FAKE' if is_fake else 'REAL'}")
        print(f"Confidence: {confidence:.2%}")
