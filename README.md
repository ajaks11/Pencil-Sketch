# PencilSketch ✏️

A simple, elegant Python tool to convert your photos into realistic pencil sketches. Built with OpenCV.

## 🎨 How It Works
The algorithm follows a classic computer vision pipeline to simulate a sketch effect:
1.  **Grayscale**: Converts the colorful image to black and white.
2.  **Inversion**: Creates a negative of the image.
3.  **Gaussian Blur**: Smooths out details to approximate shading.
4.  **Color Dodge**: Blends the grayscale image with the blurred negative to extract edges and texture.

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pencil-sketch-converter.git
    cd pencil-sketch-converter
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

**Run the tool from the command line:**

```bash
python converter.py path/to/your/image.jpg
```

**Save the result to a file:**

```bash
python converter.py input.jpg -o my_sketch.png
```

## 📁 Project Structure

-   `converter.py`: Main script handling the image processing logic.
-   `requirements.txt`: List of dependencies.

---
*Created for my Python Portfolio.*
