```markdown
# 🕹️ Subway Surf by Hand Control

Welcome to **SubwaySurf-by-Hand-Control** – a fun and interactive way to play a Subway Surfer–style game using your **hand gestures and webcam**! Built using **Python**, **OpenCV**, **MediaPipe**, and **PyAutoGUI**, this project allows you to simulate keyboard control without touching a keyboard – just wave your hand to control the game!

![Demo GIF](https://github.com/Eruumaa/SubwaySurf-by-Hand-Control/assets/your-demo.gif) <!-- You can add a real GIF or remove this line -->

---

## 🚀 Features

- 🖐️ Hand tracking using **MediaPipe**
- 🎮 Control game characters with simple hand gestures
- 🧠 Gesture detection for left, right, up, and down movements
- 🔁 Real-time feedback with **OpenCV**
- 🖥️ Works with any game using arrow keys (Subway Surfer-like games)

---

## 📁 Project Structure

```

.
├── main.py              # Main script to run hand control system
├── requirements.txt     # List of required Python packages
└── README.md            # You're reading it!

````

---

## 🔧 Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI

You can install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## 🕹️ How to Use

1. Clone this repository:

```bash
git clone https://github.com/Eruumaa/SubwaySurf-by-Hand-Control.git
cd SubwaySurf-by-Hand-Control
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the hand tracking controller:

```bash
python main.py
```

4. Open your favorite **arrow-key–controlled game** (like a Subway Surfer clone).
5. Control the game with your hand using the webcam!

   * ✋ Open/close fingers to move
   * 📷 Make sure your hand is visible to the camera

---

## 🧠 How It Works

This project uses:

* **MediaPipe** to detect hand landmarks.
* **Custom logic** to determine which fingers are open.
* **PyAutoGUI** to simulate arrow key presses.
* **OpenCV** to display the webcam and visual cues in real-time.

---

## 📸 Screenshots

*Insert screenshots or a demo GIF here to show how it works.*

---

## 🙋‍♂️ About the Creator

Hi! I'm **Aqil Mubarak**, an Informatics student at Universitas Syiah Kuala. I love building interactive projects using computer vision, hardware (like ESP32), and AI technologies.

You can find more of my work on my [GitHub profile](https://github.com/Eruumaa).

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ❤️ Contributions

Pull requests are welcome! Feel free to fork the repo and submit enhancements or bug fixes.

```
